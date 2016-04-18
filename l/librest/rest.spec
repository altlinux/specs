%define _name rest
%define ver_major 0.8
%define api_ver 0.7
%def_enable introspection
%def_disable gtk_doc
%def_disable tests

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: A library for access to RESTful web services
Group: System/Libraries
License: LGPLv2
Url: http://www.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Requires: ca-certificates

BuildRequires: glib2-devel libsoup-gnome-devel libxml2-devel gtk-doc
%{?_enable_introspection:BuildRequires: libsoup-gnome-gir-devel}

%description
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Files for development with %name.

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name library

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %_name library

%package devel-doc
Summary: Development documentation for %_name
Group: Development/C
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for the %_name library.


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--with-ca-certificates=%_datadir/ca-certificates/ca-bundle.crt

%make_build

%check
%{?_enable_tests:%make check}

%install
%makeinstall_std

%files
%_libdir/librest-%api_ver.so.*
%_libdir/librest-extras-%api_ver.so.*
%doc AUTHORS README

%files devel
%_includedir/rest-%api_ver/
%_libdir/librest-%api_ver.so
%_libdir/librest-extras-%api_ver.so
%_libdir/pkgconfig/rest*

%if_enabled introspection
%files gir
%_typelibdir/Rest-%api_ver.typelib
%_typelibdir/RestExtras-%api_ver.typelib

%files gir-devel
%_girdir/Rest-%api_ver.gir
%_girdir/RestExtras-%api_ver.gir
%endif

%files devel-doc
%_datadir/gtk-doc/html/%{_name}*%api_ver/

%changelog
* Mon Apr 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.93-alt1
- 0.7.93

* Wed Sep 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.92-alt1
- 0.7.92

* Mon Mar 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.91-alt1
- 0.7.91

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.7.90-alt1
- 0.7.90

* Thu Nov 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.12-alt1
- 0.7.12

* Mon Oct 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.11-alt1
- 0.7.11

* Sat Jul 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.10-alt2
- build without tests.

* Thu Jun 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.10-alt1
- first build for Sisyphus

