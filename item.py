
from abc import ABC, abstractmethod
import hashlib
from cryptography.fernet import Fernet
import datetime

class Item(ABC):
    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass

    def generate_checksum(self):
        self.checksum = hashlib.sha256(self.content.encode()).hexdigest()

    def verify_checksum(self):
        new_checksum = hashlib.sha256(self.content.encode()).hexdigest()
        return new_checksum == self.checksum

    @abstractmethod
    def add_timestamp(self):
        pass
    def add_timestamp(self):
        self.creation_time = datetime.datetime.now()
        self.modification_time = self.creation_time
class Lyric(Item):
    def __init__(self, content):
        self.content = content
        self.encrypted_content = None
        self.checksum = None
        self.creation_time = None
        self.modification_time = None
        self.key = Fernet.generate_key()  # Generate a key for this instance
        self.encrypt()
        self.generate_checksum()
        self.add_timestamp()

    def encrypt(self):
        cipher_suite = Fernet(self.key)
        self.encrypted_content = cipher_suite.encrypt(self.content.encode())

    def decrypt(self):
        cipher_suite = Fernet(self.key)
        decrypted_content = cipher_suite.decrypt(self.encrypted_content)
        return decrypted_content.decode()

    def add_timestamp(self):
        self.creation_time = datetime.datetime.now()
        self.modification_time = self.creation_time
    def add_timestamp(self):
        super().add_timestamp()
class MusicScore(Item):
    def __init__(self, content):
        self.content = content
        self.encrypted_content = None
        self.checksum = None
        self.creation_time = None
        self.modification_time = None
        self.key = Fernet.generate_key()  # Generate a key for this instance
        self.encrypt()
        self.generate_checksum()
        self.add_timestamp()

    def encrypt(self):
        cipher_suite = Fernet(self.key)
        self.encrypted_content = cipher_suite.encrypt(self.content.encode())

    def decrypt(self):
        cipher_suite = Fernet(self.key)
        decrypted_content = cipher_suite.decrypt(self.encrypted_content)
        return decrypted_content.decode()

    def add_timestamp(self):
        self.creation_time = datetime.datetime.now()
        self.modification_time = self.creation_time
    def add_timestamp(self):
        super().add_timestamp()
class AudioRecording(Item):
    def __init__(self, content):
        self.content = content
        self.encrypted_content = None
        self.checksum = None
        self.creation_time = None
        self.modification_time = None
        self.key = Fernet.generate_key()  # Generate a key for this instance
        self.encrypt()
        self.generate_checksum()
        self.add_timestamp()

    def encrypt(self):
        cipher_suite = Fernet(self.key)
        self.encrypted_content = cipher_suite.encrypt(self.content.encode())

    def decrypt(self):
        cipher_suite = Fernet(self.key)
        decrypted_content = cipher_suite.decrypt(self.encrypted_content)
        return decrypted_content.decode()

    def add_timestamp(self):
        self.creation_time = datetime.datetime.now()
        self.modification_time = self.creation_time
    def add_timestamp(self):
        super().add_timestamp()
        
class ItemFactory:
    @staticmethod
    def create_item(item_type, content):
        if item_type == "lyric":
            return Lyric(content)
        elif item_type == "music_score":
            return MusicScore(content)
        elif item_type == "audio_recording":
            return AudioRecording(content)
        else:
            raise ValueError("Invalid item type")