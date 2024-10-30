/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#5151AD',
        'accent': '#777772',
        'error': '#FF6363',
        'success': '#4CAF50',
        'warning': '#FFC107',
        'info': '#2196F3',
      },
    },
  },
  plugins: [],
}
