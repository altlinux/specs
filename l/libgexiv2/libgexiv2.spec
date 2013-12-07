%define _name gexiv2
%define ver_major 0.7
%define api_ver 0.4

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: GObject-based Exiv2 wrapper
Group: System/Libraries
License: GPL2
Url: https://wiki.gnome.org/Projects/gexiv2

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildRequires: gcc-c++ libexiv2-devel libgio-devel gobject-introspection-devel vala-tools
BuildRequires: python-module-pygobject3-devel rpm-build-python3 python3-module-pygobject3-devel

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

%package -n python-module-%_name
Summary: Python bindings for at-spi
Group: Development/Python

%description -n python-module-%_name
This package provides Python bindings for the gexiv2 library.

%package -n python3-module-%_name
Summary: Python3 bindings for at-spi
Group: Development/Python3

%description -n python3-module-%_name
This package provides Python3 bindings for the gexiv2 library.

%prep
%setup -n %_name-%version

%build
%configure --disable-static \
	--enable-introspection
%make_build

%install
%makeinstall_std LIB=%_lib

%files
%_libdir/%name.so.*
%doc AUTHORS README THANKS NEWS

%files devel
%_includedir/%_name/
%_libdir/%name.so
%_pkgconfigdir/%_name.pc
%_vapidir/%_name.vapi

%files gir
%_typelibdir/GExiv2-%api_ver.typelib

%files gir-devel
%_girdir/GExiv2-%api_ver.gir

%files -n python-module-%_name
%python_sitelibdir/gi/overrides/GExiv2.py*

%files -n python3-module-%_name
%python3_sitelibdir/gi/overrides/GExiv2.py*
%python3_sitelibdir/gi/overrides/__pycache__/GExiv2.cpython-*.pyc

%changelog
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

