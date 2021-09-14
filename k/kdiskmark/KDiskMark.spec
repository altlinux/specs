Name:     kdiskmark
Version:  2.2.1
Release:  alt1

Summary:  A simple open-source disk benchmark tool for Linux distros

License:  GPL-3.0
Group:    Other
Url:      https://github.com/JonMagon/KDiskMark

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires: cmake gcc-c++ qt5-base-devel qt5-tools-devel extra-cmake-modules kf5-kauth-devel kf5-kcoreaddons-devel
Requires: libkf5auth fio

%description
KDiskMark is an HDD and SSD benchmark tool with a very friendly graphical user
interface. KDiskMark with its presets and powerful GUI calls Flexible I/O
Tester and handles the output to provide an easy to view and interpret
comprehensive benchmark result.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_bindir/%name
%_datadir/%name/
%_datadir/applications/*.desktop
%_datadir/dbus-1/system-services/*.service
%_datadir/dbus-1/system.d/*.conf
%_datadir/icons/hicolor/*/*/*.png
%_datadir/polkit-1/actions/*.policy
%_usr/libexec/kauth/kdiskmark_helper

%changelog
* Tue Sep 14 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1
- Automatically updated to 2.2.1.

* Fri Jul 09 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus (Closes: #39064).
