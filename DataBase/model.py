from aiogram.types import DateTime
from sqlalchemy import BigInteger, String, Integer, ForeignKey, CheckConstraint, Time
from sqlalchemy.orm import mapped_column,DeclarativeBase,Mapped,relationship,Session
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker,create_async_engine

engine = create_async_engine(url = 'postgresql+asyncpg://postgres:admin@localhost/postgres')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50),nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    tg_id = mapped_column(BigInteger, nullable=False)
    role: Mapped[str]  = mapped_column(nullable=False)
    reg_user: Mapped["Registration_study"] = relationship(back_populates='user')

class Lesson(Base):

    __tablename__ = 'lessons'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    datetime: Mapped[str] = mapped_column(String(100))
    time_lesson:Mapped[str] = mapped_column(String(20))

    reg_lesson: Mapped["Registration_study"] = relationship(back_populates="lesson")

class Registration_study(Base):

    __tablename__ = 'registrations'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id',onupdate='CASCADE', ondelete='CASCADE'))
    lesson_id: Mapped[int] = mapped_column(ForeignKey('lessons.id',onupdate='CASCADE', ondelete='CASCADE'))

    lesson: Mapped['Lesson'] = relationship(back_populates='reg_lesson')
    user: Mapped["User"] = relationship(back_populates='reg_user')


async def async_main():

    async with engine.begin() as curs:
        await curs.run_sync(Base.metadata.create_all)


