/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        'body': ['Outfit', 'sans-serif'],
        'serif': ['Sentient', 'serif']
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
