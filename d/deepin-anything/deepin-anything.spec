%define _sysusersdir %_prefix/lib/sysusers.d

Name: deepin-anything
Version: 7.0.5
Release: alt1

Summary: The lightning-fast filename search for Deepin

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-anything
Vcs: git://github.com/linuxdeepin/deepin-anything.git

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-macros-dqt5 rpm-build-ninja rpm-build-kernel
BuildRequires: cmake glib2-devel libdtkcore-devel libmount-devel libnl-devel libpcre-devel udisks2-qt5-devel boost-devel libspdlog-devel liblucene++-devel

%description
%summary.
It is provides offline search functions.

%package -n kernel-source-%name
Summary: Kernel source for %name module
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
This is the source of the kernel %name module.

%prep
%setup
# cmake
sed -i 's|stdc++fs|stdc++|' \
  src/server/CMakeLists.txt
sed -i 's|/usr/src/${package_name}|/usr/src/kernel/sources/${package_name}|' \
  src/kernelmod/CMakeLists.txt
sed -i 's|/usr/lib/modules-load.d|%_sysconfdir/modules-load.d|' \
  src/kernelmod/CMakeLists.txt
sed -i 's|/lib|/%_lib|' \
  examples/deepin-anything-monitor/src/CMakeLists.txt
# fix pkgconfig files
sed -i -e 's|${prefix}/lib/@HOST_MULTIARCH@|%_libdir|; s|libnl-genl-3|libnl-genl-3.0|;' \
  src/server/deepin-anything-server.pc.in

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install
install -Dm644 archlinux/deepin-anything-server.sysusers %buildroot%_sysusersdir/deepin-anything-server.conf
cd %kernel_srcdir
tar -cJhf %name-0.0.tar.xz %name-0.0/
rm -rf %name-0.0/

%files
%doc README.md LICENSE CHANGELOG.md
%_bindir/deepin-anything-server
%_sysusersdir/*.conf
%_sysconfdir/modules-load.d/anything.conf

%files -n kernel-source-%name
%_usrsrc/kernel

%changelog
* Fri Jan 17 2025 Leontiy Volodin <lvol@altlinux.org> 7.0.5-alt1
- New version 7.0.5.
- Added vcs tag.
- Packaged sources for the kernel module.

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
