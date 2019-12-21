from danylenkoka.validator.lib import *
from danylenkoka.integration.valids import *
from danylenkoka.integration.dataset_structure_common import integrated_dataset



def new_line_insert(db):
    district_name = input('Введите название раойна:\n')
    boroname = boroname_validator("Введите значение boroname:\n")
    cb_num = cb_num_validator("Введите значение cb_num:\n")
    st_accem = st_accem_validator("Введите значение st_accem:\n")
    st_senate = st_senate_validator("Введите значение st_senate:\n")

    vert_wall = vert_wall_validator(input("Введите значение vert_wall:\n"))
    wire_2nd = wire_2nd_validator(input("Введите значение wire_2nd:\n"))
    cen_year = cen_year_validator(input("Введите значение cen_year:\n"))
    tree_loc = tree_loc_validator(input("Введите значение tree_loc:\n"))


    db.update({district_name:{'boroname':boroname, 'cb_num': cb_num, 'st_accem': st_accem, 'st_senate': st_senate, 'vert_wall': vert_wall,'wire_2nd':wire_2nd,'cen_year':cen_year,'tree_loc':tree_loc,}})
    return db

print(new_line_insert(integrated_dataset))