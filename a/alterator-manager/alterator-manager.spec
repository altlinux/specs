%define alterator_libexecdir %_prefix/libexec/alterator

Name: alterator-manager
Version: 0.1.11
Release: alt1

Summary: Modular tool for system configuration via D-Bus
License: GPL-2
Group: System/Configuration/Other

BuildRequires: cmake gcc
BuildRequires: libgio-devel libsystemd-devel libpolkit-devel

Source: %name-%version.tar

%description
Modular tool for system configuration via D-Bus.

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
mv -f %buildroot%_prefix/lib/systemd/user/alterator-manager-user.service \
      %buildroot%_prefix/lib/systemd/user/alterator-manager.service

%files
%_sbindir/%name
%_datadir/dbus-1/system.d/ru.basealt.alterator_manager.conf
%_unitdir/alterator-manager.service
%_prefix/lib/systemd/user/alterator-manager.service
%dir %alterator_libexecdir
%dir %_datadir/alterator/backends
%doc docs/*

%files devel
%_includedir/alterator

%changelog
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

