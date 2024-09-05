%define _sysusersdir %_prefix/lib/sysusers.d

%def_with cmake

Name: deepin-anything
Version: 6.1.9
Release: alt1

Summary: The lightning-fast filename search for Deepin

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-anything

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-macros-dqt5
BuildRequires: glib2-devel libdtkcore-devel libmount-devel libnl-devel libpcre-devel udisks2-qt5-devel
%if_with cmake
BuildRequires: cmake rpm-build-ninja
%endif

%description
%summary.
It is provides offline search functions.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name
This packages provides libraries for %name.

%package devel
Summary: Development package for %name
Group: Development/Other

%description devel
This package provides header files and libraries for %name.

%prep
%setup
patch -p1 > archlinux/0001-linux-5.6.patch
sed -i 's|/usr/lib/$(DEB_HOST_MULTIARCH)|%_libdir|; s|/usr/lib/modules-load.d|%_sysconfdir/modules-load.d|' \
  src/Makefile
sed -i 's|#include <pcre.h>|#include <pcre/pcre.h>|' \
  src/library/src/fs_buf.c
sed -i 's|/usr/bin/env python|%__python3|' \
  src/tools/calc_index.py \
  src/tools/primes.py
# cmake
sed -i 's|/usr/lib/modules-load.d|%_sysconfdir/modules-load.d|' \
  src/kernelmod/CMakeLists.txt
sed -i 's|/lib|/%_lib|' \
  examples/deepin-anything-monitor/src/CMakeLists.txt
# syntax
mv -f "src/library/inc/resourceutil .h" "src/library/inc/resourceutil.h"
sed -i 's|resourceutil .h|resourceutil.h|' \
  src/library/src/resourceutil.c \
  src/server/backend/lib/lftmanager.cpp
# fix pkgconfig files
sed -i -e 's|${prefix}/lib/@HOST_MULTIARCH@|%_libdir|; s|libudisks2-qt5|udisks2-qt5|; s|libmount|mount|; s|libpcre3-1|libpcre|; s|libnl-genl-3|libnl-genl-3.0|;' \
  src/server/backend/deepin-anything-server-lib.pc.in

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
%if_with cmake
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
#
cmake --build %_cmake__builddir -j%__nprocs
%else
%make VERSION=%version
%endif

%install
%if_with cmake
%cmake_install
%else
%makeinstall_std
%endif
mv -f %buildroot%_sysconfdir/dbus-1/system.d %buildroot%_datadir/dbus-1/system.d
install -Dm644 archlinux/deepin-anything-server.sysusers %buildroot%_sysusersdir/deepin-anything-server.conf
rm -rf %buildroot/usr/src/deepin-anything-0.0/

%files
%doc README.md LICENSE CHANGELOG.md
%_bindir/deepin-anything-server
%_datadir/dbus-1/system.d/com.deepin.anything.conf
%_datadir/dbus-1/interfaces/com.deepin.anything.xml
%_sysusersdir/*.conf
%_sysconfdir/modules-load.d/anything.conf

%files -n lib%name
%_libdir/libanything.so.*
%_libdir/libdeepin-anything-server-lib.so.*

%files devel
%_libdir/libanything.so
%_libdir/libdeepin-anything-server-lib.so
%dir %_includedir/%{name}*/
%dir %_includedir/%name/index/
%_includedir/%{name}*/*.h
%_includedir/%name/index/*.h
%_pkgconfigdir/deepin-anything-server-lib.pc

%changelog
* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 6.1.9-alt1
- New version 6.1.9.
- Built via separate qt5 instead system (ALT #48138).

* Fri Nov 17 2023 Leontiy Volodin <lvol@altlinux.org> 6.1.5-alt1
- New version 6.1.5.
- Fixed summary and description.
- Cleanup BRs.

* Tue Apr 04 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.4-alt1
- New version 6.0.4.

* Thu Dec 29 2022 Leontiy Volodin <lvol@altlinux.org> 6.0.3-alt1
- New version (6.0.3).

* Wed Oct 05 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.18-alt1
- New version (5.0.18).

* Tue Aug 16 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.13-alt2
- Changed default paths.

* Fri Feb 25 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.13-alt1
- New version (5.0.13).

* Mon May 31 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.9-alt1
- New version (5.0.9) with rpmgs script.

* Mon Feb 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.7-alt1
- New version (5.0.7) with rpmgs script.

* Tue Sep 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.1-alt1
- Initial build for ALT Sisyphus (thanks archlinux for the patch).
