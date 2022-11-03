#pytest -rA -k test_ -v----->match string
#pytest -rA---f for failed,e for error
#pytest -h
#pytest -rA -k test_ -v----->-all with more info
#pytest -rA -k test_ -v----->
#py.test -v --browser_name Edge
#py.test -rA --junitxml='report.xml'-->to get in xml report
#pytest tests/------ to get in htm report default directory
#pytest tests/ --html-report=./report --->to get in htm report specifie directory
#pytest test_e2e.py -m sampletest======>smoke or sanity
#pytest.mark.sanity
# #pytest.mark.parametrize("uname,password",[("ass","nnnn"),("hhh","dss")]

#for customized markers
#pytest.ini
#[pytest]
#addopts=-rA --html=Automation.html
#markers=
    #smoke:smoke tests
    #sanity:sanity tests

#pytest fixtures offer dramatic improvements over the classic xUnit style of setup/teardown functions:

#fixtures have explicit names and are activated by declaring their use from test functions, modules, classes or whole projects.
#fixtures are implemented in a modular manner, as each fixture name triggers a fixture function which can itself use other fixtures.
#Arrange,act,assert,cleanup
#precond
#setup,conn,API

#test
#test

#postcondition
#clean,close

#parallel excution
#pytest-xdist

#pytest test_fixtures.py -n 3(no of process)