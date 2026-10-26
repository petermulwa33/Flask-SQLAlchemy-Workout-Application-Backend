
from marshmallow import (
    Schema, fields, validate, validates_schema, ValidationError
)


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=100)
    )

    category = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=50)
    )

    equipment_needed = fields.Bool(required=True)


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(dump_only=True)
    exercise_id = fields.Int(dump_only=True)

    reps = fields.Int(
        allow_none=True,
        load_default=None,
        validate=validate.Range(min=1)
    )

    sets = fields.Int(
        allow_none=True,
        load_default=None,
        validate=validate.Range(min=1)
    )

    duration_seconds = fields.Int(
        allow_none=True,
        load_default=None,
        validate=validate.Range(min=1)
    )

    @validates_schema
    def validate_prescription(self, data, **kwargs):
        has_reps_and_sets = (
            data.get("reps") is not None
            and data.get("sets") is not None
        )

        has_duration = data.get("duration_seconds") is not None

        if not has_reps_and_sets and not has_duration:
            raise ValidationError(
                "Provide both reps and sets, or provide duration_seconds."
            )


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)

    date = fields.Date(required=True)

    duration_minutes = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    notes = fields.Str(allow_none=True)

    workout_exercises = fields.Nested(
        WorkoutExerciseSchema,
        many=True,
        dump_only=True
    )

    exercises = fields.Nested(
        ExerciseSchema,
        many=True,
        dump_only=True
    )


class ExerciseDetailSchema(ExerciseSchema):
    workout_exercises = fields.Nested(
        WorkoutExerciseSchema,
        many=True,
        dump_only=True
    )

    workouts = fields.Nested(
        WorkoutSchema,
        many=True,
        dump_only=True
    )

