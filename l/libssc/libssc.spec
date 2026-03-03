%def_disable snapshot

%define ver_major 0.4
%define api_ver 2
%define namespace SSC
%define sover 2

%def_enable introspection
%def_enable vala
%def_disable check

Name: libssc
Version: %ver_major.1
Release: alt0.5

Summary: Library for exposing Qualcomm Sensor Core to Linux
Group: System/Libraries
License: GPL-3.0-or-later
Url: https://libssc.dylanvanassche.be

Vcs: https://codeberg.org/DylanVanAssche/libssc.git

%if_disabled snapshot
Source: https://codeberg.org/DylanVanAssche/libssc/archive/v%version.tar.gz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.56
%define qmi_ver 1.33.4

BuildRequires(pre): rpm-macros-meson %{?_enable_introspection:rpm-build-gir} %{?_enable_vala:rpm-build-vala}
BuildRequires: meson
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: pkgconfig(qmi-glib) >= %qmi_ver
BuildRequires: pkgconfig(libprotobuf-c) protobuf-c-compiler
BuildRequires: pkgconfig(protobuf)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel gir(Qmi) = 1.0}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_check:
BuildRequires: pkgconfig(qrtr-glib)
BuildRequires: python3-module-pygobject3
BuildRequires: python3(google)}

%description
%name is a library to expose the sensors managed by the Qualcomm Sensor
Core found in many Qualcomm System-on-Chips (SoCs) from 2018 and
onwards.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for %name.

%package gir-devel
Summary: GObject introspection devel data for %name.
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for %name.


%prep
%setup -n %name
%{?_enable_tests:sed -i 's/pytest-3/py.test-3/' meson.build}

%build
%meson \
    %{?optflags_lto:-Db_lto=true}
%nil
%meson_build

%install
%meson_install

%check
export PYTHONPATH=${PWD}/%__builddir/data
%__meson_test

%files
#%_bindir/ssc-server*
%_bindir/ssccli
%_libdir/%name.so.%{sover}*

%doc README* CHANGELOG*

%files devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/%name.pc
%{?_enable_vala:%_vapidir/%name.*}

%if_enabled introspection
%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%changelog
* Tue Mar 03 2026 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt0.5
- first build for Sisyphus

