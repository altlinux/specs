Name: libmodulemd
Version: 2.14.0
Release: alt1

Summary: C Library for manipulating module metadata files
License: MIT
Group:   System/Libraries
Url:     https://github.com/fedora-modularity/libmodulemd

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-python3
BuildRequires: librpm-devel
BuildRequires: glib2-devel
BuildRequires: libyaml-devel
BuildRequires: libmagic-devel
BuildRequires: gobject-introspection-devel
BuildRequires: python3-module-pygobject3-devel

%description
%{summary}.

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
%{summary}.

%package -n python3-module-%name
Summary: Python3 bindings for %name
Group: Development/Python3

%description -n python3-module-%name
%{summary}.

%prep
%setup

%build
%meson \
    -Dlibmagic=enabled \
    -Drpmio=enabled \
    -Dskip_introspection=false \
    -Dtest_installed_lib=false \
    -Dwith_docs=false \
    -Dwith_manpages=enabled
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/modulemd-validator
%_libdir/*.so.*
%_man1dir/*.1*
%_libdir/girepository-1.0/*.typelib

%files devel
%_libdir/*.so
%_includedir/modulemd-2.0
%_libdir/pkgconfig/*.pc
%_datadir/gir-1.0/*.gir

%files -n python3-module-%name
%python3_sitelibdir/gi/overrides/*

%changelog
* Sun Oct 30 2022 Andrey Cherepanov <cas@altlinux.org> 2.14.0-alt1
- Initial build for Sisyphus
