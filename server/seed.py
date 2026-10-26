
from datetime import date, timedelta

from app import app
from models import db, Exercise, Workout, WorkoutExercise


with app.app_context():
    db.drop_all()
    db.create_all()

    pushups = Exercise(
        name="Push-ups",
        category="Strength",
        equipment_needed=False
    )

    squats = Exercise(
        name="Squats",
        category="Strength",
        equipment_needed=False
    )

    plank = Exercise(
        name="Plank",
        category="Core",
        equipment_needed=False
    )

    workout1 = Workout(
        date=date.today(),
        duration_minutes=45,
        notes="Upper body training"
    )

    workout2 = Workout(
        date=date.today() - timedelta(days=1),
        duration_minutes=30,
        notes="Core and legs"
    )

    db.session.add_all([
        pushups, squats, plank, workout1, workout2
    ])
    db.session.flush()

    db.session.add_all([
        WorkoutExercise(
            workout=workout1,
            exercise=pushups,
            sets=3,
            reps=12
        ),
        WorkoutExercise(
            workout=workout2,
            exercise=squats,
            sets=4,
            reps=15
        ),
        WorkoutExercise(
            workout=workout2,
            exercise=plank,
            duration_seconds=60
        )
    ])

    db.session.commit()

    print("Database seeded successfully.")
