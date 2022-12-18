Name:     kdiskmark
Version:  3.1.2
Release:  alt1

Summary:  A simple open-source disk benchmark tool for Linux distros

License:  GPL-3.0
Group:    Other
Url:      https://github.com/JonMagon/KDiskMark

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires: cmake gcc-c++ qt5-base-devel qt5-tools-devel extra-cmake-modules
BuildRequires: kf5-kauth-devel kf5-kcoreaddons-devel libpolkitqt5-qt5-devel
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
%_iconsdir/hicolor/*/*/*.png
%_datadir/polkit-1/actions/*.policy
%_usr/libexec/kdiskmark_helper
# Fix post-install unowned files
%dir %_datadir/dbus-1/system-services
%dir %_datadir/polkit-1
%dir %_datadir/polkit-1/actions
%dir %_iconsdir/hicolor/128x128
%dir %_iconsdir/hicolor/128x128/apps
%dir %_iconsdir/hicolor/24x24
%dir %_iconsdir/hicolor/24x24/apps
%dir %_iconsdir/hicolor/256x256
%dir %_iconsdir/hicolor/256x256/apps
%dir %_iconsdir/hicolor/512x512
%dir %_iconsdir/hicolor/512x512/apps
%dir %_iconsdir/hicolor/64x64
%dir %_iconsdir/hicolor/64x64/apps

%changelog
* Sat Dec 17 2022 Grigory Ustinov <grenka@altlinux.org> 3.1.2-alt1
- Build new version.

* Sun Nov 07 2021 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1
- Automatically updated to 2.3.0.

* Tue Sep 14 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1
- Automatically updated to 2.2.1.

* Fri Jul 09 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus (Closes: #39064).
