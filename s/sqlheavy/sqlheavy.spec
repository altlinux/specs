%define api_ver 0.2

Name: sqlheavy
Version: 0.2
Release: alt2

Summary: GObject wrapper for SQLite
License: LGPLv2.1 or v3
Group: System/Libraries
Url: https://github.com/nemequ/sqlheavy

# commit e83b497a
Source: %name-%version.tar

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: libgio-devel libsqlite3-devel gobject-introspection-devel vala-tools

%description
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface

%package -n lib%name
Summary: GObject wrapper for SQLite (library)
Group: System/Libraries

%description -n lib%name
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface

This package contains the shared library.

%package -n lib%name-devel
Summary: GObject wrapper for SQLite (development files)
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface

This package contains the development files.

%package -n lib%name-gir
Summary: GObject introspection data for the SQLHeavy library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the SQLHeavy library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the SQLHeavy library
Group: Development/Other
Requires: lib%name-devel = %version-%release
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the SQLHeavy library.


%prep
%setup

%build
touch ChangeLog
%autoreconf
%configure \
  --disable-static
%make_build V=1

%install
%makeinstall_std

%files -n lib%name
%_libdir/lib%name%api_ver.so.*

%files -n lib%name-devel
%_libdir/lib%name%api_ver.so
%_includedir/%name/
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%files -n lib%name-gir
%_typelibdir/SQLHeavy-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/SQLHeavy-%api_ver.gir


%changelog
* Thu Sep 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt2
- updated to 0.2_e83b497a from new url
- removed %%{name}gtk subpackages
- new {gir,}-devel subpackages

* Thu Sep 12 2013 Igor Zubkov <icesik@altlinux.org> 0.2-alt1
- build for Sisyphus

