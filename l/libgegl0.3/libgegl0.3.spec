%def_enable snapshot

%define _name gegl
%define ver_major 0.3
%define api_ver %ver_major
%if "%(rpmvercmp '%{get_version libavformat-devel}' '3.0.0')" > "0"
%def_with libavformat
%endif
%def_disable docs
%def_enable gtk_doc

Name: lib%_name%api_ver
Version: %ver_major.29
Release: alt0.1

Summary: A graph based image processing framework
License: LGPLv3+/GPLv3+
Group: System/Libraries
Url: http://www.gimp.org

%if_disabled snapshot
Source: http://download.gimp.org/pub/%_name/%ver_major/%_name-%version.tar.bz2
%else
Source: %_name-%version.tar
%endif

%define babl_ver 0.1.42

BuildRequires: asciidoc gcc-c++ graphviz glib2-devel gtk-doc intltool libSDL-devel
BuildRequires: libbabl-devel >= %babl_ver  libjpeg-devel libtiff-devel libraw-devel
BuildRequires: libgomp-devel librsvg-devel libspiro-devel openexr-devel python-modules-encodings
BuildRequires: ruby w3m liblua5-devel libgtk+3-devel enscript
BuildRequires: libexiv2-devel libjasper-devel libpng-devel liblensfun-devel
BuildRequires: liblcms2-devel libwebp-devel  libv4l-devel libpoly2tri-c-devel
BuildRequires: libgexiv2-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libjson-glib-devel gobject-introspection-devel vala-tools
BuildRequires: libavformat-devel
%{?_with_libavformat:BuildRequires: libavformat-devel libavcodec-devel libswscale-devel}

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

%package gir
Summary: GObject introspection data for the GEGL
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GEGL library.

%package gir-devel
Summary: GObject introspection devel data for the GEGL
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GEGL library.


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	%{subst_enable docs} \
	%{subst_with libavformat} \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc}
%make_build

%install
%makeinstall_std

# quick fix for gegl-sc-0.3.pc
#subst 's|gegl|gegl-%api_ver|
#       s|-lgegl-0.3-sc-0.3|-lgegl-sc-%api_ver|
#       s|gegl-0.3-0.3\/sc|gegl-%api_ver/sc|' %buildroot%_pkgconfigdir/%_name-sc-%api_ver.pc

%find_lang %_name-%api_ver

%files -f %_name-%api_ver.lang
# temporarily exclude to avoid conflict with libgegl-0.2
%exclude %_bindir/%_name
%_bindir/%_name-imgcmp
%_bindir/gcut
%_libdir/lib%_name-%api_ver.so.*
%_libdir/lib%_name-sc-%api_ver.so
%_libdir/lib%_name-npd-%api_ver.so
%dir %_libdir/%_name-%api_ver
%_libdir/%_name-%api_ver/*.so
%_libdir/%_name-%api_ver/grey2.json
%exclude %_libdir/%_name-%api_ver/*.la

%files devel
%_includedir/%_name-%api_ver/
%_libdir/lib%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_pkgconfigdir/%_name-sc-%api_ver.pc
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi
%if_enabled docs
%_datadir/gtk-doc/html/%_name/
%endif

%files gir
%_typelibdir/Gegl-%api_ver.typelib

%files gir-devel
%_girdir/Gegl-%api_ver.gir

%changelog
* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.29-alt0.1
- updated to GEGL_0_3_28-45-gfa99f10

* Tue Jul 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.18-alt1
- 0.3.18

* Mon Jun 05 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.16-alt2
- enabled libavformat support

* Mon May 15 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.16-alt1
- 0.3.16

* Thu Mar 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.14-alt1
- 0.3.14

* Thu Feb 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.12-alt1
- 0.3.12

* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt2
- rebuilt against libraw.so.16

* Wed Jun 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8

* Sat Feb 06 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt0.1
- updated to GEGL_0_3_4-96-ga299466

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt0.2
- rebuilt against libwebp.so.6

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt0.1
- 0.3.1_d03be6e2

* Thu Apr 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt2
- updated to 0.3.0_89579cc1

* Tue Feb 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- built 0.3.0 snapshot as libgegl0.3 for people/gnome

* Wed Jun 04 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt2
- rebuilt with libav10

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

