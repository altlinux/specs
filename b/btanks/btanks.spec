%def_with python3scons
%def_with lua51

Name: btanks
Version: 0.9.8083
Release: alt8

Summary: Battle Tanks is a funny battle on your desk

Packager: Ilya Mashkin <oddity at altlinux.ru>

Group: Games/Arcade
License: GPL
Url: http://btanks.sourceforge.net/
Source: %name-%version.tar

BuildRequires: gcc-c++ libsigc++2-devel
BuildRequires: hd2u libalut-devel ImageMagick libSDL-devel libSDL_image-devel libvorbis-devel scons zlib-devel libsmpeg-devel
BuildRequires: libexpat-devel libX11-devel libSM-devel libGL-devel libICE-devel
BuildRequires: libopenal1-devel libXext-devel libXi-devel libXmu-devel
%if_with lua51
BuildRequires: lua5.1-devel
%else
BuildRequires: lua-devel
%endif
BuildRequires: chrpath
#libmesa-devel
Requires: libalut libSDL libSDL_image %name-data
Requires: libopenal1

# mageia patches
# Remove RPath from binaries
Patch10:	%{name}-remove-rpath.patch
# Disable video previews of map levels (we don't distribute video anyway)
Patch11:	%{name}-disable-smpeg.patch
# Avoid problem with lib checks using c++ instead of c.
Patch12:	%{name}-libcheck.patch
# Don't override Fedora's options
Patch13:	%{name}-excessopts.patch
# gcc is now more picky about casting
Patch14:	%{name}-gcc.patch
# bted doesn't explicitly link to clunl
Patch15:	%{name}-dso.patch
Patch16:	%{name}-gcc4.7.patch
# fix build against lua 5.2
Patch17:	%{name}-0.9.8083-lua-5.2.patch
# fix build against scons 3.0
Patch18:	%{name}-scons3.patch
Patch19:	%{name}-scons-3.0.3.patch

# debian patches
Patch21:	rename-currency-symbol.patch
Patch22:	pow10f.patch


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

%patch10 -b .remove-rpath
%patch11 -b .disable-smpeg
%patch12 -b .libcheck
%patch13 -b .excessopts
%patch14 -b .gcc
%patch15 -b .dso
%patch16 -p1 -b .gcc47
%if_without lua5.1
%patch17 -p1 -b .lua-52
%endif
%if_with python3scons
%patch18 -p1 -b .scons
%patch19 -p1 -b .scons
%endif
%patch21 -p1
%patch22 -p1

dos2unix  *.txt ChangeLog *.url LICENSE
chmod 644 *.txt ChangeLog *.url LICENSE

%build
# flags need to be passed via environment or they get treated as a single
# word rather than as multiple arguments. CXXFLAGS is only needed if
# there are c++ only flags that need to get added.
export CFLAGS="%{optflags}"; \
scons %{?jobs:-j%jobs} \
	prefix=%prefix \
        lib_dir=%{_libdir} \
	resources_dir=%_datadir/%name \
	plugins_dir=%_libdir/%name \
	mode=release \
        enable_lua=true

%install
install -dm 755 %buildroot%_bindir
install -m 755 build/release/engine/btanks \
	%buildroot%_bindir
install -m 755 build/release/editor/bted \
	%buildroot%_bindir

install -dm 755 %buildroot%_libdir
install -m 644 build/release/mrt/libmrt.so \
	build/release/clunk/libclunk.so \
	build/release/engine/libbtanks_engine.so \
	build/release/sdlx/libsdlx.so \
	%buildroot%_libdir

install -dm 755 %buildroot%_libdir/%name
install -m 644 build/release/objects/libbt_objects.so \
	%buildroot%_libdir/%name/

install -dm 755 %buildroot%_libdir/%name/data

install -dm 755 %buildroot%_datadir/%name/data
cp -R data/* \
	%buildroot%_datadir/%name/data

# icon
install -dm 755 %buildroot%_miconsdir
convert engine/src/bt.xpm -resize 16x16! \
	%name.png
install -m 644 %name.png \
	%buildroot%_miconsdir

install -dm 755 %buildroot%_niconsdir
convert engine/src/bt.xpm -resize 32x32! \
	%name.png
install -m 644 %name.png \
	%buildroot%_niconsdir

install -dm 755 %buildroot%_liconsdir
convert engine/src/bt.xpm -resize 48x48! \
	%name.png
install -m 644 %name.png \
	%buildroot%_liconsdir

# menu-entry
install -dm 755 %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/%name.desktop << EOF
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
* Wed Dec 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.8083-alt8
- NMU: fixed build

* Sat Jan 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.8083-alt7
- NMU: fixed build

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.8083-alt6
- NMU: fixed build with new g++
- rebuild with new lua 5.1

* Tue Aug 07 2012 Ilya Mashkin <oddity@altlinux.ru> 0.9.8083-alt5
- fix build

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

