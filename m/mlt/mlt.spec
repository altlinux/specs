%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}

%define _unpackaged_files_terminate_build 1
%def_disable debug
%def_disable luma16bpp #if enabled produce 16bpp lumas instead of 8bpp

%def_disable mmx
%def_disable sse
%def_disable sse2
%ifarch x86_64
%set_enable mmx
%set_enable sse
%set_enable sse2
%endif
%ifarch %ix86
%set_enable mmx
%set_enable sse
%set_disable sse2
%endif

%define Name MLT
%define lname lib%name

Name: mlt
Version: 0.7.8
Release: alt1
Summary: Multimedia framework designed for television broadcasting
License: GPL
Group: Video
URL: http://sourceforge.net/projects/%name

Packager: Maxim Ivanov <redbaron@altlinux.org>

Source: %name-%version.tar
Source1: mlt++-config.h
Patch1: mlt-0.5.4-alt-configure-mmx.patch

BuildRequires: ImageMagick-tools gcc-c++ jackit-devel ladspa_sdk libSDL-devel
BuildRequires: libSDL_image-devel libX11-devel libavdevice-devel libavformat-devel
BuildRequires: libquicktime-devel libsamplerate-devel libsox-devel libswscale-devel
BuildRequires: libxml2-devel kde4libs-devel libqt4-devel swig python-devel
BuildRequires: frei0r-devel libalsa-devel

%description
%Name is a multimedia framework designed for television broadcasting.

%package utils
Summary: %name utils
Group: Video
License: GPL

%description utils
%Name utils.

%package -n %lname
Summary: %Name framework library
License: GPL
Group: System/Libraries

%description -n %lname
%Name is a multimedia framework designed for television broadcasting.

%package -n %lname-devel
Summary: Development files for %Name framework
License: GPL
Group: Development/C
Requires: %lname = %version-%release

%description -n %lname-devel
Development files for %Name framework.

%package -n %lname++
Summary: C++ wrapping for the MLT library
Group: System/Libraries

%description -n %lname++
This mlt sub-project provides a C++ wrapping for the MLT library.

%package -n %lname++-devel
Summary: Development files for %lname.
Group: Development/C++
Requires: %lname = %version-%release

%description -n %lname++-devel
Development files for %lname.

%package -n python-module-%name
Summary: Python package to work with MLT
Group: Development/Python

%description -n python-module-%name
This module allows to work with MLT using python..

%prep
%setup -q
%patch1 -p1

install -m 0644 %SOURCE1 src/mlt++/config.h

%build
export CC=gcc CXX=g++ CFLAGS="%optflags"
%configure \
	--enable-gpl \
	--enable-motion-est \
	--avformat-swscale \
	%{subst_enable mmx} \
	%{subst_enable sse} \
	%{subst_enable sse2} \
	%{subst_enable debug} \
	--luma-compress \
        %if_disabled luma16bpp
	--luma-8bpp \
        %endif
	--kde-includedir=%_K4includedir \
        --kde-libdir=%_K4lib \
        --swig-languages=python

%make_build

%install
%make DESTDIR=%buildroot install
install -d %buildroot%python_sitelibdir
install -pm 0644 src/swig/python/%name.py %buildroot%python_sitelibdir/
install -pm 0755 src/swig/python/_%name.so %buildroot%python_sitelibdir/

%files -n %name-utils
#%doc docs/melt.txt
%_bindir/melt

%files -n %lname
#%doc docs/services.txt docs/westley.txt
%_libdir/%lname.so.*
%_libdir/%name
%_datadir/%name

%files -n %lname-devel
#%doc docs/framework.txt
%_includedir/%name
%_libdir/%lname.so
%_pkgconfigdir/%name-framework.pc

%files -n %lname++
%_libdir/%lname++.so.*

%files -n %lname++-devel
%_includedir/%name++
%_libdir/%lname++.so
%_pkgconfigdir/%name++.pc

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Wed May 16 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt1
- new version

* Fri May 04 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.6-alt0.M60P.2
- rebuild with libav

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.6-alt0.M60P.1
- built for M60P

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.6-alt1
- new version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.4-alt1.1
- Rebuild with Python-2.7

* Fri Aug 12 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.4-alt0.M60P.1
- built for M60P

* Thu Aug 11 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.4-alt1
- new version

* Fri Jul 08 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- new version

* Wed Apr 27 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- new version

* Thu Sep 16 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.10-alt0.M51.1
- built for M51

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.10-alt1
- new version

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.4-alt1.M51.1
- built for M51

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.4-alt2
- fix build flags

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.4-alt1
- 0.5.4

* Wed Apr 14 2010 Maxim Ivanov <redbaron at altlinux.org> 0.5.2-alt1
- 0.5.2

* Tue Jan 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.6-alt2
- Add subpackage python-module-%name

* Thu Nov 12 2009 Maxim Ivanov <redbaron at altlinux.org> 0.4.6-alt1
- 0.4.6
- mlt++.so.2 -> mlt++.so.3 soname change

* Fri Jul 31 2009 Denis Smirnov <mithraen@altlinux.ru> 0.4.4-alt1
- 0.4.4

* Sun Jun 28 2009 Maxim Ivanov <redbaron at altlinux.org> 0.4.2-alt1.git2b33565
- Bump to 0.4.2
- inigo utility renamed to melt
- mlt-config removed, use `pkg-config mlt-framework` instead
- miracle, humperdink and valerie are moved to separate project
- mlt++ is not part of main tree

* Sat May 16 2009 Maxim Ivanov <redbaron at altlinux.org> 0.3.8-alt2
- Fix missed libm dynamic link, closes #20024

* Sat Apr 18 2009 Maxim Ivaniv <redbaron at altlinux.org> 0.3.8-alt1
- 0.3.8

* Thu Feb 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Wed Dec 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Fri Dec 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Thu Aug 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Fri Jun 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt1.svn1045
- rebuild with libquicktime.so.102

* Thu Dec 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt0.svn1045
- SVN revision r1045 2007-12-08

* Mon Sep 03 2007 Alexey Morsov <swi@altlinux.ru> 0.2.4-alt1
- 0.2.4
- new patch set (thanks to shrek@)
- lot of bug fixes

* Fri Jun 29 2007 Alexey Morsov <swi@altlinux.ru> 0.2.2-alt0.7
- changes for new ffmpeg

* Mon Apr 23 2007 Alexey Morsov <swi@altlinux.ru> 0.2.2-alt0.6
- add patch from gentoo to fix mmx on ix86
- disable mmx

* Fri Apr 20 2007 Alexey Morsov <swi@altlinux.ru> 0.2.2-alt0.5
- remove disable_fox and arch dependencies from spec (for sox >= 13.0)
- add patch for build with sox
- add sox in BR due to bug in req's in sox-devel

* Wed Feb 14 2007 Alexey Morsov <swi@altlinux.ru> 0.2.2-alt0.4
- add Packager (swi@)

* Wed Feb 14 2007 Led <led@altlinux.ru> 0.2.2-alt0.3
- fixed %name-0.2.2-modulesdir.patch

* Tue Feb 13 2007 Led <led@altlinux.ru> 0.2.2-alt0.2
- added %name-0.2.2-configure.patch
- added %name-0.2.2-x86_64.patch

* Tue Feb 13 2007 Led <led@altlinux.ru> 0.2.2-alt0.1
- initial build
- added %name-0.2.2-modulesdir.patch
