%define _unpackaged_files_terminate_build 1
%define oname org.kde.karton

Name: karton
Version: 20260804
Release: alt1

Summary: A libvirt-based Virtual Machine Manager for KDE

License: GPL-3.0-or-later and CC0-1.0 and BSD-2-Clause and CC-BY-SA-4.0 and BSD-3-Clause and GPL-2.0-or-later
Group: Emulators

Url: https://invent.kde.org/kenoi/karton
Vcs: https://invent.kde.org/kenoi/karton

Source: %name-%version.tar

Requires: libvirt-daemon-driver-qemu 
Requires: qemu

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: libvirt-devel
BuildRequires: libosinfo-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(spice-client-glib-2.0)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-qqc2-desktop-style-devel
BuildRequires: pkgconfig(libffi)
BuildRequires: kf6-kiconthemes-devel
BuildRequires: qml6(org.kde.kirigami)
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kirigami-addons-devel

%description
%summary.

%prep
%setup

%build
%K6cmake
%K6make

%install
%K6install

%files
%_bindir/%name
%_desktopdir/%oname.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/qlogging-categories?/%name.categories
%doc *.md LICENSES

%changelog
* Tue Aug 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260804-alt1
- updated to git.bd0e933af4

* Sun Sep 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 20250722-alt1
- Initial build for ALT Linux.

