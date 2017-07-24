Feature: Contact group CRUD
    Description

    Scenario Outline: Add new group
       Given a group list
       Given a new group with <name>, <header>, <footer>
       When I add this group to the list
       Then a new group list is equal to the old list with this new group

       Examples:
       | name       | header     | footer |
       | wqerqwrFGH | New header | ghjghv |
       | 123%^&*    | 456^&*(    | )(*!98 |
       | новаЯ груп | ПРОЛПО лдл | ДШРТои |

    Scenario:

