enum TaskStatus {
  PENDING = 'PENDING',
  SUCCESS = 'SUCCESS',
  FAILED = 'FAILED',
}


export type TaskJson = {
  id: string;
  name: string;
  status: TaskStatus;
  createdAt: string;
  updatedAt: string;
}


class Task {
  id: string;
  name: string;
  status: TaskStatus;
  createdAt: Date;
  updatedAt: Date;

  constructor(id: string, name: string, status: TaskStatus, createdAt: Date, updatedAt: Date) {
    this.id = id;
    this.name = name;
    this.status = status;
    this.createdAt = createdAt;
    this.updatedAt = updatedAt;
  }

  static fromJson(json: TaskJson): Task {
    return new Task(
      json.id,
      json.name,
      json.status,
      new Date(json.createdAt),
      new Date(json.updatedAt),
    );
  }

  toJson(): Record<string, unknown> {
    return {
      id: this.id,
      name: this.name,
      status: this.status,
      createdAt: this.createdAt.toISOString(),
      updatedAt: this.updatedAt.toISOString(),
    };
  }

  getFormattedCreatedAt(): string {
    return this.createdAt.toLocaleString('pt-br');
  }

  getFormattedUpdatedAt(): string {
    return this.updatedAt.toLocaleString('pt-br');
  }
}

export default Task;