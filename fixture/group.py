from model.group import Group
from  model.contact import Contact

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))) > 0:
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def edit_first_group(self, new_group_data):
        self.edit_group_by_index(0, new_group_data)

    def edit_group_by_index(self,index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit edit
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def edit_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit edit
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    group_cashe = None

    def get_group_list(self):
        if self.group_cashe is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cashe = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cashe.append(Group(name=text, id=id))
        return list(self.group_cashe)


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_in_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        contact_list = []
        wd.get("http://localhost/addressbook/index.php?group=%s" % group.id)
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name("td")
            firstname = cells[2].text
            lastname = cells[1].text
            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            contact_list.append(Contact(id = str(id), lastname=lastname, firstname=firstname))
        return contact_list