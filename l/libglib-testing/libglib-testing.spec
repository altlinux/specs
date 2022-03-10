%def_enable snapshot
%define _name glib-testing
%define api_ver 0

%def_enable check

Name: lib%_name
Version: 0.1.1
Release: alt1

Summary: GLib-based test library
Group: System/Libraries
License: LGPLv2+
Url: https://gitlab.gnome.org/pwithnall/libglib-testing

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.bz2
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.54

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson pkgconfig(gio-2.0) >= %glib_ver gtk-doc
%{?_enable_check:BuildRequires: dbus}

%description
libglib-testing is a test library providing test harnesses and mock
classes which complement the classes provided by GLib. It is intended to
be used by any project which uses GLib and which wants to write internal
unit tests.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides headers and development libraries for %name.

%package devel-doc
Summary: Development documentation for the %name
Group: Development/Documentation
Conflicts: %name < %EVR
BuildArch: noarch

%description devel-doc
This package contains development documentation for the %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%_libdir/%name-%api_ver.so.*
%doc NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%files devel-doc
%_datadir/gtk-doc/html/%name/

%changelog
* Thu Mar 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- 0.1.1-4-g366dab0

* Wed Sep 16 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus (0.1.0-2-g0c6454f)


