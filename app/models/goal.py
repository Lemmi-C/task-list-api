from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", backref="goal", lazy=True)

    def to_dict(self):
        
            goal_as_dict = {}
            goal_as_dict["id"] = self.goal_id
            goal_as_dict["title"] = self.title
            return goal_as_dict

    @classmethod
    def from_dict( cls,goal_data):
            new_goal = cls(title=goal_data["title"])
            return new_goal
    
    def tasks_to_dict(self):
            return {
                "id": self.goal_id,
                "title":self.title,
                "tasks":[task.to_dict() for task in self.tasks]
            }
