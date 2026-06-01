%define _libexecdir %_prefix/libexec
%def_disable snapshot

%define ver_major 0.4
%define api_ver 2
%define namespace SSC
%define sover 2

%define qrtr_ver 1.2

%def_enable introspection
%def_enable vala
%def_enable check

Name: libssc
Version: %ver_major.3
Release: alt1

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

BuildRequires(pre): rpm-macros-meson rpm-build-python3 %{?_enable_introspection:rpm-build-gir} %{?_enable_vala:rpm-build-vala}
BuildRequires: meson
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: pkgconfig(qmi-glib) >= %qmi_ver
BuildRequires: pkgconfig(libprotobuf-c) protobuf-c-compiler
BuildRequires: pkgconfig(protobuf)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel gir(Qmi) = 1.0}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_check:
BuildRequires: pkgconfig(qrtr)
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

%package tests
Summary: Tests for %name
Group: Development/Other
BuildArch: noarch
Requires: %name = %EVR
# may be rpm-build-python3 bug
%add_python3_req_skip ssc_common_pb2

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %name.

%prep
%setup -n %name
sed -i 's|\/_build\/|/%__builddir/|
        s|\/usr/lib/|%_libdir/|' mocking/ssc_server/ssc-server.in
%build
%meson \
    %{?optflags_lto:-Db_lto=true}
%nil
%meson_build

%install
%meson_install

%check
#export PYTHONPATH=${PWD}/%__builddir/data
%__meson_test

%files
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

%files tests
%dir %_libexecdir/installed-tests/%name
%_libexecdir/installed-tests/%name/ssc-server
%python3_sitelibdir_noarch/ssc_server/

%changelog
* Sun May 31 2026 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Mar 19 2026 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Tue Mar 03 2026 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt0.6
- enabled %%check

* Tue Mar 03 2026 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt0.5
- first build for Sisyphus

