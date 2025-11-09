document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form");

  if (!form) {
    console.error("❌ Formulário não encontrado no DOM.");
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
      alert("Por favor, preencha todos os campos.");
      return;
    }

    try {
      const res = await fetch("/salvar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (!res.ok) {
        const text = await res.text();
        throw new Error(text);
      }

      const result = await res.json();
      alert(result.message || "Lead enviado com sucesso!");
      form.reset();
    } catch (err) {
      console.error("Erro ao enviar:", err);
      alert("Erro ao enviar formulário.");
    }
  });
});
