%define _unpackaged_files_terminate_build 1
%define sover 22

Name: gvm-libs
Version: 22.22.0
Release: alt1

Summary: Support libraries for Greenbone Vulnerability Management Solution and OpenVAS
License: GPL-2.0-only
Group: System/Libraries
Url: http://www.openvas.org
VCS: https://github.com/greenbone/gvm-libs

#Source-url: https://github.com/greenbone/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch0: fix-build-arch-x32.patch
Patch1: fix-release-build.patch
Patch2: fix-linking-shared-lib.patch

BuildRequires: cmake
BuildRequires: libcjson-devel
BuildRequires: libcurl-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgio-devel
BuildRequires: libgnutls-devel
BuildRequires: libgpgme-devel
BuildRequires: libhiredis-devel
BuildRequires: libnet2-devel
BuildRequires: libpaho-mqtt-devel
BuildRequires: libpcap-devel
BuildRequires: libssh-devel
BuildRequires: libuuid-devel
BuildRequires: libxml2-devel
BuildRequires: zlib-devel

%description
The support libraries for the Greenbone Vulnerability Management
framework.

%package -n libgvm_base%sover
Summary: Support libraries for GVM
Group: System/Libraries

%description -n libgvm_base%sover
The support libraries for the Greenbone Vulnerability Management
framework.

%package -n libgvm_base-devel
Summary: Development files for the GVM base library
Group: Development/C
Requires: libgvm_base%sover = %EVR

%description -n libgvm_base-devel
The support libraries for the Greenbone Vulnerability Management
framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_base.

%package -n libgvm_gmp%sover
Summary: Support libraries for GVM
Group: System/Libraries

%description -n libgvm_gmp%sover
The support libraries for the Greenbone Vulnerability Management
framework.

%package -n libgvm_gmp-devel
Summary: Development files for the GVM gmp library
Group: Development/C
Requires: libgvm_gmp%sover = %EVR

%description -n libgvm_gmp-devel
The support libraries for the Greenbone Vulnerability Management
framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_gmp.

%package -n libgvm_osp%sover
Summary: Support libraries for GVM
Group: System/Libraries

%description -n libgvm_osp%sover
The support libraries for the Greenbone Vulnerability Management
framework.

%package -n libgvm_osp-devel
Summary: Development files for the GVM osp library
Group: Development/C
Requires: libgvm_osp%sover = %EVR

%description -n libgvm_osp-devel
The support libraries for the Greenbone Vulnerability Management
framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_osp.

%package -n libgvm_util%sover
Summary: Support libraries for GVM
Group: System/Libraries

%description -n libgvm_util%sover
The support libraries for the Greenbone Vulnerability Management
framework.

%package -n libgvm_util-devel
Summary: Development files for the GVM util library
Group: Development/C
Requires: libgvm_util%sover = %EVR
Requires: libpaho-mqtt-devel

%description -n libgvm_util-devel
The support libraries for the Greenbone Vulnerability Management
framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_util.

%package -n libgvm_boreas%sover
Summary: Support libraries for the GVM boreas library
Group: System/Libraries

%description -n libgvm_boreas%sover
The support libraries for the Greenbone Vulnerability Management
framework.

%package -n libgvm_boreas-devel
Summary: Development files for the GVM boreas library
Group: Development/C
Requires: libgvm_boreas%sover = %EVR

%description -n libgvm_boreas-devel
The support libraries for the Greenbone Vulnerability Management
framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_boreas.

%package -n libgvm_openvasd%sover
Summary: Greenbone Vulnerability Management Library openvasd
Group: System/Libraries

%description -n libgvm_openvasd%sover
%summary

%package -n libgvm_openvasd-devel
Summary: Development files for the GVM openvasd library
Group: Development/C
Requires: libgvm_openvasd%sover = %EVR

%description -n libgvm_openvasd-devel
%summary

%package -n libgvm_agent_controller%sover
Summary: Greenbone Vulnerability Management Library agent_controller
Group: System/Libraries

%description -n libgvm_agent_controller%sover
%summary

%package -n libgvm_agent_controller-devel
Summary: Development files for the GVM agent_controller library
Group: Development/C
Requires: libgvm_agent_controller%sover = %EVR

%description -n libgvm_agent_controller-devel
%summary

%package -n libgvm_http%sover
Summary: Greenbone Vulnerability Management Library HTTP
Group: System/Libraries

%description -n libgvm_http%sover
%summary

%package -n libgvm_http-devel
Summary: Development files for the GVM HTTP library
Group: Development/C
Requires: libgvm_http%sover = %EVR

%description -n libgvm_http-devel
%summary

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DSYSCONFDIR=%_sysconfdir \
    -DLOCALSTATEDIR=%_var \
    -DBUILD_ARCH=%_arch \
    -DCMAKE_C_FLAGS:STRING="%optflags -Wno-error=discarded-qualifiers"
%cmake_build

%install
%cmake_install

%files
%doc README.md

%files -n libgvm_base%sover
%_libdir/libgvm_base.so.%{sover}*

%files -n libgvm_gmp%sover
%_libdir/libgvm_gmp.so.%{sover}*

%files -n libgvm_osp%sover
%_libdir/libgvm_osp.so.%{sover}*

%files -n libgvm_util%sover
%_libdir/libgvm_util.so.%{sover}*

%files -n libgvm_boreas%sover
%_libdir/libgvm_boreas.so.%{sover}*

%files -n libgvm_openvasd%sover
%_libdir/libgvm_openvasd.so.%{sover}*

%files -n libgvm_agent_controller%sover
%_libdir/libgvm_agent_controller.so.%{sover}*

%files -n libgvm_http%sover
%_libdir/libgvm_http.so.%{sover}*

%files -n libgvm_base-devel
%dir %_includedir/gvm
%dir %_includedir/gvm/base
%_includedir/gvm/base/*.h
%_libdir/libgvm_base.so
%_pkgconfigdir/libgvm_base.pc

%files -n libgvm_gmp-devel
%dir %_includedir/gvm
%dir %_includedir/gvm/gmp
%_includedir/gvm/gmp/gmp.h
%_libdir/libgvm_gmp.so
%_pkgconfigdir/libgvm_gmp.pc

%files -n libgvm_osp-devel
%dir %_includedir/gvm
%dir %_includedir/gvm/osp
%_includedir/gvm/osp/osp.h
%_libdir/libgvm_osp.so
%_pkgconfigdir/libgvm_osp.pc

%files -n libgvm_util-devel
%dir %_includedir/gvm
%dir %_includedir/gvm/util
%_includedir/gvm/util/*.h
%_libdir/libgvm_util.so
%_pkgconfigdir/libgvm_util.pc

%files -n libgvm_boreas-devel
%dir %_includedir/gvm
%dir %_includedir/gvm/boreas
%_includedir/gvm/boreas/*.h
%_libdir/libgvm_boreas.so
%_pkgconfigdir/libgvm_boreas.pc

%files -n libgvm_openvasd-devel
%dir %_includedir/gvm
%dir %_includedir/gvm/openvasd
%_includedir/gvm/openvasd/openvasd.h
%_libdir/libgvm_openvasd.so
%_pkgconfigdir/libgvm_openvasd.pc

%files -n libgvm_agent_controller-devel
%dir %_includedir/gvm
%dir %_includedir/gvm/agent_controller
%_includedir/gvm/agent_controller/agent_controller.h
%_libdir/libgvm_agent_controller.so
%_pkgconfigdir/libgvm_agent_controller.pc

%files -n libgvm_http-devel
%dir %_includedir/gvm
%dir %_includedir/gvm/http
%_includedir/gvm/http/httputils.h
%_libdir/libgvm_http.so
%_pkgconfigdir/libgvm_http.pc

%changelog
* Mon Jun 16 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 22.22.0-alt1
- new version

* Mon Feb 17 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 22.18.0-alt1
- new version

* Wed Apr 03 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 22.9.0-alt1
- Initial build for ALT Linux
