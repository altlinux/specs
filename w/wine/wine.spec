# Spec for Wine, enhanced and localized by eterwine project
#
# All source code can be downloaded from ftp://updates.etersoft.ru/pub/Etersoft/WINE@Etersoft
# Please submit bugfixes or comments via wine@etersoft.ru
#
# Build instruction:
# install etersoft-build-utils and rpm-build-altlinux-compat for your system
# run
#    $ rpmbb wine.spec for build rpm package on ALT
# or $ rpmbph wine.spec for other distro
#
%define debug %nil

Name: wine
Version: 1.5.5
Release: alt1
Epoch: 1

Summary: Environment for running Windows applications (Etersoft edition)
Summary(ru_RU.UTF-8): Среда для запуска программ Windows (сборка от Etersoft)

License: LGPL
Group: Emulators
Url: http://winehq.org.ru/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source tarball from git://git.etersoft.ru/projects/eterwine.git
# (with Etersoft's addons and patches)
Source: ftp://updates.etersoft.ru/pub/Etersoft/Wine-public/%version/sources/tarball/%name-%version.tar

AutoReq: yes, noperl

# Thanks PLD folks for the note:
# NOTE: wine detects the following SONAMES for dlopen at build time:
#   libssl (libcrypto inside) (wininet.dll)
#   libcups (winspool.dll.so, wineps.dll.so)
#   libcurses/libncurses/libncursesw (wineconsole program)
#   libfontconfig (gdi32.dll.so)
#   libfreetype (wineps.dll.so, gdi32.dll.so)
#   libGL (x11drv.dll.so, ddraw.dll.so)
#   libjack (winejack.drv.so - explicit dependency in subpackage)
#   libX11, libXext, libXi, libXrender (x11drv.dll.so)
# thus requires rebuild after change of any of the above.
#

#==========================================================================

# Needed freetype (it is recommended to use 2.1.10 for better results)
%define freetype_ver 2.1.9

# General dependencies
BuildRequires: rpm-build-intro
BuildRequires: gcc util-linux flex bison
BuildRequires: fontconfig-devel libfreetype-devel >= %freetype_ver
BuildRequires: libncurses-devel libncursesw-devel libtinfo-devel
BuildRequires: libssl-devel zlib-devel libldap-devel libgnutls-devel
BuildRequires: libxslt-devel libxml2-devel
BuildRequires: libjpeg-devel liblcms-devel libpng-devel libtiff-devel
BuildRequires: libusb-devel libgphoto2-devel libsane-devel libcups-devel
BuildRequires: libalsa-devel jackit-devel libieee1284-devel libhal-devel
BuildRequires: libopenal-devel libGLU-devel
BuildRequires: libv4l-devel gstreamer-devel gst-plugins-devel libgsm-devel libmpg123-devel

# https://bugzilla.altlinux.org/show_bug.cgi?id=20356
BuildRequires: libesd-devel
# TODO: libjack-devel

# Note: xorg-x11-devel requires all X11 devel packages, but missed on Fedora based systems
# Require here all subpackages
# Skipped: libxorgconfig-devel libxkbfile-devel libxkbui-devel xcursorgen xorg-x11-font-utils
# xorg-x11-util-macros xorg-x11-compat-devel libXfontcache-devel libFS-devel libXdmcp-devel
# xorg-x11-xtrans-devel libdmx-devel libXp-devel libXtst-devel libXTrap-devel
BuildRequires: libICE-devel libSM-devel
BuildRequires: libX11-devel libXau-devel libXaw-devel libXrandr-devel
BuildRequires: libXext-devel libXfixes-devel libXfont-devel libXft-devel libXi-devel
BuildRequires: libXmu-devel libXpm-devel libXrender-devel
BuildRequires: libXres-devel libXScrnSaver-devel libXinerama-devel libXt-devel
BuildRequires: libXxf86dga-devel libXxf86misc-devel libXcomposite-devel
BuildRequires: libXxf86vm-devel libfontenc-devel libXdamage-devel
BuildRequires: libXvMC-devel libXcursor-devel libXevie-devel libXv-devel
BuildRequires: libudev-devel

BuildRequires: perl-XML-Simple

# with prelink not found, base address of core dlls won't be set correctly
BuildRequires: prelink

# Actually for x86_32
Requires: glibc-pthread glibc-nss
# Runtime linked
Requires: libcups libncurses libssl
Requires: libXrender libICE libuuid

# We have not to use it in production (used in winedbg)
#BuildConflicts: valgrind-devel valgrind

%if %_vendor == "alt"
#ExclusiveArch:  %{ix86}
Requires: webclient
BuildRequires: desktop-file-utils

# Use fonts-ttf-liberation instead proprietary MS Core Fonts
Requires: fonts-ttf-core

# Comment out due desktop-file-utils is missed in ALD 4.0
# For menu/MIME subsystem
#Requires(post): desktop-file-utils
#Requires(postun): desktop-file-utils
%endif

# We need predownloaded Gecko engine
Requires: wine-gecko = 1.5

Requires: lib%name = %epoch:%version-%release
Provides: %name-utils
Obsoletes: %name-utils
Obsoletes: %name-test

Provides: winetricks

#=========================================================================

%description
WINE Is Not Emulator. Wine is an Open Source implementation of the Windows
API on top of X and Unix.  Think of Wine as a compatibility layer for
running Windows programs. Wine does not require Microsoft Windows,
as it is a completely free alternative implementation of the Windows
API consisting of 100 percent LGPL code, however Wine can optionally
use native Windows DLLs if they are available. Wine provides both a
development toolkit for porting Windows source code to Unix as well as
a program loader, allowing many unmodified Windows programs to run on
x86-based Unixes, including Linux, FreeBSD, and Solaris.

It is still alpha level code; don't expect everything to work.

It is modified Wine build with some patches from Etersoft.
Check http://winehq.org.ru for an additional information.
Bug tracker: http://bugs.etersoft.ru

%description -l ru_RU.UTF-8
WINE Не Является Эмулятором. Это альтернативная реализация API Windows
3.x и Win32. Wine предоставляет как инструментарий разработки (Winelib)
для переноса унаследованных исходных кодов из среды Windows в среду
Unix, так и программный загрузчик, позволяющий исполнять двоичный код, разработанный
для Windows 3.1/95/NT, в среде разных вариантов
Unix на платформе Intel. Wine не требует наличия Microsoft Windows,
поскольку это полностью альтернативная реализация, состоящая из полностью
свободного кода.

WINE всё ещё находится в стадии разработки, поэтому
не ожидайте, что всё будет работать.

Это сборка Wine, содержащая дополнительные изменения по отношению к официальной версии.
Обращайтесь за дополнительной информацией на сайт http://winehq.org.ru
Система регистрации ошибок: http://bugs.etersoft.ru

%package -n %name-test
Summary: WinAPI test for Wine
Summary(ru_RU.UTF-8): Тест WinAPI для Wine
Group: Emulators
Requires: %name = %epoch:%version-%release

%description -n %name-test
WinAPI test for Wine (unneeded for usual work).
Warning: it may kill your X server suddenly.

%package -n lib%name
Summary: Main library for Wine
Group: System/Libraries

# Load with dl_open
Requires: libssl

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with Wine.

%description -n lib%name -l ru_RU.UTF-8
Этот пакет состоит из библиотек, которые реализуют Windows API.

########## separate libraries
%package -n lib%name-gl
Summary: DirectX/OpenGL support libraries for Wine
Group: System/Libraries
Requires: lib%name = %epoch:%version-%release

%description -n lib%name-gl
This package contains the libraries for DirectX/OpenGL support in Wine.

%package -n lib%name-twain
Summary: Twain support library for Wine
Group: System/Libraries
Requires: lib%name = %epoch:%version-%release

%description -n lib%name-twain
This package contains the library for Twain support.

##########################################################################
%package -n lib%name-devel
Summary: Headers for lib%name-devel
Group: Development/C
Requires: lib%name = %epoch:%version-%release
Obsoletes: wine-devel
Provides: wine-devel
Conflicts: libwine-vanilla-devel-static

%description -n lib%name-devel
lib%name-devel contains the header files and some utilities needed to
develop programs using lib%name.

%description -n lib%name-devel -l ru_RU.UTF-8
lib%name-devel содержит файлы для разработки программ, использующих Wine:
заголовочные файлы и утилиты, предназначенные
для компилирования программ с lib%name.

%package -n lib%name-devel-static
Summary: Static libraries for lib%name
Group: Development/C
Requires: lib%name = %epoch:%version-%release

%description -n lib%name-devel-static
lib%name-devel-static contains the static libraries needed to
develop programs which make use of Wine.

##########################################################################

%prep
%setup

%build
%configure --with-x \
%ifarch x86_64
	--enable-win64 \
%endif
	--disable-tests

make depend
%make_build


%install
%makeinstall_std
%__make -C etersoft initdir=%_initdir DESTDIR=%buildroot install-etersoft

# Do not pack non english man pages yet
rm -rf %buildroot%_mandir/*.UTF-8


%pre
%groupadd wine || :
%groupadd wineadmin || :

%post
%post_service wine
# start service during first time install (not for ALT), see rpm-build-compat
%start_service wine

%preun
%preun_service wine


%files
%doc ANNOUNCE AUTHORS LICENSE README
%lang(de) %doc documentation/README.de
%lang(es) %doc documentation/README.es
%lang(fr) %doc documentation/README.fr
%lang(hu) %doc documentation/README.hu
%lang(it) %doc documentation/README.it
%lang(ko) %doc documentation/README.ko
%lang(nb) %doc documentation/README.no
%lang(pt) %doc documentation/README.pt
%lang(pt_BR) %doc documentation/README.pt_br
%lang(tr) %doc documentation/README.tr

%_bindir/wine
%_bindir/wine-glibc
%ifnarch x86_64
%_bindir/wine-preloader
%endif

%_bindir/regsvr32
%_bindir/winecfg

# link to wine for backward compatibility
%_bindir/wineprefixcreate
%_bindir/ieinstall
%_bindir/ieuninstall
%_bindir/winetricks
%_bindir/wineregdiff
%_bindir/setnethasp
%_bindir/winelog
%_bindir/winesplash

%_bindir/wineconsole
%_bindir/wineserver

%_bindir/msiexec
%_bindir/notepad
%_bindir/regedit
%_bindir/winedbg
%_bindir/wineboot
%_bindir/winefile
%_bindir/winemine
%_bindir/winepath
%_libdir/wine/*.exe.so

%_initdir/wine
%_initdir/wine.outformat
# _localstatedir is broken on some systems as ALT Linux
#attr(0775 root wineadmin) %dir %_localstatedir/wine/
%attr(0775 root wineadmin) %dir /var/lib/wine/
# rules for fix permissions on protection keys
%_sysconfdir/udev/rules.d/99-winekeys.rules
#%_sysconfdir/sysctl.d/wine.conf
%dir %_sysconfdir/wine/
%dir %_sysconfdir/wine/reg.d/
%dir %_sysconfdir/wine/script.d/
%_sysconfdir/wine/reg.d/*.reg*
%_sysconfdir/wine/reg.d/foxpro.manual
%_sysconfdir/wine/script.d/*.sh*
%config(noreplace) %_sysconfdir/wine/config
%_desktopdir/*
%_datadir/desktop-directories/wine.directory
%_iconsdir/*
%dir %_datadir/wine/
%_datadir/wine/ies4linux/
%_datadir/wine/skel/
%_datadir/wine/menu.directory
%_datadir/wine/winesplash.xpm
%_datadir/wine/winesplash.xpm.conf
%_datadir/wine/winesplash.png
%_datadir/wine/winesplash.png.conf
%_man1dir/wine.1*
%_man1dir/wineserver.1*
%_man1dir/winedbg.1.*


%files -n lib%name
%doc LICENSE AUTHORS COPYING.LIB
%_libdir/libwine*.so.*
%dir %_libdir/wine/
%_libdir/wine/fakedlls/

%ifnarch x86_64
%_libdir/wine/*.dll16.so
%_libdir/wine/*.drv16.so
%_libdir/wine/*.exe16.so
%_libdir/wine/winoldap.mod16.so
%_libdir/wine/*.vxd.so
%endif

%_libdir/wine/*.cpl.so
%_libdir/wine/*.drv.so
%_libdir/wine/*.dll.so
%_libdir/wine/*.acm.so
%_libdir/wine/*.ocx.so
%_libdir/wine/*.tlb.so
%_libdir/wine/*.sys.so
%_datadir/wine/generic.ppd
%_datadir/wine/wine.inf
%_datadir/wine/l_intl.nls
%_datadir/wine/fonts/

# move to separate packages
%exclude %_libdir/wine/twain*
%exclude %_libdir/wine/d3d10.dll.so
%exclude %_libdir/wine/d3d8.dll.so
%exclude %_libdir/wine/d3d9.dll.so
%exclude %_libdir/wine/d3dxof.dll.so
%exclude %_libdir/wine/opengl32.dll.so
%exclude %_libdir/wine/glu32.dll.so
%exclude %_libdir/wine/wined3d.dll.so


%files -n lib%name-twain
%_libdir/wine/twain*
%_libdir/wine/gphoto2.ds.so
%_libdir/wine/sane.ds.so


%files -n lib%name-gl
%_libdir/wine/d3d10.dll.so
%_libdir/wine/d3d8.dll.so
%_libdir/wine/d3d9.dll.so
%_libdir/wine/d3dxof.dll.so
%_libdir/wine/opengl32.dll.so
%_libdir/wine/glu32.dll.so
%_libdir/wine/wined3d.dll.so


%files -n lib%name-devel
%doc LICENSE LICENSE.OLD README.winedump
%_bindir/winebuild
%_bindir/wmc
%_bindir/wrc
%_bindir/widl
%_bindir/wineg++
%_bindir/winegcc
%_bindir/winecpp
%_bindir/winedump
%_bindir/winemaker

%_includedir/wine/
%_libdir/lib*.so
%_libdir/wine/lib*.def
%_libdir/wine/libwinecrt0.a
%_libdir/wine/libadsiid.a
%_libdir/wine/libdinput.def.a
%_libdir/wine/libdxerr8.a
%_libdir/wine/libdxerr9.a
%_libdir/wine/libdxguid.a
%_libdir/wine/libstrmiids.a
%_libdir/wine/libstrmbase.a
%_libdir/wine/libuuid.a

%_man1dir/wmc.1*
%_man1dir/wrc.1*
%_man1dir/widl.1*
%_man1dir/winebuild*
%_man1dir/winedump.1.*
%_man1dir/wineg++.1.*
%_man1dir/winegcc.1.*
%_man1dir/winecpp.1.*
%_man1dir/winemaker.1.*
%_man1dir/msiexec.1.*
%_man1dir/notepad.1.*
%_man1dir/regedit.1.*
%_man1dir/regsvr32.1.*
%_man1dir/wineboot.1.*
%_man1dir/winecfg.1.*
%_man1dir/wineconsole.1.*
%_man1dir/winefile.1.*
%_man1dir/winemine.1.*
%_man1dir/winepath.1.*


%changelog
* Mon May 28 2012 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.5-alt1
- new build 1.5.5
- use wine-gecko 1.5

* Fri Mar 09 2012 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.0-alt2
- fix build

* Fri Mar 09 2012 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.0-alt1
- new release 1.4.0
- winetricks: update to 20120308
- add wineregdiff command

* Tue Jan 24 2012 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.37-alt2
- winetricks: update to 20111115
- add direct requires

* Tue Jan 17 2012 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.37-alt1
- release 1.3.37

* Sun Dec 18 2011 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.35-alt1
- release 1.3.35

* Fri Dec 09 2011 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.34-alt2
- set wine-gecko 1.4 require

* Wed Dec 07 2011 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.34-alt1
- release 1.3.34

* Sat Aug 27 2011 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.27-alt1
- release 1.3.27

* Fri Aug 26 2011 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.26e-alt1
- release 1.3.26, fix build
- drop out winehelp desktop file (ALT bug #26054)
- use wine-gecko 1.3

* Mon Apr 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.16-alt1
- release 1.3.16
- disable file type associations export by default (eterbug #7021) (ALT bug 25214)
- fix for option which is not working without export (eterbug #4327)
- update build requires

* Sun Mar 20 2011 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.14-alt2
- realize path rewrite in C code instead shell (ALT bug 23696)

* Wed Mar 02 2011 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.14-alt1
- release 1.3.14

* Wed Mar 02 2011 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.13-alt1
- release 1.3.13

* Tue Feb 01 2011 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.12-alt1
- release 1.3.12

* Fri Jan 28 2011 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.11-alt1
- release 1.3.11
- fix mailto in '1C Chronograf'
- new rules for new udev
- fix executing programs with shortcuts

* Mon Jan 10 2011 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.10-alt1
- release 1.3.10
- add default url for Wine browser, set secur32 to builtin
- update winetricks to 20101222
- winetricks: use detected MENU instead direct command
- fix WINPROC_AllocProc args (eterbug #6585), it broke regedit right menu

* Wed Dec 29 2010 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.10-alt0
- add comment to placeholder files hosts, services
- wine.init: drop out initial runlevel (altbug #24152)
- winspool.drv: return maximum possible size of the buffer when no buffer specified

* Thu Dec 23 2010 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.9-alt1
- release 1.3.9
- fix gecko requires
- fix run with spaced args (ALT bug 23696)
- use fonts-ttf-core instead fonts-ttf-liberation (ALT bug 23074)
- disable start wine service by default (ALT bug 24152)
- update winetricks to 20101008
- build with libesd support (ALT bug 20356)
- add libtiff, libv4l gstreamer, libgsm, libmpg123 buildreqs
- build with prelink using (for fixing libs' base address)

* Wed Dec 01 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.8-alt1
- release 1.3.8

* Mon Nov 15 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.7-alt1
- release 1.3.7

* Mon Nov 01 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.6-alt1
- release 1.3.6

* Mon Oct 18 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.5-alt1
- release 1.3.5

* Mon Oct 04 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.4-alt1
- release 1.3.4

* Mon Sep 20 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.3-alt1
- release 1.3.3
- fix MSWord always print 1 copy of document (#4063)

* Wed Sep 08 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.2-alt1
- release 1.3.2

* Tue Sep 07 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.1-alt1
- release 1.3.1

* Mon Sep 06 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.3.0-alt1
- release 1.3.0

* Thu Sep 02 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.2-alt1
- release 1.2

* Thu Sep 02 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.2_rc7-alt1
- release 1.2-rc7

* Thu Sep 02 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.2_rc5-alt1
- release 1.2-rc5

* Thu Sep 02 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.2_rc4-alt1
- release 1.2-rc4

* Wed Sep 01 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.2_rc3-alt1
- release 1.2-rc3

* Thu Jun 03 2010 Ilya Shpigor <elly@altlinux.org> 1:1.2_rc2-alt1
- new version 1.2-rc2

* Fri May 14 2010 Ilya Shpigor <elly@altlinux.org> 1:1.1.44-alt2
- fix error with --only-first parameter for wineboot.exe (altbug #23417)

* Thu May 13 2010 Ilya Shpigor <elly@altlinux.org> 1:1.1.44-alt1
- new version 1.1.44

* Tue May 04 2010 Ilya Shpigor <elly@altlinux.org> 1:1.1.43-alt2
- new version 1.1.43-alt2

* Mon Apr 26 2010 Ilya Shpigor <elly@altlinux.org> 1:1.1.43-alt1
- new version 1.1.43

* Mon Apr 12 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.42-alt1
- release 1.1.42

* Sat Mar 27 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.41-alt1
- release 1.1.41

* Sat Mar 27 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.40-alt1
- release 1.1.40

* Sat Mar 27 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.39-alt1
- release 1.1.39
- fix installation of etersoft tools

* Sat Mar 27 2010 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.38-alt2
- cleanup spec, build for Sisyphus

* Wed Feb 17 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.38-alt1
- release 1.1.38

* Wed Feb 17 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.37-alt1
- release 1.1.37

* Mon Feb 15 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.36-alt1
- release 1.1.36

* Wed Feb 10 2010 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.35-alt1
- release 1.1.35

* Thu Jan 21 2010 Ilya Shpigor <elly@altlinux.org> 1:1.1.34-alt3
- fix version output (altbug #22624)

* Fri Jan 08 2010 Ilya Shpigor <elly@altlinux.org> 1:1.1.34-alt2
- fix bug with wine-glibc

* Wed Jan 06 2010 Ilya Shpigor <elly@altlinux.org> 1:1.1.34-alt1
- new version 1.1.34
- don't build libwine-vanilla-devel-doc package
- fix build for x86_64

* Mon Dec 28 2009 Ilya Shpigor <elly@altlinux.org> 1:1.1.32-alt2
- enable build for x86_64 (fix altbug #10042)

* Mon Dec 14 2009 Ilya Shpigor <elly@altlinux.org> 1:1.1.32-alt1
- release 1.1.32

* Mon Dec 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.31-alt2
- add wine-gecko requires
- map-devices.sh: add e: -> /media for usability (alt bug #21159)
- drop sysctl.d set (min vmem) from install (alt bug #21075)

* Sat Dec 05 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.31-alt1
- release 1.1.31

* Mon Oct 26 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.30-alt1
- release 1.1.30

* Sun Oct 25 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.29-alt2
- cleanup spec, add libopenal, libmpg123 buildreqs
- build with libhal-devel (fix alt bug#21159)

* Thu Oct 01 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.29-alt1
- release 1.1.29

* Tue Jun 30 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.24-alt2
- rebuild with new openldap

* Sat Jun 20 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.24-alt1
- release 1.1.24

* Tue Jun 16 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.23-alt1
- fix Nalogoplatelshik printing

* Thu Jun 04 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.22-alt2
- build for ALT Linux Sisyphus

* Sun May 24 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.22-alt1
- release 1.1.22
- fix MS Office 2003 printing

* Mon May 11 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.21-alt2
- release 1.1.21
- wine start script: unset TMPDIR, hold wine drivers in memory

* Sat May 09 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.21-alt1
- merged with upstream

* Mon May 04 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.20-alt1
- merged with upstream

* Tue Apr 14 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.19-alt1
- merged with upstream

* Sat Mar 28 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.18-alt1
- new version 1.1.18

* Tue Mar 17 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.17-alt1.1
- remove twain readme
- add sysctl.d rule for winebug #12516

* Sat Mar 14 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.17-alt1
- merged with upstream
- fix 1C crashes opening html page (eterbug #3582)
- print: implement collation

* Wed Mar 04 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.16-alt2
- wine.spec: fix descriptions
- move /etc/wine .reg and .sh to new reg.d, script.d dirs
- clean up wine script
- set WINEDEBUG to disable mshtml fixmes
- wine.init: fix checking on status and start the service (eterbug #3591)

* Sat Feb 28 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.16-alt1
- new version 1.1.16
- fix ieinstall (add dll overrides) (altbug #16948)

* Sat Feb 21 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.15-alt2
- merged with upstream

* Fri Feb 13 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.15-alt1
- merged with upstream
- mshtml: Add support of IHTMLBaseElement (fix eterbugs #3343, #2517, #3025, #3107, #3168)

* Mon Feb 09 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.14-alt1
- merged with upstream
- kernel32: Fix eterbug #3116
- mshtml: Add declaration of IHTMLBaseElement
- Add registry file for Sentinel LPT key support
- msi: Automatic path correction for custom action #50 (eterbug 1126)
- winetricks: fix install corefonts (eterbug #2860)
- winetricks: default version =win98 (eterbug #3159)


* Tue Jan 20 2009 Vitaly Perov <vitperov@etersoft.ru> 1:1.1.13-alt1
- fix ieinstall (altbug #16948)
- merged with upstream
- pack exclusive .a libraries in devel package
- fix grdwine.dll build with old kernel headers

* Sat Jan 10 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.12-alt2
- merged with upstream

* Sun Jan 04 2009 Vitaly Lipatov <lav@altlinux.ru> 1:1.1.12-alt1
- build package from public source from git://git.etersoft.ru/projects/eterwine.git
- merged with upstream (wine 1.1.12)

* Fri Dec 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.10-alt4
- merged with upstream (wine 1.1.11)
- fix crashes 1C 8.0 for eterbug #1902
- disable glyph cache for non 1C application (see eterbug #3101)
- gdi32: correct order of transformation matrix elements (see eterbug #3101)
- fix mouse click on checkbox in Consultant (eterbug #3139)
- disable global exception handler if WINEDISABLEGEH is set (see eterbug #2494)
- wglUseFontOutlines: set lfWidth according to RC size (see eterbug #2999)
- add the WIN_NEEDS_FOCUS flag for delayed setting focus (eterbug #3126)
- application don't able to change ptMaxPosition in WINDOWPLACEMENT (eterbug #3129)
- add redrawing for the controls under bitmap static control (eterbug #2234)
- restore hack for eterbug #571 (enable checkbox for any style, not for 1C)
- fix window issues (eterbugs #945, #969, #2604, #2737, #2845, #2938, #3002, #3048, #3110)
- add check for correct registry creating (see eterbug #1993)
- enable beep in MessageBox (eterbug #1094)
- do not print annoying message (see eterbug #2917)
- fix FineReader 8.0 installation problem (eterbug #2560)
- fix 1C crashes in html (eterbug #2405), fix order in vtbl's (eterbug #2105)
- disable ncursesw detecting (eterbug #845)

* Thu Dec 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.10-alt3
- merged with upstream (wine 1.1.10)
- fix window issues (eterbugs #969, #1094, #1837, #2604, #2845, #2930, #2938, #2941, #3002, #3048)
- improve mountmgr, ntoskrnl (eterbug #2887)
- fix FineReader 8.0 installation problem (eterbug #2560)
- fix 1C crashes in html (eterbug #2405)
- add USER to computer name if WINEADDUSERTOCOMPNAME is set (eterbug #2620)
- add udev rule and registry file for Guardant Stealth/Net II USB key
- improve performance: skip the protection of dib sections for 1C 8.x (eterbug #2776)
- add hacks for Fallout 3 (winehq bugs #6971, #15839)
- fix segfault when copying from clipboard (eterbug #2258)
- fix services issues (see eterbug #807)
- mshtml: fix order of functions in vtbl's (for eterbug #2105)

* Fri Nov 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.10-alt2
- merged with upstream (wine 1.1.9)
- update ieinstall script (do not need cabexract now)
- disable tests build

* Mon Nov 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.10-alt1
- merge with upstream (wine 1.1.8)
- cleanup spec

* Mon Nov 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt35
- fix some window issues (eterbugs #1837, #2720, #2808, #2796)
- fix installation process for 1C 8.x updates (eterbug 2873)

* Tue Nov 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt34
- refix eterbug #683 (introduced in alt33), revert some optimisations
- disable menu jump during switch MDI windows (eterbug #2857)

* Sat Nov 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt33
- hack for the topmost showing the popup windows in 1c7 and 1c8 (eterbug #1837)
- add workaround for broken utimensat syscall on ovz kernels (see altbug #17806, fix eterbug #2740)
- changes for MDI window switching patch (eterbug #495)
- fix popup listbox issues (eterbug #2728)
- add the checking to 1c version for 1c8.0 menu patch (eterbug #2808)
- fix mountmgr.sys working, add fix for winecfg with Drive tab
- backports some fixes from wine 1.1.8
- use fdatasync instead fsync (improve database file operation speed)
- disable FileFlushBuffers if set env var WINEDISABLEFLUSH

* Fri Oct 31 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt32
- refix eterbug #993
- disable build on x86_64
- add support for eterwinesplash.xpm

* Thu Oct 30 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt31
- partial fix for MDI issues (eterbug #495)
- fix IE license text, fix wine dir checking in ieinstall
- fix build on FreeBSD

* Thu Oct 30 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt30
- set the more correct owner for MessageBox Windows in 1C77 (eterbugs #945, 2437, 2757)
- restore build with gnutls (eterbug #2701)
- fix wrong print scale (eterbug #61)
- fix run MS Office XP by collection table fixes (eterbug #2658)
- load usb key drivers only if needed
- correct fix for cpu loading by winedevice (eterbug #2726)
- fix mountmgr.sys crash (eterbug #2754)
- fix problem with dosdevices/c: directory
- close eterbugs #441, 2735, 2737, 2705

* Fri Oct 24 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt29
- merge with upstream (wine 1.1.7)
- fix companylogo installing and packing
- fix MS Office 2000 installation fixes (eterbug #771)
- temp. workaround for winedevice cpu eating (eterbug #2726)
- temp. fix build with obsoleted gnutls (eterbug #2701)

* Wed Oct 22 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt28
- winecfg: add missed companylogo.bmp (eterbug #2678)
- return umask 0002 (needed for shared mode)
- fix mshtml registering (eterbug #2676)
- some fix for popup menu in 1C (eterbug #969)
- fix automaximizing MDI windows (eterbug #2668)

* Tue Oct 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt27
- merge with upstream
- fix hangup on wine --update due broken rpc error handling (eterbug #2662)
- fix crash 1C 8.x during initial start (eterbug #2405)
- semifix crash 1C 8.x in html editor (eterbug #2105)
- fix owner drawn menu in Konsultant (close eterbug #489 again)
- some fix for topmost window behavior (eterbug #1837)
- update splash screen (eterbug #2424)
- use DEFAULT_GUI_FONT instead default SYSTEM_FONT in tabs (eterbug #2495)

* Mon Oct 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt26
- merge with upstream
- temp. add hack for printing scale (eterbug #61)
- disable some noises (eterbugs #1659, #2652)
- fix install Garant Network (eterbugs #2660)
- fix printing regress (eterbug #2654)
- move config file to /etc/wine/config
- use umask 0007 by default
- fix segfault on Mandriva 2008.1 (eterbug #2645, winebug #15650)

* Thu Oct 16 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt25
- merge with upsteam
- add install udev rules for protections keys Sentinel/Eutron
- fix eterbugs #929, 1793, 1994, 2399, 2572
- close eterbugs #721, 2028
- test Info Buhgalter 8.6 setup and run (fix eterbug #510)
- add numero sign to tahoma (fix eterbug #2002)
- fix window issues (eterbugs #945, 1129, 2168, 2409, 2437)
- fix MS Office XP installation (eterbug #610)

* Tue Oct 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt24
- merge with upstream (wine 1.1.6)
- some fixes in USB support, fix ntoskrnl and device support
- fix eterbug #837: Static is too small to display multiline text
- fix eterbug #2501: msi.dll: Fix writting incorrect value to the registry
- fix eterbug #2482: Installation of SP1 for Kompas 10 fails
- fix eterbug #2465: explorer can't open *.doc files
- comctl32: Add the selection change notification in the expand event processing for the treeview control (eterbug #2353)
- comctl32: Add the checking for the case then click was on subitem of the listview item (eterbug #840)
- uxtheme: Delete the OffsetViewportOrgEx call from the DrawThemeParentBackground. (eterbug #2349)
- winex11.drv: Fix rectangle overflow if ell_height is sufficiently big (eterbug #1971).
- winex11.drv: Improve drawing little rectangles (eterbug #1971).

* Sat Sep 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt23
- merge with upstream (wine 1.1.5)
- allow overwrite symlinks (fix eterbug #2469)

* Wed Sep 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt22
- Add the flag MDIF_IDLE to check the idle state of MFC applications (eterbug #2350)
- fix KOMPAS 10 installation (eterbug #2410)
- disable autoupdate by .update-timestamp (fix eterbug #2457)

* Mon Sep 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt21
- merge with upstream
- fix error handling in NdrSendReceive (hack for eterbug #2357)
- close splash by double click (eterbug #2436)

* Thu Sep 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt20
- fix local HASP key troubles (eterbug #2407, 1897)
- fix update/attach - remove mountmgr.sys (hack for eterbug #2357)

* Tue Sep 09 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt19
- merge with upstream (wine 1.1.4)
- window switching issues (eterbugs #495, 2302)
- fix serial devices issues (eterbugs #553, 2233)
- fix eterbugs #451, 595, 954, 1129, 2098, 2351, 2352

* Thu Aug 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt18
- add hack for FTDI USB Serial Device converter
- add hack for window switching (eterbug #495)
- add test and fix for WM_CTRLCOLOREDIT (eterbug #448)

* Tue Aug 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt17
- merge with upstream (wine 1.1.2)
- run winesplash only in commercial build
- uncomment svcctl_OpenSCManagerW (fix eterbug #2083)
- fix MAPIFindNext (eterbug #33)
- add NetShareAdd/NetShareGetInfo (eterbug #2086, #2117)
- add XML support via OpenOffice.org (eterbug #2175)
- many USB subsystem fixes, improve ntoskrnl.exe functions
- fix eterbugs #2004, 2203, close eterbug #1819
- fix build on Special Linux 3.0
- realize winver and winecfg/About with Etersoft's texts and logo

* Tue Jul 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt16
- merge with upstream (wine 1.1.1)
- revert commit c7da2d04572c0de65f41f965049ced05f9e3d90f (was for eterbug #1619)
- skip registry saving if file is read only (fix eterbug #1920)
- fix printing in 1C 8.1 (eterbug #2084)
- implemented mlang:fnIMLangFontLink_GetStrCodePages (eterbug #2013)
- fix altbug #16230 again (direct linking with init functions from freetype/fontconfig)
- fix environment creating (admin mode too)
- add desktop files for admin and update command (fix eterbug #2106)

* Tue Jul 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt15
- merge with upstream
- add winesplash command with correct trap signal, winesplash.xpm
- link gdi32 with freetype/fontconfig directly (fix altbug #16230)
- drop out patch for DestroyWindow (fix eterbug #1916, reopen #165)
- apply old patches for hack eterbugs #225, 399, 432, 985

* Thu Jul 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt14
- merge with upstream
- close eterbugs #1916, #1640
- add icons for text and table documents (eterbug #1800)
- fix setnethasp to create nethasp.ini in lower case
- do not translate Url for host wrappers (ooffice and so on)

* Tue Jun 24 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt13
- merge with upstream
- realize IMediaPlayer::put_URL (fix eterbugs #1943, #1954)
- add mplayer script - host media player wrapper
- fix wine first run initialization
- move glu32.dll.so to libwine-gl package
- cleanup spec

* Sat Jun 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt12
- WINE@Etersoft 1.0.9 rc5 (Wine 1.0 stable release)
- fix eterbugs #172, 930
- add initial wmp.dll realization (eterbug #1844)
- read config vars from /etc/sysconfig/wine (fix eterbug #1925)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt11
- fix wineusb compiling
- fix eterbugs #106, 1074, 1849, 1920

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt10
- WINE@Etersoft 1.0.9 rc4 (Wine 1.0-rc5 release)
- fix 3D issues (Kompas related), fix eterbug #954
- add wineusb, fix usb key related ntoskrnl.exe functions
- enable support for Sentinel and Eutron USB local keys
- tahoma bold font updated

* Wed Jun 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt9
- merge with upstream

* Sat May 31 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt8
- WINE@Etersoft 1.0.9 rc3 (Wine 1.0-rc3 release)

* Wed May 28 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt7
- update texts in spec
- fix wine environment initializing
- merge with upstream
- add install Flash Player 9 for Gecko

* Mon May 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt6
- WINE@Etersoft 1.0.9 rc2 (Wine 1.0-rc2 release)
- fix duplex printing (eterbug #1686)

* Fri May 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt5
- merge with upstream
- fix eterbugs #1640, 1619, 1628
- enable x86_64 target support

* Wed May 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt3
- fix fonts issues (eterbugs #1637, 1819)
- add MS Core Fonts -> Liberation replacements
- use windows/Fonts dir instead fonts
- disable some fixmes

* Mon May 19 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt2
- merge with upstream
- fix eterbug #1700
- remove winhelp command
- update winetricks to 20080519
- remove unsupported languages from ieinstall, fix iconv using
- set CompanyName to Etersoft in all dlls
- fix interpackage requires

* Sat May 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.9-alt1
- WINE@Etersoft 1.0.9 rc1 (Wine 1.0-rc1 release)
- new tarball build scheme
- drop date based version scheme, use Etersoft version of the project

* Fri Apr 04 2008 Vitaly Lipatov <lav@altlinux.ru> 20080404-alt1
- WINE@Etersoft 1.0.9 beta release (Wine 0.9.59 release)
- add parallel print jobs support
- create Microsoft.NET dir (fix eterbug #1530)
- fix pre script, remove compatibility hacks from the spec
- add wbemprox dll initial realization (fix eterbug #1154)
- enable build with debug (add --enable-debug to configure)

* Sat Mar 29 2008 Vitaly Lipatov <lav@altlinux.ru> 20080321-alt2
- disable wine autoupdate
- fix print multiple copies (bug #1119)
- fix build on Solaris
- restore mscoree.dll (fix bug #1536)

* Sat Mar 22 2008 Vitaly Lipatov <lav@altlinux.ru> 20080321-alt1
- WINE@Etersoft 1.0.9 beta release (about Wine 0.9.58 release)
- add wingding font
- fix eterbugs #127, 150, 907, 1098

* Wed Mar 12 2008 Vitaly Lipatov <lav@altlinux.ru> 20080311-alt1
- WINE@Etersoft 1.0.9 alpha release (about Wine 0.9.57 release)
- fix eterbugs #993, 1052, 1092, 1093
- fix bugs related to admin mode (eterbugs #692, 1287)
- fix update issues (eterbugs #987, 1115, 1116)
- close eterbugs #500, 547, 1022, 1303

* Sat Feb 23 2008 Vitaly Lipatov <lav@altlinux.ru> 20080222-alt1
- WINE@Etersoft 1.0.9 alpha release (about Wine 0.9.56 release)
- new ieinstall scripts (eterbug #693), add ieunstall script (eterbug #1192)
- improve extrac32 (eterbug #782)
- fix eterbugs #423, 727, 723, 846, 1090, 1095
- close eterbugs #77, 662, 734, 764, 843, 852, 914
- close MS Office related eterbugs #771, 831, 832, 928, 1068

* Tue Feb 19 2008 Vitaly Lipatov <lav@altlinux.ru> 20071130-alt10
- WINE@Etersoft 1.0.8 bugfix release (eterbugs #1120, 1167)

* Sun Jan 27 2008 Vitaly Lipatov <lav@altlinux.ru> 20071130-alt9
- WINE@Etersoft 1.0.8 bugfix release (eterbugs #1103, 674)
- fix toplevel windows issues again 
- some changes for OSMP Dealer

* Mon Jan 21 2008 Vitaly Lipatov <lav@altlinux.ru> 20071130-alt8
- WINE@Etersoft 1.0.8 bugfix release
- fix eterbugs #695, 945, 1048
- fix toplevel windows issues (eterbugs #40, 645, 1087)
- use 32 bit menu handles only for 1C 7.7 (eterbug #927)
- improve extrac32 (eterbug #984)
- full implement OleUIAddVerbMenu function (eterbug #931)

* Thu Dec 27 2007 Vitaly Lipatov <lav@altlinux.ru> 20071130-alt7
- WINE@Etersoft 1.0.8 bugfix release
- fix mcache on FreeBSD (eterbug #648)
- fix ieinstall on FreeBSD
- rewrote wine script, fix wine --attach warnings
- fix bugs #907, #855, #945, 1017
- fix Name encoding in desktop file (#960)
- disable GL calls if GLX is missed (#973), disable sound about libGL

* Fri Dec 21 2007 Vitaly Lipatov <lav@altlinux.ru> 20071130-alt6
- fix winetricks
- fix eterbugs #507, #981, #985, #142

* Sun Dec 16 2007 Vitaly Lipatov <lav@altlinux.ru> 20071215-alt1
- Wine 0.9.51 release
- update patches

* Fri Dec 14 2007 Vitaly Lipatov <lav@altlinux.ru> 20071130-alt5
- WINE@Etersoft 1.0.8 release (about Wine 0.9.50 release)
- fix build with gcc 2.95
- set Gecko load dir in wine.inf
- fix SegFault on FreeBSD
- fix insert from X clipboard (eterbug #826)

* Wed Dec 12 2007 Vitaly Lipatov <lav@altlinux.ru> 20071130-alt4
- disk e: is link to /media (/mnt for legacy systems)
- fixes for default printer (eterbugs #922, 225)
- fix eterbugs #920, 931

* Fri Dec 07 2007 Vitaly Lipatov <lav@altlinux.ru> 20071130-alt3
- remove printer entries during autoupdate
- fix components install during --attach
- print version and regnumber in winecfg

* Mon Dec 03 2007 Vitaly Lipatov <lav@altlinux.ru> 20071130-alt2
- replace xorg-x11-devel with full devel packages lists
- fix wide char to cp866 converting (eterbug #498)

* Fri Nov 30 2007 Vitaly Lipatov <lav@altlinux.ru> 20071130-alt1
- WINE@Etersoft 1.0.8 beta release (about Wine 0.9.50 release)
- add xorg-x11-devel buildreq 
- add setnethasp script
- depricate X11 font using
- cleanup spec
- fix explorer.exe against legacy rpcrt4.dll

* Wed Nov 28 2007 Vitaly Lipatov <lav@altlinux.ru> 20071109-alt2
- WINE@Etersoft 1.0.8 beta release (about Wine 0.9.49 release)
- update ieinstall script
- fix eterbugs #106, 59, 507, 544, 571, 581, 625, 650, 683, 701
- fix eterbugs #720, 724, 729, 741, 778, 843, 889, 901
- close altbugs #13521, #12294, #12369

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 20071109-alt1
- jump to Wine 0.9.49
- fix collation using

* Sun Nov 11 2007 Vitaly Lipatov <lav@altlinux.ru> 20071026-alt3
- clean up spec, remove defattr, old comments
- remove all platforms buildreqs (use rpmbph for build now)
- enable gstabs (as by default)
- fix oledbg (eterbug #750)

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 20071026-alt2
- more fixes for ieinstall
- separate GL-related dlls to libwine-gl package
- add winegecko cab and registry entry for local install
- remove multidistro release, remove multidistro freetype buildreqs

* Fri Nov 02 2007 Anatoly Lyutin <vostok@etersoft.ru> 20071026-alt1
- jump to Wine 0.9.48, more fixes

* Thu Oct 18 2007 Vitaly Lipatov <lav@altlinux.ru> 20071012-alt1
- intermediate release
- add winetricks

* Mon Sep 17 2007 Vitaly Lipatov <lav@altlinux.ru> 20070915-alt1
- WINE@Etersoft 1.0.8 alpha release (about Wine 0.9.45 release)

* Sun Jul 29 2007 Vitaly Lipatov <lav@altlinux.ru> 20070728-alt1
- WINE@Etersoft 1.0.8 pre release (about Wine 0.9.42 release)
- fix build with gcc 2.95, hack for broken rpath

* Sat Jul 21 2007 Vitaly Lipatov <lav@altlinux.ru> 20070720-alt1
- WINE@Etersoft 1.0.8 pre release (about Wine 0.9.41 release)
- fix FreeBSD segfault (eterbug #648)
- fix eterbug #24, 40, 625

* Thu Jun 21 2007 Vitaly Lipatov <lav@altlinux.ru> 20070621-alt1
- WINE@Etersoft 1.0.7 bugfix release (about Wine 0.9.39 release)
- possibly fix eterbug #631, fix eterbug #416
- fix install on ALT Linux (due new rpath)
- replace DejaVu Sans with LiberationSans-Regular (use as 'any font')
- fix groupadd for Debian based (fix eterbug #612)
- remove strict requires for desktop-file-utils on ALT Linux

* Sun Jun 17 2007 Vitaly Lipatov <lav@altlinux.ru> 20070601-alt1
- WINE@Etersoft 1.0.7 release
- fix eterbugs #363

* Fri Jun 15 2007 Vitaly Lipatov <lav@altlinux.ru> 20070601-alt1
- WINE@Etersoft 1.0.7 rc1 (Wine 0.9.38 release)
- add CIFS support (fix eterbugs #477, 590)
- fix fonts issues (encoding, substition) (eterbugs #529, 573, 580, 618)
- fix segfault during printing (eterbugs #154, 155)
- fix eterbugs #76, 124, 363, 557, 578, 593, 591, 619
- close eterbugs #56, 126, 186, 537, 585

* Fri May 25 2007 Vitaly Lipatov <lav@altlinux.ru> 20070524-alt1
- WINE@Etersoft 1.0.7 beta release (about Wine 0.9.38 release)
- add cache for wineserver requests
- fix eterbugs #53, 142, 165, 382, 487, 504

* Tue May 22 2007 Vitaly Lipatov <lav@altlinux.ru> 20070521-alt1
- WINE@Etersoft 1.0.7 alpha release (Wine 0.9.37 release)
- fix initial registry for correct using IE's interfaces
- add Debian menu and new icons from Marcelo Shima <mshima@gmail.com>
- disable libarts build (remove from all system!), remove libwine-arts package
- move install additional parts to etersoft/Makefile
- add ooffice run for doc, xsl files (partially fix eterbug #494)
- fix desktop link
- adopted for Mandriva 2007.1
- fix serial port writing (partially fix eterbug #124)

* Mon Mar 05 2007 Vitaly Lipatov <lav@altlinux.ru> 20070302-alt1
- WINE@Etersoft 1.0.6 bugfix release (Wine 0.9.31 release)
- fix build with old GL library, fix service control error during msi install
- fix wine --admin, fix C drive permissions
- fix build on FreeBSD 5.4
- fix ieinstall script, fix map_devices.sh
- fix cmd file executing

* Tue Feb 27 2007 Vitaly Lipatov <lav@altlinux.ru> 20070226-alt1
- WINE@Etersoft 1.0.6 release (about Wine 0.9.31 release)
- fix Java Swing segfault (eterbug #399), fix font size (use DejaVuSans as default)
- close eterbugs #442, #486
- fix ieinstall script (for install from current dir distro)
- fix printer dialog issues (eterbugs #74, #144)
- fixes for ownerdraw menu size, no network messagebox for Consultant (eterbugs #489, #172)
- fix input in text window for 1C 8.0 (eterbug #432)

* Sat Feb 24 2007 Vitaly Lipatov <lav@altlinux.ru> 20070223-alt1
- WINE@Etersoft 1.0.6 beta release (about Wine 0.9.31 release)
- add lock checking during first run
- fix printer driver locating in changed Win98/WinXP environment (eterbug #452)
- enable russian/byelorussian/ukrainian collation for cp1251 (fix eterbug #39)
- more fixes (fix eterbugs #80, 111, #470)
- close eterbug #51, 169, 189

* Tue Jan 16 2007 Vitaly Lipatov <lav@altlinux.ru> 20061224-alt2
- WINE@Etersoft 1.0.5 bugfix release (about Wine 0.9.28 release)
- fix IE 6 install without commercial part
- fix copying between Wine applications (eterbug #421), in wineconsole (eterbug #433)
- fix Escape reaction in MessageBox (eterbug #37)
- fix menu delays in 1C 8.x
- close eterbug #398 for russian/ukrainuan input in Ubuntu 6.10

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 20061224-alt1
- WINE@Etersoft 1.0.5 bugfix release (about Wine 0.9.28 release)
- fix wine install on Ubuntu 6.10 (dash compatibility)
- fix IE 6 install without Internet connection
- fix copying from Wine applications to clipboard (eterbug #421)
- mainstream: update GL code, mshtml/OLE fixes

* Thu Dec 14 2006 Vitaly Lipatov <lav@altlinux.ru> 20061212-alt1
- WINE@Etersoft 1.0.5 release (about Wine 0.9.27 release)
- change russian text encoding in spec to UTF-8 for foreign rpm workaround
- fix for correct retrieve CF_TEXT (used in old apps like 1C7.7) (fix eterbug #60)
- fix console input/output encoding (needs ncursesw for UTF8 locale) (fix eterbug #297)
- disable mscoree for a time

* Tue Dec 12 2006 Vitaly Lipatov <lav@altlinux.ru> 20061212-alt0.1
- WINE@Etersoft 1.0.5 prerelease (about Wine 0.9.27 release) - fix bug #10155
- add Ukrainian and Byelorussian characters to bitmap fonts
- wcmd removed (use wineconsole cmd instead)
- hack: always use wine-pthread (wine-kthread (on kernel 2.4) is broken now)
- fix eterbugs #38, 43, 107, 109, 133, 158, 159, 163, 176, 186

* Thu Oct 26 2006 Vitaly Lipatov <lav@altlinux.ru> 20060902-alt3
- WINE@Etersoft 1.0.4 bugfix release
- fix init.d/wine dir creating
- use wine-pthread only as WINELOADER

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 20060902-alt2
- WINE@Etersoft 1.0.4 release (about Wine 0.9.20 release)
- fix eterbug #285 (division by zero when papers is not available)
- add require glibc-core-i686 for ALT Linux Compact 3.0
- fix paths in wine launcher (for correct wineprefixcreate)
- do not need libcapi20, libuninames for build
- fix window's buttons in GNOME	(eterbug #187), thanks to Nickolay V. Shmyrev 
- fixes for Linux XP compatible
- add ies4linux scripts, fix build Win64 for x86_64
- cleanup spec, do not overwrite Wine's ChangeLog
- reenable patch for mmap on FreeBSD

* Tue Sep 12 2006 Vitaly Lipatov <lav@altlinux.ru> 20060902-alt1
- WINE@Etersoft 1.0.4 prerelease (about Wine 0.9.20 release)
- fix eterbugs #72, 105, 124, 128, 131, 167, 175, 178, 183
- remove --rpath usage at all, remove requires Xdialog, hd2u

* Tue Aug 29 2006 Vitaly Lipatov <lav@altlinux.ru> 20060829-alt0.1
- WINE@Etersoft 1.0.4 prerelease (about Wine 0.9.19 release)
- fix winecfg segfault due broken patch (altbug #9602)
- link wineprefixcreate to wine
- fix X running from winelog (unneeded dependens)
- disable --rpath usage (rpm does not recognize paths like /usr/bin/../lib in requires)
- fix eterbugs #140

* Wed Aug 02 2006 Vitaly Lipatov <lav@altlinux.ru> 20060802-alt0.1
- WINE@Etersoft 1.0.4 prerelease (about Wine 0.9.18 release)
- enable stack execution (execstack) if possible

* Sun Jun 25 2006 Vitaly Lipatov <lav@altlinux.ru> 20060610-alt2
- WINE@Etersoft 1.0.3 bug fix release
- fix executing third party install scripts
- export DEV variable for map_devices script
- disable execute permission for map_devices
- eterbug #177 fixed

* Sun Jun 18 2006 Vitaly Lipatov <lav@altlinux.ru> 20060610-alt1
- WINE@Etersoft 1.0.3 release (about Wine 0.9.15 release)
- remove VerSetConditionMask from kernel32
- fixes for native dll loading on FreeBSD
- fix upper/lower functions in combobox (for Cli-BB) (eterbug #153)
- add patch for fix splash screen managed state
- add some delays and cases for processor load problem (eterbug #48)
- fix vendor info in winecfg/About

* Tue May 30 2006 Vitaly Lipatov <lav@altlinux.ru> 20060530-alt1
- add checking for 1C 77 in wine start script
- add getuname, srvapi stub dlls, remove wineps tolerance
- remove wineprefixcreate (incorporated in wine start script)

* Sat May 20 2006 Vitaly Lipatov <lav@altlinux.ru> 20060520-alt1
- WINE@Etersoft 1.0.2 release (closed eterbug #73, #121)
- new build, fix defattr
- fix binfmt module loading (service wine)
- fix minizing, maximizing window, MDI maximizing (eterbug #91, winebug #4960)
- add admin setup functionality (see wine --admin, wine --attach)
- disable warning about registry saving error
- add categories to desktop file

* Tue May 02 2006 Vitaly Lipatov <lav@altlinux.ru> 20060422-alt2
- WINE@Etersoft 1.0.1 release
- remove some registry entries, update package description
- add check for broken (too short) system registry
- add some mapi functions (fix eterbug #33)
- disable fontforge requiring, disable some unuseful messages
- also fix eterbugs #68, #71, #88, #93, #35
- add patches for FreeBSD, old gcc
- add patch against accidentally stack overflow (MENU_FindItem)
- temp. disable owner draw tabs

* Sat Apr 15 2006 Vitaly Lipatov <lav@altlinux.ru> 20060414-alt1
- WINE@Etersoft 1.0.1 prerelease (about WINE 0.9.12)
- rearranged additional files (make source tarball shared with FreeBSD build)
- add registry entry for each program separately
- move all patches to addon tarball
- fix dos devices search (eterbug #59 fixed)
- add wineadmin group creating
- add provides wine-etersoft-public
- add warning if WINE dir is obsoleted
- rewrite service script in universal manner
- enable service script using (for wine's program direct executing)
- remove fnt2dbf as unneeded (freetype already supports .fnt fonts)
- add --update option for update WINE tree from previous versions

* Sun Apr 02 2006 Vitaly Lipatov <lav@altlinux.ru> 20060402-alt1
- development release (about WINE 0.9.11)
- improve initial scripts
- improve DLL overrides (add support for IE6 install)
- add patch for shrink file paths (thanks to argentum@)
- disable rpath using (due broken requires in RPM)

* Thu Mar 16 2006 Vitaly Lipatov <lav@altlinux.ru> 20060316-alt1
- development release (about WINE 0.9.10)
- add patch against window focus (eterbug #34 fixed)
- add patch against close messagebox handling (eterbug #37 fixed)
- half fix bug with DEL (eterbug #38)
- rewrite patches for font search
- change default color theme to Etersoft's one
- fix unable to run user's start.exe (eterbug #47)

* Thu Mar 09 2006 Vitaly Lipatov <lav@altlinux.ru> 20060302-alt4
- WINE@Etersoft 1.0.0 release
- set default umask for wine to 0007
  (rational: group writeable, no world readable is needed for file sharing)
- remove if_with from this spec

* Wed Mar 08 2006 Vitaly Lipatov <lav@altlinux.ru> 20060302-alt3
- WINE@Etersoft 1.0 prelease
- add prelink in buildreqs for ALT Linux, Redhat brothers, Debian/Ubuntu
- add build conflicts with valgrind
- fix build requires to freetype (was missed in prev. ALT release)
- add check for freetype build complete
- add improved bitmap (and marlett.ttf too) fonts
- do not build fonts with fontforge here (use tested&prepacked)
- remove tinfo substing in configure
- fix bug with flex >= 2.5.33
- cleanup spec (remove obsoleted lines, remove chstk using)
- move additional files to standalone tarball (SOURCE5)

* Thu Mar 02 2006 Vitaly Lipatov <lav@altlinux.ru> 20060302-alt1
- new version (WINE 0.9.9 release), WINE@Etersoft 1.0 beta
- fix required freetype version
- no need ttf Arial anymore, update font find patch
- fix add drv/dll/exe/16 packaging
- do not place path to /usr/lib/wine in ld.so.conf.d/
- fix Redhat build requires and so
- remove version substing from spec
- rearrange freetype dependencies (check for version now)
- add libxml2-devel, libxslt buildreq for correct msxml building

* Wed Feb 15 2006 Vitaly Lipatov <lav@altlinux.ru> 20060215-alt1
- new version (WINE 0.9.8 release)
- add patch for wine system fonts directory support
- remove links to dll.so from _libdir
- really applied patch with sharing files support
- fix make install
- init file is replaceable now
- cleanup spec
- winetest is not packaged now
- packing README.* for some languages
- remove old DESTDIR patch

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 20060209-alt1
- new version (about WINE 0.9.8), WINE@Etersoft 1.0 Network alpha
- remove wine-fonts-ttf package (incorporate fonts in libwine)
- remove any font issues from spec
- cleanup spec with rpmcs
- move fonts from _datadir/fonts/wine to _datadir/wine/fonts
- move share dir to libwine package
- build with libwine-etersoft Network support patch
- add winelog script for prepare debug output, use for support@
- remove glibc-devel-static from requires

* Sat Dec 17 2005 Vitaly Lipatov <lav@altlinux.ru> 20051216-alt1
- WINE@Etersoft 0.9 release (about WINE 0.9.4)
- clean spec
- build with libwine-etersoft support patch
- fix wineshelllink (bug #8596)
- add msi native support in alt.reg
- fix man placement, fix man extension

* Thu Dec 08 2005 Vitaly Lipatov <lav@altlinux.ru> 20051208-alt1
- new version from CVS (according to WINE 0.9.3)
- test with various popular applications

* Sun Nov 13 2005 Vitaly Lipatov <lav@altlinux.ru> 20051107-alt1
- new version
- rewrite map_devices.sh
- do not use drive_c (c: is real dir now)
- add /var/lib/wine-default support
- disable hard debugging
- hack for winetest disable

* Thu Nov 10 2005 Vitaly Lipatov <lav@altlinux.ru> 20051107-alt0.M30.1
- build for ALT Linux 3.0 Compact

* Tue Nov 08 2005 Vitaly Lipatov <lav@altlinux.ru> 20051107-eter1alt
- WINE@Etersoft Single 0.9 beta
- fix menu file (used wine-utils)
- unidistro spec

* Mon Nov 07 2005 Vitaly Lipatov <lav@altlinux.ru> 20051107-alt0.1
- add patch from FC for link fonts to WINDOWS\FONTS
- move all files from wine-utils to wine package
- move libcrt0.a to -devel

* Tue Oct 25 2005 Vitaly Lipatov <lav@altlinux.ru> 20051025-alt0.1
- new version (about 0.9 beta)
- split API test into standalone package wine-test
- add cases for other Linux distribution
- workaround about ttmkfdir
- move fon files to wine-fonts-ttf package

* Sat Sep 24 2005 Vitaly Lipatov <lav@altlinux.ru> 20050924-alt0.1
- add dcom98 install support
- some compatibility fixes for Mandriva (thanks to Denis Philippov @mezon.ru)

* Thu Sep 22 2005 Vitaly Lipatov <lav@altlinux.ru> 20050922-alt0.1
- new version

* Wed Aug 31 2005 Vitaly Lipatov <lav@altlinux.ru> 20050831-alt0.1
- new version (release 20050830 nearly)

* Tue Aug 23 2005 Vitaly Lipatov <lav@altlinux.ru> 20050822-eter0.1
- new version
- automated apply reg files from /etc/wine/*.reg

* Tue Aug 02 2005 Vitaly Lipatov <lav@altlinux.ru> 20050715-eter0.2
- add /etc/wine/map_devices.sh for default drive mapping
- enable install application icon to desktop directory WINE Applications
- add fixed registry entries
- fix scripts

* Fri Jul 22 2005 Vitaly Lipatov <lav@altlinux.ru> 20050715-alt0.1
- new version
- see http://winehq.org.ru for details

* Fri Jul 08 2005 Vitaly Lipatov <lav@altlinux.ru> 20050517-alt2
- last release with config file
- add Wine Configuration (winecfg) to menu
- fix bug #7281
- fix CD autorun script bug
- fixed wine launcher script bug

* Thu Jun 16 2005 Vitaly Lipatov <lav@altlinux.ru> 20050517-alt1
- tested version for Sisyphus

* Wed Jun 15 2005 Vitaly Lipatov <lav@altlinux.ru> 20050517-eter4
- add wine.desktop
- fix menu entries
- fix default config file (set WinXP version to imitate)
- fix autorun for html support

* Sat May 21 2005 Vitaly Lipatov <lav@altlinux.ru> 20050517-eter3
- add hack for button focus problem
- add hack for MS Office 97 SwapMouse

* Tue May 17 2005 Vitaly Lipatov <lav@altlinux.ru> 20050517-eter1
- new version
- documentation removed

* Fri May 13 2005 Vitaly Lipatov <lav@altlinux.ru> 20050304-eter2
- back to stable version

* Fri Apr 22 2005 Vitaly Lipatov <lav@altlinux.ru> 20050422-eter1
- about release 20050419

* Fri Apr 15 2005 Vitaly Lipatov <lav@altlinux.ru> 20050415-alt1
- CVS version
- fix bug #6536

* Fri Apr 08 2005 Vitaly Lipatov <lav@altlinux.ru> 20050323-alt1
- fix wine launcher
- remove path from config

* Wed Mar 23 2005 Vitaly Lipatov <lav@altlinux.ru> 20050323-eter1
- CVS version
- fix wineshelllink

* Fri Mar 04 2005 Vitaly Lipatov <lav@altlinux.ru> 20050304-eter1
- CVS version

* Mon Feb 28 2005 Vitaly Lipatov <lav@altlinux.ru> 20050225-alt1
- CVS version
- fix wine launcher and wine shelllink
- add icons for menu group
- add program defaults for wine config

* Mon Feb 14 2005 Vitaly Lipatov <lav@altlinux.ru> 20050211-alt1
- new version

* Thu Feb 03 2005 Vitaly Lipatov <lav@altlinux.ru> 20050119-alt3
- change icon to png format
- change menu entry
- enable static library build
- move lib/*.so to devel package

* Wed Jan 26 2005 Vitaly Lipatov <lav@altlinux.ru> 20050119-alt2
- start wine service after install wine package
- change menu entry

* Wed Jan 19 2005 Vitaly Lipatov <lav@altlinux.ru> 20050119-alt1
- minor changes, CVS version

* Thu Jan 13 2005 Vitaly Lipatov <lav@altlinux.ru> 20050111-alt1
- new release

* Wed Jan 05 2005 Vitaly Lipatov <lav@altlinux.ru> 20050104-alt1
- CVS version
- change menu section to WINE Applications
- wine-multiuser support improved
- developing utilities resorted
- fix verbose during update wine package

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 20041201-alt1
- new release

* Mon Nov 29 2004 Vitaly Lipatov <lav@altlinux.ru> 20041019-alt2
- fix for exe.so only executable
- add some locale fixes
- enable using dlls from DCOM98 by default
- add liblcms-devel dependence (for support MSCMS)

* Fri Nov 05 2004 Vitaly Lipatov <lav@altlinux.ru> 20041019-alt1
- new version
- remove strange dependences
- update packages description
- update default config
- make wine libs executable
- add uninstaller to menu

* Wed Sep 15 2004 Vitaly Lipatov <lav@altlinux.ru> 20040914-alt1
- new version
- update config

* Fri Sep 03 2004 Vitaly Lipatov <lav@altlinux.ru> 20040813-alt1
- new version
- step to ld.conf.so.d with libdir information
- add winelauncher

* Thu Jul 22 2004 Vitaly Lipatov <lav@altlinux.ru> 20040716-alt1
- new version
- fix menu file encoding
- fix cdrom path (for subfs)
- fix postun_ldconfig
- update config, set win98 version to imitate
- rewrite winereboot

* Tue Jun 22 2004 Vitaly Lipatov <lav@altlinux.ru> 20040615-alt2
- add glibc-devel-static buildreq
- move to Applications/Emulators menu section
- disable -gstabs+ gcc option for optimize objects size during compilation
- use a macro for ldconfig

* Sun Jun 20 2004 Vitaly Lipatov <lav@altlinux.ru> 20040615-alt1
- new version
- correct bug with default disk settings
- use wineprefixcreate for first tune
- do not install winelancher
- turn on wine program menu and rewrite wineshelllink script

* Thu May 20 2004 Vitaly Lipatov <lav@altlinux.ru> 20040505-alt1.1
- add link ttydrv with libtinfo (for build with new ncurses)
- build with new glibc

* Fri May 14 2004 Vitaly Lipatov <lav@altlinux.ru> 20040505-alt1
- new version
- default config file synchronized with original

* Sat Apr 10 2004 Vitaly Lipatov <lav@altlinux.ru> 20040408-alt1
- new version

* Tue Apr 06 2004 Vitaly Lipatov <lav@altlinux.ru> 20040309-alt2
- remove require ms-fonts-ttf
- move winearts.drv.so to separate package libwine-arts
- move twine to separate package libwine-twain

* Sun Mar 14 2004 Vitaly Lipatov <lav@altlinux.ru> 20040309-alt1
- new version
- fix bug with /usr/lib/wine permissions
- add menu entries for autorun and reboot

* Tue Feb 17 2004 Vitaly Lipatov <lav@altlinux.ru> 20040121-alt1
- disable devel-static
- add documentation in separate packages
- fix bug with wine-glibc
- update default config
- add icon for wine
- patch for winhelp

* Sun Jan 25 2004 Vitaly Lipatov <lav@altlinux.ru> 20040121-alt0.2
- new version
- clean up spec
- add winetest and winebrowser
- tested with some programs

* Tue Dec 16 2003 Vitaly Lipatov <lav@altlinux.ru> 20031212-alt1
- new version
- winetest build disabled
- tested with 1C 7.7, FineReader Sprint 5.0, Microsoft Word/Excel 97

* Sat Dec 06 2003 Vitaly Lipatov <lav@altlinux.ru> 20031118-alt1
- new version
- add libwine-devel-static package
- rewrite spec (consult with WineX spec and wine spec from ASP Linux)
- fix %build missing (bug #3339 from wrar-alt@mail.ru)
- disable start wine-config.pl from wine
- exclude kde requires from wineshelllink (bug #3360)
- build ntpl enable
- bulld with curses support again

* Mon Oct 27 2003 Vitaly Lipatov <lav@altlinux.ru> 20031016-alt1
- new version

* Thu Sep 25 2003 Vitaly Lipatov <lav@altlinux.ru> 20030911-alt1
- new version
- add Provides: libntdll.dll.so

* Wed Apr 16 2003 Vitaly Lipatov <lav@altlinux.ru> 20030408-alt1
- new snapshot
- build without arts support

* Tue Apr 01 2003 Vitaly Lipatov <lav@altlinux.ru> 20030318-alt1
- new snapshot
- build without curses (ttydrv) support due build problem with acs_map
- update buildrequires

* Thu Nov 21 2002 AEN <aen@altlinux.ru> 20021031-alt4
- %_libdir/lib* moved to lib%name package

* Tue Nov 19 2002 AEN <aen@altlinux.ru> 20021031-alt3
- installation scripts fixed

* Sun Nov 10 2002 AEN <aen@altlinux.ru> 20021031-alt2
- header files moved to right place

* Sun Nov 10 2002 AEN <aen@altlinux.ru> 20021031-alt1
- new version
- spec rewritten
- new patches from MDK,RH & Debian
- new Alt config

* Tue Nov 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 20011004-alt4
- Specfile cleanup.
- Rewritten startup script.
- Fixed typo in %{name}launcher.
- Added libwine_uuid.a to devel subpackage.

* Fri Oct 19 2001 AEN <aen@logic.ru> 20011004-alt3
- wineshelllink removed

* Wed Oct 17 2001 AEN <aen@logic.ru> 20011004-alt2
- wine group added in %pre

* Tue Oct 16 2001 AEN <aen@logic.ru> 20011004-alt1
- 20011004

* Tue Oct 16 2001 AEN <aen@logic.ru> 20010824-alt1
- 20010824

* Tue Sep 18 2001 AEN <aen@logic.ru> 20010731-alt2
- fixed documentation in package

* Tue Sep 18 2001 AEN <aen@logic.ru> 20010731-alt1
- alt1,2 patches

* Tue Sep 11 2001 Stefan van der Eijk <stefan@eijk.nu> 20010731-2mdk
- BuildRequires: sgml-tools
- Remove redundant BuildRequires: glibc-devel, XFree86-devel

* Mon Aug 13 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 20010731-1mdk
- 20010731.
- Rework completly the specfile (move wine from /usr/X11R6 in /usr).
- Add binfmt service to let use launch .exe file directly with wine.
- Merge rh changes.
- Requires latest setup for wine user.

* Thu Jul 12 2001 David BAUDENS <baudens@mandrakesoft.com> 20010629-1mdk
- 20010629

* Fri Jun  8 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 20010510-1mdk
- 20010510.

* Sun Apr 22 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 20010418-1mdk
- 20010418.

* Tue Mar 27 2001 David BAUDENS <baudens@mandrakesoft.com> 20010326-1mdk
- 20010326

* Sun Mar 18 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 20010305-1mdk
- Add /usr/X11R6/lib/wine to ld.so.conf.
- Rewrote all automaticall detection scripts and default config.
- 20010305.

* Thu Dec 07 2000 David BAUDENS <baudens@mandrakesoft.com> 20001202-1mdk
- 20001202
- Disable optimizations for this release (don't build)

* Tue Nov 28 2000 David BAUDENS <baudens@mandrakesoft.com> 20001026-4mdk
- Move libraries in %%prefix/lib/wine

* Tue Nov 28 2000 David BAUDENS <baudens@mandrakesoft.com> 20001026-3mdk
- Add flex bison (Frederic CROZAT) and Mesa-common-devel to BuildRequires
- Little spec clean up

* Fri Nov 10 2000 David BAUDENS <baudens@mandrakesoft.com> 20001026-2mdk
- Build with glibc-2.2 & gcc-2.96

* Fri Oct 27 2000 David BAUDENS <baudens@mandrakesoft.com> 20001026-1mdk
- 20001026

* Wed Oct 04 2000 David BAUDENS <baudens@mandrakesoft.com> 20001002-1mdk
- 20001002

* Mon Sep 11 2000 David BAUDENS <baudens@mandrakesoft.com> 20000909-1mdk
- 20000909

* Tue Sep 05 2000 David BAUDENS <baudens@mandrakesoft.com> 20000821-5mdk
- Rebuild with right options

* Sun Sep 03 2000 David BAUDENS <baudens@mandrakesoft.com> 20000821-4mdk
- Allow to use without install devel package

* Sat Aug 26 2000 David BAUDENS <baudens@mandrakesoft.com> 20000821-3mdk
- Add packager tag

* Tue Aug 22 2000 David BAUDENS <baudens@mandrakesoft.com> 20000821-2mdk
- Add librpcrt4.so in devel package

* Tue Aug 22 2000 David BAUDENS <baudens@mandrakesoft.com> 20000821-1mdk
- 20000821
- Make RPMLint happy (thanks to Guillaume COTTENCEAU)
- Split in two packages (devel and non devel)

* Mon Aug 14 2000 David BAUDENS <baudens@mandrakesoft.com> 20000801-2mdk
- Fix macro disastear
- Enable OpenGL - It needs a lot of tests, so please report bugs
- Some little enhancements in wine-config
- Back in /usr/X11R6
- Spec clean up

* Tue Aug 08 2000 Geoffrey Lee <snailtalk2mandrakesoft.com> 20000801-1mdk
- s|20000716|20000801|
- *real* macrosifications

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 20000716-2mdk
- automatically added BuildRequires

* Wed Jul 19 2000 David BAUDENS <baudens@mandrakesoft.com> 20000716-1mdk
- 20000716
- BM
- Move into /usr

* Mon Jul 10 2000 David BAUDENS <baudens@mandrakesoft.com> 20000614-1mdk
- 20000614
- Make Pixel happy

* Sat May 27 2000 David BAUDENS <baudens@mandrakesoft.com> 20000526-1mdk
- 20000526

* Mon May 01 2000 David BAUDENS <baudens@mandrakesoft.com> 20000430-1mdk
- 20000430
- spec cleanup
- Update URL
- Update LICENSE

* Tue Apr 18 2000 Warly <warly@mandrakesoft.com> 20000326-3mdk
- New group

* Tue Mar 30 2000 David BAUDENS <baudens@mandrakesoft.com> 20000326-2mdk
- Fix wine-config

* Mon Mar 27 2000 David BAUDENS <baudens@mandrakesoft.com> 20000326-1mdk
- 20000326

* Sun Mar 26 2000 David BAUDENS <baudens@mandrakesoft.com> 20000227-2mdk
- Use new group
- Clean up spec

* Wed Mar 01 2000 David BAUDENS <baudens@mandrakesoft.com> 20000227-1mdk
- 20000227

* Thu Dec 09 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Build with new Mesa

* Fri Nov 18 1999 - David BAUDNS <baudens@mandrakesoft.com>
- 991114

* Mon Nov 01 1999 - David BAUDENS <baudens@mandrakesoft.com>
- 991031
- Add i486, i686 and k6 arch
- Delete all locale summary and description (it's in po now)

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 990923

* Thu Aug 05 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- Fix an old bug in the spec (Thanks dark chmouel)

* Thu Aug 05 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- Updated to 19990731

* Wed Jul 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix %post script syntax.

* Tue Jul  6 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 990704
	* windows/*.c, ole/*.c, files/*.c, multimedia/*.c:
	Converted to the new debug interface, using script written by Patrik
	Stridvall.

* Thu May 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fixed %post scripts.
- Upgrade Prereq.

* Wed May 19 1999 Bernhard RosenkrДnzer <bero@mandrakesoft.com>
- 990518
- --enable-dll
- add de locale
- ignore RPM_OPT_FLAGS - Wine segfaults if compiled with more optimizations
  than -O2.

* Wed May 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake 6.0 adaptations.
- 990508

* Tue Apr 05 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 990328.

* Tue Mar 16 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 990314
- Fix in the wine-config postinstall script.

* Sun Jan 03 1999 Pablo Saratxaga <srtxg@chanae.alphanet.ch>
- deleted the %post %postun of package wine-debug (no more needed since
  the wrapper does now the job)
- make use of %prefix definition; now changing almost one line you can
  choose wether you want to install in /usr/local or /usr or %prefix
- changed %post so it is only done the *first* time it is installed
  (otherwise people will hate us for doing weird things whith their
  hand made configurations)

* Tue Dec 29 1998 Chmouel Boudjnah <crbc@club-internet.fr>
- Adding speciale wine-conf for mandrake
- Adding postinstall script
- Changing the ./configure to put wine.conf in /etc and prefix on %prefix
- First version receveid from Pablo Saratxaga <srtxg@chanae.alphanet.ch>
