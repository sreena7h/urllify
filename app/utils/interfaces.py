from abc import abstractmethod, ABC


class ITextGen(ABC):
    @abstractmethod
    def generate_unique_string(self):
        pass


class IShortURL(ABC):
    text_gen_obj: ITextGen

    @abstractmethod
    def generate(self):
        pass
