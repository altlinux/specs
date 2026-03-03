%def_enable introspection
%def_enable docs
%define soname 0

Name: libqrtr-glib
Version: 1.4.0
Release: alt1

Summary: Qualcomm IPC Router protocol helper library
License: LGPLv2+
Group: System/Libraries
URL: https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib
Vcs: https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson rpm-macros-meson >= 1.3.1-alt1

BuildRequires: glib2-devel libgio-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_docs:BuildRequires: gi-docgen}

%define _unpackaged_files_terminate_build 1

%description
libqrtr-glib is a glib-based library to use and manage the QRTR (Qualcomm
IPC Router) bus.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: glib2-devel

%description devel
This package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
%summary

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
%summary

%if_enabled docs
%package devel-doc
Summary: This package contains development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Requires: %name-devel = %version-%release

%description devel-doc
This package contains development documentation for %name
%endif

%prep
%setup
%patch -p1

%build
%ifarch %e2k
%def_disable werror
%else
%def_enable werror
%endif

%meson \
	%{subst_enable_meson_bool introspection introspection} \
	%{subst_enable_meson_bool docs gtk_doc} \
	%{subst_enable_meson_bool werror werror}

%meson_build -v

%install
%meson_install

%files
%doc NEWS README.md AUTHORS
%_libdir/%name.so.%soname
%_libdir/%name.so.%soname.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*.typelib

%files gir-devel
%_datadir/gir-1.0/*.gir
%endif

%if_enabled docs
%files devel-doc
%_datadir/doc/%{name}-1.0/
%endif

%changelog
* Tue Mar 03 2026 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Added soname check.
- Added docs knob.
- Used macros from rpm-macros-meson.
- Packaged NEWS, README.md and AUTHORS files.
- Updated to 1.4.0 (closes: #58096).

* Tue Mar 01 2022 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Thu Dec 09 2021 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Thu Feb 25 2021 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Initial build.

