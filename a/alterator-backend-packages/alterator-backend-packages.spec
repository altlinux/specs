%define _unpackaged_files_terminate_build 1

Name: alterator-backend-packages
Version: 0.2.12
Release: alt1

Summary: Alterator backends for managing system packages
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-backend-packages

BuildArch: noarch

Source0: %name-%version.tar

Requires: alterator-interface-packages = %version-%release
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.29
Requires: apt >= 0.5.15lorg2-alt97
Requires: logrotate

BuildRequires(pre): rpm-macros-alterator
BuildRequires: make

%package -n alterator-interface-packages
Summary: Alterator interfaces for managing system packages
Group: System/Configuration/Other

%description
Alterator backends for managing system packages and package repositories
through apt and rpm.

%description -n alterator-interface-packages
Alterator interfaces for managing system packages and package repositories
through apt and rpm.

%prep
%setup

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%dir %_logdir/alterator/
%dir %_logdir/alterator/apt
%ghost %_logdir/alterator/apt/*.log
%_datadir/apt/scripts/*.lua
%config(noreplace) %_logrotatedir/alterator-logger.logrotate
%config %_sysconfdir/apt/apt.conf.d/*.conf
%_libexecdir/%name/*
%dir %_alterator_datadir/backends
%_alterator_datadir/backends/*.backend
%dir %_alterator_datadir/objects
%_alterator_datadir/objects/*.object

%files -n alterator-interface-packages
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/interfaces
%dir %_datadir/polkit-1
%dir %_datadir/polkit-1/actions
%_datadir/dbus-1/interfaces/*.xml
%_datadir/polkit-1/actions/*.policy
%doc LICENSE CHANGELOG.md

%changelog
* Fri Nov 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.12-alt1
- Add 'exit_status = true' for new version of executor.

* Tue Aug 26 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.2.11-alt1
- Add translations

* Mon Aug 18 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.10-alt1
- Fix failure if LC_ALL is unbound.

* Tue Jul 29 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.9-alt1
- Add line for more early signal of start of transaction.

* Tue Jul 22 2025 Kozyrev Yuri <kozyrevid@altlinux.org> 0.2.8-alt1
- Remove remaining unsafe methods from apt1

* Fri Jul 11 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.2.7-alt1
- Add new ApplyAsync and CheckApply methods to work with pkgpriorities.
- Move the package installation to the Makefile (thx Kirill Sharov).
- Cleaning the apt1 interface (thx Kirill Sharov).
- Add logrotate for apt logger (thx Kirill Sharov).
- Change the URL to altlinux.space.

* Tue Jun 17 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.6-alt1
- Fix localization for output of methods on org.altlinux.alterator.apt1.

* Fri Apr 25 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.2.5-alt1
- Set same polkit action_id org.altlinux.alterator.apt1.InstallOrRemove
  for Update, Install, Reinstall, Remove and DistUpgrade (already same) methods.
- Set same polkit action_id org.altlinux.alterator.apt1.Search policy for
  ListAllPackages and other search methods.
- Set same polkit action_id org.altlinux.alterator.apt1.Info for LastUpdate,
  LastDistUpgrade and other info methods.

* Fri Apr 25 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.2.4-alt1
- Fix newest installation package with same EVR in Install apt method.
- Set interface subpackage version same as backend package version.

* Tue Apr 22 2025 Pavel Khromov <hromovpi@altlinux.org> 0.2.3-alt1
- Fix reply type of CheckReinstall apt method.

* Fri Apr 18 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.2-alt1
- Split rpm1.List output.
- Add group to rpm1.List output.

* Thu Apr 04 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.1-alt1
- New version (see CHANGELOG.md).

* Thu Apr 04 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.0-alt2
- Fix release record in CHANGELOG.md.

* Thu Apr 03 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.2.0-alt1
- New version (see CHANGELOG.md).

* Wed Feb 05 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.4-alt1
- Fix timeouts for install and remove (thx Kozyrev Yuri).
- Turn lastUpdate tracker into loggers for apt updates and dist-upgrades
  (thx Kirill Sharov).
- Add lastDistUpgrade method to apt interface (thx Kozyrev Yuri).

* Mon Dec 09 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- Fix incorrect names of packages from ListAllPackages method.
- Change alterator entries format from ini to toml.

* Tue Oct 22 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.2-alt1
- Change prefix from ru.basealt to org.altlinux.
- Remove error output from Info methods.

* Wed Sep 25 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- Fix some incorrect package names in List method of apt backend.
- Add lastUpdate method to apt backend.
- Add error output to all methods.

* Wed May 29 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
