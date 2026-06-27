%define _unpackaged_files_terminate_build 1

Name: lomiri-schemas
Version: 0.1.11
Release: alt1

Summary: Configuration schemas used by Lomiri
License: LGPL-2.1
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-schemas

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: ayatana-cmake-modules
BuildRequires: intltool
BuildRequires: pkgconfig(glib-2.0)

BuildArch: noarch

%description
The Lomiri shell is the primary user interface for Lomiri based mobile
devices.

This package contains the configuration schemas used by Lomiri.

%package devel
Summary: Configuration schemas used by Lomiri (development files)
Group: Development/Other
Requires: %name = %version-%release
BuildArch: noarch

%description devel
The Lomiri shell is the primary user interface for Lomiri based mobile
devices.

This package contains the development files for %name.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS ChangeLog COPYING README.md
%_datadir/accountsservice/interfaces/com.lomiri.AccountsService.Input.xml
%_datadir/accountsservice/interfaces/com.lomiri.AccountsService.SecurityPrivacy.xml
%_datadir/accountsservice/interfaces/com.lomiri.AccountsService.Sound.xml
%_datadir/accountsservice/interfaces/com.lomiri.touch.AccountsService.Phone.xml
%_datadir/accountsservice/interfaces/com.lomiri.touch.AccountsService.SecurityPrivacy.xml
%_datadir/accountsservice/interfaces/com.lomiri.touch.AccountsService.Sound.xml
%_datadir/glib-2.0/schemas/com.lomiri.Shell.gschema.xml
%_datadir/glib-2.0/schemas/com.lomiri.notifications.settings.gschema.xml
%_datadir/glib-2.0/schemas/com.lomiri.phone.gschema.xml
%_datadir/glib-2.0/schemas/com.lomiri.sound.gschema.xml
%_datadir/glib-2.0/schemas/com.lomiri.touch.sound.gschema.xml
%_datadir/glib-2.0/schemas/com.lomiri.touch.system.gschema.xml
%_datadir/polkit-1/actions/com.lomiri.AccountsService.policy
%_datadir/polkit-1/rules.d/50-com.lomiri.AccountsService.rules

%files devel
%_datadir/pkgconfig/lomiri-schemas.pc
%_datadir/dbus-1/interfaces/com.lomiri.AccountsService.Input.xml
%_datadir/dbus-1/interfaces/com.lomiri.AccountsService.SecurityPrivacy.xml
%_datadir/dbus-1/interfaces/com.lomiri.AccountsService.Sound.xml
%_datadir/dbus-1/interfaces/com.lomiri.touch.AccountsService.Phone.xml
%_datadir/dbus-1/interfaces/com.lomiri.touch.AccountsService.SecurityPrivacy.xml
%_datadir/dbus-1/interfaces/com.lomiri.touch.AccountsService.Sound.xml

%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.11-alt1
- New version 0.1.11.

* Thu Jan 15 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.10-alt1
- New version 0.1.10.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.9-alt1
- New version 0.1.9.

* Mon Jul 14 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.8-alt1
- Initial build for Sisyphus
