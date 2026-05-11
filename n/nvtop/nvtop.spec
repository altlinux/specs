%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type
%define _unpackaged_files_terminate_build 1
%define git %nil

%def_enable tests

Name: nvtop
Version: 3.3.2
Release: alt3

Summary: (h)top like task monitor for AMD, Intel and Nvidia GPUs
Group: Monitoring
License: GPLv3
Url: https://github.com/Syllo/nvtop
Vcs: https://github.com/Syllo/nvtop

Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libsystemd-devel libudev-devel libdrm-devel libncurses-devel
%if_enabled tests
BuildRequires: libgtest-devel ctest
%endif

%description
Nvtop stands for Neat Videocard TOP, a (h)top like task monitor for AMD, Intel
and NVIDIA GPUs. It can handle multiple GPUs and print information about them in
a htop familiar way.

%prep
%setup
%patch -p1

%build
%_cmake \
	-DNVIDIA_SUPPORT=ON \
	-DAMDGPU_SUPPORT=ON \
%if_enabled tests
	-DBUILD_TESTING=ON \
%endif
	-DINTEL_SUPPORT=ON
%cmake_build

%install
%cmake_install

%if_enabled tests
%check
pushd %_cmake__builddir
make test
popd
%endif

%files
%doc README.* COPYING
%_bindir/%name
%_man1dir/%name.*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop
%_datadir/metainfo/io.github.syllo.%name.metainfo.xml

%changelog
* Mon May 11 2026 L.A. Kostis <lakostis@altlinux.ru> 3.3.2-alt3
- Drop libnvidia-ml requirement (closes #59079).

* Tue Mar 03 2026 L.A. Kostis <lakostis@altlinux.ru> 3.3.2-alt2
- Enable debuginfo.
- Enable tests.

* Mon Mar 02 2026 L.A. Kostis <lakostis@altlinux.ru> 3.3.2-alt1
- 3.3.2.

* Mon Jan 19 2026 L.A. Kostis <lakostis@altlinux.ru> 3.3.1-alt1
- 3.3.1.

* Sat Apr 19 2025 L.A. Kostis <lakostis@altlinux.ru> 3.2.0-alt1
- 3.2.0.

* Tue Mar 05 2024 L.A. Kostis <lakostis@altlinux.ru> 3.1.0-alt1
- 3.1.0.

* Thu Jun 15 2023 L.A. Kostis <lakostis@altlinux.ru> 3.0.2-alt1
- 3.0.2.

* Wed May 24 2023 L.A. Kostis <lakostis@altlinux.ru> 3.0.1-alt3.g04721e3
- Updated to GIT 04721e3:
  + MSM/Adreno support
  + fix AMD gpu tx/rx readings.

* Thu May 04 2023 L.A. Kostis <lakostis@altlinux.ru> 3.0.1-alt2
- Fix requires for nvidia.

* Wed May 03 2023 L.A. Kostis <lakostis@altlinux.ru> 3.0.1-alt1
- Initial build for ALTLinux.
