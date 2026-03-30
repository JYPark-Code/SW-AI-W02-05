import { useState, useEffect, useRef, useCallback } from "react";

// ─── 예제 그래프 (4도시) ───────────────────────────────────────────────────
const SAMPLE_W = [
  [0, 10, 15, 20],
  [10, 0, 35, 25],
  [15, 35, 0, 30],
  [20, 25, 30, 0],
];
const T = 4;
const CITY_LABELS = ["A", "B", "C", "D"];
const CITY_COLORS = ["#FF6B6B", "#4ECDC4", "#FFE66D", "#A29BFE"];

// 도시 위치 (원형 배치)
const CITY_POS = [
  { x: 200, y: 60 },
  { x: 340, y: 160 },
  { x: 280, y: 300 },
  { x: 100, y: 300 },
];

// ─── 비트마스크 시각화 컴포넌트 ───────────────────────────────────────────
function BitMask({ value, size, label, highlight }) {
  const bits = Array.from({ length: size }, (_, i) => (value >> (size - 1 - i)) & 1);
  return (
    <div className="bitmask-row">
      {label && <span className="bitmask-label">{label}</span>}
      <div className="bitmask-bits">
        {bits.map((b, i) => (
          <div
            key={i}
            className={`bit ${b ? "bit-on" : "bit-off"} ${highlight === size - 1 - i ? "bit-highlight" : ""}`}
          >
            {b}
          </div>
        ))}
      </div>
      <span className="bitmask-decimal">= {value}</span>
      <span className="bitmask-cities">
        ({bits.map((b, i) => b ? CITY_LABELS[size - 1 - i] : null).filter(Boolean).join(",") || "없음"} 방문)
      </span>
    </div>
  );
}

// ─── 그래프 SVG ───────────────────────────────────────────────────────────
function GraphView({ currentCity, visitedMask, pathEdges }) {
  const edges = [];
  for (let i = 0; i < T; i++)
    for (let j = i + 1; j < T; j++)
      if (SAMPLE_W[i][j] > 0) edges.push({ from: i, to: j, w: SAMPLE_W[i][j] });

  return (
    <svg width="440" height="360" style={{ fontFamily: "'JetBrains Mono', monospace" }}>
      {/* 엣지 */}
      {edges.map(({ from, to, w }, idx) => {
        const isActive = pathEdges.some(
          (e) => (e.from === from && e.to === to) || (e.from === to && e.to === from)
        );
        return (
          <g key={idx}>
            <line
              x1={CITY_POS[from].x} y1={CITY_POS[from].y}
              x2={CITY_POS[to].x} y2={CITY_POS[to].y}
              stroke={isActive ? "#FFE66D" : "#2d3561"}
              strokeWidth={isActive ? 3 : 1.5}
              strokeDasharray={isActive ? "none" : "5,3"}
              opacity={isActive ? 1 : 0.5}
            />
            <text
              x={(CITY_POS[from].x + CITY_POS[to].x) / 2}
              y={(CITY_POS[from].y + CITY_POS[to].y) / 2 - 6}
              fill={isActive ? "#FFE66D" : "#7f8fa6"}
              fontSize="12"
              textAnchor="middle"
            >
              {w}
            </text>
          </g>
        );
      })}
      {/* 노드 */}
      {CITY_POS.map((pos, i) => {
        const visited = (visitedMask >> i) & 1;
        const isCurrent = currentCity === i;
        return (
          <g key={i}>
            {isCurrent && (
              <circle cx={pos.x} cy={pos.y} r={28} fill={CITY_COLORS[i]} opacity={0.25} />
            )}
            <circle
              cx={pos.x} cy={pos.y} r={20}
              fill={visited ? CITY_COLORS[i] : "#1a1f3a"}
              stroke={isCurrent ? "#FFE66D" : CITY_COLORS[i]}
              strokeWidth={isCurrent ? 3 : 1.5}
            />
            <text x={pos.x} y={pos.y + 5} fill={visited ? "#000" : CITY_COLORS[i]}
              fontSize="14" fontWeight="bold" textAnchor="middle">
              {CITY_LABELS[i]}
            </text>
          </g>
        );
      })}
    </svg>
  );
}

// ─── DP 테이블 ─────────────────────────────────────────────────────────────
function DPTable({ dp, nowHighlight, visitedHighlight }) {
  const states = Array.from({ length: 1 << T }, (_, i) => i);
  return (
    <div className="dp-table-wrap">
      <div className="dp-table-header">
        <div className="dp-cell dp-head">도시\visited</div>
        {states.map((v) => (
          <div key={v} className={`dp-cell dp-head ${visitedHighlight === v ? "dp-hl-col" : ""}`}>
            <span style={{ fontSize: "10px" }}>{v.toString(2).padStart(T, "0")}</span>
          </div>
        ))}
      </div>
      {Array.from({ length: T }, (_, city) => (
        <div key={city} className="dp-table-row">
          <div className={`dp-cell dp-head ${nowHighlight === city ? "dp-hl-row" : ""}`}
            style={{ color: CITY_COLORS[city] }}>
            {CITY_LABELS[city]}
          </div>
          {states.map((v) => {
            const val = dp[city][v];
            const isHL = nowHighlight === city && visitedHighlight === v;
            return (
              <div key={v} className={`dp-cell ${isHL ? "dp-hl-cell" : ""} ${val !== -1 && val !== Infinity ? "dp-filled" : ""}`}>
                {val === -1 ? "·" : val === Infinity ? "∞" : val}
              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
}

// ─── 재귀 스택 뷰 ──────────────────────────────────────────────────────────
function CallStack({ stack }) {
  return (
    <div className="call-stack">
      {stack.slice().reverse().map((frame, i) => (
        <div key={i} className={`stack-frame ${i === 0 ? "stack-top" : ""}`}>
          <span className="stack-fn">dfs(</span>
          <span style={{ color: CITY_COLORS[frame.now] }}>now={CITY_LABELS[frame.now]}</span>
          <span className="stack-fn">, </span>
          <span className="stack-visited">
            visited=<span className="stack-bits">{frame.visited.toString(2).padStart(T, "0")}</span>
          </span>
          <span className="stack-fn">)</span>
          {frame.note && <span className="stack-note"> ← {frame.note}</span>}
        </div>
      ))}
    </div>
  );
}

// ─── 메인 ─────────────────────────────────────────────────────────────────
export default function TSPVisualizer() {
  const [steps, setSteps] = useState([]);
  const [stepIdx, setStepIdx] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(700);
  const intervalRef = useRef(null);

  // ─── 전체 실행 기록 생성 ──────────────────────────────────────────────
  useEffect(() => {
    const dpMemo = Array.from({ length: T }, () => new Array(1 << T).fill(-1));
    const recorded = [];
    const callStack = [];

    function recordSnapshot(note, extra = {}) {
      recorded.push({
        dp: dpMemo.map((r) => [...r]),
        stack: callStack.map((f) => ({ ...f })),
        note,
        ...extra,
      });
    }

    function dfs(now, visited) {
      callStack.push({ now, visited, note: "" });
      recordSnapshot(`dfs(${CITY_LABELS[now]}, ${visited.toString(2).padStart(T,"0")}) 진입`, {
        now, visited, pathEdges: buildEdges(callStack),
      });

      // base case
      if (visited === (1 << T) - 1) {
        const ret = SAMPLE_W[now][0] === 0 ? Infinity : SAMPLE_W[now][0];
        callStack[callStack.length - 1].note = `모두방문! →0 비용:${ret}`;
        recordSnapshot(`모든 도시 방문 완료. 시작(A)으로 복귀 비용: ${ret}`, {
          now, visited, pathEdges: buildEdges(callStack),
        });
        callStack.pop();
        return ret;
      }

      // 메모 체크
      if (dpMemo[now][visited] !== -1) {
        callStack[callStack.length - 1].note = `캐시 HIT! → ${dpMemo[now][visited]}`;
        recordSnapshot(`dp[${CITY_LABELS[now]}][${visited.toString(2).padStart(T,"0")}] 캐시 재사용 → ${dpMemo[now][visited]}`, {
          now, visited, pathEdges: buildEdges(callStack),
        });
        const cached = dpMemo[now][visited];
        callStack.pop();
        return cached;
      }

      let result = Infinity;
      for (let next = 0; next < T; next++) {
        if (SAMPLE_W[now][next] === 0 || (visited >> next) & 1) continue;

        callStack[callStack.length - 1].note = `→${CITY_LABELS[next]} 시도`;
        recordSnapshot(`${CITY_LABELS[now]} → ${CITY_LABELS[next]} 이동 시도 (비용 ${SAMPLE_W[now][next]})`, {
          now, visited,
          tryNext: next,
          pathEdges: buildEdges(callStack),
        });

        const sub = dfs(next, visited | (1 << next));
        const candidate = SAMPLE_W[now][next] + sub;
        if (candidate < result) result = candidate;

        callStack[callStack.length - 1] = { now, visited, note: `min 갱신 → ${result}` };
        recordSnapshot(`귀환. 현재 best=${result}`, {
          now, visited, pathEdges: buildEdges(callStack),
        });
      }

      dpMemo[now][visited] = result;
      callStack[callStack.length - 1].note = `저장 dp=${result}`;
      recordSnapshot(`dp[${CITY_LABELS[now]}][${visited.toString(2).padStart(T,"0")}] = ${result} 저장`, {
        now, visited, pathEdges: buildEdges(callStack),
      });
      callStack.pop();
      return result;
    }

    function buildEdges(stack) {
      const edges = [];
      for (let i = 0; i < stack.length - 1; i++) {
        edges.push({ from: stack[i].now, to: stack[i + 1].now });
      }
      return edges;
    }

    dfs(0, 1 << 0);
    setSteps(recorded);
    setStepIdx(0);
  }, []);

  // ─── 자동 재생 ────────────────────────────────────────────────────────
  useEffect(() => {
    if (playing) {
      intervalRef.current = setInterval(() => {
        setStepIdx((prev) => {
          if (prev >= steps.length - 1) { setPlaying(false); return prev; }
          return prev + 1;
        });
      }, speed);
    }
    return () => clearInterval(intervalRef.current);
  }, [playing, speed, steps.length]);

  const cur = steps[stepIdx] || { dp: Array.from({ length: T }, () => new Array(1 << T).fill(-1)), stack: [], note: "", pathEdges: [], now: 0, visited: 1 };

  const allMask = (1 << T) - 1;

  return (
    <div className="app">
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Sora:wght@400;600;700&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { background: #0d1117; }
        .app {
          background: #0d1117;
          min-height: 100vh;
          color: #e6edf3;
          font-family: 'Sora', sans-serif;
          padding: 20px;
        }
        h1 {
          font-family: 'JetBrains Mono', monospace;
          font-size: 18px;
          color: #58a6ff;
          letter-spacing: 0.05em;
          margin-bottom: 4px;
        }
        .subtitle { font-size: 12px; color: #7f8fa6; margin-bottom: 16px; }

        .layout { display: grid; grid-template-columns: 440px 1fr; gap: 16px; }
        .panel {
          background: #161b22;
          border: 1px solid #21262d;
          border-radius: 10px;
          padding: 14px;
        }
        .panel-title {
          font-family: 'JetBrains Mono', monospace;
          font-size: 11px;
          color: #8b949e;
          letter-spacing: 0.08em;
          text-transform: uppercase;
          margin-bottom: 10px;
          border-bottom: 1px solid #21262d;
          padding-bottom: 6px;
        }

        /* Controls */
        .controls {
          display: flex; gap: 8px; align-items: center;
          margin-bottom: 16px; flex-wrap: wrap;
        }
        .btn {
          background: #21262d; border: 1px solid #30363d;
          color: #e6edf3; border-radius: 6px;
          padding: 6px 14px; cursor: pointer;
          font-family: 'JetBrains Mono', monospace; font-size: 12px;
          transition: all 0.15s;
        }
        .btn:hover { background: #30363d; }
        .btn-primary { background: #1f6feb; border-color: #388bfd; }
        .btn-primary:hover { background: #388bfd; }
        .step-info {
          font-family: 'JetBrains Mono', monospace;
          font-size: 12px; color: #8b949e;
        }
        .speed-label { font-size: 12px; color: #8b949e; }
        input[type=range] { accent-color: #58a6ff; }

        /* Progress */
        .progress-bar {
          height: 3px; background: #21262d; border-radius: 2px;
          margin-bottom: 12px;
        }
        .progress-fill {
          height: 100%; background: #58a6ff; border-radius: 2px;
          transition: width 0.2s;
        }

        /* Note box */
        .note-box {
          background: #1c2333; border-left: 3px solid #58a6ff;
          padding: 10px 14px; border-radius: 0 6px 6px 0;
          font-family: 'JetBrains Mono', monospace; font-size: 13px;
          color: #e6edf3; min-height: 40px; margin-bottom: 12px;
        }

        /* Bitmask */
        .bitmask-row {
          display: flex; align-items: center; gap: 8px;
          margin-bottom: 6px; font-family: 'JetBrains Mono', monospace;
        }
        .bitmask-label { font-size: 11px; color: #8b949e; width: 60px; }
        .bitmask-bits { display: flex; gap: 3px; }
        .bit {
          width: 24px; height: 24px; border-radius: 4px;
          display: flex; align-items: center; justify-content: center;
          font-size: 13px; font-weight: bold;
          transition: all 0.2s;
        }
        .bit-on { background: #1f6feb; color: #fff; }
        .bit-off { background: #21262d; color: #484f58; }
        .bit-highlight { box-shadow: 0 0 0 2px #FFE66D; }
        .bitmask-decimal { font-size: 12px; color: #FFE66D; min-width: 24px; }
        .bitmask-cities { font-size: 11px; color: #7f8fa6; }

        /* DP Table */
        .dp-table-wrap {
          overflow-x: auto; font-family: 'JetBrains Mono', monospace;
          font-size: 10px;
        }
        .dp-table-header, .dp-table-row { display: flex; }
        .dp-cell {
          width: 38px; min-width: 38px; height: 30px;
          display: flex; align-items: center; justify-content: center;
          border: 1px solid #21262d; color: #484f58;
          transition: all 0.2s;
        }
        .dp-head { color: #8b949e; background: #161b22; font-weight: 600; }
        .dp-filled { color: #58a6ff; }
        .dp-hl-col { background: #1c2333 !important; }
        .dp-hl-row { background: #1c2333 !important; }
        .dp-hl-cell { background: #0d419d !important; color: #fff !important; font-weight: bold; }

        /* Call Stack */
        .call-stack {
          display: flex; flex-direction: column; gap: 3px;
          max-height: 200px; overflow-y: auto;
          font-family: 'JetBrains Mono', monospace; font-size: 11px;
        }
        .stack-frame {
          padding: 5px 10px; border-radius: 4px;
          background: #21262d; border-left: 2px solid #30363d;
          transition: all 0.2s;
        }
        .stack-top {
          background: #1c2333; border-left: 3px solid #58a6ff;
          color: #e6edf3;
        }
        .stack-fn { color: #d2a8ff; }
        .stack-visited { color: #a5d6ff; }
        .stack-bits { color: #79c0ff; letter-spacing: 2px; }
        .stack-note { color: #3fb950; font-style: italic; }

        /* Bottom grid */
        .bottom-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px; }

        /* Section legend */
        .legend { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 8px; }
        .legend-item { display: flex; align-items: center; gap: 4px; font-size: 11px; color: #7f8fa6; }
        .legend-dot { width: 10px; height: 10px; border-radius: 50%; }
      `}</style>

      <h1>// TSP · 비트마스크 DP + DFS 시각화</h1>
      <p className="subtitle">4개 도시 외판원 문제 — dp[now][visited] 메모이제이션으로 중복 탐색 제거</p>

      {/* Controls */}
      <div className="controls">
        <button className="btn" onClick={() => { setPlaying(false); setStepIdx(0); }}>⏮ 처음</button>
        <button className="btn" onClick={() => setStepIdx((p) => Math.max(0, p - 1))}>◀ 이전</button>
        <button className={`btn ${playing ? "" : "btn-primary"}`} onClick={() => setPlaying((p) => !p)}>
          {playing ? "⏸ 일시정지" : "▶ 재생"}
        </button>
        <button className="btn" onClick={() => setStepIdx((p) => Math.min(steps.length - 1, p + 1))}>다음 ▶</button>
        <button className="btn" onClick={() => setStepIdx(steps.length - 1)}>마지막 ⏭</button>
        <span className="speed-label">속도:</span>
        <input type="range" min={150} max={1500} step={50} value={speed}
          onChange={(e) => setSpeed(Number(e.target.value))} style={{ width: 80 }} />
        <span className="step-info">{stepIdx + 1} / {steps.length}</span>
      </div>

      <div className="progress-bar">
        <div className="progress-fill" style={{ width: `${steps.length ? (stepIdx / (steps.length - 1)) * 100 : 0}%` }} />
      </div>

      {/* 현재 단계 설명 */}
      <div className="note-box">{cur.note || "..."}</div>

      <div className="layout">
        {/* 왼쪽: 그래프 */}
        <div className="panel">
          <div className="panel-title">🗺 그래프 — 현재 위치 & 경로</div>
          <GraphView
            currentCity={cur.now ?? 0}
            visitedMask={cur.visited ?? 1}
            pathEdges={cur.pathEdges ?? []}
          />
          <div className="legend">
            {CITY_LABELS.map((l, i) => (
              <div key={i} className="legend-item">
                <div className="legend-dot" style={{ background: CITY_COLORS[i] }} />
                <span>{l}</span>
              </div>
            ))}
            <div className="legend-item">
              <div style={{ width: 20, height: 2, background: "#FFE66D" }} />
              <span>현재 경로</span>
            </div>
          </div>
        </div>

        {/* 오른쪽: 비트마스크 설명 + 스택 */}
        <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
          <div className="panel">
            <div className="panel-title">🔢 비트마스크 상태 해석</div>
            <BitMask value={cur.visited ?? 1} size={T} label="visited" />
            <BitMask value={allMask} size={T} label="목표값" />
            <div style={{ marginTop: 8, fontSize: "11px", color: "#7f8fa6", fontFamily: "'JetBrains Mono', monospace", lineHeight: 1.8 }}>
              <div style={{ color: "#d2a8ff" }}>visited == (1 &lt;&lt; T) - 1 이면 모두 방문</div>
              <div>visited &amp; (1 &lt;&lt; next) → next 방문 여부 확인</div>
              <div>visited | (1 &lt;&lt; next) → next 방문 표시</div>
            </div>
          </div>

          <div className="panel">
            <div className="panel-title">📞 재귀 호출 스택 (위가 현재)</div>
            <CallStack stack={cur.stack ?? []} />
          </div>
        </div>
      </div>

      {/* DP 테이블 */}
      <div className="bottom-grid">
        <div className="panel" style={{ gridColumn: "1 / -1" }}>
          <div className="panel-title">💾 DP 테이블 — dp[now][visited] (파란 셀 = 저장된 값, 노란 테두리 = 현재 위치)</div>
          <DPTable
            dp={cur.dp ?? Array.from({ length: T }, () => new Array(1 << T).fill(-1))}
            nowHighlight={cur.now ?? 0}
            visitedHighlight={cur.visited ?? 1}
          />
          <div style={{ marginTop: 10, fontSize: "11px", color: "#7f8fa6", fontFamily: "'JetBrains Mono', monospace" }}>
            · = 미계산 &nbsp;|&nbsp; 숫자 = 메모된 최소비용 &nbsp;|&nbsp; ∞ = 경로없음
          </div>
        </div>
      </div>
    </div>
  );
}
