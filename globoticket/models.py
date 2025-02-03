import decimal
from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from datetime import date

from globoticket.database import SessionLocal

Base = declarative_base()

class DBCategory(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)


class DBEvent(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_code: Mapped[str] = mapped_column(unique=True)
    date: Mapped[date]
    price: Mapped[decimal.Decimal]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped[DBCategory] = relationship()

    def __str__(self):
        return f"{self.id}: {self.product_code:10} {self.category.name:10} {self.date} ${self.price}"


session = SessionLocal()
results = session.execute(select(DBCategory)).scalars()
print("\n".join(category.name for category in results))

results = session.execute(select(DBEvent)).scalars()
print("\n".join(str(event) for event in results))