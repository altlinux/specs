%define _name rest
%define ver_major 0.7
%def_enable introspection
%def_disable gtk_doc
%def_disable tests

Name: lib%_name
Version: %ver_major.12
Release: alt1

Summary: A library for access to RESTful web services
Group: System/Libraries
License: LGPLv2
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

# from fedora
Patch: rest-fixdso.patch

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
%setup -q -n %_name-%version
%patch -p1 -b .fixdso

%build
%configure --disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--with-ca-certificates=%_datadir/ca-certificates/ca-bundle.crt

%make_build

%check
%{?_enable_tests:%make check}

%install
%make DESTDIR=%buildroot install

%files
%_libdir/librest-%ver_major.so.*
%_libdir/librest-extras-%ver_major.so.*
%doc AUTHORS README

%files devel
%_includedir/rest-%ver_major
%_libdir/librest-%ver_major.so
%_libdir/librest-extras-%ver_major.so
%_libdir/pkgconfig/rest*

%if_enabled introspection
%files gir
%_typelibdir/Rest-%ver_major.typelib
%_typelibdir/RestExtras-%ver_major.typelib

%files gir-devel
%_girdir/Rest-%ver_major.gir
%_girdir/RestExtras-%ver_major.gir
%endif

%files devel-doc
%_datadir/gtk-doc/html/%{_name}*%ver_major/

%changelog
* Thu Nov 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.12-alt1
- 0.7.12

* Mon Oct 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.11-alt1
- 0.7.11

* Sat Jul 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.10-alt2
- build without tests.

* Thu Jun 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.10-alt1
- first build for Sisyphus

