%define _unpackaged_files_terminate_build 1

Name: filediff-gui
Version: 0.1.0
Release: alt1

Summary: An application showing the capabilities of libfilediff library
License: GPL-3.0
Group: File tools
URL: https://github.com/qualimock/filediff-gui
VCS: https://github.com/qualimock/filediff-gui

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: libfilediff-devel

%description
%summary.

%prep
%setup
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/filediff-gui
%_iconsdir/hicolor/scalable/apps/filediff-gui.svg
%_desktopdir/filediff-gui.desktop

%changelog
* Mon Dec 2 2024 Alexey Volkov <qualimock@altlinux.org> 0.1.0-alt1
- Initial build for ALT
