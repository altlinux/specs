%define _unpackaged_files_terminate_build 1

Name: systemdgenie
Version: 0.99.0
Release: alt1

Summary: Systemd managment utility
License: GPLv2+
Group: System/Configuration/Boot and Init
Url: https://invent.kde.org/system/systemdgenie.git

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-kf5

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: kf5-kauth-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kxmlgui-devel
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
%K5build

%install
%K5install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING NEWS README.md
%_K5bin/%name
%_K5dbus_sys_srv/org.kde.kcontrol.%name.service
%_K5libexecdir/kauth/%{name}helper
%_K5dbus/system.d/org.kde.kcontrol.%name.conf
%_K5xdgapp/org.kde.%name.desktop
%_K5xmlgui/%name/%{name}ui.rc
%_datadir/polkit-1/actions/org.kde.kcontrol.%name.policy

%changelog
* Thu Jan 30 2025 Nikolay Strelkov <snk@altlinux.org> 0.99.0-alt1
- Initial build for Sisyphus
