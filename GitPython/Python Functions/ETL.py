
from functions import Reader, Transformer,Loader


# could have moved this to the the class but it is not standard practice as it is script logic not a definition
if __name__ == "__main__":
    file_reader = Reader("/Users/dfibi/Downloads/student_test_scores_extended.csv")

print(file_reader[0])
print(file_reader[1])
print(file_reader.read())

"""
Drop columns "Number of Siblings", "Lunch Type", "Test Preparation", "Study Time (hours)", "Favorite Subject" and "Main Teacher"
     number           '5'             '6'            '7'                       '8'                  '9'                '12'
     index            '4'             '5'            '6'                       '7'                  '8'                '11'
"""

transformed = Transformer(file_reader, header_index=0)
print("Before dropping columns:", transformed.get_data())

transformed.drop_columns(["Number of Siblings", "Lunch Type", "Test Preparation", "Study Time (hours)", "Favorite Subject", "Main Teacher"])
print("After dropping non academic score columns:", transformed.get_data())

towrite = Loader(transformed.get_data())
towrite.load(format="csv", delimiter=",", file_name="Just_the_data")