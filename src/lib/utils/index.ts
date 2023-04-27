export const formatDate = (x: string | Date) => {
  const d = new Date(x);
  const months = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"];

  return `${d.getDate()} ${months[d.getMonth()]} ${d.getFullYear()}`;
};

export const LIST_TO_NAME = {
  insiemepersona: "Insieme per Sona",
  viviamosona: "Viviamo Sona",
};
