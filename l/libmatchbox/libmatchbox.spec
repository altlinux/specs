# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen libICE-devel libSM-devel libcheck-devel pkgconfig(x11) pkgconfig(xft)
# END SourceDeps(oneline)

Name: libmatchbox
Version: 1.9
Release: alt4
Summary: Libraries for the Matchbox Desktop
License: LGPLv2+
Group: System/Libraries
Url: http://projects.o-hand.com/matchbox/
Packager: Sugar Development Team <sugar@packages.altlinux.org>

%def_disable static

Source: http://matchbox-project.org/sources/%name/%version/%name-%version.tar.bz2
Source1: %name.watch
Patch: libmatchbox-1.9-alt-DSO.patch
Patch10:	libmatchbox-1.9-add-needed.patch
Patch11:	libmatchbox-1.9-libpng.patch

BuildRequires: pkg-config
BuildRequires: libXft-devel
BuildRequires: libXext-devel
BuildRequires: libpango-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libxsettings-client-devel

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package devel
Summary: Header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.
%endif

%prep
%setup
%patch -p2
%patch10 -p1 -b .add-needed
%patch11 -p1 -b .libpng

%build
autoreconf -fisv
%configure \
	--enable-pango \
	--enable-jpeg \
	--enable-png \
	--enable-xsettings \
	%{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%doc AUTHORS ChangeLog README COPYING
%dir %{_includedir}/libmb
%{_includedir}/libmb/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Fri Nov 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt4
- build with libxsettings-client-devel

* Fri Nov 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3
- added patches 10 and 11 from fedora

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt2.2
- Fixed build

* Tue Dec 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt2.1
- Rebuilt for soname set-versions

* Sat Dec 13 2008 Aleksey Lim <alsroot@altlinux.org> 1.9-alt2
- move .so to devel package

* Sun Nov 16 2008 Aleksey Lim <alsroot@altlinux.org> 1.9-alt1
- first build for ALT Linux Sisyphus
