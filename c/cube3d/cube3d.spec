Name: cube3d
Version: 2005.08.29
Release: alt2.qa2

Summary: First person shooter game
License: Zlib license
Group: Games/Arcade

URL: http://www.cubeengine.com/
Source: cube-src-%version.tar

Requires: cube3d-data >= 2005

# Automatically added by buildreq on Wed Jul 04 2007
BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_mixer-devel libX11-devel libGLU-devel zlib-devel
BuildRequires: desktop-file-utils

%description
Cube is an open source multiplayer and singleplayer first person shooter
game built on an entirely new and very unconventional engine. Cube is a
landscape-style engine that pretends to be an indoor FPS engine, which
combines very high precision dynamic occlusion culling with a form of
geometric mipmapping on the whole world for dynamic LOD for configurable
fps & graphic detail on most machines. Uses OpenGL & SDL. 

%prep
%setup -q -n cube-src-%version

%build
cd ./enet
touch NEWS AUTHORS ChangeLog
autoreconf -fisv
%configure
%make_build

cd ../src
%make_build CXXOPTFLAGS="%optflags -fsigned-char" CXX='g++ -L%_x11libdir'

%install
install -pD -m755 src/cube_client %buildroot%_gamesbindir/cube_client
install -pD -m755 src/cube_server %buildroot%_gamesbindir/cube_server
install -pD -m755 cube3d.sh %buildroot%_gamesbindir/cube3d

install -m755 -d %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=The Cube shooter
Comment=The Cube shooter game
Exec=%_gamesbindir/cube3d
# TODO!!!
#Icon=%name
Terminal=false
StartupNotify=false
Categories=Game;Action;
EOF
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Action \
	--add-category=ActionGame \
	%buildroot%_desktopdir/cube3d.desktop

%files
%define _customdocdir %_docdir/cube3d
%doc readme.txt
%_gamesbindir/cube_client
%_gamesbindir/cube_server
%_gamesbindir/cube3d
%_desktopdir/%{name}.desktop

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2005.08.29-alt2.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for cube3d

* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 2005.08.29-alt2.qa1
- NMU: converted menu to desktop file

* Wed Jul 04 2007 Alexey Tourbin <at@altlinux.ru> 2005.08.29-alt2
- imported sources into git and adapted for gear
- fixed type casts for x86_64
- fixed menu group (#5626)

* Wed Apr 26 2006 Alexey Tourbin <at@altlinux.ru> 2005.08.29-alt1
- pick up from orphaned
- new snapshot
- data pack now packaged separately

* Mon Jan 12 2004 Alexander Nekrasov <canis@altlinux.ru> 2003.12.23-alt2
- changelog is corrected
- cretion of a directory demos is added

* Thu Jan 09 2004 Alexander Nekrasov <canis@altlinux.ru> 2003.12.23-alt1
- new version
- building of cube3d server is added

* Fri Oct 17 2003 Alexander Nekrasov <canis@altlinux.ru> 2002.10.20-alt4
- the binary files are built from the source code

* Thu Oct 16 2003 Alexander Nekrasov <canis@altlinux.ru> 2002.10.20-alt3
- the problems with a system of the user's configurations are corrected

* Thu Oct 09 2003 Alexander Nekrasov <canis@altlinux.ru> 2002.10.20-alt2
- the system of the user's configurations, is built

* Tue Oct 07 2003 Alexander Nekrasov <canis@altlinux.ru> 2.10.20-alt1
- first build
