import Task from "@/types/task";
import TaskInstance from "./instance";

export default function TasksList({ tasks }: { tasks: Task[] }) {
  return (
    <div>
      {tasks.map((task) => (<TaskInstance key={task.id} task={task} />))}
    </div>
  );
}
