/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./{static,templates}/**/*.{html,js}"],
    theme: {
      extend: {},
    },
    plugins: [require("daisyui")],
    daisyui: {
      themes: ["light", "dark", "forest"],
    }
  }