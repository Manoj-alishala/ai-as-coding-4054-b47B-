courses = {}
def add_course(course_id, name, credits):
    """
    Adds a course to the course management system.

    Parameters:
    course_id (str): The unique identifier for the course.
    name (str): The name of the course.
    credits (int): The number of credits for the course.

    Returns:
    None
    """
    courses[course_id] = {'name': name, 'credits': credits}
def remove_course(course_id):
    """Removes a course from the course management system.
    Parameters:
    course_id (str): The unique identifier for the course to be removed.
    Returns:
    None
    """
    if course_id in courses:
        del courses[course_id]

def get_course(course_id):
    """
    Retrieves the details of a course from the course management system.

    Parameters:
    course_id (str): The unique identifier for the course to be retrieved.

    Returns:
    dict: A dictionary containing the name and credits of the course, or None if the course does not exist.
    """
    return courses.get(course_id)

print(get_course('CS101'))  # Output: None
add_course('CS101', 'Introduction to Computer Science', 4)
print(get_course('CS101'))  # Output: {'name': 'Introduction to Computer Science', 'credits': 4}
remove_course('CS101')
print(get_course('CS101'))  # Output: None
# To display the module documentation in the terminal, you can use the following code:
import pydoc
print(pydoc.render_doc('course'))
