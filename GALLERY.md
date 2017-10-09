`doit` gallery
==============

# The idea: users inspired by examples of `doit` usage

`doit` users may inspire each other by sharing their use of `doit`. Even plain output
of `$ doit list` or `$doit list --all` may reveal to others unexpected but valuable way of using
`doit`.

# Proposed content

## Purpose annotation

Short summary of intended use and purpose of given `doit` application. It shall be very short. It
might be handy to use user story format as:

> As a user of my personal notebook I want to be able setting notebook connectivity (wifi, mobile
> internet) up and down from command line as command line is my most favourite UI.

## Short or long list of `doit` tasks

Apart from title, which would described the purpose of given `doit` usage, users would provide
output of `doit list` and `doit list --all`.

    $ doit list
    available   List all available configured connections.
    status      List currently active network connections.
    up          Set given connection up (specific connection name required).
    down        Set given connection down.
    radio       Report status of network radio devices
    radioon     Set network radio device on
    radiooff    Set network radio device off.

To make it more educative and to allow hiding sensitive information from it, it would be allowed to
edit the order of commands and to modify (slightly) the text shown.

The same applies to `$ doit list --all` if it adds any value:


    available       List all available configured connections.
    status          List currently active network connections.
    up              Set given connection up (specific connection name required).
    up:VPN
    up:home
    up:office
    up:hotspot
    up:train
    up:mobile
    down            Set given connection down.
    down:VPN
    down:home
    down:office
    down:hotspot
    down:train
    down:mobile
    radio           Report status of network radio devices
    radioon         Set network radio device on
    radioon:wifi
    radioon:wwan
    radiooff        Set network radio device off.
    radiooff:wifi
    radiooff:wwan

## Example of real usage

Describe more details about usage. Whatever gives the reader better idea about it. No need to be
exhaustive, it shall just inspire, not instruct how to do it.

E.g.:

When I travel by train and want to connect to (already preconfigured) train wifi:

    $ doit up:train
    .  up:train
    Connection succesfully activated (Active D-Bus path: /org/freedesktop/NetworkManager/ActiveConnection/1)

When in aeroplane, before take-off I switch all radio network devices:

    $ doit radiooff
    .  radiooff:wifi
    .  radiooff:wwan

When on the road and in need of mobile connectivity provided by LTE modem within my notebook:

    $ doit up:tm
    .  up:mobile
    Connection succesfully activated (Active D-Bus path: /org/freedesktop/NetworkManager/ActiveConnection/3)

## `doit` added value
What are the main advantages of using given `doit` based solution.

E.g.: Set of `nmcli` calls (e.g. `$ nmcli c up mobile`) packed into well named doit tasks, which are
easy to call and easy to list when one needs to remind how they are named.

## Meta (versions etc.)
Provide information about environment, where it is used, e.g.:

- Python: 3.6
- doit: 0.30.3
- OS: Ubuntu 16.04

## Users
Describe the type of users, their number etc.

- Number of users: 1
- Type of user: developer living on command line

## commands and packages used
Just list what command line tools are expected to be installed and what python packages installed.

### shell commands
- nmcli (network manager CLI)

### python packages
- doit

## dodo file
Did you use `dodo.py`, used another file name and pointed to it via command line switch or this
stuff is embedded into another application?

Is dodo file standalone, imports other python packages of your own or other python packages 

dodo file dependencies:
- standalone dodo file
- import tasks or actions from other modules within the same project
- import tasks or actions from other packages installed

Possibly describe size of the file (number of lines of dodo.py)

Is the code available somewhere? (either url or "no", do not promise publishing as it generates noise as others would ask you to share it really) 

e.g. single dodo file `dodo.py`, 82 lines. Not shared.

## `doit` technologies used

Insight into what `doit` features were used. No need to show off the author knows a lot and uses a
lot, in fact, one can show off, things can be done real simple.

- file dependency (file_dep): yes/no
- task dependency (task_dep): yes/no
- clean task (clean): no/yes/custom
- python-action: yes/no
- cmd-action: yes/no
- calculated uptodate (uptodate): yes/no
- subtasks: yes/no

## Any other interesting stuff

Provide any more details, which might be interesting.

# Collecting and publishing gallery items

Gallery shall not generate too much extra burden and obligations. Expectations are:

- for contributor (of gallery item):
    - easy to add and edit
- for gallery maintainer:
    - do not generate any extra burden, if not necessary
- for gallery visitor:
    - simple to find and read gallery entries.

I was considering following options:
- a blog
- github source repository
- github wiki page
- github issue tracker
- Google Spreadsheet (a form to commit the entry)

In fact, there are two roles: to collect and to publish. In some cases they can be merged.

To me the optimal solution seems github issue tracker in dedicated repository.

# Dedicated Github repository doit-gallery
Here I detail my proposal for using Github repo:

Set up Github repository `pydoit/doit-gallery`.

Create README.rst there, explaining code of conduct:
- purpose of this repository
    - allow sharing information about different `doit` usage
        - contributors file issues describing their case
        - readers read about them
    - nothing more: no code, no issue resolution
- for contributors
    - just file an issue describing your usage. Use the template.
- for maintainers:
    - if feasible, add tags allowing to sort issues/items
- for readers:
    - search issues, learn a bit about different users
    - this is not the place to ask for support

# Roadmap

- Agree on the gallery concept and initial approach
- Set up github repo pydoit/doit-gallery
- Seed with first set of items
- Add README.rst
- Review the approach, fix the code of conduct if needed
- Invite others to contribute
