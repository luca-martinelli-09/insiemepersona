export interface Post {
  id: string;
  date: Date;
  title: string;
  abstract: string;
  image: string;
}

export interface Candidato {
  id: string;
  name: string;
  surname: string;
  gender: "M" | "F";
  birthday: Date;
  birthplace: string;
  location: string;
  type: "consigliere" | "sindaco";
  image: string;
  cv: string;
  casellario: string;
  list: ("viviamosona" | "insiemepersona")[];
}