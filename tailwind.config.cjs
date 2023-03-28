/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        'body': ['"Noto Sans"', 'sans-serif'],
        'serif': ['Arvo', 'serif'],
        'display': ['"David Libre"']
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
