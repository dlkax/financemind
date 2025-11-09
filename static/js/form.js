document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#form");
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      name: document.querySelector("#name").value.trim(),
      email: document.querySelector("#email").value.trim(),
      phone: document.querySelector("#phone").value.trim(),
    };

    if (!data.name || !data.email || !data.phone) {
      alert("Por favor, preencha todos os campos!");
      return;
    }

    try {
      const res = await fetch(window.location.origin + "/salvar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      const result = await res.json();
      if (res.ok) {
        alert(result.message || "Lead salvo com sucesso!");
        form.reset();
      } else {
        alert("Erro no servidor: " + (result.message || "tente novamente."));
      }
    } catch (err) {
      console.error("Erro ao enviar:", err);
      alert("Erro ao enviar o formulário. Tente novamente.");
    }
  });
});
