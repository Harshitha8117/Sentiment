document.getElementById("analyzeBtn").addEventListener("click", async () => {
  const review = document.getElementById("review").value.trim();
  const result = document.getElementById("result");

  if (!review) {
    result.innerHTML = `<div class="text-red-600">Please enter a review first.</div>`;
    return;
  }

  const res = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ review }),
  });

  const data = await res.json();

  result.innerHTML = `
    <div class="text-3xl">${data.emoji}</div>
    <div class="mt-2">${data.description} (${data.sentiment.toUpperCase()})</div>
  `;

  // Animate result (clean reflow + bounce)
  result.classList.remove("scale-90", "scale-110");
  void result.offsetWidth; // trigger reflow
  result.classList.add("scale-110");
  setTimeout(() => result.classList.remove("scale-110"), 300);
});
