%define alterator_libexecdir %_prefix/libexec/alterator

Name: alterator-manager
Version: 0.1.22
Release: alt1

Summary: Modular tool for system configuration via D-Bus
License: GPL-2
Group: System/Configuration/Other

BuildRequires: cmake gcc
BuildRequires: libgio-devel libsystemd-devel libpolkit-devel

Source: %name-%version.tar

%description
Modular tool for system configuration via D-Bus.

%package tools
Summary: Auxiliary tools for the alterator-manager.
Group: Development/Other

%description tools
Auxiliary tools for the alterator-manager.

%package devel
Summary: Headers for developing alterator-manager modules
Group: Development/Other
Requires: libgio-devel

%description devel
Headers for developing alterator-manager modules.


%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%alterator_libexecdir
mkdir -p %buildroot%_datadir/alterator/backends
mkdir -p %buildroot%_datadir/alterator/backends/user
mkdir -p %buildroot%_datadir/alterator/backends/system
mkdir -p %buildroot%_sysconfdir/alterator/backends
mkdir -p %buildroot%_sysconfdir/alterator/backends/user
mkdir -p %buildroot%_sysconfdir/alterator/backends/system
mkdir -p %buildroot%_datadir/polkit-1/actions
mkdir -p %buildroot%_rpmlibdir/
mv -f %buildroot%_prefix/lib/systemd/user/alterator-manager.service-user \
      %buildroot%_prefix/lib/systemd/user/alterator-manager.service
mv -f %buildroot%_datadir/dbus-1/services/ru.basealt.alterator-manager.service-user \
      %buildroot%_datadir/dbus-1/services/ru.basealt.alterator-manager.service

%files
%_sbindir/%name
%_datadir/dbus-1/system.d/ru.basealt.alterator-manager.conf
%_datadir/dbus-1/services/ru.basealt.alterator-manager.service
%_datadir/dbus-1/system-services/ru.basealt.alterator-manager.service
%_unitdir/alterator-manager.service
%_prefix/lib/systemd/user/alterator-manager.service
%_datadir/polkit-1/actions/ru.basealt.alterator.manager.policy
%_rpmlibdir/%name.filetrigger
%dir %alterator_libexecdir
%dir %_datadir/alterator/backends
%dir %_datadir/alterator/backends/user
%dir %_datadir/alterator/backends/system
%dir %_sysconfdir/alterator/backends
%dir %_sysconfdir/alterator/backends/user
%dir %_sysconfdir/alterator/backends/system
%doc docs/*

%files devel
%_includedir/alterator

%files tools
%_bindir/am-dev-tool


%changelog
* Thu Jul 11 2024 Ivan Savin <svn17@altlinux.org> 0.1.22-alt1
- Add missing 'static' for GDBusSubtreeVTable subtree_vtable.
- Make the service in system mode bus-activatable.
- Fix warning incompatible pointer type.

* Fri May 31 2024 Ivan Savin <svn17@altlinux.org> 0.1.21-alt1
- Add missing g_module_close() and remove unnecessary g_free().
- Add parameter 'object' to method 'GetSignals' on object /ru/basealt/alterator
  in interface ru.baseatl.alterator.manager.

* Tue May 28 2024 Ivan Savin <svn17@altlinux.org> 0.1.20-alt1
- Add GetAllObjects and GetAllInterfaces to ru.basealt.alterator.manager
  on /ru/basealt/alterator.
- Rename output parameter of GetSignals from objects to signals
  (ru.basealt.alterator.manager /ru/basealt/alterator).

* Tue Mar 19 2024 Ivan Savin <svn17@altlinux.org> 0.1.19-alt1
- Add new directories for the backend files in /etc.
- Update docs/README-ru.md.

* Tue Mar 12 2024 Ivan Savin <svn17@altlinux.org> 0.1.18-alt1
- Make the service in user mode bus-activatable.
- Disable authorization check for the default interface in user mode.
- Update docs/README-ru.md.
- Add separate directories for .backend files.
- Add missing argument types to function definitions and declarations.

* Mon Feb 05 2024 Ivan Savin <svn17@altlinux.org> 0.1.17-alt1
- Add the ability to use the full interface name in backend files.
- Update docs/README-ru.md.

* Fri Jan 26 2024 Ivan Savin <svn17@altlinux.org> 0.1.16-alt5
- Add check in filetrigger that the system is loaded using systemd (chernigin@).

* Thu Jan 25 2024 Ivan Savin <svn17@altlinux.org> 0.1.16-alt4
- Remove unnecessary debug output.

* Thu Jan 25 2024 Ivan Savin <svn17@altlinux.org> 0.1.16-alt3
- Fix: fix filetrigger (chernigin@).

* Wed Jan 24 2024 Ivan Savin <svn17@altlinux.org> 0.1.16-alt2
- Fix filetrigger (kozyrevid@).

* Fri Jan 19 2024 Ivan Savin <svn17@altlinux.org> 0.1.16-alt1
- Add filetrigger to restart the service (kozyrevid@).

* Tue Jan 16 2024 Ivan Savin <svn17@altlinux.org> 0.1.15-alt2
- Update docs/README-ru.md.

* Wed Jan 10 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.15-alt1
- Add policy file for alterator-manager itself.

* Wed Dec 27 2023 Ivan Savin <svn17@altlinux.org> 0.1.14-alt1
- Add the alterator-manager-tools package with the am-dev-tool utility.
- Remove automatic generation of policy files (for polkit).
- Update docs/README-ru.md.

* Mon Dec 25 2023 Ivan Savin <svn17@altlinux.org> 0.1.13-alt2
- Add creation of /etc/alterator/backends directory for backend files.

* Mon Dec 18 2023 Ivan Savin <svn17@altlinux.org> 0.1.13-alt1
- Fix the backends_data table creation, it is created only if the pointer is
  NULL.
- Lines that are too long are split into shorter ones.

* Fri Dec 08 2023 Ivan Savin <svn17@altlinux.org> 0.1.12-alt1
- Change the name of the Node field in the Alterator Entry section to Name.
- Update docs/README-ru.md.

* Mon Nov 27 2023 Ivan Savin <svn17@altlinux.org> 0.1.11-alt1
- Change the format of the top section of backend files.
- Add the ability to set an action_id without a ru.basealt.alterator prefix
  using the action_id field in the manager section.
- Improve memory release logic for variables in the save_info_from_backend_file
  function in file alterator_manager_backends.h.
- Update docs/README-ru.md.

* Wed Nov 01 2023 Ivan Savin <svn17@altlinux.org> 0.1.10-alt2
- Update docs/README-ru.md.

* Tue Oct 31 2023 Ivan Savin <svn17@altlinux.org> 0.1.10-alt1
- Add name checking when adding an environment variable. The name must not
  contain =.
- Rename ManagerData structure fields from _table to _data.

* Fri Oct 27 2023 Ivan Savin <svn17@altlinux.org> 0.1.9-alt1
- Fix method names in ru.basealt.alterator.manager.
- Add automatic cleaning of environment variables.
- Add support environment variables management for dbus senders (sin@).
- Fix typos in alterator_manager_backends.h (sin@).

* Mon Oct 16 2023 Ivan Savin <svn17@altlinux.org> 0.1.8-alt1
- Fix: wrong method names in ru.basealt.alterator.manager.

* Wed Sep 20 2023 Ivan Savin <svn17@altlinux.org> 0.1.7-alt4
- Fix: fail to start when the backend files not found.

* Wed Sep 06 2023 Ivan Savin <svn17@altlinux.org> 0.1.7-alt3
- Undo changes from 0.1.7-alt2. This change causes "double free or
  corruption".

* Wed Sep 06 2023 Ivan Savin <svn17@altlinux.org> 0.1.7-alt2
- Fix: add g_free() for newly-allocated copy of the string after
  g_variant_get().

* Tue Jul 11 2023 Ivan Savin <svn17@altlinux.org> 0.1.7-alt1
- Add the ability to validate interfaces by template.
- Update docs/README-ru.md.

* Fri Jun 23 2023 Ivan Savin <svn17@altlinux.org> 0.1.6-alt1
- Add the ability to run the alterator-manager in user mode (systemctl --user).
- Update docs/README-ru.md.

* Fri Jun 09 2023 Ivan Savin <svn17@altlinux.org> 0.1.5-alt2
- Change defaults for polkit actions.

* Thu Jun 01 2023 Ivan Savin <svn17@altlinux.org> 0.1.5-alt1
- Add the get_interfaces method to the ru.basealt.alterator.manager interface.
- Add checking of user rights to execute methods using polkit in the default
  interfaces.

* Mon May 22 2023 Ivan Savin <svn17@altlinux.org> 0.1.4-alt1
- Add checking of user rights to execute methods using polkit.
- Data from alterator-manager is now transferred not in a GHashTable,
  but in a structure ManagerData.
- Add check for the correctness of the interface name in a backend file.
- Add check for the correctness of the node name in a backend file.
- Add automatic addition of prefix 'ru.basealt.alterator.' to the interface
  name from a file.
- Update docs/README-ru.md.

* Fri Apr 21 2023 Ivan Savin <svn17@altlinux.org> 0.1.3-alt1
- Add thread_limit option to manager section in backend file.
- Update doc/README-ru.md.

* Tue Apr 11 2023 Ivan Savin <svn17@altlinux.org> 0.1.2-alt1
- Add the get_signals method to the ru.basealt.alterator.manager interface that
  returns a list of signal names (stdout/stderr). The arguments to this method
  are the interface name and the method name.

* Tue Apr 04 2023 Ivan Savin <svn17@altlinux.org> 0.1.1-alt2
- Add readme file (RU).

* Thu Mar 09 2023 Ivan Savin <svn17@altlinux.org> 0.1.1-alt1
- Add a default interface called manager into root.
- The manager contains a method get_objects that returns object paths by
  interface name.

* Thu Feb 16 2023 Ivan Savin <svn17@altlinux.org> 0.1.0-alt1
- All backend files are now loaded in the manager, and modules receive a
  pointer to a table with data that contains information about D-Bus objects
  and handlers. One file describes one interface for one module.
- g_dbus_connection_register_object replaced by
  g_dbus_connection_register_subtree.
- The interaction between the manager and modules has changed: the module now
  returns not xml, but an instance of GDBusInterfaceInfo (it writes a pointer
  to this instance to the table with data received from the manager, a
  pointer to the vtable is also written there).

* Sat Oct 22 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.0.3-alt1
- Improve errors treatment.
- Rename source files from plugin to modules in common style.
- Add support loading backends prototype with interfaces from
  alterator_manager_interface in modules.

* Thu Oct 13 2022 Ivan Savin <svn17@altlinux.org> 0.0.2-alt1
- Add devel.

* Fri Aug 19 2022 Ivan Savin <svn17@altlinux.org> 0.0.1-alt1
- Initial commit.

