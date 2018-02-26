%if %_vendor == "alt"
%ifarch x86_64
	%def_with build64
%else
    %def_without build64
%endif
%else
   %def_without build64
%endif

Name: wine-vanilla
Version: 1.5.5
Release: alt2

Summary: Wine - environment for running Windows 16/32/64 bit applications

License: LGPL
Group: Emulators
Url: http://winehq.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

# See http://git.etersoft.ru/people/lav/packages/?p=wine.git;a=shortlog;h=refs/heads/vanilla
# Source tarball from git.etersoft.ru, branch vanilla (pulled from wine's git)
Source: ftp://updates.etersoft.ru/pub/Etersoft/Wine-vanilla/%version/sources/tarball/%name-%version.tar
Source1: etersoft/winetricks
Source2: %name-%version-desktop.tar

AutoReq: yes, noperl

%define freetype_ver 2.1.9

# General dependencies
BuildRequires: rpm-build-compat >= 1.0
BuildRequires: gcc util-linux flex bison
BuildRequires: fontconfig-devel libfreetype-devel >= %freetype_ver
BuildRequires: libncurses-devel libncursesw-devel libtinfo-devel
BuildRequires: libssl-devel zlib-devel libldap-devel libgnutls-devel
BuildRequires: libxslt-devel libxml2-devel
BuildRequires: libjpeg-devel liblcms-devel libpng-devel libtiff-devel
BuildRequires: libgphoto2-devel libsane-devel libcups-devel
BuildRequires: libalsa-devel jackit-devel libgsm-devel libmpg123-devel
BuildRequires: libopenal-devel libGLU-devel
BuildRequires: libusb-devel libieee1284-devel libhal-devel
BuildRequires: libv4l-devel gstreamer-devel gst-plugins-devel

# https://bugzilla.altlinux.org/show_bug.cgi?id=20356
BuildRequires: libesd-devel

BuildRequires: libICE-devel libSM-devel
BuildRequires: libX11-devel libXau-devel libXaw-devel libXrandr-devel
BuildRequires: libXext-devel libXfixes-devel libXfont-devel libXft-devel libXi-devel
BuildRequires: libXmu-devel libXpm-devel libXrender-devel
BuildRequires: libXres-devel libXScrnSaver-devel libXinerama-devel libXt-devel
BuildRequires: libXxf86dga-devel libXxf86misc-devel libXcomposite-devel
BuildRequires: libXxf86vm-devel libfontenc-devel libXdamage-devel
BuildRequires: libXvMC-devel libXcursor-devel libXevie-devel libXv-devel

BuildRequires: perl-XML-Simple

# with prelink not found, base address of core dlls won't be set correctly
BuildRequires: prelink

# Actually for x86_32
Requires: glibc-pthread glibc-nss

# Enable with can build on x86_64
# GCC v4.4 is needed for build wine64
#ExclusiveArch:  %{ix86}
Requires: webclient

Requires: wine-gecko = 1.5

BuildRequires: desktop-file-utils
# Use it instead proprietary MS Core Fonts
# Requires: fonts-ttf-liberation

# not linked directly
Requires: libncurses

# For menu/MIME subsystem
Requires: desktop-file-utils

Requires: lib%name = %version-%release
Conflicts: wine

Provides: winetricks

#=========================================================================

%description
While Wine is usually thought of as a Windows(TM) emulator, the Wine
developers would prefer that users thought of Wine as a Windows
compatibility layer for UNIX. This package includes a program loader,
which allows unmodified Windows 3.x/9x/NT binaries to run on x86 and x86_64
Unixes. Wine does not require MS Windows, but it can use native system
.dll files if they are available.

%package -n %name-test
Summary: WinAPI test for Wine
Summary(ru_RU.UTF-8): Тест WinAPI для Wine
Group: Emulators
Requires: %name = %version-%release

%description -n %name-test
WinAPI test for Wine (unneeded for usual work).
Warning: it may kill your X server suddenly.

%package -n lib%name
Summary: Main library for Wine
Group: System/Libraries
Conflicts: libwine

# Runtime linked
Requires: libcups libncurses
Requires: libXrender libICE libuuid
Requires: libssl

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with Wine.

%description -n lib%name -l ru_RU.UTF-8
Этот пакет состоит из библиотек, которые реализуют Windows API.


%package -n lib%name-gl
Summary: DirectX/OpenGL support libraries for Wine
Group: System/Libraries
Requires: lib%name = %version-%release
Conflicts: libwine-gl

%description -n lib%name-gl
This package contains the libraries for DirectX/OpenGL support in Wine.

%package -n lib%name-twain
Summary: Twain support library for Wine
Group: System/Libraries
Requires: lib%name = %version-%release
Conflicts: libwine-twain

%description -n lib%name-twain
This package contains the library for Twain support.


%package -n lib%name-devel
Summary: Headers for lib%name-devel
Group: Development/C
Requires: lib%name = %version-%release
Obsoletes: wine-devel
Provides: wine-devel
Conflicts: libwine-devel

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
Requires: lib%name = %version-%release
Conflicts: libwine-devel-static
Conflicts: libwine-devel

%description -n lib%name-devel-static
lib%name-devel-static contains the static libraries needed to
develop programs which make use of Wine.


%prep
%setup

%build
%configure --with-x --disable-tests \
%if_with build64
	--enable-win64 \
%endif
	--without-esd

%__make depend
%make_build


%install
%makeinstall_std
install -m755 %SOURCE1 %buildroot%_bindir/winetricks
# unpack desktop files
cd %buildroot%_desktopdir
tar xvf %SOURCE2

# Do not pack non english man pages yet
rm -rf %buildroot%_mandir/*.UTF-8

%if %_vendor != "alt"
%post
%update_menus
%update_desktopdb

%postun
%clean_menus
%clean_desktopdb

%post -n lib%name
%post_ldconfig

%postun -n lib%name
%postun_ldconfig
%endif

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

%if_without build64
%_bindir/wine
%_bindir/wine-preloader
%else
%_bindir/wine64
%endif

%_bindir/regsvr32
%_bindir/winecfg

%_bindir/winetricks
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

#%_initdir/wine
#%_initdir/wine.outformat
%_desktopdir/*
%dir %_datadir/wine/

%_man1dir/wine.*
%_man1dir/msiexec.*
%_man1dir/notepad.*
%_man1dir/regedit.*
%_man1dir/regsvr32.*
%_man1dir/wineboot.*
%_man1dir/winecfg.*
%_man1dir/wineconsole.*
%_man1dir/winefile.*
%_man1dir/winemine.*
%_man1dir/winepath.*
%_man1dir/wineserver.*
%_man1dir/winedbg.*


%files -n lib%name
%doc LICENSE AUTHORS COPYING.LIB
%_libdir/libwine*.so.*
%dir %_libdir/wine/
%_libdir/wine/fakedlls/

%if_without build64
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
%doc LICENSE LICENSE.OLD
%_bindir/function_grep.pl
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
#%_aclocaldir/wine.m4

%_man1dir/wmc.*
%_man1dir/wrc.*
%_man1dir/widl.*
%_man1dir/winebuild.*
%_man1dir/winedump.*
%_man1dir/wineg++.*
%_man1dir/winegcc.*
%_man1dir/winecpp.*
%_man1dir/winemaker.*


%files -n lib%name-devel-static
%_libdir/wine/lib*.a
%exclude %_libdir/wine/libwinecrt0.a

%changelog
* Mon May 28 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt2
- fix wine-gecko requires to 1.5

* Sat May 26 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt1
- new version 1.5.5

* Fri Mar 09 2012 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0
- update winetricks to 20120308
- fix requires

* Sat Jan 14 2012 Vitaly Lipatov <lav@altlinux.ru> 1.3.37-alt1
- new version 1.3.37

* Sat Dec 31 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.36-alt1
- new version 1.3.36

* Sat Dec 17 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.35-alt1
- new version 1.3.35
- update winetricks to 20111115

* Tue Dec 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.34-alt1
- new version 1.3.34, use wine-gecko 1.4

* Sat Nov 05 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.32-alt1
- new version 1.3.32

* Tue Nov 01 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.31-alt1
- new version 1.3.31
- update winetricks to 20110629

* Tue Oct 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.30-alt1
- new version 1.3.30

* Fri Aug 26 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.27-alt1
- new version 1.3.26, use wine-gecko 1.3

* Mon Aug 22 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.26-alt1
- new version 1.3.26
- drop out winehelp desktop file

* Thu Jun 02 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.21-alt1
- new version 1.3.21

* Fri Apr 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.19-alt1
- new version 1.3.19

* Sun Apr 17 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.18-alt1
- new version 1.3.18

* Mon Apr 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.17-alt2
- fix build requires (add missed libtiff-devel, gstreamer plugin base, libgnutls-devel)

* Sat Apr 02 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.17-alt1
- new version 1.3.17
- again winetricks: do not use zenity/kdialog via direct run (ALT bug 24838)
- add libncurses requires

* Wed Mar 30 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt3
- drop xorg-x11-proto-devel buildreqs
- pack all man files

* Tue Mar 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt2
- winetricks: update to 20110324
- winetricks: do not use zenity/kdialog via direct run (ALT bug 24838)

* Sat Mar 19 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt1
- new version 1.3.16
- update winetricks to 20110318
- require wine-gecko 1.2.0
- add some desktop files for menu (ALT bug 25237)

* Thu Dec 30 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3.10-alt2
- winetricks: use detected MENU instead direct command (ALT bug 24838)

* Mon Dec 27 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3.10-alt1
- new version 1.3.10 (ALT bug 24273)

* Fri Jul 16 2010 Ilya Shpigor <elly@altlinux.org> 1.2_rc7-alt1
- new version 1.2-rc7

* Mon Jun 14 2010 Ilya Shpigor <elly@altlinux.org> 1.2_rc3-alt1
- new version 1.2-rc3

* Mon May 31 2010 Ilya Shpigor <elly@altlinux.org> 1.2_rc2-alt1
- new version 1.2-rc2

* Tue May 25 2010 Ilya Shpigor <elly@altlinux.org> 1.1.44-alt3
- fix build for x86_64 architecture (try 2)

* Fri May 14 2010 Ilya Shpigor <elly@altlinux.org> 1.1.44-alt2
- fix build for x86_64 architecture

* Tue May 11 2010 Ilya Shpigor <elly@altlinux.org> 1.1.44-alt1
- new version 1.1.44

* Mon Apr 19 2010 Ilya Shpigor <elly@altlinux.org> 1.1.43-alt1
- new version 1.1.43

* Mon Apr 05 2010 Ilya Shpigor <elly@altlinux.org> 1.1.42-alt1
- new version 1.1.42

* Mon Mar 22 2010 Ilya Shpigor <elly@altlinux.org> 1.1.41-alt1
- new version 1.1.41

* Sat Mar 06 2010 Ilya Shpigor <elly@altlinux.org> 1.1.40-alt1
- new version 1.1.40

* Sun Feb 21 2010 Ilya Shpigor <elly@altlinux.org> 1.1.39-alt1
- new version 1.1.39

* Mon Feb 08 2010 Ilya Shpigor <elly@altlinux.org> 1.1.38-alt1
- new version 1.1.38

* Mon Jan 25 2010 Ilya Shpigor <elly@altlinux.org> 1.1.37-alt1
- new version 1.1.37

* Mon Jan 18 2010 Ilya Shpigor <elly@altlinux.org> 1.1.36-alt2
- add winetricks to wine-vanilla package (fix altbug #22650)

* Sat Jan 16 2010 Ilya Shpigor <elly@altlinux.org> 1.1.36-alt1
- new version 1.1.36

* Fri Jan 08 2010 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt4
- fix conflict libwine-vanilla-devel-static with libwine-devel

* Wed Jan 06 2010 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt3
- don't build libwine-vanilla-devel-doc package

* Wed Jan 06 2010 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt2
- build the libwine-vanilla-devel-doc package as the architecture-independent

* Fri Dec 25 2009 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt1
- new version 1.1.35

* Fri Dec 25 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.34-alt2
- enable build for x86_64 (fix altbug #10042)

* Fri Dec 11 2009 Ilya Shpigor <elly@altlinux.org> 1.1.34-alt1
- new version 1.1.34

* Tue Nov 24 2009 Ilya Shpigor <elly@altlinux.org> 1.1.33-alt1
- new version 1.1.33

* Sat Oct 24 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.32-alt1
- new version 1.1.32

* Sat Aug 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt2
- fix services.exe crash (altbug #20927)

* Fri Jul 24 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt1
- new version 1.1.26

* Thu Jul 23 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.25-alt1
- new version 1.1.25

* Tue Jun 30 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.24-alt1
- new version 1.1.24

* Tue May 26 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.22-alt1
- new version 1.1.22

* Sat May 09 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.21-alt1
- new version 1.1.21

* Sat Mar 28 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.18-alt1
- new version 1.1.18

* Fri Mar 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.17-alt1
- new version 1.1.17

* Sat Feb 28 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.16-alt1
- new version 1.1.16

* Sun Feb 15 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.15-alt1
- new version 1.1.15

* Fri Feb 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version 1.1.14

* Sat Jan 17 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt1
- new version 1.1.13

* Tue Jan 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.12-alt1
- merge with upstream (1.1.12)

* Fri Dec 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.11-alt1
- merge with upstream (1.1.11)
- add libhal-devel buildreq

* Fri Nov 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.9-alt1
- merge with upstream (1.1.9)

* Sat Nov 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt1
- merge with upstream (1.1.8)

* Sat Nov 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt2
- rebuild configure
- remove autoconf due too old autoconf in ALT 4.0

* Wed Oct 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt1
- merge with upstream (1.1.7)
- add autoconf -f due strange configure

* Fri Sep 19 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt1
- merge with upstream (1.1.5)
- revert to original sources from git://source.winehq.org/git/wine.git

* Wed Jul 16 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- merge with upstream (1.1.1)
- cleanup spec, return update_menus
- fix altbug #16230 again (run init functions from linked libs)

* Tue Jul 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- merge with upsteam
- link gdi32 with freetype/fontconfig directly (fix altbug #16230)
- disable RPATH for installed libs (LDRPATH_INSTALL=)

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build from vanilla source for ALT Linux Sisyphus
