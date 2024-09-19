%def_disable snapshot

%define ver_major 1.82
%define api_ver 1.0
%define gir_api_ver 1.0
%def_enable doctool
%ifarch ppc64le armh
%def_disable check
%else
%def_disable check
%endif
%def_enable gtk_doc

Name: gobject-introspection
Version: %ver_major.0
Release: alt1

Summary: Introspection system for GObject-based libraries
Group: System/Libraries
License: GPL-2.0-or-later and LGPL-2.0-or-later and MIT
Url: https://live.gnome.org/GObjectIntrospection

Provides: gir-repository = %EVR
Obsoletes: gir-repository

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%endif

%add_python3_path %_libdir/%name/giscanner
#https://bugzilla.altlinux.org/38965
# python3(pkgconfig) provided by giscanner/pkgconfig.py
%filter_from_provides /python3(pkgconfig)/d
%filter_from_requires /python3(distutils.*)/d

%define glib_ver 2.82.0
%define python_ver 3.8

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: /proc meson libgio-devel >= %glib_ver
BuildRequires: flex gtk-doc libcairo-devel libcairo-gobject-devel libffi-devel
BuildRequires: python3-devel >= %python_ver python3(setuptools._distutils)
%{?_enable_doctool:BuildRequires: python3-module-mako python3-module-markdown}

%description
GObject introspection provides tools and libraries to help manage its
common metadata format for representing GObject-based C APIs, designed
for bindings, documentation tools and API verification.

%package x11
Summary: x11-dependent typelibs
Group: System/Libraries
Requires: %name = %EVR

%description x11
This package provides x11-dependent typelibs from %name package.

%package devel
Summary: Libraries and headers for gobject-introspection
Group: Development/C
Requires: %name = %EVR libgio-devel rpm-build-gir
Requires: %name-x11 = %EVR
#Requires: libgirepository%api_ver = %EVR
Requires: libgirepository%api_ver-devel = %EVR
Requires: python3(setuptools._distutils)
Provides: gir-repository-devel = %EVR
Obsoletes: gir-repository-devel

%description devel
GObject introspection provides tools and libraries to help manage its
common metadata format for representing GObject-based C APIs, designed
for bindings, documentation tools and API verification.

This package provides libraries and headers for gobject-introspection.

%package -n libgirepository%api_ver
Summary: GObject Introspection Library (API 1.0)
Group: System/Libraries

%description -n libgirepository%api_ver
This package provides shared GObject Introspection library.

%package -n libgirepository%api_ver-devel
Summary: development package for GObject Introspection library (API 1.0)
Group: Development/C
Requires: libgirepository%api_ver = %EVR

%description -n libgirepository%api_ver-devel
This package provides development files for GObject Introspection library.

%package devel-doc
Summary: Documentation for gobject-introspection
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
GObject introspection provides tools and libraries to help manage its
common metadata format for representing GObject-based C APIs, designed
for bindings, documentation tools and API verification.

This package provides development documentation for
gobject-introspection.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%meson \
	%{subst_enable_meson_feature doctool doctool} \
	%{subst_enable_meson_bool gtk_doc gtk_doc} \
	-Dpython=%__python3
%meson_build

%install
%meson_install

%check
%__meson_test -v

%files
%dir %_typelibdir/
%_typelibdir/DBus-1.0.typelib
%_typelibdir/DBusGLib-1.0.typelib
%_typelibdir/GIRepository-2.0.typelib
%_typelibdir/GL-1.0.typelib
%_typelibdir/cairo-1.0.typelib
%_typelibdir/fontconfig-2.0.typelib
%_typelibdir/freetype2-2.0.typelib
%_typelibdir/libxml2-2.0.typelib
%_typelibdir/win32-1.0.typelib
%_typelibdir/Vulkan-1.0.typelib

%files x11
%_typelibdir/xfixes-4.0.typelib
%_typelibdir/xft-2.0.typelib
%_typelibdir/xlib-2.0.typelib
%_typelibdir/xrandr-1.3.typelib

%files devel
%_bindir/g-ir-annotation-tool
%_bindir/g-ir-compiler
%_bindir/g-ir-doc-tool
%_bindir/g-ir-generate
%_bindir/g-ir-inspect
%_bindir/g-ir-scanner
%dir %_libdir/%name
%_libdir/%name/giscanner/
%_girdir/
%_datadir/%name-%api_ver
%_datadir/aclocal/introspection.m4
%_man1dir/*.1*

%files -n libgirepository%api_ver
%_libdir/libgirepository-%api_ver.so.*

%files -n libgirepository%api_ver-devel
%_includedir/%name-%api_ver
%_libdir/libgirepository-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_pkgconfigdir/%name-no-export-%api_ver.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Fri Sep 13 2024 Yuri N. Sedunov <aris@altlinux.org> 1.82.0-alt1
- 1.82.0

* Mon Apr 01 2024 Yuri N. Sedunov <aris@altlinux.org> 1.80.1-alt1
- 1.80.1

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1.80.0-alt2
- updated to 1.80.0-13-g2b5b9397

* Sat Mar 09 2024 Yuri N. Sedunov <aris@altlinux.org> 1.80.0-alt1
- 1.80.0
- build against debootstraped glib-2.80.0-alt2

* Tue Jan 02 2024 Yuri N. Sedunov <aris@altlinux.org> 1.78.1-alt2
- new libgirepository1.0{,-devel} subpackages

* Fri Oct 13 2023 Yuri N. Sedunov <aris@altlinux.org> 1.78.1-alt1.3
- fixed %%check w/o distutils

* Thu Oct 12 2023 Yuri N. Sedunov <aris@altlinux.org> 1.78.1-alt1.2
- g-i-devel requires setuptools (ALT #47966)

* Sun Oct 08 2023 Yuri N. Sedunov <aris@altlinux.org> 1.78.1-alt1.1
- updated dependencies for python3 >= 3.11.6-alt1 w/o distutils

* Sat Sep 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1.78.1-alt1
- 1.78.1

* Thu Mar 23 2023 Yuri N. Sedunov <aris@altlinux.org> 1.76.1-alt1
- 1.76.1

* Tue Mar 14 2023 Yuri N. Sedunov <aris@altlinux.org> 1.76.0-alt1
- 1.76.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 1.74.0-alt1
- 1.74.0

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 1.72.0-alt1
- 1.72.0

* Fri Sep 17 2021 Yuri N. Sedunov <aris@altlinux.org> 1.70.0-alt1
- 1.70.0

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 1.68.0-alt1
- 1.68.0

* Sat Oct 03 2020 Yuri N. Sedunov <aris@altlinux.org> 1.66.1-alt1
- 1.66.1

* Sat Sep 19 2020 Yuri N. Sedunov <aris@altlinux.org> 1.66.0-alt1
- 1.66.0

* Sat Sep 19 2020 Yuri N. Sedunov <aris@altlinux.org> 1.64.1-alt2
- filtered "python3(pkgconfig)" from provides (ALT #38965)

* Sun Apr 05 2020 Yuri N. Sedunov <aris@altlinux.org> 1.64.1-alt1
- 1.64.1

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1.64.0-alt1
- 1.64.0

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.62.0-alt1
- 1.62.0 (ported to Meson build system)

* Sat Jun 15 2019 Yuri N. Sedunov <aris@altlinux.org> 1.60.2-alt1
- 1.60.2

* Fri Apr 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.60.1-alt1.1
- enabled %%check

* Sun Apr 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1.60.1-alt1
- 1.60.1

* Sun Mar 10 2019 Yuri N. Sedunov <aris@altlinux.org> 1.60.0-alt1
- 1.60.0

* Sun Dec 30 2018 Yuri N. Sedunov <aris@altlinux.org> 1.58.3-alt1
- 1.58.3

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.58.2-alt1
- 1.58.2

* Mon Nov 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.58.1-alt1
- 1.58.1

* Fri Aug 31 2018 Yuri N. Sedunov <aris@altlinux.org> 1.58.0-alt1
- 1.58.0

* Thu Apr 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.56.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.56.1-alt1
- 1.56.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.56.0-alt1
- 1.56.0 with python3

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.54.1-alt1
- 1.54.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 1.54.0-alt1
- 1.54.0

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1.52.1-alt1
- 1.52.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 1.52.0-alt1
- 1.52.0

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.50.0-alt1
- 1.50.0

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.48.0-alt1
- 1.48.0

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.46.0-alt1
- 1.46.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.44.0-alt1
- 1.44.0

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 1.42.0-alt1
- 1.42.0

* Fri Apr 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.40.0-alt1.1
- updated to 5b105135d2 (fixed BGO #724886)

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.40.0-alt1
- 1.40.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.38.0-alt1
- 1.38.0

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 1.36.0-alt1
- 1.36.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 1.34.2-alt1
- 1.34.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 1.34.1.1-alt1
- 1.34.1.1

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 1.34.1-alt1
- 1.34.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.34.0-alt1
- 1.34.0

* Wed Apr 18 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.1-alt1
- 1.32.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.0-alt1
- 1.32.0

* Fri Jan 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt2
- updated from upstream git, in particular fixed build on arm platform

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.30.0-alt1.1
- Rebuild with Python-2.7

* Fri Sep 23 2011 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt1
- 1.30.0

* Tue Aug 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.29.17-alt1
- 1.29.17

* Fri Aug 12 2011 Yuri N. Sedunov <aris@altlinux.org> 1.29.16-alt1
- 1.29.16

* Thu Jun 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.29.0-alt1
- 1.29.0

* Sat Mar 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.6-alt1
- 0.10.6

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt1
- 0.10.4

* Fri Feb 25 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

* Wed Feb 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Mon Jan 31 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1
- new devel-doc subpackage (aris@)

* Thu Dec 23 2010 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Oct 18 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt1
- pre 0.9.11 snapshot
- Obsoletes: gir-repository

* Thu Aug 19 2010 Kirill A. Shutemov <kas@altlinux.org> 0.6.14-alt2
- Rebuild with new libffi.

* Fri Jun 04 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.14-alt1
- 0.6.14

* Wed May 26 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.12-alt1
- 0.6.12

* Tue Apr 20 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.10-alt1
- 0.6.10

* Wed Mar 31 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.9-alt2
- rebuild with modified rpm-build-gir

* Fri Mar 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.9-alt1
- 0.6.9

* Fri Mar 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.8-alt1
- 0.6.8

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.7-alt2
- devel: requires rpm-build-gir

* Thu Dec 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.7-alt1
- 0.6.7

* Mon Dec 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Sun Sep 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.3-alt1
- initial release

