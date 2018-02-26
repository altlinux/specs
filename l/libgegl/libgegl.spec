%def_disable docs

Name: libgegl
Version: 0.2.0
Release: alt1
Summary: A graph based image processing framework
License: LGPLv3+/GPLv3+
Group: System/Libraries
Url: http://www.gimp.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: gegl-%version.tar
Patch: gegl-%version-%release.patch

BuildRequires: asciidoc gcc-c++ graphviz glib2-devel gtk-doc intltool libSDL-devel libavformat-devel libbabl-devel libjpeg-devel libopenraw-devel
BuildRequires: librsvg-devel libspiro-devel openexr-devel python-modules-encodings ruby w3m liblua5-devel libgtk+2-devel enscript
BuildRequires: libexiv2-devel libjasper-devel libpng-devel liblensfun-devel

%description
GEGL (Generic Graphics Library) is a graph based image processing framework.
GEGLs original design was made to scratch GIMPs itches for a new
compositing and processing core. This core is being designed to have
minimal dependencies. and a simple well defined API.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the libraries and header files needed for
developing with %name.

%prep
%setup -q -n gegl-%version
%patch -p1

%build
%autoreconf
%configure \
	%{subst_enable docs} \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang gegl-0.2

%files -f gegl-0.2.lang
%_bindir/gegl
%_libdir/*.so.*
%dir %_libdir/gegl-0.2
%_libdir/gegl-0.2/*.so

%files devel
%_includedir/gegl-0.2
%_libdir/*.so
%_pkgconfigdir/*.pc
%if_enabled docs
%_datadir/gtk-doc/html/gegl
%endif

%changelog
* Wed Apr 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Tue Aug 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.1.6-alt2
- disabled ffmpeg

* Tue Feb 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Tue Oct 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.2-alt2
- updated build dependencies

* Wed Mar 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Mon Jan 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt2
- updated build dependencies

* Mon Oct 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Mon Jul 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt4
- fixed build with fresh gcc

* Mon Jul 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt3
- disabled docs

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt2
- rebuild with libpng12 1.2.37-alt2

* Mon Apr 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt0.M50.1
- build for branch 5.0

* Mon Feb 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt1
- 0.0.22

* Thu Feb 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.20-alt4
- rebuild with libavcodec.so.52

* Thu Jan 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.20-alt3
- drop fill plugin

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.20-alt2
- rebuild

* Fri Oct 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.20-alt1
- 0.0.20

* Thu Oct 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.18-alt2
- disabled workshop operations
- build docs

* Wed Oct 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.18-alt1
- initial release

