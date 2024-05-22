from typing import TYPE_CHECKING, List
import db as _db
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _db.Base.metadata.create_all(bind=_db.engine)



def get_database():
    database = _db.SessionLocal()

    try:
        yield database
    finally:
        database.close()





async def create_contact(contact: _schemas.CreateContact, db: "Session") -> _schemas.Contact:
    contact = _models.Contact(**contact.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return _schemas.Contact.model_validate(contact)



async def get_all_contacts(db: "Session") -> List[_schemas.Contact]:
    contacts = db.query(_models.Contact).all()

    return contacts
    # return list(map(_schemas.Contact.from_attributes, contacts))


async def get_contact(contact_id: int, db:"Session") ->_schemas.Contact:
    contact = db.query(_models.Contact).filter(_models.Contact.id == contact_id).first()
    return contact


async def delete_contact(contact_id: int, db: "Session") -> List[_schemas.Contact]:
    contact = db.query(_models.Contact).filter(_models.Contact.id == contact_id).first()
    db.delete(contact)
    db.commit()
    
    contacts = db.query(_models.Contact).all()

    return contacts

 

async def update_contact(contact_data: _schemas.CreateContact, contact: _models.Contact, db: "Session"):
    contact.first_name = contact_data.first_name
    contact.last_name = contact_data.last_name
    contact.email = contact_data.email
    contact.phone_number = contact_data.phone_number


    db.commit()
    db.refresh(contact)
    return _schemas.Contact.model_validate(contact)