%define _name gexiv2
%define ver_major 0.14
%define api_ver 0.10

%def_enable gtk_doc
%def_enable vala
%def_enable python3
%def_enable check

Name: lib%_name
Version: %ver_major.3
Release: alt1

Summary: GObject-based Exiv2 wrapper
Group: System/Libraries
License: GPL-2.0-or-later
Url: https://wiki.gnome.org/Projects/gexiv2

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildRequires(pre): rpm-macros-meson %{?_enable_python3:rpm-build-python3}
BuildRequires: meson gcc-c++ libexiv2-devel libgio-devel gobject-introspection-devel
%{?_enable_python3:BuildRequires: python3-module-pygobject3-devel}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_vala:BuildRequires: vala-tools}

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

%package devel
Group: Development/C
Requires: %name = %version-%release
Summary: GObject-based Exiv2 wrapper - development files

%description devel
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

This package provides headers and libraries needed to develop
applications using gexiv2 library.

%package devel-doc
Summary: Development documentation for gexiv2
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

This package contains development documentation for gexiv2 library.

%package gir
Summary: GObject introspection data for the gexiv2 library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the gexiv2 library.

%package gir-devel
Summary: GObject introspection devel data for the gexiv2 library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the gexiv2 library.

%package -n python3-module-%_name
Summary: Python3 bindings for at-spi
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%_name
This package provides Python3 bindings for the gexiv2 library.

%prep
%setup -n %_name-%version

%build

%meson \
	-Dintrospection=true \
	%{?_enable_vala:-Dvapi=true} \
	%{?_enable_gtk_doc:-Dgtk_doc=true} \
	%{?_disable_python3:-Dpython3=false}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name.so.*
%doc AUTHORS README* THANKS NEWS

%files devel
%_includedir/%_name/
%_libdir/%name.so
%_pkgconfigdir/%_name.pc
%{?_enable_vala:%_vapidir/%_name.*}

%files gir
%_typelibdir/GExiv2-%api_ver.typelib

%files gir-devel
%_girdir/GExiv2-%api_ver.gir

%{?_enable_python3:
%files -n python3-module-%_name
%python3_sitelibdir_noarch/gi/overrides/GExiv2.py*
%python3_sitelibdir_noarch/gi/overrides/__pycache__/GExiv2.cpython-*.pyc}

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%changelog
* Fri Jun 28 2024 Yuri N. Sedunov <aris@altlinux.org> 0.14.3-alt1
- 0.14.3

* Tue Jul 25 2023 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt1
- 0.14.2

* Sat May 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- 0.12.3

* Sat Feb 20 2021 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- 0.12.2

* Sat Nov 14 2020 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt2
- disabled Python 2 support

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sat Jan 05 2019 Yuri N. Sedunov <aris@altlinux.org> 0.10.10-alt1
- 0.10.10

* Mon Nov 19 2018 Yuri N. Sedunov <aris@altlinux.org> 0.10.9-alt1
- 0.10.9

* Tue Feb 06 2018 Yuri N. Sedunov <aris@altlinux.org> 0.10.8-alt1
- 0.10.8

* Sun Dec 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.10.7-alt1
- 0.10.7

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.10.6-alt1
- 0.10.6

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt2
- rebuilt against libexiv2.so.26

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt1
- 0.10.5

* Tue Aug 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt1
- 0.10.4

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt2
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10.3-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

* Wed Sep 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Sat Apr 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Thu Feb 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Fri Dec 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0
- new -gir{,-devel}, python{,3}-module-* subpackages

* Fri Jan 25 2013 Vladimir Lettiev <crux@altlinux.ru> 0.5.0-alt1
- New version 0.5.0

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.4.1-alt1
- New version 0.4.1

* Thu Nov 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.3.1-alt1
- New version 0.3.1

* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2.2-alt1
- New version 0.2.2

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.1-alt1
- New version 0.2.1

* Tue Jul 27 2010 Vladimir Lettiev <crux@altlinux.ru> 0.1.0-alt1
- initial build

