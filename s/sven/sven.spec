Name: sven
Version: 0.6
Release: alt2.1.qa1

Summary: Sven - multimedia keyboard daemon
License: GPL
Group: System/Configuration/Other

Url: http://sven.linux.kiev.ua/

Source0: %name-%version.tar.bz2
Source1: %name.png
Source2: %name.desktop
Patch0: %name-0.6-alt-makefile-as_needed.patch
Patch1: %name-0.6-alt-warnings.patch
Patch2: %name-0.6-alt-autoconvert-warnings.patch
Patch3: %name-0.6-alt-gcc4_1-warnings.patch
Patch4: %name-0.6-alt-autoconvert_layouts.patch
Patch5: %name-0.6-alt-autoconvert_save.patch
Patch6: %name-0.6-alt-fixes.patch
Patch7: %name-0.6-alt-autoconvert_layouts-2.patch
Patch8: %name-0.6-alt-audacious.patch
Patch9: %name-0.6-alt-fix-sentinel.patch
Patch10: %name-0.6-alt-warnings-2.patch
Patch11: %name-0.6-alt-translation.patch
Patch12: %name-0.6-alt-doc-bugs.patch

# Automatically added by buildreq on Tue Jan 23 2007
BuildRequires: libgtk+2-devel libpcre-devel libX11-devel libXext-devel libXi-devel libXmu-devel libXtst-devel xorg-cf-files

%description
Sven is a good program for multimedia buttons. You can adjust it for any keyboard.
It is possible to adjust for performance of different programs for each button.

%package devel
Summary: development files for %name
Group: Development/C
Requires: %name

%description devel
Contains development files you'll need to build plugins for %name.

%prep
%setup -q -n %name-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
./autogen.sh
%configure

%make

%install
mkdir -p %buildroot{%_bindir,%_datadir/pixmaps,%_datadir/applications,%_datadir/%name,%_libdir/%name}
make install DESTDIR=%buildroot

#do not pack static files
rm -f %buildroot%_libdir/lib%name.a

#menu support

mkdir -p %buildroot%_iconsdir
mkdir -p %buildroot%_datadir/pixmaps
mkdir -p %buildroot%_datadir/applications
#%%__cp %_builddir/%name-%version/images/%name.png %buildroot%_iconsdir/
install -pD -m644 %SOURCE1 %buildroot%_iconsdir/
install -pD -m644 %SOURCE1 %buildroot%_datadir/pixmaps/
install -pD -m644 %SOURCE2 %buildroot%_datadir/applications/

%find_lang %name

%files -n %name -f %name.lang
%doc AUTHORS BUGS-ru NEWS ChangeLog COPYING README
%_bindir/*
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
%_datadir/%name
%_libdir/%name
%_iconsdir/%name.png
%_libdir/lib%name.so.*

%files devel
%_includedir/%name
%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.6-alt2.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * update_menus for sven
  * postclean-03-private-rpm-macros for the spec file

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6-alt2.1
- NMU:
  * updated build dependencies

* Tue Feb 20 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 0.6-alt2
- fixed gcc warnings patch (fixed plugin loading)

* Fri Feb 16 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 0.6-alt1
- re-added desktop file
- removed old menu entry
- translation fixes

* Sat Feb 03 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 0.6-alt0.ev5
- added sentinel patch (thanks to damir@)
- fixed several gcc warnings

* Thu Jan 25 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 0.6-alt0.ev4
- fixed several autocovert layouts
- added built-in support of Audacious player

* Tue Jan 23 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 0.6-alt0.ev3
- fixed autoconvert for Russia - Winkeys and U.S. English layouts
- fixed autoconvert parameters save
- fixed segfault in plugin unloading
- fixed segfault in cdrom plugin

* Tue Jan 16 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 0.6-alt0.ev2
- fixed --as-needed build
- fixed several gcc4.1 warnings

* Fri Dec 15 2006 Egor Vyscrebentsov <evyscr@murom.net> 0.6-alt0.ev1
- 0.6
- fixed several gcc warnings

* Sun Sep 25 2005 Vladimir Lettiev <crux@altlinux.ru> 0.4.3.3-alt1
- 0.4.3.3
- removed translation patch 

* Wed Aug 31 2005 Vladimir Lettiev <crux@altlinux.ru> 0.4.3.2-alt1
- 0.4.3.2 
- previous patches merged to upstream
- updated translation patch

* Sun Aug 28 2005 Vladimir Lettiev <crux@altlinux.ru> 0.4.3.1-alt1
- 0.4.3.1
- patches: translation (ru.po), makefile (fix build of plugin)

* Sun Aug 28 2005 Vladimir Lettiev <crux@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Tue Jun 21 2005 Vladimir Lettiev <crux@altlinux.ru> 0.4.1-alt1
- 0.4.1
- added devel package

* Wed Jun 08 2005 Vladimir Lettiev <crux@altlinux.ru> 0.4-alt1
- 0.4

* Thu May 06 2004 Vladimir Lettiev <crux@altlinux.ru> 0.3-alt1
- released new version
- removed unnecessary patches
- fixed grammar errors in ru.po
- force install sven.desktop for correct build in hasher

* Mon Apr 12 2004 Vladimir Lettiev <crux@altlinux.ru> 0.2-alt1
- initial release for Sisyphus
