Name: libdxflib
Version: 3.26.4
Release: alt1
Summary: A C++ library for reading and writing DXF files

License: GPLv2+
Group: Development/C++
Url: http://www.ribbonsoft.com/en/90-dxflib
Packager: Anton Midyukov <antohami@altlinux.org>

# Source-url: https://qcad.org/archives/dxflib/dxflib-%version-src.tar.gz
Source: dxflib-%version.tar

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel

%description
dxflib is an open source C++ library mainly for parsing DXF files.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
dxflib is an open source C++ library mainly for parsing DXF files.

The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n dxflib-%version
# Build as a shared library
%__subst 's/CONFIG += staticlib/CONFIG += shared/' dxflib.pro

%build
# https://github.com/qcad/qcad/pull/16
%qmake_qt5 \
  VERSION=%version \
  CONFIG-=qt

%make_build

%install
install -d -m 0755 %buildroot%_libdir
cp -pr %name.so* %buildroot%_libdir

install -d -m 0755 %buildroot%_includedir/dxflib
cp -pr src/*.h %buildroot%_includedir/dxflib

# Generate pkgconfig file
install -d -m 0755 %buildroot%_pkgconfigdir
cat << 'EOF' > %buildroot%_pkgconfigdir/dxflib.pc
prefix=%prefix
exec_prefix=%_exec_prefix
libdir=%_libdir
includedir=%_includedir

Name: dxflib
Description: A C++ library for reading and writing DXF files
Version: %version
Libs: -L${libdir} -ldxflib
Cflags: -I${includedir}/dxflib
EOF

%files
%doc gpl-2.0greater.txt dxflib_commercial_license.txt
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/dxflib.pc

%changelog
* Wed Dec 22 2021 Anton Midyukov <antohami@altlinux.org> 3.26.4-alt1
- new version (3.26.4) with rpmgs script
- build with qt5

* Sun Oct 20 2019 Anton Midyukov <antohami@altlinux.org> 3.17.0-alt1
- initial build for ALT Sisyphus
