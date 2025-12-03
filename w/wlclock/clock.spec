Name:    wlclock
Version: 0.0
Release: alt1
Summary: Wayland Clock
License: GPL-3.0-only
Group:   System/Base
URL:     https://github.com/depau/wlclock
VCS:     https://github.com/depau/wlclock
Source:  %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: libgtkmm3-devel
BuildRequires: cmake
BuildRequires: gcc-c++

%description
An Xclock replacement for Wayland (and X11), prettier.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/wlclock
%doc README.md LICENSE

%changelog
* Thu Nov 27 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 0.0-alt1
- Initial build.
