Name:    qtextpad
Version: 1.12
Release: alt1
Summary: A Lightweight Qt-based code and text editor
License: GPL-3.0-only
Group:   System/Base
URL:     https://github.com/zrax/qtextpad
VCS:     https://github.com/zrax/qtextpad
Source:  %name-%version.tar

BuildRequires: cmake
BuildRequires: make
BuildRequires: qt6-base-devel
BuildRequires: gcc-c++
BuildRequires: libcups-devel
BuildRequires: kf6-syntax-highlighting-devel

%description
QTextPad is designed to be a simple,
lightweight text editor that works seamlessly and
simply across several desktop platforms.

%prep
%setup
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%doc COPYING README.md

%changelog
* Tue Jan 13 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 1.12-alt1
- Initial build.
