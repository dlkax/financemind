document.querySelector("#form").addEventListener("submit", async (e) => {
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


    if (!res.ok) {
      const errText = await res.text();
      console.error("Erro de resposta:", errText);
      alert("Erro no servidor. Tente novamente.");
      return;
    }

    const result = await res.json();
    alert(result.message || "Lead salvo com sucesso!");
    
    // Limpa o formulário se der certo
    if (result.success) {
      document.querySelector("#form").reset();
    }

  } catch (err) {
    console.error("Erro ao enviar formulário:", err);
    alert("Erro ao enviar o formulário. Verifique sua conexão e tente novamente.");
  }
  src="/static/js/form.js"
});