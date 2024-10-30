type PaginationRootProps = {
  page: number,
  totalPages: number
  setPage: (page: number) => void,
}


export default function PaginationRoot({page, setPage, totalPages}: PaginationRootProps) {
  const pageRange = Array.from({ length: totalPages }, (_, i) => i + 1);

  return (
    <div className="flex justify-center items-center space-x-2">
      <button className="bg-gray-700 text-white px-4 py-2 rounded-lg">Previous</button>
      {pageRange.map((pageNumber) => (
        <button
          key={pageNumber}
          className={`px-4 py-2 rounded-lg ${pageNumber === page ? 'bg-gray-700 text-white' : 'bg-gray-300'}`}
          onClick={() => setPage(pageNumber)}
        >
          {pageNumber}
        </button>
      ))}
      <button className="bg-gray-700 text-white px-4 py-2 rounded-lg">Next</button>
    </div>
  );
}