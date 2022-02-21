%define _unpackaged_files_terminate_build 1

Name: gpui
Version: 0.2.0
Release: alt4

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

BuildRequires: desktop-file-utils ImageMagick-tools

Requires: admx-basealt

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

for size in 48 64 128 256 512; do
    mkdir -p %buildroot%_datadir/icons/hicolor/''${size}x''${size}/apps/
    convert ../setup/logo_1024_1024.png -resize ''${size}x''${size} \
    %buildroot%_datadir/icons/hicolor/''${size}x''${size}/apps/gpui.png
done

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

%_datadir/icons/hicolor/48x48/apps/gpui.png
%_datadir/icons/hicolor/64x64/apps/gpui.png
%_datadir/icons/hicolor/128x128/apps/gpui.png
%_datadir/icons/hicolor/256x256/apps/gpui.png
%_datadir/icons/hicolor/512x512/apps/gpui.png

%_desktopdir/gpui.desktop

%changelog
* Mon Feb 21 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt4
- Fixes:
  + #73754 Fix translations in open admx dialog.
  + #73747 Fix translation of command line options.
  + #73625 Fix add application icon.
  + #73788 Fix add admx-basealt to spec.
  + #73738 Fix add manual.

* Fri Feb 18 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt3
- Fixes:
  + #73617 Fix difference of about window from that of ADMC.
  + #73627 Fix invalid header of the main window.
  + #73629 Fix absent translation of program icon in start menu.
  + Fix disabling and non configuring policies.

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
