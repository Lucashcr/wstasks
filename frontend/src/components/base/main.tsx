type MainProps = {
  children: React.ReactNode;
};


export default function Main({children}: MainProps) {
  return (
    <main className="flex-grow max-w-[1280px] w-full mx-auto p-8">
      {children}
    </main>
  );
}
