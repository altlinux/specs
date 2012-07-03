Name: cube3d-data
Version: 2005.08.29
Release: alt2

Summary: First person shooter game (data pack)
License: distributable
Group: Games/Arcade

URL: http://www.cubeengine.com/
Source: cube_2005_08_29_unix.tar.gz

BuildArch: noarch
Conflicts: cube3d < 2005

%description
Cube is an open source multiplayer and singleplayer first person shooter
game built on an entirely new and very unconventional engine. Cube is a
landscape-style engine that pretends to be an indoor FPS engine, which
combines very high precision dynamic occlusion culling with a form of
geometric mipmapping on the whole world for dynamic LOD for configurable
fps & graphic detail on most machines. Uses OpenGL & SDL. 

%prep
%setup -q -n cube

%install
mkdir -p %buildroot%_gamesdatadir/cube3d
cp -av autoexec.cfg data packages %buildroot%_gamesdatadir/cube3d

%files
%define _customdocdir %_docdir/cube3d
%doc readme* docs/*
%_gamesdatadir/cube3d

%changelog
* Sun Aug 26 2007 Alexey Tourbin <at@altlinux.ru> 2005.08.29-alt2
- changed License tag to "distributable" (some game data and maps
  are under the terms "free to distribute as long as you make no
  profit, and leave the files intact")

* Wed Apr 26 2006 Alexey Tourbin <at@altlinux.ru> 2005.08.29-alt1
- initial revision
