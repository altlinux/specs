%define _name SDL_gfx
%define ver_major 2.0
%define soname 13

Name: lib%_name%soname
Version: %ver_major.23
Release: alt2

Summary: SDL graphics drawing primitives and other support functions
License: zlib
Group: System/Libraries

URL: http://www.ferzkopp.net/Software/%_name-%ver_major/
Source: http://www.ferzkopp.net/Software/%_name-%ver_major/%_name-%version.tar.gz

BuildRequires: gcc-c++ imake libICE-devel libSDL-devel xorg-cf-files

%description
The %_name library offers several components: Graphic Primitives, Rotozoomer,
Framerate control, and MMX image filters. The Primitives component provides
basic drawing routines: pixels, hlines, vlines, lines, aa-lines, rectangles,
circles, ellipses, trigons, polygons, Bezier curves, and an 8x8 pixmap font for
drawing onto any SDL Surface. Full alpha blending, hardware surface locking, and
all surface depths are supported. The Rotozoomer can use interpolation for high
quality output.

%prep
%setup -n %_name-%version

%build
./autogen.sh
%configure --enable-shared --disable-static --with-x \
%ifnarch %ix86 x86_64
    --disable-mmx
%endif

%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

#%%files devel
%exclude %_libdir/*.so
%exclude %_includedir/SDL/*
%exclude %_pkgconfigdir/*


%changelog
* Sun Dec 07 2014 Yuri N. Sedunov <aris@altlinux.org> 2.0.23-alt2
- compat library without -devel subpackage

* Sat Dec 10 2011 Victor Forsiuk <force@altlinux.org> 2.0.23-alt1
- 2.0.23

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.22-alt1.1
- Rebuilt for debuginfo

* Fri Nov 05 2010 Victor Forsiuk <force@altlinux.org> 2.0.22-alt1
- 2.0.22

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.20-alt1.1
- Rebuilt for soname set-versions

* Wed Feb 03 2010 Victor Forsiuk <force@altlinux.org> 2.0.20-alt1
- 2.0.20

* Mon Mar 27 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.13-alt2
- fix URL
- fix BuildRequires
- disable MMX for x86_64

* Fri Feb 04 2005 Alexey Tourbin <at@altlinux.ru> 2.0.13-alt1
- NMU: updated from 2.0.7 to 2.0.13 (#5575), soname changed
- added compatibility macros for filledpie* renamed functions

* Wed Jun 11 2003 Sergey V Turchin <zerg at altlinux dot org> 2.0.7-alt2
- fix provides

* Tue Jun 10 2003 Sergey V Turchin <zerg at altlinux dot org> 2.0.7-alt1
- new version

* Thu Jan 23 2003 Rider <rider@altlinux.ru> 2.0.3-alt3
- fix rebuild in new invironment (automake)

* Mon Oct 14 2002 Sergey V Turchin <zerg@altlinux.ru> 2.0.3-alt2
- rebuild with gcc3.2

* Tue Aug 13 2002 Sergey V Turchin <zerg@altlinux.ru> 2.0.3-alt1
- initial spec
