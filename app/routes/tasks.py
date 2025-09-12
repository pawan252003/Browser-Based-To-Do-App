from flask import Blueprint, redirect, request, url_for, flash, render_template, session
from app import db
from app.models import Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def view_task():
    if "user_id" not in session:
        flash("Please login first!", "error")
        return redirect(url_for("auth.login"))

    # Show only the tasks for this user
    tasks = Task.query.filter_by(user_id=session["user_id"]).all()
    return render_template("tasks.html", tasks=tasks)


@tasks_bp.route('/add', methods=["POST"])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for("auth.login"))
    
    title = request.form.get("title")
    if title:
        new_task = Task(title=title, status="Pending", user_id=session['user_id'])
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully", "success")
    
    return redirect(url_for("tasks.view_task"))

@tasks_bp.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_status(task_id):
    task = Task.query.filter_by(id=task_id, user_id=session['user_id']).first()
    if task:
        if task.status == "Pending":
            task.status = "Working"
        elif task.status == "Working":
            task.status = "Done"
        else:
            task.status = "Pending"
        db.session.commit()
    return redirect(url_for("tasks.view_task"))

@tasks_bp.route("/tasks/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully", "success")
    return redirect(url_for("tasks.view_task"))


@tasks_bp.route("/clear", methods=["POST"])
def clear_task():
    Task.query.filter_by(user_id=session['user_id']).delete()
    db.session.commit()
    flash("All your tasks cleared", "success")
    return redirect(url_for("tasks.view_task"))

