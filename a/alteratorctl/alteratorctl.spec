%define _unpackaged_files_terminate_build 1
%define short_name actl

Name: alteratorctl
Version: 0.2.1
Release: alt1

Summary: CLI for alterator-explorer
License: GPL-2.0+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alteratorctl

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake cmake-modules gcc glib2-devel libdbus-glib-devel libgio-devel libpcre2-devel
BuildRequires: libffi-devel zlib-devel libmount-devel libblkid-devel libselinux-devel libtomlc99-devel libgumbo-devel
BuildRequires: libpolkit-devel libjson-glib-devel

Requires: alterator-manager >= 0.1.29
Requires: alterator-module-executor >= 0.1.25
Requires: alterator-backend-packages >= 0.2.8
Requires: alterator-backend-component >= 0.3.0
Requires: alterator-interface-edition >= 0.2.0
Requires: alterator-interface-diag >= 0.1.4
Requires: alterator-backend-systeminfo >= 0.4.0
Requires: alterator-interface-service >= 0.2.1-alt2
Requires: libtomlc99 polkit libjson-glib

Source0: %name-%version.tar

%filter_from_requires /fish/d
%filter_from_requires /bash/d

%description
A command line tool for using alterator DBus objects.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std
ln -s %_bindir/%name %buildroot%_bindir/%short_name

%files
%_bindir/%name
%_bindir/%short_name
%_datadir/alteratorctl/lang/ru/LC_MESSAGES/%name.mo
%_datadir/alteratorctl/scripts/completion_wrapper
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/bash-completion/completions/%short_name
%_datadir/fish/vendor_completions.d/%short_name.fish

%changelog
* Wed Nov 26 2025 Pavel Khromov <hromovpi@altlinux.org> 0.2.1-alt1
- Sorting the order of running tests for the selected diagnostic tool.
- Optimizing the launch of diagnostic tests.
- Show parameters description in services play (thx Oleg Chagaev).

* Tue Nov 18 2025 Pavel Khromov <hromovpi@altlinux.org> 0.2.0-alt1
- Services module implementation (thx Andrey Alekseev and Oleg Chagaev).
- Fix completions (thx Kozyrev Yuri).
- Fix components (thx Kirill Sharov).

* Tue Sep 16 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.15-alt1
- Fixed printing of components of selected editions.
- Fix of confirmation message for packages apt operations.

* Tue Sep 02 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.14-alt1
- Fix localization of output of installation/removal of components.
- Fix localization of output of installation/removal/updating of packages by apt.
- Fix sending of wrong locale data to dbus connection.
- Use as instead ay on batch interfaces of components.

* Tue Aug 05 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.13-alt1
- Increased the version of a required dependency from alterator-interface-edition and
- alterator-backend-systeminfo

* Sat Jul 26 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.12-alt1
- Increased the version of a required dependency from alterator-backend-packages
- Moved completions setup logic to completions/CMakeLists

* Fri Jul 18 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.11-alt1
- Fix working bash-completions with actl symlink to alteratorctl.

* Tue Jul 01 2025 Andrey Limachko <liannnix@altlinux.org> 0.1.10-alt1
- Fixed typos (thx Elena Mishina).
- Added Bash and Fish completion (thx Kozyrev Yuri).

* Sat May 31 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.9-alt1
- Fixing build requires and creating symbolic link named actl

* Fri Apr 18 2025 Kozyrev Yuri <kozyrevid@altlinux.org> 0.1.8-alt1
- fix: fixed package list during install

* Wed Apr 16 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.7-alt1
- New version

* Thu Apr 10 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.6-alt1
- New version
- Changed versions in the installation dependencies

* Tue Apr 01 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.5-alt1
- Add dependencies from specified required packages
- Add LICENSE file
- Edit summary and description

* Thu Mar 27 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.4-alt1
- Add libpolkit-devel to build requires

* Wed Mar 26 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.3-alt1
- New version depending on the version of the alterator-backend-batch-components depending on the version

* Tue Mar 18 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.2-alt1
- New version

* Mon Mar 17 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.1-alt1
- New version

* Thu Mar 13 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.0-alt1
- Removing unnecessary dependencies

* Mon Mar 10 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.11-alt2
- Adding polkit to dependencies

* Fri Mar 07 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.11-alt1
- New version

* Thu Mar 06 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.10-alt1
- Adding dependencies on backends of alteratorctl modules

* Tue Feb 25 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.9-alt2
- Adding html parser library libgumbo-devel to build requires

* Mon Feb 17 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.9-alt1
- Reworking the help calls
- User-friendly interface of the diag module. Make default list tools and list tool tests commands
- Display all information using the default description command in systeminfo module
- Working with components names. Reworking components output

* Fri Dec 13 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.8-alt2
- fix interface validation
- refactor commands

* Tue Dec 10 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.8-alt1
- move to toml

* Thu Nov 07 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.7-alt1
- implement last-update in packages module
- add descriptions to editions in editions module
- fix error messages
- implement sysinfo module
- diag and manager modules can work with objects on system or session buses

* Mon Oct 21 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.6-alt1
- change prefix from ru.basealt to org.altlinux
- add systeminfo module

* Wed Oct 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.5-alt3
- two ways of getting information about an object are implemented: plain text and keyed parsed content
- fix components and packages modules

* Fri Sep 27 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.5-alt2
- fix component module
- implement obtaining information about the object both in text and parsed form

* Mon Sep 16 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.5-alt1
- implement Alterator Entry parsing
- add diag module

* Thu Aug 22 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.4-alt1
- add common method
- refactor internal client modules to check objects and interfaces
- locale fix
- add translations

* Wed Jul 31 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.3-alt1
- refactor manager module
- implement diag module

* Tue Jul 23 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.2-alt1
- implement manager, packages and components modules

* Sun Jun 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.1-alt1
- initial build
