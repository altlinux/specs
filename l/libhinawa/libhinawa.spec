%define _unpackaged_files_terminate_build 1

%define sover 4
%define api_ver 4.0
%def_enable docs

Name: libhinawa
Version: 4.0.2
Release: alt1

Summary: I/O library for IEEE 1394 asynchronous transactions
License: LGPL-2.1-or-later
Group: Development/C

Url: https://github.com/alsa-project/libhinawa
Vcs: https://github.com/alsa-project/libhinawa
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: gobject-introspection-devel
%if_enabled docs
BuildRequires: gi-docgen
%endif

%description
I/O library for IEEE 1394 asynchronous transactions to/from units on the bus,
with GObject Introspection.

%package -n %name%sover
Summary: I/O library for IEEE 1394 asynchronous transactions
Group: System/Libraries

%description -n %name%sover
I/O library for IEEE 1394 asynchronous transactions to/from units on the bus,
with GObject Introspection.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name%sover = %EVR

%description gir
GObject introspection data for the %name.

%package gir-devel
Summary: GObject introspection development data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection development data for the %name.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%sover = %EVR

%description devel
This package contains the libraries and header files that are needed
for writing applications with libhinawa.

%package devel-doc
Summary: Documentation for %name
Group: Development/Documentation
Conflicts: %name%sover < %EVR
BuildArch: noarch

%description devel-doc
Documentation subpackage for %name.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool docs doc}
%nil
%meson_build

%install
%meson_install

%files -n %name%sover
%_libdir/%name.so.%sover
%_libdir/%name.so.%sover.*

%files gir
%_typelibdir/Hinawa-%api_ver.typelib

%files gir-devel
%_girdir/Hinawa-%api_ver.gir

%files devel
%_libdir/libhinawa.so
%_includedir/hinawa/*.h
%_libdir/pkgconfig/hinawa.pc

%if_enabled docs
%files devel-doc
%doc %_datadir/doc/hinawa/
%endif

%changelog
* Tue Sep 01 2026 Pavel Mitrofanov <cobalt@altlinux.org> 4.0.2-alt1
- Initial commit.
