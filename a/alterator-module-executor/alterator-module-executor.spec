Name: alterator-module-executor
Version: 0.1.27
Release: alt1

Summary: Alterator-manager module for running executable files and scripts
License: GPL-2
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-module-executor

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc libtomlc99-devel libjson-c-devel
BuildRequires: libgio-devel libsystemd-devel libpolkit-devel
BuildRequires: alterator-manager-devel >= 0.1.30

Requires: alterator-manager >= 0.1.30-alt1
Requires: libtomlc99 >= 1.0
Requires: libjson-c5 >= 0.17

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
* Wed Sep 03 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.27-alt1
- Fix duplication of signals in introspection.

* Thu Aug 07 2025 Ivan Savin <svn17@altlinux.org> 0.1.26-alt2
- Fix dependencies in spec.

* Wed Aug 06 2025 Ivan Savin <svn17@altlinux.org> 0.1.26-alt1
- Add the ability to create methods with multiple return values (strings). The
  names of these output arguments are specified by an array in the stdout_json
  field in the backend file. The method expects a string containing a json
  object from the running process. Having received such an object, it parses
  it and extracts strings from it whose keys correspond to the names specified
  in the stdout_json field.

* Tue Jul 08 2025 Ivan Savin <svn17@altlinux.org> 0.1.25-alt1
- Add the ability to use string arrays as method parameters.

* Thu Apr 17 2025 Ivan Savin <svn17@altlinux.org> 0.1.24-alt1
- Add the ability to return an array of byte arrays as string array.

* Tue Apr 15 2025 Ivan Savin <svn17@altlinux.org> 0.1.23-alt1
- Fix broken stdout_byte_arrays. The stdout_byte_arrays_enabled condition
  was missed when the process was spawned.
- Fix a bag when all stdout output from the child process is turned off, its
  output goes to the parent process's stdout.

* Thu Apr 10 2025 Ivan Savin <svn17@altlinux.org> 0.1.22-alt1
- Fix memory leak, after g_strconcat the g_free was not always called.
- Remove unnecessary checks. In case of failure on g_new0 and g_thread_new
  the program aborts.
- Remove unnecessary field from the structure.

* Tue Apr 01 2025 Ivan Savin <svn17@altlinux.org> 0.1.21-alt1
- Add the ability to return integer exit status.
  Executor can return integer exit status from child process. Before that,
  it was boolean (sheriffkorov@).

* Tue Apr 01 2025 Ivan Savin <svn17@altlinux.org> 0.1.20-alt1
- Fix: set pipes to null if not used (parovoz@).

* Fri Mar 28 2025 Ivan Savin <svn17@altlinux.org> 0.1.19-alt2
- Updated the warning text displayed when a spawned process fails.

* Thu Mar 27 2025 Ivan Savin <svn17@altlinux.org> 0.1.19-alt1
- Add functionality allowing the manager to track whether the module is busy.

* Tue Mar 04 2025 Ivan Savin <svn17@altlinux.org> 0.1.18-alt1
- Add the ability to return stdout as an array of byte arrays.
- Fix error handling on stdout strings.

* Fri Feb 21 2025 Ivan Savin <svn17@altlinux.org> 0.1.17-alt1
- Fix closing stdin. Now stdin is closed immediately after sending a special
  parameter.

* Mon Feb 10 2025 Ivan Savin <svn17@altlinux.org> 0.1.16-alt2
- Fix missing file closing.

* Fri Feb 07 2025 Ivan Savin <svn17@altlinux.org> 0.1.16-alt1
- Add the ability to pass a string to the stdin of the spawned process via a
  special parameter. If the "stdin_string" field is specified in the
  configuration file with the value "true", then one more parameter is added
  to the list of parameters (at the end of the list) - stdin. The string from
  this parameter will be sent to the stdin of the process immediately after
  launch.

* Wed Feb 05 2025 Ivan Savin <svn17@altlinux.org> 0.1.15-alt1
- Extend control of environment variables. You can now add environment
  variables for a method only if they are specified in the configuration file.
  You can also set default values for these variables.

* Fri Dec 06 2024 Ivan Savin <svn17@altlinux.org> 0.1.14-alt1
- Transition backend files to toml format.

* Thu Oct 31 2024 Ivan Savin <svn17@altlinux.org> 0.1.13-alt2
- Change BuildRequires from alterator-manager-devel >= 0.1.23 to
  alterator-manager-devel >= 0.1.24.

* Mon Oct 14 2024 Ivan Savin <svn17@altlinux.org> 0.1.13-alt1
- Renaming object paths and interface names and bus name from ru.basealt to
  org.altlinux.

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

