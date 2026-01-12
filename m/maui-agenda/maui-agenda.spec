%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-agenda
Version: 1.0.2
Release: alt1

Summary: Calendar App based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/maui-agenda

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: libmauikit-devel
BuildRequires: libmauikit-calendar-devel

# no libmauikit-calendar-devel
ExcludeArch: %ix86 riscv64

Requires: libmauikit
Requires: libmauikit-calendar

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang agenda

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/agenda %buildroot%_bindir/org.kde.agenda
sed -i "s|Exec=agenda|Exec=org.kde.agenda|" %buildroot%_desktopdir/org.kde.agenda.desktop

%files -f agenda.lang
%doc README.md
%_bindir/org.kde.agenda
%_desktopdir/org.kde.agenda.desktop
%_iconsdir/hicolor/scalable/apps/agenda.svg
%_datadir/metainfo/org.kde.agenda.metainfo.xml

%changelog
* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
