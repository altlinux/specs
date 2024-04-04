%define _unpackaged_files_terminate_build 1
%define sover 22

Name: gvm-libs
Version: 22.9.0
Release: alt1

Summary: Support libraries for Greenbone Vulnerability Management Solution and OpenVAS
License: GPL-2.0-or-later
Group: System/Libraries
Url: http://www.openvas.org
VCS: https://github.com/greenbone/gvm-libs

#Source-url: https://github.com/greenbone/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch0: fix-build-arch-x32.patch
Patch1: fix-release-build.patch
Patch2: fix-linking-shared-lib.patch

BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0) >= 2.42
BuildRequires: pkgconfig(zlib) >= 1.2.8
BuildRequires: libgpgme-devel >= 1.7.0
BuildRequires: pkgconfig(gnutls) >= 3.2.15
BuildRequires: pkgconfig(uuid) >= 2.25.0
BuildRequires: pkgconfig(libssh) >= 0.6.0
BuildRequires: pkgconfig(hiredis) >= 0.10.1
BuildRequires: pkgconfig(libxml-2.0) >= 2.0
BuildRequires: libnet2-devel
BuildRequires: libpcap-devel
BuildRequires: libgcrypt-devel
BuildRequires: libpaho-mqtt-devel >= 1.3.0

%description
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_base%sover
Summary: Support libraries for GVM
Group: System/Libraries

%description -n libgvm_base%sover
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_base-devel
Summary: Development files for the GVM base library
Group: Development/C
Requires: libgvm_base%sover = %EVR

%description -n libgvm_base-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_base.

%package -n libgvm_gmp%sover
Summary: Support libraries for GVM
Group: System/Libraries

%description -n libgvm_gmp%sover
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_gmp-devel
Summary: Development files for the GVM gmp library
Group: Development/C
Requires: libgvm_gmp%sover = %EVR

%description -n libgvm_gmp-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_gmp.

%package -n libgvm_osp%sover
Summary: Support libraries for GVM
Group: System/Libraries

%description -n libgvm_osp%sover
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_osp-devel
Summary: Development files for the GVM osp library
Group: Development/C
Requires: libgvm_osp%sover = %EVR

%description -n libgvm_osp-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_osp.

%package -n libgvm_util%sover
Summary: Support libraries for GVM
Group: System/Libraries

%description -n libgvm_util%sover
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_util-devel
Summary: Development files for the GVM util library
Group: Development/C
Requires: libgvm_util%sover = %EVR
Requires: libpaho-mqtt-devel

%description -n libgvm_util-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_util.

%package -n libgvm_boreas%sover
Summary: Support libraries for the GVM boreas library
Group: System/Libraries

%description -n libgvm_boreas%sover
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libgvm_boreas-devel
Summary: Development files for the GVM boreas library
Group: Development/C
Requires: libgvm_boreas%sover = %EVR

%description -n libgvm_boreas-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libgvm_boreas.

%prep
%setup
%patch0 -p2
%patch1 -p2
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
%doc CHANGELOG.md README.md

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

%files -n libgvm_base-devel
%dir %_includedir/gvm
%_includedir/gvm/base
%_libdir/libgvm_base.so
%_pkgconfigdir/libgvm_base.pc

%files -n libgvm_gmp-devel
%dir %_includedir/gvm
%_includedir/gvm/gmp
%_libdir/libgvm_gmp.so
%_pkgconfigdir/libgvm_gmp.pc

%files -n libgvm_osp-devel
%dir %_includedir/gvm
%_includedir/gvm/osp/
%_libdir/libgvm_osp.so
%_pkgconfigdir/libgvm_osp.pc

%files -n libgvm_util-devel
%dir %_includedir/gvm
%_includedir/gvm/util
%_libdir/libgvm_util.so
%_pkgconfigdir/libgvm_util.pc

%files -n libgvm_boreas-devel
%dir %_includedir/gvm
%_includedir/gvm/boreas
%_libdir/libgvm_boreas.so
%_pkgconfigdir/libgvm_boreas.pc

%changelog
* Wed Apr 03 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 22.9.0-alt1
- Initial build for ALT Linux
