Name: karton
Version: 20250722
Release: alt1

Summary: A libvirt-based Virtual Machine Manager for KDE

License: GPL-3.0-or-later and CC0-1.0 and BSD-2-Clause and CC-BY-SA-4.0
Group: Emulators

Url: https://invent.kde.org/kenoi/karton
Vcs: https://invent.kde.org/kenoi/karton

Source: %name-%version.tar

Requires: libvirt-daemon-driver-qemu 
Requires: qemu

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules libvirt-devel libosinfo-devel
BuildRequires: qt6-base-devel qt6-declarative-devel qt6-multimedia-devel
BuildRequires: pkgconfig(glib-2.0) pkgconfig(spice-client-glib-2.0)
BuildRequires: pkgconfig(libpcre2-8) kf6-kirigami-devel kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel kf6-qqc2-desktop-style-devel pkgconfig(libffi)
BuildRequires: kf6-kiconthemes-devel qml6(org.kde.kirigami) kf6-kio-devel

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
%_datadir/applications/*%name.desktop
%_iconsdir/hicolor/scalable/apps/*.png
%_datadir/qlogging-categories?/%name.categories
%doc *.md LICENSES

%changelog
* Sun Sep 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 20250722-alt1
- Initial build for ALT Linux.

