"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   a) Encapsulation: Keeping the logic (methods) as close to the data (attributes)
      as possible. This also helps us organize code into discrete chunks which
      increases scalability. 
    
   b) Abstraction: Making code as humanly-readable as possible. We don't have to
      know exactly how a function/method works to be able to use it.

   c) Polymorphism: You can use different things in the same way and get an
      expected result. For example, you can add integers and concatenate strings
      together with the '+' operator.

2. What is a class?

   A class is an object that can contain attributes and methods. They can provide
   initial values for their instances and contain implemenations of methods which
   act on those instances.

3. What is an instance attribute?

   An instance attribute is data that descrpolymorphismibes an instance of a class. Different
   instances can have the same attributes with different values. 

4. What is a method?

   A method is a function that acts on an instance. Methods are created in classes.
   A method can only be called from objects of the class(es) it belongs to.

5. What is an instance in object orientation?

   When we create a new object of a certain class, that object is an instance of
   that class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute describes the class and all of its instances. It is often
   used to provide an initial value for all instances of its class. An instance
   value is data that only belongs to that particular instance.

   We might set an attribute as a class attribute when all instances will be
   instantiated with the same value for that attribute. For example, if all Car
   objects start out with grey hubcaps, we would set hubcaps = 'grey' as a class
   attribute.

   We use instance attributes when each instance will probably have different
   values for the same attribute. For example, Car objects can have different
   makes and models. One instance of Car could have make = 'Toyota' and another
   instance could have make = 'Subaru

"""


class Student(object):
    """A student with a first name, last name, and address."""

    def __init__(self, first_name, last_name, address):
        """Initializes a student with first_name, last_name, and address as
        strings.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __str__(self):
        """Stringify student.

        Returns first name and last name.
        """

        return '%s %s' % (self.first_name, self.last_name)


class Question(object):
    """A question in an exam. It has one correct answer."""

    def __init__(self, question, correct_answer):
        """Initializes a question with the question and correct_answer as 
        strings.
        """

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Prints question to console and prompts user of an answer.

        Returns True or False depending on whether the correct answer matches
        the user's answer.
        """

        answer = raw_input(self.question + ' > ')

        if answer.lower() == self.correct_answer.lower():
            return True

        return False


class Exam(object):
    """An exam.

    It has a name, which is the type of exam it is, and it has a list of
    questions.
    """

    def __init__(self, name):
        """Initializes an exam with a name as a string and a list of questions.
        """

        self.questions = []
        self.name = name

    def __str__(self):
        """Returns the name of the exam."""

        return self.name

    def add_question(self, question, correct_answer):
        """Makes a Question and adds it to the exam's list of questions."""

        self.questions.append(Question(question, correct_answer))

    def administer(self):
        """Administers all of the exam's questions and returns the user's score.

        User's score is returned as a percent score.
        """

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return score / float(len(self.questions))


class Quiz(Exam):
    """A quiz."""

    def administer(self):
        """Administers all of the quiz's questions and returns true if the user
        passed.

        Returns false if user answers less than half of the questions correctly.
        """

        score = super(Quiz, self).administer()

        if score >= 0.5:
            return True
        return False


def take_test(exam, student):
    """Administers an exam to a student and assigns the score to the student.

    Prints a message to the screen indicating the score.
    """

    score = exam.administer()
    student.score = score

    print "%s's score for %s: %s" % (student, exam, score)


def example():
    exam = Exam('quiz')
    exam.add_question('Spell "apple"', 'apple')
    exam.add_question('Spell "berry"', 'berry')
    exam.add_question('Spell "cherry"', 'cherry')

    student = Student('Big', 'Bird', '123 Sesame Street')

    take_test(exam, student)
