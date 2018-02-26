%define popIF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define popIF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define popIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define popIF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"
%undefine __libtoolize

%def_disable static
%def_disable cpp
%def_enable glib
%def_disable qt4
%def_disable qt3
%def_enable devel
%def_disable utils
%def_enable xpdfheaders
%def_disable gir

%define rname poppler
%define somajor 13
%define somajor_cpp 0
%define somajor_qt 3
%define somajor_qt4 3
%define somajor_glib 6
%define major 0
%define minor 16
%define bugfix 7
Name: %rname%somajor
Version: %major.%minor.%bugfix
Release: alt6
%define poppler_devel_name lib%name-devel
%define poppler_cpp_devel_name lib%name-cpp-devel
%define poppler_glib_devel_name lib%name-glib-devel
%define poppler_qt_devel_name lib%name-qt-devel
%define poppler_qt4_devel_name lib%name-qt4-devel

Group: Publishing
Summary: PDF rendering library
License: GPL
Url: http://poppler.freedesktop.org/
Packager: Sergey V Turchin <zerg at altlinux dot org>

Source: %rname-%version.tar
Source1: version-script.qt4
Patch1: poppler-0.14.1-alt-qt.patch
Patch2: version-script.qt4.patch
# RH
Patch10: poppler-0.12.1-objstream.patch
Patch11: poppler-0.12.4-annot-appearance.patch

# Automatically added by buildreq on Fri Apr 01 2011 (-bi)
#BuildRequires: gcc-c++ glib-networking glibc-devel-static gtk-doc gvfs imake libXt-devel libcurl-devel libgtk+2-devel libgtk+2-gir-devel libjpeg-devel liblcms-devel libopenjpeg-devel libqt3-devel libqt4-devel libqt4-gui libqt4-xml libxml2-devel python-modules-compiler python-modules-encodings time xorg-cf-files

BuildRequires(pre): rpm-utils
%if_enabled qt3
BuildRequires(pre): libqt3-devel
BuildRequires: glibc-devel-static
%endif
%if_enabled qt4
BuildRequires(pre): libqt4-devel
%endif
%if_enabled glib
BuildRequires: glib2-devel
%endif
BuildRequires: gcc-c++ glibc-devel libcurl-devel libgtk+2-devel
BuildRequires: libgtk+2-gir-devel libjpeg-devel liblcms-devel libopenjpeg-devel
BuildRequires: libxml2-devel gtk-doc libcairo-gobject-devel
BuildRequires: libXt-devel
BuildRequires: zlib-devel

%description
Poppler is a fork of the xpdf PDF viewer developed by Derek Noonburg
of Glyph and Cog, LLC.  The purpose of forking xpdf is twofold.
First, we want to provide PDF rendering functionality as a shared
library, to centralize the maintenence effort.  Today a number of
applications incorporate the xpdf code base, and whenever a security
issue is discovered, all these applications exchange patches and put
out new releases.  In turn, all distributions must package and release
new version of these xpdf based viewers.  It's safe to say that
there's a lot of duplicated effort with the current situaion.  Even if
poppler in the short term introduces yet another xpdf derived code
base to the world, we hope that over time these applications will
adopt poppler.  After all, we only need one application to use poppler
to break even.

%package -n lib%name
Summary: PDF rendering library
Group: System/Libraries
Requires: poppler-data
%description -n lib%name
Poppler is a fork of the xpdf PDF viewer developed by Derek Noonburg
of Glyph and Cog, LLC.  The purpose of forking xpdf is twofold.
First, we want to provide PDF rendering functionality as a shared
library, to centralize the maintenence effort.  Today a number of
applications incorporate the xpdf code base, and whenever a security
issue is discovered, all these applications exchange patches and put
out new releases.  In turn, all distributions must package and release
new version of these xpdf based viewers.  It's safe to say that
there's a lot of duplicated effort with the current situaion.  Even if
poppler in the short term introduces yet another xpdf derived code
base to the world, we hope that over time these applications will
adopt poppler.  After all, we only need one application to use poppler
to break even.

%package -n %rname
Group: Publishing
Summary: PDF rendering library utils
Requires: lib%name = %version-%release
Provides: poppler-utils = %version-%release
Provides: xpdf-utils = 3.02-alt6
Obsoletes: xpdf-utils <= 3.02-alt5
Conflicts: xpdf-reader <= 3.02-alt5
Conflicts: pdftohtml
%description -n %rname
Poppler is a fork of the xpdf PDF viewer developed by Derek Noonburg
of Glyph and Cog, LLC.  The purpose of forking xpdf is twofold.
First, we want to provide PDF rendering functionality as a shared
library, to centralize the maintenence effort.  Today a number of
applications incorporate the xpdf code base, and whenever a security
issue is discovered, all these applications exchange patches and put
out new releases.  In turn, all distributions must package and release
new version of these xpdf based viewers.  It's safe to say that
there's a lot of duplicated effort with the current situaion.  Even if
poppler in the short term introduces yet another xpdf derived code
base to the world, we hope that over time these applications will
adopt poppler.  After all, we only need one application to use poppler
to break even.

%package -n lib%rname%somajor_qt-qt
Summary: Qt3 frontend library for %name
Group: System/Libraries
Requires: lib%name = %version-%release
%if_enabled qt3
Requires: libqt3 >= %{get_version libqt3}
%endif
Provides: lib%rname-qt = %version-%release
Obsoletes: lib%rname-qt < %version-%release
%popIF_ver_gteq "%major.%minor" "0.10"
Provides: libpoppler08-qt = %version-%release
Obsoletes: libpoppler08-qt < %version-%release
%if "%somajor_qt" != "4"
Provides: libpoppler4-qt = %version-%release
Obsoletes: libpoppler4-qt < %version-%release
%endif
%endif
%description -n lib%rname%somajor_qt-qt
Qt3 frontend library for %name

%package -n lib%rname%somajor_qt4-qt4
Summary: Qt4 frontend library for %name
Group: System/Libraries
Requires: lib%name = %version-%release
%if_enabled qt4
Requires: libqt4-core >= %{get_version libqt4-core}
%endif
%popIF_ver_gteq "%major.%minor" "0.10"
Provides: libpoppler08-qt4 = %version-%release
Obsoletes: libpoppler08-qt4 < %version-%release
%if "%somajor_qt4" != "4"
Provides: libpoppler4-qt4 = %version-%release
Obsoletes: libpoppler4-qt4 < %version-%release
%endif
%endif
%description -n lib%rname%somajor_qt4-qt4
Qt4 frontend library for %name

%package -n lib%rname%somajor_glib-glib
Summary: Glib frontend library for %name
Group: System/Libraries
Requires: lib%name = %version-%release
%description -n lib%rname%somajor_glib-glib
Glib frontend library for %name

%package -n lib%rname%somajor_cpp-cpp
Summary: Pure C++ wrapper for poppler
Group: System/Libraries
Requires: lib%name = %version-%release
%description -n lib%rname%somajor_cpp-cpp
Pure C++ wrapper for poppler


%package -n %poppler_devel_name
Summary: Development files for %name
Group: Development/C
Provides: lib%name-devel = %version-%release
Obsoletes: lib%name-devel < %version-%release
Requires: lib%name = %version-%release
%if "%poppler_devel_name" != "lib%rname-devel"
Conflicts: lib%rname-devel
%endif
%description -n %poppler_devel_name
Libraries, include files, etc you can use to develop poppler applications

%package -n %poppler_cpp_devel_name
Summary: Development files for C++ wrapper
Group: Development/C++
Requires: lib%rname%somajor_cpp-cpp = %version-%release
Requires: %poppler_devel_name = %version-%release
%if "%poppler_cpp_devel_name" != "lib%rname-cpp-devel"
Conflicts: lib%rname-cpp-devel
%endif
%description -n %poppler_cpp_devel_name
Libraries, include files, etc you can use to develop
poppler applications with pure C++

%package -n %poppler_glib_devel_name
Summary: Development files for %name-glib
Group: Development/GNOME and GTK+
Requires: lib%rname%somajor_glib-glib = %version-%release
Requires: %poppler_devel_name = %version-%release
%if "%poppler_glib_devel_name" != "lib%rname-glib-devel"
Conflicts: lib%rname-glib-devel
%endif
%description -n %poppler_glib_devel_name
Libraries, include files, etc you can use to develop
poppler applications with Glib/Gtk+

%package -n %poppler_qt_devel_name
Summary: Development files for %name-qt
Group: Development/KDE and QT
Requires: lib%rname%somajor_qt-qt = %version-%release
Requires: %poppler_devel_name = %version-%release
%if "%poppler_qt_devel_name" != "lib%rname-qt-devel"
Conflicts: lib%rname-qt-devel
%endif
%description -n %poppler_qt_devel_name
Libraries, include files, etc you can use to develop
poppler applications with Qt3

%package -n %poppler_qt4_devel_name
Summary: Development files for %name-qt4
Group: Development/KDE and QT
Requires: lib%rname%somajor_qt4-qt4 = %version-%release
Requires: %poppler_devel_name = %version-%release
%if "%poppler_qt4_devel_name" != "lib%rname-qt4-devel"
Conflicts: lib%rname-qt4-devel
%endif
%description -n %poppler_qt4_devel_name
Libraries, include files, etc you can use to develop
poppler applications with Qt4

%package -n lib%rname-gir
Summary: GObject introspection data for the Poppler library
Group: System/Libraries
Requires: lib%rname%somajor_glib-glib = %version-%release
%description -n lib%rname-gir
GObject introspection data for the Poppler library

%package -n lib%rname-gir-devel
Summary: GObject introspection devel data for the Poppler library
Group: System/Libraries
BuildArch: noarch
Requires: lib%rname-gir = %version-%release
Requires: %poppler_glib_devel_name = %version-%release
%description -n lib%rname-gir-devel
GObject introspection devel data for the Poppler library

%package -n %{poppler_devel_name}-static
Summary: Static libraries for libpoppler
Group: Development/Other
Provides: lib%name-devel-static = %version-%release
Obsoletes: lib%name-devel-static < %version-%release
Requires: %poppler_devel_name = %version-%release
%description -n %{poppler_devel_name}-static
This package contains development libraries required for packaging
statically linked libpoppler-based software

%prep
%setup -q -n %rname-%version
install -m 0644 %SOURCE1 qt4/src/
%patch1 -p1
# qt4 versioning
%patch2 -p1
#
#%patch10 -p1
%patch11 -p1

chmod a-x goo/GooTimer.h

%autoreconf
#aclocal --force -I m4
#automake
#autoconf --force

%build
export QT3DIR=%_qt3dir QT4DIR=%_qt4dir
%configure \
    --disable-rpath \
    %{subst_enable static} \
    --enable-shared \
    --enable-compile-warnings=yes \
    --enable-libcurl \
%if_enabled xpdfheaders
    --enable-xpdf-headers \
%endif
    --enable-zlib \
%if_disabled cpp
    --disable-poppler-cpp \
%endif
%if_disabled glib
    --disable-poppler-glib \
%endif
%if_disabled qt3
    --disable-poppler-qt \
%endif
%if_disabled qt4
    --disable-poppler-qt4 \
%endif
    --enable-compile-warnings=yes
#    --disable-abiword-output \

%make_build

%install
%makeinstall

%if_enabled utils
%files -n %rname
%_bindir/pdf*
%_man1dir/pdf*
%endif

%files -n lib%name
%doc AUTHORS ChangeLog NEWS README* TODO
%_libdir/libpoppler.so.%somajor
%_libdir/libpoppler.so.%somajor.*

%if_enabled gir
%files -n lib%rname-gir
%_typelibdir/Poppler-*.typelib
%if_enabled devel
%files -n lib%rname-gir-devel
%_girdir/Poppler-*.gir
%endif
%endif

%if_enabled glib
%files -n lib%rname%somajor_glib-glib
%_libdir/libpoppler-glib.so.%somajor_glib
%_libdir/libpoppler-glib.so.%somajor_glib.*
%if_enabled devel
%files -n %poppler_glib_devel_name
%_includedir/poppler/glib/
%_libdir/libpoppler-glib.so
%_pkgconfigdir/poppler-cairo.pc
%_pkgconfigdir/poppler-glib.pc
%endif
%endif

%if_enabled qt3
%files -n lib%rname%somajor_qt-qt
%_libdir/libpoppler-qt.so.%somajor_qt
%_libdir/libpoppler-qt.so.%somajor_qt.*
%if_enabled devel
%files -n %poppler_qt_devel_name
%_includedir/poppler/qt3/
%_libdir/libpoppler-qt.so
%_pkgconfigdir/poppler-qt.pc
%endif
%endif

%if_enabled qt4
%files -n lib%rname%somajor_qt4-qt4
%_libdir/libpoppler-qt4.so.%somajor_qt4
%_libdir/libpoppler-qt4.so.%somajor_qt4.*
%if_enabled devel
%files -n %poppler_qt4_devel_name
%_includedir/poppler/qt4/
%_libdir/libpoppler-qt4.so
%_pkgconfigdir/poppler-qt4.pc
%endif
%endif

%if_enabled cpp
%files -n lib%rname%somajor_cpp-cpp
%_libdir/libpoppler-cpp.so.%somajor_cpp
%_libdir/libpoppler-cpp.so.%somajor_cpp.*
%if_enabled devel
%files -n %poppler_cpp_devel_name
%_includedir/poppler/cpp/
%_libdir/libpoppler-cpp.so
%_pkgconfigdir/poppler-cpp.pc
%endif
%endif

%if_enabled devel
%files -n %poppler_devel_name
%dir %_includedir/poppler
%_includedir/poppler/*.h
#%_includedir/poppler/Function.cc
%_includedir/poppler/fofi
%_includedir/poppler/splash/
%_includedir/poppler/goo/
%_libdir/libpoppler.so
%_pkgconfigdir/poppler.pc
%_pkgconfigdir/poppler-splash.pc
#%_datadir/gtk-doc/html/poppler

%if_enabled static
%files -n %{poppler_devel_name}-static
%_libdir/*.a
%endif
%endif

%changelog
* Thu Jan 12 2012 Andrey Cherepanov <cas@altlinux.org> 0.16.7-alt6
- Fix zlib support

* Wed Dec 14 2011 Andrey Cherepanov <cas@altlinux.org> 0.16.7-alt5
- Enable devel packing (closes: #26671)

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.7-alt4
- don't build qt3 binding and devel files

* Tue Nov 08 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.7-alt3
- fix to build

* Mon Nov 07 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.7-alt2
- build only required components

* Tue Aug 30 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.7-alt0.M60P.1
- built for M60P

* Mon Aug 29 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.7-alt1
- new version

* Fri Apr 15 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.4-alt2
- provide poppler-utils (ALT#25422)
- don't package glib-demo

* Fri Apr 01 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.4-alt1
- new version

* Fri Mar 18 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.3-alt1
- new version

* Fri Feb 11 2011 Sergey V Turchin <zerg@altlinux.org> 0.16.2-alt1
- new version

* Mon Nov 08 2010 Sergey V Turchin <zerg@altlinux.org> 0.14.5-alt1
- new version

* Thu Oct 14 2010 Sergey V Turchin <zerg@altlinux.org> 0.14.4-alt1
- new version

* Thu Aug 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.14.2-alt1
- new version

* Mon Aug 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.14.1-alt1
- new version (ALT#23738)

* Fri Feb 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.12.4-alt0.M51.1
- built for M51

* Fri Feb 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.12.4-alt1
- new version
- built with lcms
- update version scripts

* Tue Dec 29 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.3-alt0.M51.1
- built for M51

* Tue Dec 29 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.3-alt1
- new version

* Fri Dec 11 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.2-alt0.M51.1
- built for M51

* Fri Dec 11 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.2-alt1
- new version
- CVE-2009-3607

* Mon Oct 19 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.1-alt1
- new version
- add linker version script for libpoppler
- security fixes:
    - CVE-2009-3608 ObjectStream integer overflow

* Mon Sep 14 2009 Sergey V Turchin <zerg@altlinux.org> 0.12.0-alt1
- new version

* Tue Jul 07 2009 Sergey V Turchin <zerg@altlinux.org> 0.10.7-alt2
- obsolete xpdf-utils

* Tue May 19 2009 Sergey V Turchin <zerg@altlinux.org> 0.10.7-alt1
- new version

* Tue Apr 21 2009 Sergey V Turchin <zerg@altlinux.org> 0.10.6-alt2
- built for sisyphus

* Mon Apr 20 2009 Vladimir Lettiev <crux@altlinux.ru> 0.10.6-alt1
- new version
- security fixes:
    - CVE-2009-0799 xpdf OOB Read
    - CVE-2009-0800 xpdf Multiple Input Validation Flaws
    - CVE-2009-1179 xpdf Integer Overflow
    - CVE-2009-1180 xpdf Invalid free()
    - CVE-2009-1181 xpdf NULL dereference DoS
    - CVE-2009-1182 xpdf MMR Decoder Buffer Overflows
    - CVE-2009-1183 xpdf MMR Infinite Loop DoS
    - CVE-2009-1187 poppler CairoOutputDev integer overflow
    - CVE-2009-1188 poppler SplashBitmap integer overflow

* Mon Mar 16 2009 Sergey V Turchin <zerg@altlinux.org> 0.10.5-alt1
- new version

* Tue Feb 17 2009 Sergey V Turchin <zerg at altlinux dot org> 0.10.4-alt3
- fix build requires

* Mon Feb 16 2009 Sergey V Turchin <zerg at altlinux dot org> 0.10.4-alt1
- new version (fixes SA:33853)

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 0.10.3-alt1
- new version

* Tue Dec 16 2008 Sergey V Turchin <zerg at altlinux dot org> 0.10.2-alt1
- new version
- remove deprecated macroses from specfile

* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 0.10.0-alt3
- fix provides/obsoletes

* Tue Oct 14 2008 Sergey V Turchin <zerg at altlinux dot org> 0.10.0-alt2
- fix provides/obsoletes
- add versioning to qt4 subpackage

* Mon Oct 13 2008 Sergey V Turchin <zerg at altlinux dot org> 0.10.0-alt1
- new version

* Thu Oct 09 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.7-alt2
- don't use cmake (fix #17493)

* Thu Sep 11 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.7-alt1
- new version

* Fri Aug 22 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.6-alt1
- new version
- add conflict to pdftohtml

* Tue Jul 29 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.5-alt1
- new version
- built with zlib
- CVE-2008-2950

* Mon Jun 09 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.3-alt2
- fix conflicts to xpdf-reader

* Sat Jun 07 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.3-alt1
- new version

* Fri Apr 18 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt4
- fix to install OptionalContent.h

* Fri Apr 18 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt3
- rename devel subpackages to real names
- rebuilt with new cairo
- add patch from RH to fix a crash when no optional content groups are defined

* Tue Apr 15 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt2
- fix lib install dir on x86_64

* Tue Apr 15 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt1
- new version

* Mon Apr 14 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 0.6.4-alt1
- new version
- add patch from FC to make ObjStream usable

* Thu Dec 27 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.3-alt1
- new version

* Thu Nov 08 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt3
- add patch to fix CVE-2007-4352, CVE-2007-5392, CVE-2007-5393

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt2
- fix tarball

* Fri Oct 12 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt1
- new version

* Mon Oct 08 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt6
- fix provides/obsoletes

* Mon Oct 08 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt5
- replace poppler-0.5

* Wed Sep 26 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt4
- include unsupported xpdf headers into devel package

* Mon Sep 24 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt3
- add obsoletes instead conflicts

* Wed Sep 19 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt2
- provide devel packages to override poppler-devel-0.5

* Tue Sep 04 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- new version

* Mon Aug 06 2007 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt6
- add patch to fix CVE-2007-3387

* Mon Jun 25 2007 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt5
- fix %%files intersections (#11804)

* Wed Nov 01 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt4
- fix patch for cairo

* Tue Oct 31 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt3
- fix compile with cairo < 0.9

* Tue Oct 03 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt2
- fix find Qt4 on x86_64

* Mon Oct 02 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.4-alt1
- new version
- built with Qt4

* Mon Jul 17 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.3-alt1
- new version

* Mon Jun 05 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.1-alt2
- built without Qt4

* Tue May 16 2006 Sergey V Turchin <zerg at altlinux dot org> 0.5.1-alt1
- new version
- fix %%files in -devel subpackages
- built with Qt4

* Fri Mar 31 2006 Sergey V Turchin <zerg at altlinux dot org> 0.4.5-alt2
- fix lib*.so list in *-devel packages

* Tue Feb 14 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.5-alt1
- Updated to 0.4.5.
- Cleaned up the spec a bit.

* Wed Feb 08 2006 Sergey V Turchin <zerg at altlinux dot org> 0.4.4-alt2
- fix linking with qt
- split qt,glib,devel libraries to subpackages
- fix %%url
- fix requires
- fix build requires

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.4-alt1.1
- Rebuilt for new pkg-config dependencies.

* Wed Jan 11 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.4.4-alt1
- new  version

* Tue Dec 13 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.4.3-alt1
- new version

* Mon Sep 05 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Mon Aug 29 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.4.1-alt1
- new version

* Tue Jun 21 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Mon Jun 06 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.3.2-alt2
- Change package summary

* Wed May 25 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.3.2-alt1
- First version of RPM

