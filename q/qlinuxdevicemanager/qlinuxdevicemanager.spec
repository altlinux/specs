%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: qlinuxdevicemanager
Version: 1.3.0
Release: alt1

Summary: Device Manager implementation and Hardware System Information Viewer
License: GPL-3.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/birdie-github/QLinuxDeviceManager

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libv4l2)
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: pkgconfig(libkmod)

%if_with check
BuildRequires: ctest
%endif

%description
QLinuxDeviceManager is a lightweight graphical device manager for Linux,
inspired by Windows Device Manager. Browse your hardware, inspect kernel
drivers, check device properties and view system information in one desktop
application.

It works on X11 and Wayland, requires no particular desktop environment,
and runs as a normal user. Hardware information stays on your computer;
the application does not upload it.

%prep
%setup

%build
%cmake \
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%check
%ctest -V

%files
%doc doc README.md SCREENSHOTS.md screenshots
%_bindir/qlinuxdevicemanager
%dir %_datadir/QLinuxDeviceManager
%_datadir/QLinuxDeviceManager/project.json
%_desktopdir/io.github.birdie-github.QLinuxDeviceManager.desktop
%_iconsdir/hicolor/*/apps/io.github.birdie-github.QLinuxDeviceManager.png
%_iconsdir/hicolor/scalable/apps/io.github.birdie-github.QLinuxDeviceManager.svg

%changelog
* Wed Oct 14 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
