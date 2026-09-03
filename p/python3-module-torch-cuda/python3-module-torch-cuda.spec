%define _unpackaged_files_terminate_build 1

%def_with check

%def_with system_onnx
%def_with gloo
%def_with tensorpipe
%def_without mpi
%def_without rocm
%def_with cuda

# NVCC is incompatible with GCC 15, use GCC 14 as host compiler.
%set_gcc_version 14

%global __find_debuginfo_files %nil

%define optflags_lto %nil

Name:    python3-module-torch-cuda
Version: 2.12.0
Release: alt1

Summary: Tensors and dynamic neural networks in Python with strong acceleration support (with CUDA support)
License: BSD-3-Clause
Group:   Development/ML
URL:     https://pytorch.org/
VCS:     https://github.com/pytorch/pytorch.git

Source0: python3-module-torch-cuda-%version.tar
Source1: third_party.tar
Source2: _install_paths.py.in

Patch0: 0001-Disabled-submodule-search.patch
Patch1: 0002-Fixed-system-libs-cmake.patch
Patch2: 0003-Added-support-for-system-installed-cuDNN-Frontend.patch
Patch3: 0004-Used-system-cutlass-instead-of-bundled.patch
Patch4: 0005-Use-system-valgrind-instead-of-bundled.patch
Patch5: 0006-Reenable-half-ops-for-nccl-symm-mem.patch
Patch6: 0007-Used-system-devel-paths.patch

ExclusiveArch: x86_64 aarch64
# Disable python3 autoprovides to avoid duplicate Provides between CPU/CUDA variants.
AutoProv: nopython3

# Drop self requires for torch
%filter_from_requires /python3(torch.*)/d
%filter_from_requires /^libtorch.*\.so/d
%filter_from_requires /^libc10.*\.so/d
%filter_from_requires /^libshm\.so/d

# Drop optional CUDA codegen/tooling Requires.
# Core CUDA support is provided by built C++/CUDA libraries.
%filter_from_requires /python3(cutlass.*)/d
%filter_from_requires /python3(cuda.bindings.driver)/d

# Drop optional integration/export/test Requires.
# They are not needed for core torch import or eager/CUDA runtime.
%filter_from_requires /python3(coremltools.*)/d
%filter_from_requires /python3(expecttest)/d
%filter_from_requires /python3(onnxscript.*)/d
%filter_from_requires /python3(optree.*)/d
%filter_from_requires /python3(pytorch_lightning)/d
%filter_from_requires /python3(tensorboard.*)/d
%filter_from_requires /python3(libfb.py.log)/d


BuildRequires(pre): cmake rpm-build-python3
BuildRequires: gcc%_gcc_version-c++
BuildRequires: ninja-build
BuildRequires: valgrind-devel
BuildRequires: libfmt-devel
BuildRequires: libgomp-devel
BuildRequires: libonnx-devel
BuildRequires: libmpfr-devel
BuildRequires: libgmp-devel
BuildRequires: libfftw3-devel
BuildRequires: eigen3-devel
BuildRequires: liblapack-devel
BuildRequires: libsleef-devel
BuildRequires: FP16-devel
BuildRequires: fxdiv-devel
BuildRequires: libpsimd-devel
BuildRequires: libcpuinfo-devel
BuildRequires: libpthreadpool-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: moodycamel-concurrentqueue-devel
%if_with mpi
BuildRequires: openmpi-devel
%endif
%if_with cuda
BuildRequires: nvidia-cuda-devel
BuildRequires: libcudnn-devel
BuildRequires: libnccl-devel
BuildRequires: nvidia-cuda-devel-static
BuildRequires: cudnn-frontend-devel
BuildRequires: nvidia-cutlass-headers
%endif
BuildRequires: pybind11-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-protobuf
BuildRequires: python3-module-pyyaml
BuildRequires: python3-module-packaging
BuildRequires: python3-module-numpy
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-requests
BuildRequires: python3-module-six
BuildRequires: python3-module-jinja2

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-expecttest
BuildRequires: python3-module-sympy
%endif

Provides:      pytorch
Conflicts:     python3-module-torch-cpu

Requires:      libtorch-cuda = %EVR

%description
%summary.

PyTorch is an optimized tensor library for deep learning using GPUs and CPUs.

%package 	-n libtorch-cuda-devel
Summary: 	Headers, CMake config and link libraries for C++ libtorch (CUDA)
Group: 		Development/ML
Requires: 	libtorch-cuda = %EVR
# Disable python3 autoprovides to avoid duplicate Provides between CPU/CUDA variants.
AutoProv: 	nopython3
Obsoletes: 	python3-module-torch-cuda-devel < %EVR
Conflicts: 	libtorch-cpu-devel

%description 	-n libtorch-cuda-devel
Development files (headers and CMake package configuration) for building
C++ programs and extensions against the CUDA build of libtorch.

%package 	-n libtorch-cuda-cpu
Summary: 	python3-module-torch-cuda shared libraries for CPU
Group: 		System/Libraries
# Disable python3 and lib autoprovides to avoid duplicate Provides between CPU/CUDA variants.
AutoProv: 	nopython3, nolib
Conflicts: 	libtorch-cpu

%description 	-n libtorch-cuda-cpu
CPU PyTorch libraries for system use. Other packages can
link to use python3-module-torch-cuda from C++ or Python extensions.

%package 	-n libtorch-cuda
Summary:  	PyTorch shared libraries with CUDA
Group: 		System/Libraries
# Disable python3 autoprovides to avoid duplicate Provides between CPU/CUDA variants.
AutoProv: 	nopython3
Requires: 	libtorch-cuda-cpu = %EVR

%description 	-n libtorch-cuda
CUDA-enabled python3-module-torch-cuda libraries for system use.
Other packages can link to run GPU-accelerated operations
with python3-module-torch-cuda.

%prep
%setup -a1
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6 -p1

install -pm0644 %SOURCE2 torch/_install_paths.py.in

#Use system fmt

#Try to include fmt before ATen to fix build
sed -i '53a find_package(fmt REQUIRED)' CMakeLists.txt

sed -i -e 's@add_subdirectory(${PROJECT_SOURCE_DIR}/third_party/fmt)@#add_subdirectory(${PROJECT_SOURCE_DIR}/third_party/fmt)@' cmake/Dependencies.cmake
sed -i -e 's@set_target_properties(fmt-header-only PROPERTIES INTERFACE_COMPILE_FEATURES "")@#set_target_properties(fmt-header-only PROPERTIES INTERFACE_COMPILE_FEATURES "")@' cmake/Dependencies.cmake
sed -i '/list(APPEND Caffe2_DEPENDENCY_LIBS fmt::fmt-header-only)/i find_package(fmt REQUIRED)' cmake/Dependencies.cmake

# Fix XNNPACK System Library
sed -i -e 's@if(NOT XNNPACK_LIBRARY or NOT microkernels-prod_LIBRARY)@if(NOT XNNPACK_LIBRARY)@' cmake/Dependencies.cmake

# No third_party FXdiv
sed -i -e 's@if(NOT TARGET fxdiv)@if(MSVC AND USE_XNNPACK)@' caffe2/CMakeLists.txt
sed -i -e 's@TARGET_LINK_LIBRARIES(torch_cpu PRIVATE fxdiv)@#TARGET_LINK_LIBRARIES(torch_cpu PRIVATE fxdiv)@' caffe2/CMakeLists.txt

# Fix installing to /usr/lib64
sed -i -e 's@DESTINATION ${PYTHON_LIB_REL_PATH}@DESTINATION ${CMAKE_INSTALL_PREFIX}/${PYTHON_LIB_REL_PATH}@' caffe2/CMakeLists.txt

# Use system moodycamel-concurrentqueue instead of bundled
sed -i -e 's@${PROJECT_SOURCE_DIR}/third_party/concurrentqueue@/usr/include/concurrentqueue@' cmake/Dependencies.cmake

%build
%add_optflags -Wno-error=maybe-uninitialized
%add_optflags -Wno-error=array-parameter
%add_optflags -I%_builddir/python3-module-torch-cuda-%version/third_party
%add_optflags -I%_includedir/valgrind

export BUILD_CUSTOM_PROTOBUF=OFF
export BUILD_NVFUSER=OFF
export BUILD_SHARED_LIBS=ON
export BUILD_TEST=OFF
export CMAKE_PREFIX_PATH=/usr/lib64/cmake:$CMAKE_PREFIX_PATH
export CMAKE_BUILD_TYPE=RelWithDebInfo
export CMAKE_FIND_PACKAGE_PREFER_CONFIG=ON
export CAFFE2_LINK_LOCAL_PROTOBUF=OFF
export INTERN_BUILD_MOBILE=OFF
export USE_FAKELOWP=OFF
export USE_FBGEMM=OFF
export USE_FLASH_ATTENTION=OFF
export USE_ITT=OFF
export USE_KINETO=OFF
export USE_KLEIDIAI=OFF
export USE_LITE_INTERPRETER_PROFILER=OFF
export USE_LITE_PROTO=OFF
export USE_MAGMA=OFF
export USE_MIMALLOC=OFF
export USE_MEM_EFF_ATTENTION=OFF
export USE_MKLDNN=OFF
export USE_MPI=OFF
export USE_NNPACK=OFF
export USE_NUMPY=ON
export USE_OPENMP=ON
export USE_PYTORCH_QNNPACK=OFF
export USE_SYSTEM_SLEEF=ON
export USE_SYSTEM_EIGEN_INSTALL=ON
export USE_SYSTEM_PYBIND11=ON
export USE_SYSTEM_LIBS=OFF
export USE_SYSTEM_NCCL=OFF
export USE_XNNPACK=OFF
export USE_XPU=OFF
export USE_SYSTEM_PTHREADPOOL=ON
export USE_SYSTEM_CPUINFO=ON
export USE_SYSTEM_FP16=ON
export USE_SYSTEM_FXDIV=ON
export USE_SYSTEM_PSIMD=ON
export USE_SYSTEM_XNNPACK=OFF
export USE_SYSTEM_ONNX=OFF
export USE_DISTRIBUTED=ON
%if_with tensorpipe
export USE_TENSORPIPE=ON
export TP_BUILD_LIBUV=OFF
%endif
%if_with gloo
# Using bundled Gloo implementation.
# Reason: PyTorch depends on CUDA-specific Gloo code (including c10::Half and c10::BFloat16
# support) which is not present in the system Gloo library.
export USE_SYSTEM_GLOO=OFF
export USE_GLOO=ON
%endif
%if_with rocm
export USE_ROCM=ON
export USE_ROCM_CK=OFF
export USE_MAGMA=ON
%endif
%if_with system_onnx
export USE_SYSTEM_ONNX=ON
%endif
%if_with mpi
export USE_MPI=ON
%endif
%if_with cuda
export USE_NCCL=ON
export USE_SYSTEM_NCCL=ON
export NCCL_INCLUDE_DIR="/usr/include/"
export USE_CUDA=ON
export USE_CUDNN=ON
export USE_SYSTEM_NVTX=ON
export CMAKE_CUDA_ARCHITECTURES="50;70;75;80;86;89;90;90a"
%else
export USE_CUDA=OFF
export USE_CUDNN=OFF
%endif
export CMAKE_POLICY_VERSION_MINIMUM=3.5

export NUM_PROC=%__nprocs
[ "$NUM_PROC" -gt 8 ] && NUM_PROC=8
export MAX_JOBS=$NUM_PROC
export CMAKE_BUILD_PARALLEL_LEVEL=$NUM_PROC
export NINJAFLAGS="-j$NUM_PROC -v"
export NINJA_STATUS='[%%f/%%t %%e] '
export TORCH_SYSTEM_INCLUDE_DIR=%_includedir
export TORCH_SYSTEM_CMAKE_PREFIX_PATH=%_datadir/cmake

# --- keepalive ---
{ %pyproject_build; } & build_pid=$!

while kill -0 "$build_pid" 2>/dev/null; do
    echo "torch-cuda: still building... $(date -u +'%%F %%T')" >&2
    sleep 300
done

wait "$build_pid"

%install
%pyproject_install

# Place .so libraries in /usr/lib64 to make them discoverable by system packages
# (such as python3-module-torchvision).
LIBS="libc10.so libc10_cuda.so libtorch_cpu.so libtorch_cuda.so \
      libtorch_cuda_linalg.so libshm.so libtorch.so"

for f in $LIBS; do
    install -Dm755 %buildroot%python3_sitelibdir/torch/lib/$f %buildroot%_libdir/
    rm -f %buildroot%python3_sitelibdir/torch/lib/$f
done

# Expose C++ headers and CMake configs at system paths (Closes: # 58168).

install -d %buildroot%_includedir %buildroot%_datadir/cmake

pushd %buildroot%python3_sitelibdir/torch

# Move all C++ headers to the system include directory.
%ifarch aarch64
# Do not ship headers of the bundled private mimalloc dependency.
rm -rf include/mimalloc-*
%endif
mv include/* %buildroot%_includedir/
rmdir include

# Move CMake package files to the system CMake directory.
for d in share/cmake/*; do
    mv "$d" %buildroot%_datadir/cmake/
done
rmdir share/cmake
rmdir share

popd

# PyTorch generates CMake targets for its wheel layout (torch/lib).
# Adjust them after relocating libraries and CMake files to system paths.
find %buildroot%_datadir/cmake/Caffe2 \
    -type f -name 'Caffe2Targets-*.cmake' \
    -exec sed -i \
        's#${_IMPORT_PREFIX}/lib/#${_IMPORT_PREFIX}/%{_lib}/#g' {} +

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
export LD_LIBRARY_PATH=%buildroot%_libdir

testdir="$PWD/test"
cd %buildroot%python3_sitelibdir

pytest_opts="-ra -q -p no:cacheprovider --disable-warnings"

# CUDA devices are not available in the build environment,
# so only representative CPU-side tests of the CUDA-enabled build are run.
%__python3 -m pytest $pytest_opts \
%ifarch aarch64
    -k 'not test_randint_distribution_cpu' \
%endif
    "$testdir/test_type_promotion.py" \
    "$testdir/test_tensor_creation_ops.py" \
    "$testdir/test_indexing.py" \
    "$testdir/test_view_ops.py" \
    "$testdir/test_shape_ops.py"

%files
%doc *.md LICENSE
%_bindir/torchrun
%_bindir/torchfrtrace
%python3_sitelibdir/torch/
%python3_sitelibdir/functorch
%python3_sitelibdir/torchgen
%python3_sitelibdir/*.dist-info

%files -n libtorch-cuda-devel
%_includedir/ATen
%_includedir/c10
%_includedir/caffe2
%_includedir/torch
%_includedir/tensorpipe
%_includedir/libshm.h
%_includedir/THC
%_datadir/cmake/ATen
%_datadir/cmake/Caffe2
%_datadir/cmake/Tensorpipe
%_datadir/cmake/Torch

%files 		-n libtorch-cuda-cpu
%_libdir/*.so
%exclude %_libdir/libc10_cuda.so
%exclude %_libdir/libtorch_cuda.so
%exclude %_libdir/libtorch_cuda_linalg.so

%files 		-n libtorch-cuda
%_libdir/libc10_cuda.so
%_libdir/libtorch_cuda.so
%_libdir/libtorch_cuda_linalg.so

%changelog
* Mon Aug 31 2026 Nikita Shmatko <nash@altlinux.org> 2.12.0-alt1
- Updated to 2.12.0 version.
- Reenabled half ops for nccl symm-mem.
- Switched to system pybind11.
- Moved C++ headers to include dir and
  CMake files to datadir/cmake (Closes #58168).
- Renamed subpackage devel to libtorch-cuda-devel.
- Switched to upstream Git-based gear layout.
- Fixed CMake target paths for relocated libraries.
- Returned aarch64 build.
- Turned on tests.
- Used system paths for development files.

* Mon Jul 13 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.10.0-alt4
- Switched to GCC 14 as cuda toolchain doesn't support GCC 15+ at the moment.
- Excluded aarch64 build as it doesn't fit in 8 hours limit.

* Wed Mar 18 2026 Nikita Shmatko <nash@altlinux.org> 2.10.0-alt3
- Added cuda-devel-static to requires (Closes: #58170).

* Mon Mar 02 2026 Nikita Shmatko <nash@altlinux.org> 2.10.0-alt2
- Built torch-cuda on aarch64.
- Vendored mimalloc for better aarch64 memory allocation.

* Tue Feb 24 2026 Nikita Shmatko <nash@altlinux.org> 2.10.0-alt1
- Updated to 2.10.0 version.
- Used bundled pybind11 insted of system.
- Vendored cutlass files for examples used in build.
- Minor specfile fixes.

* Fri Feb 13 2026 Nikita Shmatko <nash@altlinux.org> 2.9.1-alt1
- Updated to version 2.9.1.
- Enabled building with system-provided NVTX.
- Dropped copying of valgrind headers, used system ones.
- Updated package descriptions for libtorch and libtorch-cuda for clarity.
- Relocated heavy .so files and their runtime deps to /usr/lib64,
  added symlinks in site-packages.
- Renamed package to python3-module-torch-cuda and subpackages libtorch
  and libtorch-cuda to libtorch-cuda-cpu and libtorch-cuda.

* Wed Nov 26 2025 Nikita Shmatko <nash@altlinux.org> 2.9.0-alt1
- Updated to version 2.9.0.
- Removed leftover broken CUDA Toolkit dependency removals.
- Switched to bundled Gloo instead of the system package.
- Enabled usage of the system ONNX package.

* Wed Nov 05 2025 Nikita Shmatko <nash@altlinux.org> 2.7.1-alt2
- CUDA support improvements:
  + Added CUDA support via build flags.
  + Removed broken dependencies on CUDA Toolkit components.
  + Patched build to use system cuDNN frontend.
  + Fixed usage of system fmt library.
  + Added bundled version of Cutlass headers.

* Mon Oct 13 2025 Nikita Shmatko <nash@altlinux.org> 2.7.1-alt1
- Initial build for Sisyphus.
