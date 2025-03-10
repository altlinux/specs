Name:    bino
Version: 2.3
Release: alt1

Summary: 3D video player
License: GPL-3.0
Group:   Video
Url:     https://github.com/marlam/bino

Source0: %name-%version.tar

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
    %buildroot%_datadir/applications/org.bino3d.bino.desktop
appstream-util validate-relax --nonet \
   %buildroot%_datadir/metainfo/org.bino3d.bino.metainfo.xml

%files
%doc LICENSE.md README.md NEWS.md
%_bindir/%name
%_datadir/applications/org.bino3d.bino.desktop
%_datadir/icons/hicolor/*/apps/org.bino3d.bino.*
%_datadir/metainfo/org.bino3d.bino.metainfo.xml
%_datadir/doc/%name
%_man1dir/*

%changelog
* Fri Jan 17 2025 Sergey Palcheh <minergenon@altlinux.org> 2.3-alt1
- initial build for ALT Sisyphus

