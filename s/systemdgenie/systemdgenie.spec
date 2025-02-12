%define _unpackaged_files_terminate_build 1

Name: systemdgenie
Version: 0.100.0
Release: alt0.1

Summary: Systemd managment utility
License: GPLv2+
Group: System/Configuration/Boot and Init
Url: https://invent.kde.org/system/systemdgenie.git
%K6init

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel
BuildRequires: kf6-kauth-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-ktexteditor-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-kio-devel
BuildRequires: libsystemd-devel

Requires: systemd

%description
SystemdGenie is a systemd management utility based on KDE technologies.
It provides a graphical frontend for the systemd daemon, which allows for
viewing and controlling systemd units, logind sessions as well as easy
modification of configuration and unit files.

%prep
%setup

%build
%K6build

%install
%K6install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING NEWS README.md
%_K6bin/%name
%_K6dbus_sys_srv/org.kde.kcontrol.%name.service
%_K6exec/kauth/%{name}helper
%_K6dbus/system.d/org.kde.kcontrol.%name.conf
%_K6xdgapp/org.kde.%name.desktop
%_K6data/kxmlgui?/%name/
%_datadir/polkit-1/actions/org.kde.kcontrol.%name.policy

%changelog
* Wed Feb 12 2025 Sergey V Turchin <zerg@altlinux.org> 0.100.0-alt0.1
- build with KF6 (closes: 53040)

* Thu Jan 30 2025 Nikolay Strelkov <snk@altlinux.org> 0.99.0-alt1
- Initial build for Sisyphus
