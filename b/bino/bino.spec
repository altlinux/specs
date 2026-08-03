Name:    bino
Version: 2.8
Release: alt1

Summary: 3D video player
License: GPL-3.0-or-later
Group:   Video
URL:     https://bino3d.org
VCS:     https://github.com/marlam/bino

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: qt6-base-devel qt6-multimedia-devel qt6-tools-devel
BuildRequires: libappstream-glib libappstream-glib-gir libqvr-devel pandoc

%description
Bino is a 3D video player. It supports stereoscopic 3D video with a wide
variety of input and output formats. It also supports multi-display video
and it can be used for powerwalls, virtual reality installations and other
multi-projector setups.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate \
    %buildroot%_desktopdir/org.bino3d.bino.desktop
appstream-util validate-relax --nonet \
   %buildroot%_datadir/metainfo/org.bino3d.bino.metainfo.xml

%files
%doc LICENSE.md README.md NEWS.md
%_bindir/%name
%_desktopdir/org.bino3d.bino.desktop
%_iconsdir/hicolor/*/apps/org.bino3d.bino.*
%_datadir/metainfo/org.bino3d.bino.metainfo.xml
%docdir %_datadir/doc/%name
%_datadir/doc/%name
%_man1dir/%name.1*

%changelog
* Mon Aug 03 2026 Sergey Palcheh <minergenon@altlinux.org> 2.8-alt1
- new version 2.8

* Wed May 27 2026 Sergey Palcheh <minergenon@altlinux.org> 2.7-alt1
- new version (2.7)

* Fri Jan 17 2025 Sergey Palcheh <minergenon@altlinux.org> 2.3-alt1
- initial build for ALT Sisyphus

