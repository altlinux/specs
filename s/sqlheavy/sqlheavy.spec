# TODO: fix this
%set_verify_elf_method unresolved=relaxed

Name: sqlheavy
Version: 0.2
Release: alt1

Summary: GObject wrapper for SQLite
License: LGPLv2.1 or v3
Group: System/Libraries
Url: http://gitorious.org/sqlheavy

# commit 7ae6112960a0ac4d77d904dd8cc561dcac62b6e2
Source0: %name.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: libgio-devel libsqlite3-devel libgtk+2-devel vala

%description
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface

%package -n libsqlheavy
Summary: GObject wrapper for SQLite (library)
Group: System/Libraries

%description -n libsqlheavy
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface

This package contains the shared library.

%package -n libsqlheavy-devel
Summary: GObject wrapper for SQLite (development files)
Group: Development/C

Requires: libsqlheavy = %version-%release

%description -n libsqlheavy-devel
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface

This package contains the development files.

%package -n libsqlheavygtk
Summary: SQLHeavy GTK+ integration library (library)
Group: System/Libraries

Requires: libsqlheavy = %version-%release

%description -n libsqlheavygtk
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface

This package contains a library to help integrate SQLHeavy into GTK+
applications.

%package -n libsqlheavygtk-devel
Summary: SQLHeavy GTK+ integration library (development files)
Group: Development/C

Requires: libsqlheavygtk = %version-%release

%description -n libsqlheavygtk-devel
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface

This package contains the development files for a library to help
integrate SQLHeavy into GTK+ applications.

%prep
%setup -q -n %name

%build
touch ChangeLog
%autoreconf
%configure \
  --disable-static
%make_build V=1

%install
%make_install DESTDIR=%buildroot install

%files -n libsqlheavy
%_libdir/libsqlheavy0.2.so.*
%_datadir/sqlheavy/0.2/schemas/*

%files -n libsqlheavy-devel
%_libdir/libsqlheavy0.2.so
%_includedir/sqlheavy/sqlheavy-0.2/SQLHeavy.h
%_pkgconfigdir/sqlheavy-0.2.pc

%_datadir/vala/vapi/sqlheavy-0.2.deps
%_datadir/vala/vapi/sqlheavy-0.2.vapi


%files -n libsqlheavygtk
%_libdir/libsqlheavygtk0.2.so.*

%files -n libsqlheavygtk-devel
%_libdir/libsqlheavygtk0.2.so
%_includedir/sqlheavy/sqlheavy-0.2/SQLHeavyGTK.h
%_pkgconfigdir/sqlheavygtk-0.2.pc

%_datadir/vala/vapi/sqlheavygtk-0.2.deps
%_datadir/vala/vapi/sqlheavygtk-0.2.vapi

# TODO:
#    /usr/lib/girepository-1.0/SQLHeavy-0.2.typelib
#    /usr/share/gir-1.0/SQLHeavy-0.2.gir
#    /usr/share/man/man1/sqlheavy-gen-orm.1.gz

%changelog
* Thu Sep 12 2013 Igor Zubkov <icesik@altlinux.org> 0.2-alt1
- build for Sisyphus

