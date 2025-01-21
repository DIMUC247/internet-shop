from typing import List

from sqlalchemy import String,ForeignKey,Table,Column
from sqlalchemy.orm import Mapped,mapped_column,relationship,declarative_base
from flask_sqlalchemy import SQLAlchemy


Base = declarative_base()
db = SQLAlchemy(model_class=Base,engine_options=dict(echo=True))


prod_rev_assoc = Table(
    "prod_rev_assoc",
    Base.metadata,
    Column("prod_id",ForeignKey("products.id"),primary_key=True),
    Column("rev_id",ForeignKey("rewiews.id"),primary_key=True)
)

class Review(Base):
    __tablename__ = "reviews"

    id:Mapped[int] = mapped_column(primary_key=True)
    text:Mapped[str] = mapped_column(String())
    grade:Mapped[int] = mapped_column(String())


class Prosuct(Base):
    __tablename__ = "products"

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]= mapped_column(String())
    description:Mapped[str] = mapped_column(String())
    img_url:Mapped[str] = mapped_column(String())
    reviews: Mapped[List[Review]] = relationship(secondary=prod_rev_assoc)

