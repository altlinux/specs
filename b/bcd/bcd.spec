%global commit0 d94c9fa77c11afe7d04670d92b3930c417e19f4b
%global shortcommit0 %(c=%commit0; echo ${c:0:7})
%global date0 20180610
%global optflags_lto %nil
%global soname 0
%global gcc_ver 14

%ifarch x86_64 aarch64
%def_with cuda
%filter_from_requires /libcudart\.so\.12/d
%endif

Name: bcd
Version: 1.1
Release: alt5.%{?date0}git%{?shortcommit0}
Summary: Bayesian Collaborative Denoiser for Monte-Carlo Rendering
Group: Graphics
# BSD: main program
# AGPLv3+: src/io/exr
License: BSD AND AGPL-3.0+
Url: https://github.com/superboubek/bcd
Source0: %url/archive/%commit0/%name-%shortcommit0.tar
# Many patches are tight to upstream accepting building shared
# and removing bundled dependencies
# https://github.com/superboubek/bcd/issues/12
# don't use bundled deps
Patch0: bcd-nodeps.patch
# Missing includes
# https://github.com/superboubek/bcd/pull/11
Patch1: bcd-gcc.patch
# Use system eigen3
Patch2: bcd-eigen3.patch
# Turn into a shared library forging SONAME (no ABI stability expected)
Patch3: bcd-links.patch
# Remove cuda arch - not supported in current nvcc
Patch4: bcd-cuda.patch
# Use system json
Patch5: bcd-json.patch
# TODO
# BCD calls exit
#https://github.com/superboubek/bcd/issues/13

# Eigen 5.X.X requires C++14
# https://gitlab.com/libeigen/eigen/-/releases/5.0.0
Patch6: bcd-cxx14.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: make
BuildRequires: gcc-c++ pkgconfig

BuildRequires: openexr-devel
BuildRequires: eigen3
BuildRequires: nlohmann-json-devel
BuildRequires: zlib-devel
BuildRequires: libgomp-devel
%if_with cuda
BuildRequires: nvidia-cuda-devel
BuildRequires: gcc%{gcc_ver}-c++ libgomp%{gcc_ver}-devel
%endif

%description
BCD allows to denoise images rendered with Monte Carlo path tracing and
provided in the form of their samples statistics (average, distribution
and covariance of per-pixel color samples). BCD can run in CPU (e.g.,
renderfarm) or GPU (e.g., desktop) mode. It can be integrated as a library
to any Monte Carlo renderer, using the provided sample accumulator to
interface the Monte Carlo simulation with the BCD internals, and comes
with a graphics user interface for designing interactively the denoising
parameters, which can be saved in JSON format and later reused in batch.

BCD has been designed for easy integration and low invasiveness in the
host renderer, in a high spp context (production rendering). There are
at least three ways to integrate BCD in a rendering pipeline, by either:

* Dumping all samples in a raw file, using the raw2bcd tool to generate
the rendering statistics from this file and then running the BCD using
the CLI tool.

* Exporting the mandatory statistics from the rendering loop in EXR
format and running the BCD CLI tool to obtain a denoised image.

* Directly integrating the BCD library into the renderer, using the
sample accumulator to post samples to BCD during the path tracing and
denoising the accumulated values after rendering using the library.

%package -n lib%name%soname
Summary: BCD library
Group: System/Libraries
Provides: lib%name = %EVR

%description -n lib%name%soname
BCD library

%package cli
Summary: Tools for %name
Group: Graphics
Requires: lib%name = %EVR

%description cli
The %name-cli package contains libraries and header files for
developing applications that use %name.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %name-%commit0
%autopatch -p1

%build
%add_optflags -Wno-return-type
export CXXFLAGS="%optflags $(pkg-config --cflags eigen3) -I%_includedir/nlohmann"
export LDFLAGS="$(pkg-config --libs eigen3)"
%{?_with_cuda: export GCC_VERSION=%gcc_ver}
%cmake \
  -Wno-dev \
  -DBCD_BUILD_GUI=OFF \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
  -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" \
  -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" \
  %{?_with_cuda: \
   -DCUDA_TOOLKIT_ROOT_DIR=%prefix \
   -DCUDA_NVCC_FLAGS="--std c++14" \
   -DCUDA_USE_STATIC_CUDA_RUNTIME=OFF \
  } \
  %{!?_with_cuda:-DBCD_USE_CUDA=OFF}
  %nil
%cmake_build

%install
%cmake_install

%if "%_lib" == "lib64"
mv %buildroot%prefix/lib \
  %buildroot%_libdir
%endif

mkdir -p %buildroot%_includedir
cp -pr include/* %buildroot%_includedir

%files -n lib%name%soname
%doc README.md LICENSE.txt
%_libdir/*.so.0*

%files cli
%_bindir/bcd-cli
%_bindir/bcd-raw-converter

%files devel
%_includedir/bcd
%_libdir/*.so

%changelog
* Thu Apr 23 2026 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt5.20180610gitd94c9fa
- gcc: downgrade to 14 due cuda requires.

* Wed Jan 07 2026 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt4.20180610gitd94c9fa
- Fix FTBFS with new OpenEXR.
- aarch64: enable cuda.

* Sat Oct 25 2025 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt3.20180610gitd94c9fa
- Use -std=c++14 for new eigen3 and cuda (to fix FTBFS).

* Mon May 12 2025 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt2.20180610gitd94c9fa
- BR: simplify for new cuda.

* Sun Apr 13 2025 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt1.20180610gitd94c9fa
- Initial build for ALTLinux
- Based on bcd-1.1-16.20180610gitd94c9fa.fc42.src.rpm

