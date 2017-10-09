===================================
dodo.py for Network Manager (nmcli)
===================================

The file shall allow simpler interaction with network manager `nmcli` from command line, e.g.::

    $ donet up:work_lan2

will connect to your already configured connection named `work_lan2`.

To switch all radio devices on your notebook down::

    $ donet radiooff

and you are ready to take off.

Quick Start
===========

Initial examples shall be run from the directory with `dodo.py` file.

Later on we will show, how to run it from anywhere using arbitrary name.

Run the command the first time:: 

    $ doit
    WARNING: File .connections not found.
    To create one, call subcommand: init
    Feel free to shorten the connection list.
    === Short list of subcommands:
    available   List all available configured connections.
    down        Set given connection down.
    init        (re)create file .connections listing connection names to use
    radio       Report status of network radio devices
    radiooff    Set network radio device off.
    radioon     Set network radio device on
    status      List currently active network connections.
    up          Set given connection up (specific connection name required).
    === For complete list use subcommand: list --all


Before fixing the problem with missing `.connections` file, lets list all current subcommands::

    $ doit list --all
    WARNING: File .connections not found.
    To create one, call subcommand: init
    Feel free to shorten the connection list.
    available       List all available configured connections.
    down            Set given connection down.
    init            (re)create file .connections listing connection names to use
    radio           Report status of network radio devices
    radiooff        Set network radio device off.
    radiooff:wifi
    radiooff:wwan
    radioon         Set network radio device on
    radioon:wifi
    radioon:wwan
    status          List currently active network connections.
    up              Set given connection up (specific connection name required).

Note, that the `radiooff` and `radioon` show names after colon, but `up` and `down` does not as we
miss names of connections to set up or down.

Lets create `.connections` file::

    $ doit init
    WARNING: File .connections not found.
    To create one, call subcommand: init
    Feel free to shorten the connection list.
    .  init

    $ cat .conections
    home
    work

Actual content of the file will differ as it shows exact connection names on your computer.

If you feel there are too many names, feel free to delete the lines which you are not going to
manage using this utility.

Listing all subcommands shows different result::

    $ doit list --all
    available       List all available configured connections.
    down            Set given connection down.
    down:home
    down:work
    init            (re)create file .connections listing connection names to use
    radio           Report status of network radio devices
    radiooff        Set network radio device off.
    radiooff:wifi
    radiooff:wwan
    radioon         Set network radio device on
    radioon:wifi
    radioon:wwan
    status          List currently active network connections.
    up              Set given connection up (specific connection name required).
    up:home
    up:work

We see, that for each connection name present in `.connections` there is one extra item for
`up:{name}` and `down:{name}`.

Assuming you are working at home and use WiFi `home`, `status` shall show something like::

    $ doit status
    .  status
    NAME             UUID                                  TYPE             DEVICE
    home             eaaf269a-34ec-4e5e-8c64-6cfba2d9777c  802-11-wireless  wlp4s0

Now put it down::

    $ doit down:home
    .  down:kemp
    Connection 'home' successfully deactivated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/1)

and we check the status::

    $ doit status
    .  status
    NAME             UUID                                  TYPE             DEVICE

where will be no item. Note, that if you use multiple connections, your results will differ.

To set the connection up again::

    $ doit up:kemp
    .  up:kemp
    Spojení úspěšně aktivováno (D-Bus aktivní cesta: /org/freedesktop/NetworkManager/ActiveConnection/3)

Note, that to change the WiFi you use, there is no need to set it `down` first, as Network Manager
will automatically do it for you.

Feel free to explore more commands.

How to run the utility from anywhere using arbitrary name
=========================================================

Preceding examples had to be run from directory, where is the `dodo.py` file.

For daily use, we want to call it simply from anywhere.

Define bash function `~/.aliases` (or any other file, which is sourced when your console starts)::

    function donet() {
        (cd ~/devel/pydoit/samples/nmcli && doit $*)
    }

Be sure to use the directory you have the `dodo.py` file in.

Reload your console and you shall be able doing all the magic as above but this time replacing
`doit` with `donet` and doing so from anywhere::

    $ donet
    === Short list of subcommands:
    available   List all available configured connections.
    down        Set given connection down.
    init        (re)create file .connections listing connection names to use
    radio       Report status of network radio devices
    radiooff    Set network radio device off.
    radioon     Set network radio device on
    status      List currently active network connections.
    up          Set given connection up (specific connection name required).
    === For complete list use subcommand: list --all


How to edit connection names
============================
This tool is using connection names as provided by Network Manager.

Feel free to rename any connection to a name, which is simpler to use and remember.

This holds true even for WiFi SSID names as connection.id and SSID are distinct parameters.

E.g. listing connection names::

    $ nmcli connection
    NAME             UUID                                  TYPE             DEVICE
    home             d4d75b34-8ea6-4c05-bfaa-625ede14db5e  802-11-wireless  --
    Work_Network     b3b52328-5f07-47e5-b19f-4f7a15693ae1  802-11-wireless  --

shows name `Work_Network`.

To rename it to `work`::

    $ nmcli connection modify Work_Network connection.id work

And listing connection names again::

    $ nmcli connection
    NAME             UUID                                  TYPE             DEVICE
    home             d4d75b34-8ea6-4c05-bfaa-625ede14db5e  802-11-wireless  --
    work             b3b52328-5f07-47e5-b19f-4f7a15693ae1  802-11-wireless  --

shows we have succeeded.

.. warning:: Make sure to update your `.connections` file after any change.
