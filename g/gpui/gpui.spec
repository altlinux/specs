%define _unpackaged_files_terminate_build 1

Name: gpui
Version: 0.1.0
Release: alt2

Summary: Group policy editor
License: GPLv2+
Group: Other
Url: https://github.com/august-alt/gpui

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-tools-devel
BuildRequires: libsmbclient-devel libsmbclient

BuildRequires: qt5-base-common
BuildRequires: doxygen
BuildRequires: libxerces-c-devel
BuildRequires: xsd

Source0: %name-%version.tar

%description
Group policy editor

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%doc INSTALL.md
%_bindir/gpui-main

%_libdir/libgpui-gui.so
%_libdir/libgpui-io.so
%_libdir/libgpui-model.so

%_libdir/gpui/plugins/libadml-plugin.so
%_libdir/gpui/plugins/libadmx-plugin.so
%_libdir/gpui/plugins/libreg-plugin.so
%_libdir/gpui/plugins/libspol-plugin.so
%_libdir/gpui/plugins/libpol-plugin.so

%_libdir/gpui/plugins/libdrives-plugin.so
%_libdir/gpui/plugins/libfiles-plugin.so
%_libdir/gpui/plugins/libfolders-plugin.so
%_libdir/gpui/plugins/libini-plugin.so
%_libdir/gpui/plugins/libshares-plugin.so
%_libdir/gpui/plugins/libshortcuts-plugin.so
%_libdir/gpui/plugins/libvariables-plugin.so

%_libdir/gpui/plugins/libsmb-storage-plugin.so

%changelog
* Tue Feb 01 2022 Vladimir Rubanov <august@altlinux.org> 0.1.0-alt2
- A first implementation of smb routines.

* Mon Jul 05 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build
