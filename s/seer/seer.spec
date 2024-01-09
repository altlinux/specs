%define progname seergdb
Name: seer
Version: 2.3
Release: alt1
Source: %name-%version.tar.gz
Summary: A gui frontend to gdb
Group: Development/Debuggers
License: GPLv3

# Automatically added by buildreq on Tue Jan 09 2024
# optimized out: bash5 cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libglvnd-devel libgpg-error libp11-kit libqt6-charts libqt6-core libqt6-dbus libqt6-gui libqt6-opengl libqt6-openglwidgets libqt6-printsupport libqt6-svg libqt6-widgets libsasl2-3 libssl-devel libstdc++-devel libvulkan-devel libxkbcommon-devel pkg-config python3 python3-base qt6-base-common qt6-base-devel sh5
BuildRequires: cmake qt6-charts-devel qt6-svg-devel

%description
Seer - a gui frontend to gdb for Linux. (Ernie Pasveer epasveer@att.net)
This project is actively worked on. The aim is a simple, yet pleasing gui to gdb.

%prep
%setup

%build
cd src
%cmake -DQTVERSION=QT6
%cmake_build

%install
cd src
%cmake_install
for icon in resources/%{progname}*.png; do
        SIZE=${icon##*x}; SIZE=${SIZE%%.png}
        install -D $icon %buildroot%_iconsdir/hicolor/${SIZE}x${SIZE}/%progname.png
done
install -D resources/%progname.desktop %buildroot%_desktopdir/%progname.desktop

%files
%doc *.md src/resources/help src/resources/ABOUT.md
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/*

%changelog
* Tue Jan 09 2024 Fr. Br. George <george@altlinux.ru> 2.3-alt1
- Autobuild version bump to 2.3

