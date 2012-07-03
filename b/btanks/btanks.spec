%define _prefix	/usr

Name: btanks
Version: 0.9.8083
Release: alt4.1

Summary: Battle Tanks is a funny battle on your desk

Packager: Ilya Mashkin <oddity at altlinux.ru>

Group: Games/Arcade
License: GPL
Url: http://btanks.sourceforge.net/
Source: %name-%version.tar

BuildRequires: hd2u libalut-devel gcc-c++ ImageMagick  libSDL-devel libSDL_image-devel libsigc++2.0-devel libvorbis-devel pkgconfig scons zlib-devel libsmpeg-devel
BuildRequires: liblua5-devel libexpat-devel libX11-devel libSM-devel libGL-devel libICE-devel
BuildRequires: libopenal1-devel libXext-devel libXi-devel libXmu-devel
BuildPreReq: chrpath
#libmesa-devel
Requires: libalut libSDL libSDL_image %name-data
Requires: libopenal1

%package data
Summary: Data files for Battle Tanks
Group: Games/Arcade
License: GPL
BuildArch: noarch

%description
Battle Tanks is a funny battle on your desk, where you can
choose one of three vehicles and eliminate your enemy using
the whole arsenal of weapons. has original cartoon-like
graphics and cool music, it is fun and dynamic, it has
several network modes for deathmatch and cooperative
.. what else is needed to have fun with your friends?

And all is packed and ready for you in Battle Tanks.

%description data
Battle Tanks is a funny battle on your desk, where you can
choose one of three vehicles and eliminate your enemy using
the whole arsenal of weapons. has original cartoon-like
graphics and cool music, it is fun and dynamic, it has
several network modes for deathmatch and cooperative
.. what else is needed to have fun with your friends?

And all is packed and ready for you in Battle Tanks.

This package contains all data files for Battle Tanks


%prep
%setup -q -n %name-%version

dos2unix     *.txt ChangeLog *.url LICENSE
%__chmod 644 *.txt ChangeLog *.url LICENSE

%build
scons %{?jobs:-j%jobs} \
	prefix=%prefix \
	resources_dir=%_datadir/%name \
	plugins_dir=%_libdir/%name \
	mode=release

%install
%__install -dm 755 %buildroot%_bindir
%__install -m 755 build/release/engine/btanks \
	%buildroot%_bindir
%__install -m 755 build/release/editor/bted \
	%buildroot%_bindir

%__install -dm 755 %buildroot%_libdir
%__install -m 644 build/release/mrt/libmrt.so \
	build/release/clunk/libclunk.so \
	build/release/engine/libbtanks_engine.so \
	build/release/sdlx/libsdlx.so \
	%buildroot%_libdir

%__install -dm 755 %buildroot%_libdir/%name
%__install -m 644 build/release/objects/libbt_objects.so \
	%buildroot%_libdir/%name/

%__install -dm 755 %buildroot%_libdir/%name/data

%__install -dm 755 %buildroot%_datadir/%name/data
%__cp -R data/* \
	%buildroot%_datadir/%name/data

# icon
%__install -dm 755 %buildroot%_miconsdir
convert engine/src/bt.xpm -resize 16x16! \
	%name.png
%__install -m 644 %name.png \
	%buildroot%_miconsdir

%__install -dm 755 %buildroot%_niconsdir
convert engine/src/bt.xpm -resize 32x32! \
	%name.png
%__install -m 644 %name.png \
	%buildroot%_niconsdir

%__install -dm 755 %buildroot%_liconsdir
convert engine/src/bt.xpm -resize 48x48! \
	%name.png
%__install -m 644 %name.png \
	%buildroot%_liconsdir

# menu-entry
%__install -dm 755 %buildroot%_datadir/applications
%__cat > %buildroot%_datadir/applications/%name.desktop << EOF
[Desktop Entry]
Type=Application
Name=Battle Tanks
Comment='Battle Tanks' is a funny battle on your desk
Exec=btanks
Icon=%name
Categories=Game;ActionGame;
EOF

for i in %buildroot%_libdir/*.so %buildroot%_libdir/btanks/*.so \
	%buildroot%_bindir/*
do
	chrpath -d $i ||:
done

%clean
[ -d %buildroot -a "%buildroot" != "" ] && %__rm -rf %buildroot

%files
%doc *.txt ChangeLog *.url LICENSE
%_bindir/btanks
%_bindir/bted
%_libdir/%name/
%_libdir/*.so

%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_datadir/applications/%{name}*.desktop

%files data
%dir %_datadir/%name
%dir %_datadir/%name/data
%_datadir/%name/data/*

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8083-alt4.1
- Removed bad RPATH

* Sat Apr 23 2011 Ilya Mashkin <oddity@altlinux.ru> 0.9.8083-alt4
- fix build

* Thu Feb 24 2011 Ilya Mashkin <oddity@altlinux.ru> 0.9.8083-alt3
- fix build

* Mon Jan 10 2011 Ilya Mashkin <oddity@altlinux.ru> 0.9.8083-alt0.M51.2
- build for 5.1

* Mon Nov 08 2010 Denis Pynkin <dans@altlinux.ru> 0.9.8083-alt2
- fixed #24509

* Sat Jan 16 2010 Ilya Mashkin <oddity@altlinux.ru> 0.9.8083-alt1
- New version

* Mon Dec 29 2008 Ilya Mashkin <oddity@altlinux.ru> 0.8.7686-alt1
- new version
- apply repocop patch
- update requires

* Tue Sep 16 2008 Denis Pynkin <dans@altlinux.ru> 0.8.7656-alt1
- version 0.8-Final
- libexpat-devel added to build requires

* Mon Jul 21 2008 Denis Pynkin <dans@altlinux.ru> 0.8.7479-alt1
- Splitted into 2 packages
- Moved libbt_objects.so from to plugins dir %_libdir/%name
- Patch for correct g++ behavior with "+" operator
- Removed bzip2 compression
- Added libsmpeg-devel in build requires

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.6.5069-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for btanks

* Sat Dec 22 2007 Ilya Mashkin <oddity@altlinux.ru> 0.6.5069-alt1
- First Build for Sisyphus

* Fri Oct 05 2007 Toni Graffy <toni@links2linux.de> - 0.6.5069-0.pm.1
- update to 0.5.4800
* Sat Sep 01 2007 Toni Graffy <toni@links2linux.de> - 0.5.4800-0.pm.1
- update to 0.5.4800
* Wed Aug 29 2007 Toni Graffy <toni@links2linux.de> - 0.5.4794-0.pm.1
- update to 0.5.4794
* Wed Aug 15 2007 Toni Graffy <toni@links2linux.de> - 0.5.4740-0.pm.1
- update to 0.5.4740
* Mon Jul 30 2007 Toni Graffy <toni@links2linux.de> - 0.5.4549-0.pm.1
- Initial rpm build 0.5.4549

