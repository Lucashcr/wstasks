import { useMemo } from "react";

export default function Footer() {
  const year = useMemo(() => new Date().getFullYear(), []);

  return (
    <footer className="w-full flex flex-col align-center bg-zinc-700 p-4">
      <p className="text-center text-xs">Lucas Rocha &copy; {year}</p>
    </footer>
  );
}
