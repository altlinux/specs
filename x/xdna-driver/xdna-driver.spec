%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# aiebu ships a static library; keep machine code in it, not just GIMPLE.
%define optflags_lto -flto=auto -ffat-lto-objects

%define soversion 2

Name: xdna-driver
Version: 2.21.75
Release: alt1

Summary: AMD XDNA NPU userspace stack (XRT runtime and SHIM library)
License: Apache-2.0 MIT
Group: System/Kernel and hardware
Url: https://github.com/amd/xdna-driver
Requires: xrt = %EVR
Requires: xrt-plugin-amdxdna = %EVR
Vcs: https://github.com/amd/xdna-driver

ExclusiveArch: x86_64

Source: %name-%version.tar
Patch0: %name-%version-submodules.patch
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ninja-build git-core
BuildRequires: boost-devel-headers boost-filesystem-devel boost-program_options-devel
BuildRequires: boost-interprocess-devel boost-asio-devel
BuildRequires: libdrm-devel
BuildRequires: ocl-icd-devel opencl-headers
BuildRequires: rapidjson-devel libssl-devel libuuid-devel
BuildRequires: libncurses-devel systemtap-sdt-devel
BuildRequires: python3-dev pybind11-devel

%description
Userspace stack for AMD XDNA NPUs (Ryzen AI: Phoenix, Hawk Point,
Strix Point, Krackan Point): the XRT (Xilinx Runtime) base libraries
and tools (xrt-smi) plus the XDNA SHIM plugin library
(libxrt_driver_xdna) which connects XRT to the in-kernel amdxdna
driver.

The kernel module amdxdna.ko is provided by the kernel itself
(CONFIG_DRM_ACCEL_AMDXDNA, Linux >= 6.14) and the NPU firmware
is provided by the firmware-linux package.

This is a metapackage pulling in the runtime and the NPU plugin.

%package -n libxrt%soversion
Summary: XRT (Xilinx Runtime) core shared libraries
Group: System/Libraries

%description -n libxrt%soversion
Core shared libraries of the Xilinx Runtime (XRT):
libxrt_core, libxrt_coreutil, libxdp_core and the XDP module plugins.

%package -n xrt
Summary: XRT (Xilinx Runtime) command line tools
Group: System/Kernel and hardware
Requires: libxrt%soversion = %EVR

%description -n xrt
Command line tools of the Xilinx Runtime (XRT): xrt-smi (system
management interface for AMD XDNA NPU devices), xclbinutil and
xrt-runner. Validation images are not included.

%package -n xrt-plugin-amdxdna
Summary: XRT SHIM plugin for AMD XDNA NPUs
Group: System/Libraries
Requires: libxrt%soversion = %EVR
Requires: firmware-linux

%description -n xrt-plugin-amdxdna
SHIM plugin library (libxrt_driver_xdna) connecting the Xilinx
Runtime to the in-kernel amdxdna driver of AMD XDNA NPUs (Ryzen AI).

The package also installs a security limits drop-in raising the
memlock limit, which is required to allocate buffer objects on the
NPU (re-login or reboot is needed for it to take effect).

%package -n libxrt-devel
Summary: Development files for XRT (Xilinx Runtime)
Group: Development/C++
Requires: libxrt%soversion = %EVR
Requires: libuuid-devel
Requires: boost-devel-headers

%description -n libxrt-devel
Headers, pkg-config and CMake files for developing applications
against the Xilinx Runtime (XRT).

%package -n libxrt-devel-static
Summary: Static XRT (Xilinx Runtime) libraries
Group: Development/C++
Requires: libxrt-devel = %EVR

%description -n libxrt-devel-static
Static libraries of the Xilinx Runtime (XRT).

%package -n python3-module-pyxrt
Summary: Python 3 bindings for XRT (Xilinx Runtime)
Group: Development/Python3
Requires: libxrt%soversion = %EVR

%description -n python3-module-pyxrt
Python 3 bindings (pyxrt) for the Xilinx Runtime (XRT).

%prep
%setup
%autopatch -p1
cp xrt/src/runtime_src/core/common/elf/LICENSE.txt LICENSE.ELFIO
cp xrt/src/runtime_src/core/common/gsl/LICENSE LICENSE.GSL

%build
%cmake -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DXRT_YOCTO=ON \
  -DAIEBU_BUILD_UTILS=OFF \
  -DXDNA_INSTALL_VALIDATION_DATA=OFF \
  -DSKIP_KMOD=ON
%cmake_build

%install
%cmake_install
rm -rf %buildroot/bins
rm -f %buildroot%_sysconfdir/OpenCL/vendors/xilinx.icd
mkdir -p %buildroot%_datadir/bash-completion/completions
mv %buildroot%_datadir/completions/xbutil-bash-completion \
  %buildroot%_datadir/bash-completion/completions/xrt-smi
rm -rf %buildroot%_datadir/completions
rm -rf %buildroot%_datadir/cmake/AIEBU
rm -f %buildroot%_libdir/libaiebu.a
mkdir -p %buildroot%_sysconfdir/security/limits.d
cat > %buildroot%_sysconfdir/security/limits.d/99-amdxdna.conf <<'EOF'
@render soft memlock unlimited
@render hard memlock unlimited
EOF

%files
%doc README.md

%files -n libxrt%soversion
%doc xrt/LICENSE LICENSE.ELFIO LICENSE.GSL
%_libdir/libxrt_core.so.%{soversion}*
%_libdir/libxrt_coreutil.so.%{soversion}*
%_libdir/libxdp_core.so.%{soversion}*
%_libdir/xrt/

%files -n xrt
%doc xrt/LICENSE
%_bindir/xrt-smi
%_bindir/xclbinutil
%_bindir/xrt-runner
%_datadir/bash-completion/completions/xrt-smi
%_datadir/xrt/
%_datadir/doc/xrt/

%files -n xrt-plugin-amdxdna
%doc xrt/LICENSE
%_libdir/libxrt_driver_xdna.so.%{soversion}*
%config(noreplace) %_sysconfdir/security/limits.d/99-amdxdna.conf

%files -n libxrt-devel
%doc xrt/LICENSE
%_includedir/xrt/
%_pkgconfigdir/xrt.pc
%_libdir/libxrt_core.so
%_libdir/libxrt_coreutil.so
%_datadir/cmake/XRT/

%files -n libxrt-devel-static
%doc xrt/LICENSE LICENSE.ELFIO LICENSE.GSL
%_libdir/libxrt_core.a
%_libdir/libxrt_coreutil.a

%files -n python3-module-pyxrt
%doc xrt/LICENSE
%python3_sitelibdir/pyxrt*.so

%changelog
* Wed Oct 21 2026 Semen Fomchenkov <armatik@altlinux.org> 2.21.75-alt1
- Initial build for ALT Sisyphus.
