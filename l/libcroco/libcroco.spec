%define ver_major 0.6

Name: libcroco
Version: %ver_major.11
Release: alt2

Summary: A CSS2 parsing library
License: LGPL
Group: System/Libraries
Url: ftp://ftp.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.0
%define libxml2_ver 2.4.23

%def_with apidocs

Requires: glib2 >= %glib_ver
Requires: libxml2 >= %libxml2_ver

BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libxml2-devel >= %libxml2_ver

BuildRequires: zlib-devel
%{?_with_apidocs:BuildRequires: gtk-doc doxygen}

%description
Libcroco is a standalone CSS2 parsing and manipulation library.

%package devel
Summary: Libraries and include files for developing with %name
Group: Development/C
Requires: %name = %version-%release
Requires: pkgconfig >= 0.8
Requires: glib2-devel >= %glib_ver
Requires: libxml2-devel >= %libxml2_ver

%description devel
This package provides the necessary development libraries and include
files to develop with %name.

%if_with apidocs
%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains development documentation for %name
%endif

%package -n css-utils
Summary: Command line CSS tools
Group: Text tools
Requires: %name = %version-%release

%description -n css-utils
This package provides csslint - program to parse CSS files. It is useful
for detecting errors both in CSS code and in the CSS parser itself.

%prep
%setup

%build
%configure --disable-static

%make_build
%{?_with_apidocs:%make_build apidoc}

%install
%makeinstall

%check
%make check

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS README TODO

%files devel
%_bindir/croco-%ver_major-config
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%if_with apidocs
%doc docs/{apis/html,examples}
%endif

%if_with apidocs
%files devel-doc
%_datadir/gtk-doc/html/%name/
%endif

%files -n css-utils
%_bindir/csslint-%ver_major

%changelog
* Mon Jan 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.6.11-alt2
- mike: conditional apidocs build via the added switch (for bootstrap)

* Thu Dec 17 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.11-alt1
- 0.6.11

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.10-alt1
- 0.6.10

* Sat Oct 31 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.9-alt1
- 0.6.9

* Fri Oct 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.8-alt1
- 0.6.8

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.7-alt1
- 0.6.7

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.6-alt1
- 0.6.6

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.5-alt1
- 0.6.5

* Tue Feb 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.4-alt1
- 0.6.4

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- 0.6.3

* Wed Mar 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt3
- rebuilt for debuginfo

* Thu Oct 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt2
- rebuild

* Wed Feb 04 2009 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- new version
- removed obsolete %%post{,un}_ldconfig

* Wed Mar 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.6.1-alt1
- new version (0.6.1)

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Sun Apr 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Sun Dec 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt1
- 0.4.0
- do not package .la files.

* Wed Oct 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt2
- fixed buildreqs.

* Tue Jul 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Mon Jun 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri Apr 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1.0-alt1
- First build for Sisyphus.
