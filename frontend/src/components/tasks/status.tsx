const statusColorMapping: Record<string, string> = {
  'PENDING': 'text-info border border-info',
  'SUCCESS': 'text-success border border-success',
  'FAILED': 'text-error border border-error',
};


function getStatusClasses(status: string) {
  const classes = 'px-2 py-1 rounded-full text-xs font-semibold';
  return `${classes} ${statusColorMapping[status]}`;
}


export default function TaskStatus({ status }: { status: string }) {
  return (
    <span className={getStatusClasses(status)}>{status}</span>
  );
}
