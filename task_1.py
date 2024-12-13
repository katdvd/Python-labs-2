import doctest


class Book:
    """
    A class of a book with a title, author, and number of pages.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Creates a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            pages (int): The number of pages in the book. Must be positive.

        Raises:
            ValueError: If pages is not a positive integer.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.title
        '1984'
        >>> book.pages
        328
        """
        self.title = title
        self.author = author
        if pages <= 0:
            raise ValueError("Number of pages must be positive.")
        self.pages = pages

    def read_pages(self, pages_read: int) -> int:
        """
        Reads a certain amount of book pages.

        Args:
            pages_read (int): The number of pages to read. Must be positive and not exceed remaining pages.

        Returns:
            int: The remaining number of pages.

        Raises:
            ValueError: If pages_read is not positive or exceeds remaining pages.

        >>> book = Book("1984", "George Orwell", 262)
        >>> remaining = book.read_pages(50)
        >>> remaining
        212
        """
        if pages_read <= 0:
            raise ValueError("Pages read must be positive.")
        if pages_read > self.pages:
            raise ValueError("Cannot read more pages than are available.")
        self.pages -= pages_read
        return self.pages

    def get_summary(self, summary: str = "No summary provided.") -> str:
        """
        Provides a summary of the book.

        Args:
            summary (str, optional): A brief summary of the book. Defaults to "No summary provided."

        Returns:
            str: A formatted summary string.

        >>> book = Book("1984", "George Orwell", 262)
        >>> summary = book.get_summary("A dystopian novel.")
        >>> summary
        '1984 by George Orwell: A dystopian novel.'
        """
        return f"{self.title} by {self.author}: {summary}"


class Car:
    """
    Represents a car with a make, model, and fuel level.
    """

    def __init__(self, make: str, model: str, fuel_level: float):
        """
        Initializes a new Car instance.

        Args:
            make (str): The manufacturer of the car.
            model (str): The model of the car.
            fuel_level (float): The current fuel level in liters. Must be non-negative.

        Raises:
            ValueError: If fuel_level is negative.

        >>> car = Car("Tesla", "model y", 50.0)
        >>> car.make
        'Tesla'
        >>> car.fuel_level
        50.0
        """
        self.make = make
        self.model = model
        if fuel_level < 0:
            raise ValueError("Fuel level cannot be negative.")
        self.fuel_level = fuel_level

    def drive(self, distance: float) -> float:
        """
        Drives the car a specified distance, consuming fuel.

        Args:
            distance (float): The distance to drive in km. Must be positive.

        Returns:
            float: The remaining fuel level.

        Raises:
            ValueError: If distance is not positive or fuel is insufficient.

        >>> car = Car("Toyota", "Corolla", 50.0)
        >>> remaining_fuel = car.drive(100.0)
        >>> remaining_fuel
        40.0
        """
        fuel_consumption_per_km = 0.1
        if distance <= 0:
            raise ValueError("Distance must be positive.")
        required_fuel = distance * fuel_consumption_per_km
        if required_fuel > self.fuel_level:
            raise ValueError("Insufficient fuel to drive the distance.")
        self.fuel_level -= required_fuel
        return self.fuel_level

    def refuel(self, amount: float = 10.0) -> None:
        """
        Refuels the car by a certain amount.

        Args:
            amount (float, optional): The amount of fuel to add in liters. Defaults to 10.0.

        Raises:
            ValueError: If amount is not positive.

        >>> car = Car("Toyota", "Corolla", 40.0)
        >>> car.refuel(20.0)
        >>> car.fuel_level
        60.0
        >>> car.refuel()
        >>> car.fuel_level
        70.0
        """
        if amount <= 0:
            raise ValueError("Refuel amount must be positive.")
        self.fuel_level += amount


class UserProfile:
    """
    Is a user profile with a username, number of friends, and posts.
    """

    def __init__(self, username: str, friends: int, posts: int):
        """
        Creates a new UserProfile instance.

        Args:
            username (str): The username of the profile.
            friends (int): The number of friends. Must be non-negative.
            posts (int): The number of posts. Must be non-negative.

        Raises:
            ValueError: If friends or posts are negative.

        >>> profile = UserProfile("Sample name", 150, 45)
        >>> profile.username
        'Sample name'
        >>> profile.friends
        150
        >>> profile.posts
        45
        """
        self.username = username
        if friends < 0:
            raise ValueError("Number of friends cannot be negative.")
        self.friends = friends
        if posts < 0:
            raise ValueError("Number of posts cannot be negative.")
        self.posts = posts

    def add_friends(self, new_friends: int) -> int:
        """
        Adds a certain number of friends to the profile.

        Args:
            new_friends (int): The number of friends to add. Must be positive.

        Returns:
            int: The updated number of friends.

        Raises:
            ValueError: If new_friends is not positive.

        >>> profile = UserProfile("john_doe", 150, 45)
        >>> updated_friends = profile.add_friends(10)
        >>> updated_friends
        160
        """
        if new_friends <= 0:
            raise ValueError("Number of new friends must be positive.")
        self.friends += new_friends
        return self.friends

    def create_post(self, content: str = "No content.") -> None:
        """
        Creates a new post on the profile.

        Args:
            content (str, optional): The content of the post. Defaults to "No content."

        >>> profile = UserProfile("john_doe", 150, 45)
        >>> profile.create_post("Hello World!")
        New post created: Hello World!
        >>> profile.posts
        46
        >>> profile.create_post()
        New post created: No content.
        >>> profile.posts
        47
        """
        self.posts += 1
        print(f"New post created: {content}")


if __name__ == "__main__":
    doctest.testmod()

    book = Book("Sample name", "Sample author", 180)
    print(book.get_summary("Lorem ipsum dolor sit amet, consectetuer adipiscing elit."))
    remaining_pages = book.read_pages(30)
    print(f"Pages left: {remaining_pages}")

    car = Car("UAZ", "Patriot", 40.0)
    print(f"Fuel level: {car.fuel_level} l")
    car.drive(150)
    print(f"Fuel level: {car.fuel_level} l")
    car.refuel()
    print(f"Fuel level: {car.fuel_level} l")

    profile = UserProfile("Sample name", 200, 50)
    profile.add_friends(25)
    profile.create_post("Hello world!")