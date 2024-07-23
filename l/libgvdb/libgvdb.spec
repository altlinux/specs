%define _unpackaged_files_terminate_build 1
%def_with docs

Name: libgvdb
Version: 0.0
Release: alt2.git816b474

Summary: Python binding (PyGObject) of GVDB library
License: LGPLv2.1
Group: System/Libraries
URL: https://gitlab.gnome.org/GNOME/gvdb
VCS: https://gitlab.gnome.org/GNOME/gvdb

Source: %name-%version.tar
Patch: %name-%version-%release-alt.patch

BuildRequires(pre): rpm-macros-meson rpm-build-gir

BuildRequires: python3-module-pygobject3-devel python3-devel
BuildRequires: libgio-devel gobject-introspection-devel
BuildRequires: yelp-tools
BuildRequires: meson

%description
GVDB (GVariant Database) is a simple database file format that stores a mapping
from strings to GVariant values in a way that is extremely efficient for lookups.

%package devel
Summary: Headers for developing programs that will use gvdb
Group: Development/C
Requires: %name = %version-%release

%description devel
GVDB is a library for working with the GVariant database.
This package contains the headers that programmers will need to develop
applications using the gvdb library. applications that use the gvdb library.

%package gir
Summary: GObject introspection data for the Gvdb-1.0 library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Gvdb-1.0 library

%prep
%setup -q
%patch -p1

%build
%meson
%meson_build

cd gvdb
g-ir-scanner --namespace=Gvdb --nsversion=1.0 \
     --include GLib-2.0 --include Gio-2.0 \
     -L ../%__builddir --library=gvdb \
     --accept-unprefixed --output=Gvdb.gir \
     --c-include="gvdb-format.h" *.h *.c \
     -I/usr/include/glib-2.0/ -I/usr/include/gio-unix-2.0/ \
     -I/usr/lib64/glib-2.0/include --warn-all
g-ir-compiler Gvdb.gir -o Gvdb-1.0.typelib 

g-ir-doc-tool --language C -o ./documentation Gvdb.gir
cd documentation/
yelp-build html .

%install
mkdir -p %buildroot/%_typelibdir
cp gvdb/Gvdb-1.0.typelib %buildroot%_typelibdir

mkdir -p %buildroot/%_includedir/gvdb
cp gvdb/*.h %buildroot/%_includedir/gvdb

%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%doc README.md
%_libdir/%name.so.*

%files devel
%doc alt/docs/* gvdb/documentation/
%_includedir/gvdb
%_includedir/gvdb/gvdb-builder.h
%_includedir/gvdb/gvdb-format.h
%_includedir/gvdb/gvdb-reader.h
%_libdir/%name.so

%files gir
%_typelibdir/*.typelib

%changelog
* Tue Jul 23 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.0-alt2.git816b474
- initial build for Sisyphus

* Tue Jul 16 2024 Maria Alexeeva <alxvmr@altlinux.org> 0.0-alt1.git816b474
- first build

