%def_disable static
%if_enabled static
%define buildstatic 0
%else
%define buildstatic 0
%endif

Name: arts
Version: 1.5.10
Release: alt5.1
Serial: 1

Source: %name-%version.tar

# RH
Patch1: arts-1.1.4-debug.patch
Patch2: arts-1.5.0-check_tmp_dir.patch
Patch3: arts-1.3.1-alsa.patch
Patch4: arts-acinclude.patch
Patch5: libltdl-CVE-2009-3736.patch

# SuSE
Patch22: arts-vorbis-fix.dif

# MDK
Patch31: arts-1.1.4-64bit-fixes.patch
Patch32: arts-1.1.4-lib64.patch

# ALT
Patch100: arts-1.0.1-mcop_home.patch
Patch101: arts-1.0.2-tmpdir.patch
Patch102: arts-1.5.6-flags.patch
Patch103: arts-1.1.4-no_ltdl.patch
Patch104: arts-1.3.92-la2so.patch
Patch105: arts-1.2.3-glib-ldflags.patch
Patch106: arts-1.2.3-detect-esd.patch
Patch107: arts-1.5.10-alt-automake.patch
Patch108: arts-1.5.10-mcopclass-la-replace-so.patch

Group: System/Servers
Summary: aRts (analog realtime synthesizer) - the KDE sound system
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0

Requires: lib%name = %serial:%version-%release
##Conflicts: lib%name-devel-static < %serial:%version-%release
##Conflicts: kdemultimedia-arts <= 3.1.4-alt2 kdemultimedia-noatun <= 3.1.4-alt2

# Automatically added by buildreq on Thu Apr 08 2004 (-bi)
BuildRequires: cmake kde-common-devel gcc-c++ libtqt-devel
BuildRequires: glib2-devel libalsa-devel libltdl7-devel
BuildRequires: libjpeg-devel libmad-devel libpng-devel
BuildRequires: libstdc++-devel pkgconfig zlib-devel
BuildRequires: jackit-devel libaudiofile-devel libmad-devel
BuildRequires: libogg-devel libvorbis-devel
BuildRequires: libqt3-devel > 3.0
# hack against apt
#BuildRequires: libqt3-qsa > 3.0 libqt3-qsa-devel > 3.0

Packager: Sergey V Turchin <zerg@altlinux.org>

%description
aRts is a short form for "analog realtime synthesizer". The idea of the whole
thing is to create/process sound using small modules which do certain tasks.
These may be create a waveform (oscillators), play samples, filter data, add
signals, perform effects like delay/flanger/chorus, or output the data to the
soundcard.

%package -n lib%name
Group: Graphical desktop/KDE
Summary: The libraries for arts

%description -n lib%name
Libraries needed for arts.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files for arts
Requires: lib%name = %serial:%version-%release libalsa-devel
Requires: jackit-devel libaudiofile-devel libmad-devel
Requires: libogg-devel libvorbis-devel
Requires: glib2-devel libalsa-devel libpng-devel
#
%description -n lib%name-devel
Development files for arts.

%package -n lib%name-devel-static
Group: Development/KDE and QT
Summary: Static libraries for arts
Requires: lib%name-devel = %serial:%version-%release
#
%description -n lib%name-devel-static
Static libraries for arts.

%package -n lib%name-qtmcop
Group: Graphical desktop/KDE
Summary: Qt specific arts sound stuff
Requires: lib%name = %serial:%version-%release
Requires: %{get_dep libqt3}
Provides: lib%name-qt = %serial:%version-%release
Obsoletes: lib%name-qt <= %serial:%version-%release
#
%description -n lib%name-qtmcop
Libraries for sound support for Qt library

%package -n lib%name-qtmcop-devel
Group: Development/KDE and QT
Summary: Development files for arts and Qt
Requires: lib%name = %serial:%version-%release
Requires: lib%name-devel = %serial:%version-%release
Requires: lib%name-qt = %serial:%version-%release
Requires: libqt3-devel
Provides: lib%name-qt-devel = %serial:%version-%release
Obsoletes: lib%name-qt-devel <= %serial:%version-%release
#
%description -n lib%name-qtmcop-devel
Development files for sound support for Qt library

%package -n lib%name-qtmcop-devel-static
Group: Development/KDE and QT
Summary: Static libraries for development with arts and Qt
Requires: lib%name-qt-devel = %serial:%version-%release
#Requires: libqt3-devel-static
Provides: lib%name-qt-devel-static = %serial:%version-%release
Obsoletes: lib%name-qt-devel-static <= %serial:%version-%release
#
%description -n lib%name-qtmcop-devel-static
Static libraries for sound support for Qt library

%package -n lib%name-gmcop
Group: System/Libraries
Summary: Glib specific art sound stuff
Requires: lib%name = %serial:%version-%release
#
%description -n lib%name-gmcop
Libraries for sound support for Glib library

%package -n lib%name-gmcop-devel
Group: Development/C++
Summary: Development files for arts and Glib
Requires: lib%name = %serial:%version-%release lib%name-gmcop = %serial:%version-%release
#
%description -n lib%name-gmcop-devel
Development files for sound support for Glib library

%package -n lib%name-gmcop-devel-static
Group: Development/C++
Summary: Static libraries for development with arts and Glib
Requires: lib%name-gmcop-devel = %serial:%version-%release
Requires: glib2-devel-static
#
%description -n lib%name-gmcop-devel-static
Static libraries for sound support for Glib library


%prep
%setup -q -n %name-%version
%patch1 -p1
#%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1
#
#%patch22 -p0
#
%patch31 -p1
#%patch32 -p1
#
#%patch100 -p1
#%patch101 -p1
#%patch102 -p1
#%patch103 -p1
#%patch104 -p1
#%patch105 -p1
#%patch106 -p1
#%patch107 -p1
%patch108 -p1

%build
BD=%_builddir/%name-%version/BUILD
export LD_LIBRARY_PATH=$BD/mcop:$LD_LIBRARY_PATH

%K3cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBIN_INSTALL_DIR=%_bindir \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DBUILD_ALL="ON" \
    -DCMAKE_SKIP_RPATH="OFF" \
    -DWITH_GCC_VISIBILITY="ON" \
    -DINCLUDE_INSTALL_DIR:INTERNAL=%_K3includedir/%name
%K3make

%install
%K3install

mv %buildroot/%_includedir/artsc %buildroot/%_K3includedir/

%files
%_bindir/artscat
%_bindir/artsd*
%_bindir/artsp*
%_bindir/artss*
%_bindir/artsw*
%_bindir/artsr*
#%_bindir/testdhandle

%files -n libarts
%_libdir/libartsc.so*
%_libdir/libartscbackend.so*
%_libdir/libartsdsp.so*
%_libdir/libartsdsp_st.so*
%_libdir/libartsgsl.a
%_libdir/libartsflow.so*
%_libdir/libartsflow_idl.so*
%_libdir/libartswavplayobject.so*
%_libdir/libartsgslplayobject.so*
%_libdir/libkmedia2.so*
%_libdir/libkmedia2_idl.so*
%_libdir/libsoundserver_idl.so*
%_libdir/libmcop.so*
%_libdir/libmcop_mt.so*
#_libdir/libx11globalcomm.so*
#
%dir %_libdir/mcop/
%_libdir/mcop/*.mcopclass
%_libdir/mcop/*.mcoptype
#
%dir %_libdir/mcop/Arts
%_libdir/mcop/Arts/*.mcopclass

%files -n libarts-devel
%_bindir/artsc-config
%_bindir/mcopidl
#
%dir %_K3includedir/arts/
%_K3includedir/arts/gsl
%_K3includedir/arts/*.h
%exclude %_K3includedir/arts/*?iomanager.h
%_pkgconfigdir/%name.pc
#
%_K3includedir/arts/*.idl
#
%dir %_K3includedir/artsc/
%_K3includedir/artsc/*.h
#

%files -n lib%name-qtmcop
%_libdir/libqtmcop.so*
%files -n lib%name-qtmcop-devel
%_K3includedir/arts/qiomanager.h

%files -n lib%name-gmcop
%_libdir/libgmcop.so*
%files -n lib%name-gmcop-devel
%_K3includedir/arts/giomanager.h

%if %buildstatic
%files -n libarts-devel-static
%_libdir/libartsc.a
%_libdir/libartscbackend.a
%_libdir/libartsdsp.a
%_libdir/libartsdsp_st.a
%_libdir/libartsflow.a
%_libdir/libartsflow_idl.a
%_libdir/libartswavplayobject.a
%_libdir/libartsgslplayobject.a
%_libdir/libkmedia2.a
%_libdir/libkmedia2_idl.a
%_libdir/libsoundserver_idl.a
%_libdir/libmcop.a
%_libdir/libmcop_mt.a
#_libdir/libx11globalcomm.a
%files -n lib%name-qtmcop-devel-static
%_libdir/libqtmcop.a
%files -n lib%name-gmcop-devel-static
%_libdir/libgmcop.a
%endif

%changelog
* Mon Feb 24 2014 Roman Savochenko <rom_as@altlinux.ru> 1:1.5.10-alt5.1
- Rebild without dependency to libqt3-devel-cxx

* Tue Jul 30 2013 Roman Savochenko <rom_as@altlinux.ru> 1:1.5.10-alt5
- Return ARTS build to Sisyphus and branches from trinitydesktop.org
  but best sound for external program call and more programms provide.

* Fri Feb 05 2010 Sergey V Turchin <zerg@altlinux.org> 1:1.5.10-alt3.M51.1
- built for M51

* Fri Feb 05 2010 Sergey V Turchin <zerg@altlinux.org> 1:1.5.10-alt4
- fix to compile (ALT#22891)
- fix CVE-2009-3736

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 1:1.5.10-alt3
- fix to build

* Tue Dec 02 2008 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.10-alt2
- remove deprecated macroses from specfile

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.10-alt1
- new version

* Thu Feb 21 2008 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.9-alt1
- new version

* Tue Oct 16 2007 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.8-alt1
- new version

* Tue May 22 2007 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.7-alt1
- new version

* Wed Mar 28 2007 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.6-alt6
- keep libtool files

* Wed Mar 28 2007 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.6-alt5
- fix configure options

* Wed Mar 28 2007 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.6-alt4
- rebuilt

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.6-alt3
- rebuilt

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.6-alt2
- rebuilt without libaudio

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.6-alt1
- new version

* Thu Nov 09 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.5-alt2
- remove linux-libc-headers from build requires

* Thu Oct 12 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.5-alt1
- new version

* Tue Aug 29 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.4-alt1
- new version

* Tue Jun 13 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.3-alt2
- CVE-2006-2916

* Thu Jun 01 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.3-alt1
- new version

* Mon May 15 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.2-alt3
- rebuilt whith new gcc

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.2-alt2
- add patch from RH, fix alsa to be default

* Wed Mar 29 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.2-alt1
- new version

* Wed Mar 22 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.1-alt2
- fix build with new ld

* Tue Jan 31 2006 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.1-alt1
- new version

* Thu Jan 12 2006 LAKostis <lakostis at altlinux dot org> 1:1.5.0-alt4.1
- NMU;
- apply fixes from FC (see their #169631).

* Thu Dec 22 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.0-alt4
- built with -Os

* Thu Dec 22 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.0-alt3
- add la-files

* Tue Dec 20 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.0-alt2
- enable gcc visibility

* Mon Nov 28 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.5.0-alt1
- new version

* Mon Oct 10 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.4.1-alt4
- temporary don't link with --enable-new-dtags

* Tue Oct 04 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.4.1-alt3
- fix %%qtdir

* Mon Jul 11 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.4.1-alt2
- x86_64 fixes; thanks mouse@alt

* Wed Jun 01 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.4.1-alt1
- new version

* Thu Mar 31 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.4.0-alt1
- new version

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.3.2-alt3
- rebuild

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.3.2-alt2
- rebuild with gcc3.4

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 1:1.3.2-alt1
- rebuild

* Mon Jan 03 2005 ZerG <zerg@altlinux.ru> 1:1.3.2-alt0.0.M24
- new version

* Wed Oct 06 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.3.1-alt1
- new version

* Mon Sep 27 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.3.0-alt1
- new version

* Tue Jul 13 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.2.3-alt2
- build libgmcop

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.2.3-alt1
- new version

* Fri May 14 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.2.2-alt3
- add patches from SuSE for fix vorbis dcache_block_size and mcop buffer aliasing

* Wed Apr 14 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.2.2-alt2
- add patch from RH for glib2

* Thu Apr 08 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.2.2-alt1
- new version

* Fri Mar 19 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.2.1-alt2
- rebuild with ltdl

* Thu Mar 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.2.1-alt1
- new version

* Fri Feb 27 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.2.0-alt1
- new version
- build with gmcop support

* Mon Dec 29 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.4-alt6
- rebuild with gcc3.3

* Wed Dec 03 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.4-alt5
- fix loading libartscbackend.so

* Mon Dec 01 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.4-alt4
- remove *.la
- rename kdelibs-sound to libarts-qt
- fix provides/requires

* Fri Nov 28 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.4-alt3
- rebuild

* Fri Nov 14 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.4-alt2
- rebuild

* Wed Sep 17 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.4-alt1
- new version

* Mon Aug 18 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.3-alt2
- update code from cvs

* Thu Jul 31 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.3-alt1
- update code from cvs

* Mon Jul 21 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.3-alt0.2
- update code from cvs
- turn strict ansi off

* Fri Jul 18 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.3-alt0.1
- update code from cvs

* Mon Jun 16 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.1.2-alt2
- update from cvs ARTS_1_1_BRANCH
- add RH patch2

* Wed May 21 2003 Sergey V Turchin <zerg at altlinux dot ru> 1:1.1.2-alt1
- update from cvs ARTS_1_1_BRANCH
- add xine-arts-plugin patches

* Thu Mar 13 2003 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt11
- update from cvs ARTS_1_1_BRANCH

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt10
- fix requires

* Wed Feb 05 2003 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt9
- build static libraries

* Thu Jan 23 2003 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt8
- fix requires
- add patch from RH

* Fri Jan 17 2003 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt6
- fix patch2

* Sat Jan 04 2003 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt5
- update from cvs

* Mon Dec 23 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt4
- add MDK patches
- disable objprelink

* Wed Dec 18 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt3
- rebuild

* Wed Dec 18 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt2
- rebuild

* Wed Nov 27 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt1
- update from cvs

* Thu Nov 21 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt0.7
- update from cvs

* Fri Nov 15 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt0.6
- update from cvs ARTS_1_1_0_RELEASE

* Tue Nov 05 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt0.5.rc2
- rc2

* Tue Oct 29 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt0.4.rc1
- rc1

* Mon Oct 14 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt0.3
- add gsl files

* Wed Oct 09 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.1.0-alt0.2
- update code from cvs HEAD

* Thu Oct 03 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.3-alt8
- fix requires && provides

* Fri Sep 27 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.3-alt7
- fix requires

* Fri Sep 27 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.3-alt6
- update from cvs
- fix requires

* Tue Sep 17 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.3-alt5
- rebuild with new XFree86

* Mon Sep 09 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.3-alt4
- rebuild with objprelink

* Thu Sep 05 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.3-alt3
- rebuild with gcc 3.2

* Fri Aug 16 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.3-alt1
- fix %%version && rebuild

* Mon Aug 05 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.2-alt3
- update from cvs

* Mon Jul 08 2002 ZerG <zerg@altlinux.ru> 1:1.0.2-alt2
- add patch for writing temp files to $TMPDIR

* Wed Jul 03 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.2-alt1
- new version

* Fri Jun 07 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.1-alt2
- update from cvs
- add patch changeing ~/.mcop to ~/.mcop1

* Sun May 26 2002 ZerG <zerg@altlinux.ru> 1:1.0.1-alt1
- new version

* Tue May 21 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.0-alt5
- fix Requires

* Wed May 15 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.0-alt4
- update from cvs
- add obsoletes -devel-static
- fix buildrequires

* Wed May 08 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.0-alt3
- update from cvs

* Fri Apr 19 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.0-alt2
- move to /usr

* Fri Apr 19 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.0-alt2
- 

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.0-alt1
- new version

* Mon Apr 01 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.0-alt0.2.cvs20020401
- update from cvs

* Thu Mar 28 2002 Sergey V Turchin <zerg@altlinux.ru> 0.9.9-alt0.1.rc3
- build for ALT

* Wed Mar 13 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020313.1
- Build with autoconf 2.53, automake 1.5

* Thu Feb 14 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020114.1
- initial package
