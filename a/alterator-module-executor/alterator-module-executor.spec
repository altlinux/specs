Name: alterator-module-executor
Version: 0.1.12
Release: alt1

Summary: Alterator-manager module for running executable files and scripts
License: GPL-2
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-module-executor

BuildRequires: cmake gcc
BuildRequires: libgio-devel libsystemd-devel libpolkit-devel
BuildRequires: alterator-manager-devel >= 0.1.18

Requires: alterator-manager >= 0.1.18-alt1

Source: %name-%version.tar

%description
Alterator-manager module for running executable files and scripts.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std
#mkdir -p %buildroot%_datadir/alterator/modules/executor

%files
#%dir %_datadir/alterator/modules/executor
/usr/libexec/alterator/*

%changelog
* Thu Aug 29 2024 Ivan Savin <svn17@altlinux.org> 0.1.12-alt1
- Fix node name check in searching through the table of known methods.
- Add missing static for interface_vtable.
- Add missing const for parameters of add_method_to_table.
- Add missing g_strdups during filling out of the table of known methods.

* Fri Mar 15 2024 Ivan Savin <svn17@altlinux.org> 0.1.11-alt2
- Change BuildRequires from alterator-manager-devel >= 0.1.10 to
  alterator-manager-devel >= 0.1.18.
* Thu Feb 15 2024 Ivan Savin <svn17@altlinux.org> 0.1.11-alt1
- Disable UTF-8 channel encoding if return from stdout is enabled as a byte
  array.

* Tue Jan 23 2024 Ivan Savin <svn17@altlinux.org> 0.1.10-alt1
- Clean line break symbol in end of line for stdout and stderr strings (sin@).
- Add project URL to spec (sin@).

* Tue Jan 16 2024 Ivan Savin <svn17@altlinux.org> 0.1.9-alt1
- Add a timeout field for methods. The timeout field contains the period of time
  after which the SIGKILL will be sent to the process.

* Mon Nov 27 2023 Ivan Savin <svn17@altlinux.org> 0.1.8-alt1
- Add support for the action_id field from the InterfaceObjectInfo structure.

* Tue Oct 31 2023 Ivan Savin <svn17@altlinux.org> 0.1.7-alt1
- Add the ability to add environment variables from the alterator-manager
  database.
- Add memory freeing for the structure with data for launching processes in case
  of a process startup error and in case of a command line parsing error.
- Add reduction of thread counters in case of command line parsing error and in
  case of process startup error.

* Tue Jul 11 2023 Ivan Savin <svn17@altlinux.org> 0.1.6-alt1
- Add validation of interfaces by template.

* Fri Jun 23 2023 Ivan Savin <svn17@altlinux.org> 0.1.5-alt1
- Add the ability to work in user mode (systemctl --user).
- Add the ability to output data from stdout and stderr when condition is
  G_IO_HUP. Continues to read from channel until error or EOF.

* Mon May 22 2023 Ivan Savin <svn17@altlinux.org> 0.1.4-alt1
- Add checking of user rights to execute methods using polkit.
- Data from alterator-manager is now transferred not in a GHashTable, but in
  a structure ManagerData.

* Fri Apr 21 2023 Ivan Savin <svn17@altlinux.org> 0.1.3-alt1
- Add limit on the number of threads for the method. How many method instances
  can be run at the same time.

* Tue Apr 04 2023 Ivan Savin <svn17@altlinux.org> 0.1.2-alt1
- Add the ability to return stdout and stderr through an array of strings or
  an array of bytes (stdout only).
- The signal name is now formed by concatenating the string specified in
  the backend file and the sender. Dots and colons in the sender are replaced
  with underscores. If the signal name in the backend file is not specified,
  then the signals are disabled.
- Add the ability to limit stdout and stderr arrays in bytes (Default 524288).
- Add the ability to disable the return of stdout and stderr arrays using
  special options in the backend file.

* Mon Feb 27 2023 Ivan Savin <svn17@altlinux.org> 0.1.1-alt1
- Fix child's stderr and stdout pipes not closing.

* Thu Feb 16 2023 Ivan Savin <svn17@altlinux.org> 0.1.0-alt1
- All backend files are now loaded in the manager, and modules receive a
  pointer to a table with data that contains information about D-Bus objects
  and handlers. One file describes one interface for one module.
- The interaction between the manager and modules has changed: the module now
  returns not xml, but an instance of GDBusInterfaceInfo (it writes a pointer
  to this instance to the table with data received from the manager, a
  pointer to the vtable is also written there).

* Tue Dec 20 2022 Ivan Savin <svn17@altlinux.org> 0.0.3-alt1
- Add child process's stdout and stderr through signals.

* Sat Oct 22 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.0.2-alt1
- Second work version.

* Wed Oct 12 2022 Ivan Savin <svn17@altlinux.org> 0.0.1-alt1
- First work version.

