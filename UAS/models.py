from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Baju(Base):
    __tablename__ = 'Data_PemilihanBaju'
    No: Mapped[str] = mapped_column(primary_key=True)
    Tipe_Kain: Mapped[str] = mapped_column()
    Bahan: Mapped[int] = mapped_column()
    Aktivitas: Mapped[int] = mapped_column()
    Harga: Mapped[int] = mapped_column()
    Cuaca: Mapped[int] = mapped_column()
    Panjang_Lengan: Mapped[int] = mapped_column()  
    
    def __repr__(self) -> str:
        return f"Baju(No={self.No!r}, Harga={self.Harga!r})"
