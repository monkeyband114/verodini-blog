/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./base/**/**/*.html"],
  theme: {
    screens: {
      sm: "480px",
      md: "768px",
      lg: "976px",
      xl: "1440px",
    },
    extend: {
      colors: {
        mainBlue: "hsla(176, 100%, 36%, 1)",
        lightGrey1: "#EFF0F3",
        lightGrey2: "#E4E5E9",
        mainGrey: "#C0C0C0",
        darkGrey: "#9A9494",
        mainBlack: "#2B2C34",
      },
    },
  },
  plugins: [],
};
