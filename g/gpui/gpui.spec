%define _unpackaged_files_terminate_build 1

Name: gpui
Version: 0.2.0
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

BuildRequires: desktop-file-utils

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

cd %_cmake__builddir
desktop-file-install --dir=%buildroot%_desktopdir \
                     --set-key Exec --set-value %_bindir/gpui-main \
                     ../setup/gpui.desktop

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

%_desktopdir/gpui.desktop

%changelog
* Wed Feb 17 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt2
- Fixes:
  + Fix string saving to pol file.

* Wed Feb 16 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt1
- 0.2.0
- Features:
  + Implement signal based save system.
  + Introduce policy element types into policy elements.
- Fixes:
  + Fix combo box indices and values.

* Tue Feb 01 2022 Vladimir Rubanov <august@altlinux.org> 0.1.0-alt2
- A first implementation of smb routines.

* Mon Jul 05 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build
