document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#form");
  if (!form) {
    console.error("Formulário não encontrado!");
    return;
  }

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
      alert(result.message || result.error);

      if (result.success) form.reset();
    } catch (err) {
      console.error("Erro ao enviar formulário:", err);
      alert("Erro ao enviar formulário. Tente novamente.");
    }
  });
});
