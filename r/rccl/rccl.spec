%define build_type RelWithDebInfo
%define optflags_lto %nil
%define soname 1
%def_with msccl
%define rocm_version 6.1.2

Name: rccl
Version: 2.18.6
Release: alt0.1
License: BSD-3-Clause-Clear/Apache-2.0/MIT
Summary: ROCm Communication Collectives Library
Url: https://github.com/ROCm/rcclr
Group: System/Libraries

Source: %name-%version.tar

BuildRequires(pre): cmake rocm-cmake = %rocm_version /proc
BuildRequires: llvm-rocm-devel = %rocm_version clang-rocm-devel = %rocm_version clang-rocm-tools = %rocm_version
BuildRequires: libstdc++-devel
BuildRequires: hip-devel = %rocm_version rocm-comgr-devel = %rocm_version hsa-rocr-devel = %rocm_version
BuildRequires: hipify-clang = %rocm_version librocm-smi = %rocm_version librocm-smi-devel = %rocm_version

ExclusiveArch: x86_64 ppc64le aarch64

%description
RCCL (pronounced "Rickle") is a stand-alone library of standard collective
communication routines for GPUs, implementing all-reduce, all-gather, reduce,
broadcast, reduce-scatter, gather, scatter, and all-to-all. There is also
initial support for direct GPU-to-GPU send and receive operations.

It has been optimized to achieve high bandwidth on platforms using PCIe, xGMI
as well as networking using InfiniBand Verbs or TCP/IP sockets. RCCL supports
an arbitrary number of GPUs installed in a single node or multiple nodes, and
can be used in either single- or multi-process (e.g., MPI) applications.


%package -n lib%{name}%{soname}
Summary: ROCm Communication Collectives Library
Group: System/Libraries
Provides: %name = %EVR

%description -n lib%{name}%{soname}
RCCL (pronounced "Rickle") is a stand-alone library of standard collective
communication routines for GPUs, implementing all-reduce, all-gather, reduce,
broadcast, reduce-scatter, gather, scatter, and all-to-all. There is also
initial support for direct GPU-to-GPU send and receive operations.

It has been optimized to achieve high bandwidth on platforms using PCIe, xGMI
as well as networking using InfiniBand Verbs or TCP/IP sockets. RCCL supports
an arbitrary number of GPUs installed in a single node or multiple nodes, and
can be used in either single- or multi-process (e.g., MPI) applications.

%package -n lib%{name}-devel
Summary: %name development headers and library
Group: Development/C++
Provides: %{name}-devel = %EVR

%description -n lib%{name}-devel
%name development headers and library

%prep
%setup
subst 's,cat ${ROCM_PATH}/.info/version,echo %rocm_version,' CMakeLists.txt

%build
export ALTWRAP_LLVM_VERSION=rocm
%ifarch aarch64
mkdir -p /tmp/bits
cat >/tmp/bits/math-vector.h <<EOF
#include <bits/libm-simd-decl-stubs.h>
#undef __ADVSIMD_VEC_MATH_SUPPORTED
#undef __SVE_VEC_MATH_SUPPORTED
EOF
%endif
%cmake \
    -Wno-dev \
    -DROCM_PATH=%_prefix \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
%ifarch aarch64
    -DCMAKE_CXX_FLAGS="%optflags -isystem /tmp" \
%endif
%if_with msccl
    -DENABLE_MSCCL_KERNEL=ON \
%else
    -DENABLE_MSCCL_KERNEL=OFF \
%endif
    %nil
%cmake_build

%install
%cmake_install
# compat install
rm -rf %buildroot%_prefix/%name
# we list license anyway
rm -rf %buildroot%_docdir/%name

%files -n lib%{name}%{soname}
%doc README.md LICENSE.txt NOTICES.txt CHANGELOG.md
%_libdir/lib%{name}.so.%{soname}*

%files -n lib%{name}-devel
%_includedir/%name
%_libdir/lib%{name}.so
%_libdir/cmake/%name
%if_with msccl
%_datadir/%name
%endif

%changelog
* Mon Jul 08 2024 L.A. Kostis <lakostis@altlinux.ru> 2.18.6-alt0.1
- initial build for ALTLinux.


