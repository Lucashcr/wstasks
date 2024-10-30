import Task from "@/types/task";
import TaskStatus from "./status";

export default function TaskInstance({ task }: { task: Task }) {
  return (
    <div key={task.id} className="p-4 border border-zinc-500 my-2 rounded-xl flex justify-between">
      <div>
        <h2>ID: {task.id}</h2>
        <p>Created at: {task.getFormattedCreatedAt()}</p>
        <p>Updated at: {task.getFormattedUpdatedAt()}</p>
      </div>
      <div>
        <TaskStatus status={task.status} />
      </div>
    </div>
  );
}
