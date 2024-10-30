import { toast } from "react-toastify";

interface createNewTaskProps {
  updateTasksCallback: () => Promise<void>;
}

async function createNewTask(updateTasksCallback: () => Promise<void>) {
  const response = await fetch("http://localhost:8000/create-task", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({}),
  });

  if (response.ok) {
    updateTasksCallback();
    toast.success("Task created successfully", {
      position: "top-right",
    });
  } else {
    toast.error("Failed to create task");
  }
}

export default function DispatchTask({updateTasksCallback}: createNewTaskProps) {
  return (
    <div className="flex justify-end">
      <button
        className="bg-primary py-2 px-4 rounded-full"
        onClick={() => createNewTask(updateTasksCallback)}
      >
        Create new task
      </button>
    </div>
  );
}
