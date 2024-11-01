import { useCallback, useEffect, useRef, useState } from "react";

import Footer from "@/components/base/footer";
import Header from "@/components/base/header";
import Main from "@/components/base/main";
import DispatchTask from "@/components/buttons/dispatch-task";
import TasksList from "@/components/tasks/list";
import PaginationRoot from "./components/pagination/root";

import Task, { TaskJson } from "@/types/task";

import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const toastStyle = {
  success: "bg-success",
  error: "bg-error",
  info: "bg-info",
  warning: "bg-warning",
  default: "bg-primary",
  dark: "bg-accent",
};

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const fetchTasks = useCallback(async () => {
    const urlParams = new URLSearchParams({
      page: page.toString(),
    });
    const response = await fetch(`http://127.0.0.1:8000?${urlParams}`);
    const data = await response.json();
    const tasks = data.tasks.map((task: TaskJson) => Task.fromJson(task));
    setTasks(tasks);
    setTotalPages(data.totalPages);
  }, [page]);

  useEffect(() => {
    fetchTasks();
  }, [fetchTasks]);

  const ws = useRef<WebSocket | null>(null);

  useEffect(() => {
    ws.current = new WebSocket("ws://127.0.0.1:8000/ws/tasks");

    ws.current.onopen = () => {
      console.log("WebSocket connected");
    };

    ws.current.onmessage = (message) => {
      const data = JSON.parse(message.data);

      if (!data.task_id) {
        return;
      }
      switch (data.status) {
        case "SUCCESS":
          toast.success(`Task ${data.task_id} completed`);
          break;
        case "FAILURE":
          toast.error(`Task ${data.task_id} failed`);
          break;
        case "PENDING":
          toast.info(`Task ${data.task_id} is in progress`);
          break;
      }

      fetchTasks();
    }

    ws.current.onclose = () => {
      console.log("WebSocket closed");
    };

    return () => {
      ws.current?.close();
    };
  }, [fetchTasks]);

  return (
    <>
      <Header />
      <Main>
        <DispatchTask updateTasksCallback={fetchTasks} />
        <TasksList tasks={tasks} />
        <PaginationRoot page={page} setPage={setPage} totalPages={totalPages} />
      </Main>
      <Footer />
      <ToastContainer
        toastClassName={(context) =>
          toastStyle[context?.type || "default"] +
          " relative flex p-3 mb-2 min-h-10 rounded-md justify-between overflow-hidden cursor-pointer"
        }      
        position="top-left"
        autoClose={3000}
        closeOnClick
        pauseOnFocusLoss
        pauseOnHover
        theme="colored"
      />
    </>
  );
}

export default App;
