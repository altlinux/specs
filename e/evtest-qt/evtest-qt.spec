Name:    evtest-qt
Version: 0.3.0
Release: alt1

Summary: Linux Joystick Tester for Qt
License: GPL-3.0-or-later
Group:   Other
URL:     https://github.com/Grumbel/evtest-qt

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libudev-devel libevdev-devel qt6-base-devel

%description
evtest-qt is a graphical input device tester for Linux, analogous to the
evtest command-line tool. It lists attached evdev devices and shows
absolute axes, relative axes, buttons, and multitouch state in real time.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSES/*.txt README.md
%_bindir/evtest-qt
%_desktopdir/evtest-qt.desktop
%_iconsdir/hicolor/scalable/apps/evtest-qt.svg

%changelog
* Sun Aug 02 2026 Sergey Palcheh <minergenon@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
