from sqlalchemy import Integer, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column

from datetime import datetime, timezone


class AbstractModel:
    id = mapped_column(
        Integer, primary_key=True, autoincrement=True, nullable=False, unique=True, sort_order=-1
    )

    created_at = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc), sort_order=-1
    )


Base = declarative_base(cls=AbstractModel)
