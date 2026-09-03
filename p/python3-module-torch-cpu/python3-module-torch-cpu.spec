%define _unpackaged_files_terminate_build 1

%def_with check

%def_with system_onnx
%def_with gloo
%def_with tensorpipe
%def_without mpi
%def_without rocm

%define optflags_lto %nil

Name:    python3-module-torch-cpu
Version: 2.12.0
Release: alt1

Summary: Tensors and dynamic neural networks in Python with strong acceleration support (CPU-only)
License: BSD-3-Clause
Group:   Development/ML
URL:     https://pytorch.org/
VCS:     https://github.com/pytorch/pytorch.git

Source0: python3-module-torch-cpu-%version.tar
Source1: third_party.tar
Source2: _install_paths.py.in

Patch0: 0001-Disabled-submodule-search.patch
Patch1: 0002-Fixed-system-libs-cmake.patch
Patch2: 0003-Use-system-valgrind-instead-of-bundled.patch
Patch3: 0004-Used-system-devel-paths.patch

ExclusiveArch: x86_64 aarch64
# Disable python3 autoprovides to avoid duplicate Provides between CPU/CUDA variants.
AutoProv: nopython3

# Remove self requires for torch
%filter_from_requires /python3(torch.*)/d
%filter_from_requires /^libtorch.*\.so/d
%filter_from_requires /^libc10.*\.so/d
%filter_from_requires /^libshm\.so/d

# Remove CUDA packages requires for CPU package
%filter_from_requires /python3(cutlass.*)/d
%filter_from_requires /python3(cuda.bindings.driver)/d

# Ignoring packages that unnecessary to work
%filter_from_requires /python3(coremltools.*)/d
%filter_from_requires /python3(expecttest)/d
%filter_from_requires /python3(onnxscript.*)/d
%filter_from_requires /python3(optree.*)/d
%filter_from_requires /python3(pytorch_lightning)/d
%filter_from_requires /python3(tensorboard.*)/d
%filter_from_requires /python3(libfb.py.log)/d

BuildRequires(pre): cmake rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: valgrind-devel
BuildRequires: libfmt-devel
BuildRequires: libgomp-devel
BuildRequires: libonnx-devel
BuildRequires: libmpfr-devel
BuildRequires: libgmp-devel
BuildRequires: libfftw3-devel
BuildRequires: eigen3
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
BuildRequires: python3-module-sympy
BuildRequires: python3-module-expecttest
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-filelock
BuildRequires: python3-module-networkx
BuildRequires: python3-module-psutil
%endif

Provides: 	pytorch
Obsoletes: 	python3-module-torch < %EVR

Requires: 	libtorch-cpu = %EVR

%description
%summary.

PyTorch is an optimized tensor library for deep learning using GPUs and CPUs.
This package contains a CPU-only version built for x86_64 and aarch64.

%package 	-n libtorch-cpu-devel
Summary: 	Headers, CMake config and link libraries for C++ libtorch (CPU)
Group: 		Development/ML
Requires: 	libtorch-cpu = %EVR
# Disable python3 autoprovides to avoid duplicate Provides between CPU/CUDA variants.
AutoProv: 	nopython3
Obsoletes: 	python3-module-torch-devel < %EVR
Obsoletes: 	python3-module-torch-cpu-devel < %EVR

%description 	-n libtorch-cpu-devel
Development files (headers and CMake package configuration) for building
C++ programs and extensions against the CPU build of libtorch.

%package 	-n libtorch-cpu
Summary: 	python3-module-torch-cpu shared libraries for CPU
Group: 		System/Libraries
# Disable python3 autoprovides to avoid duplicate Provides between CPU/CUDA variants.
AutoProv: 	nopython3, nolib
Obsoletes: 	libtorch < %EVR

%description 	-n libtorch-cpu
CPU PyTorch libraries for system use. Other packages can
link to use python3-module-torch-cpu from C++ or Python extensions.

%prep
%setup -a1
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p1

install -pm0644 %SOURCE2 torch/_install_paths.py.in

#Use system fmt
#Include fmt before ATen to fix build
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
%add_optflags -I%_builddir/python3-module-torch-cpu-%version/third_party
%add_optflags -I%_includedir/valgrind

export BUILD_CUSTOM_PROTOBUF=OFF
export BUILD_NVFUSER=OFF
export BUILD_SHARED_LIBS=ON
export BUILD_TEST=OFF
export CMAKE_BUILD_TYPE=RelWithDebInfo
export CMAKE_FIND_PACKAGE_PREFER_CONFIG=ON
export CAFFE2_LINK_LOCAL_PROTOBUF=OFF
export INTERN_BUILD_MOBILE=OFF
export USE_CUDA=OFF
export USE_FAKELOWP=OFF
export USE_FBGEMM=OFF
export USE_FLASH_ATTENTION=OFF
export USE_ITT=OFF
export USE_KINETO=OFF
export USE_KLEIDIAI=OFF
export USE_LITE_INTERPRETER_PROFILER=OFF
export USE_LITE_PROTO=OFF
export USE_MAGMA=OFF
export USE_MEM_EFF_ATTENTION=OFF
export USE_MKLDNN=OFF
export USE_MPI=OFF
export USE_MIMALLOC=OFF
export USE_NCCL=OFF
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
export USE_DISTRIBUTED=ON
%if_with tensorpipe
export USE_TENSORPIPE=ON
export TP_BUILD_LIBUV=OFF
%endif
%if_with gloo
# Using bundled Gloo implementation.
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
%ifarch aarch64
NPROCS=%__nprocs
export NPROCS
export MAX_JOBS=$NPROCS
export CMAKE_BUILD_PARALLEL_LEVEL=$NPROCS
%endif
export TORCH_SYSTEM_INCLUDE_DIR=%_includedir
export TORCH_SYSTEM_CMAKE_PREFIX_PATH=%_datadir/cmake

%pyproject_build

%install
%pyproject_install

# Place .so libraries in /usr/lib64 to make them discoverable by system packages
# (such as python3-module-torchvision).
LIBS="libc10.so libtorch_cpu.so \
	libshm.so libtorch.so"

for f in $LIBS; do
    install -Dm755 %buildroot%python3_sitelibdir/torch/lib/$f %buildroot%_libdir/
    rm -f %buildroot%python3_sitelibdir/torch/lib/$f
done

# Expose C++ headers and CMake configs at system paths.

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
export LD_LIBRARY_PATH=%buildroot%_libdir
export PYTHONPATH=%buildroot%python3_sitelibdir
export CPLUS_INCLUDE_PATH=%buildroot%_includedir:%buildroot%_includedir/torch/csrc/api/include
export LIBRARY_PATH=%buildroot%_libdir

testdir="$PWD/test"
cd %buildroot%python3_sitelibdir

# Fail fast if the extension does not load.
%__python3 -c 'import torch; print(torch.__version__)'

pytest_opts="-ra -q -p no:cacheprovider --disable-warnings"

# Representative CPU test subset. GPU/XPU/distributed suites are not run.
#
# test_qengine is excluded because this build intentionally disables
# FBGEMM and QNNPACK.
#
# test_scalar_tensor_dim_compiled_mode_cpu is excluded because it exercises
# TorchInductor, which is outside this CPU package test subset.
#
# test_print is run separately below because other tests modify global
# torch print options and make it order-dependent.
%__python3 -m pytest $pytest_opts \
    -k 'not test_qengine and not test_scalar_tensor_dim_compiled_mode_cpu and not test_print' \
    "$testdir/test_type_promotion.py" \
    "$testdir/test_tensor_creation_ops.py" \
    "$testdir/test_indexing.py" \
    "$testdir/test_view_ops.py" \
    "$testdir/test_shape_ops.py" \
    "$testdir/test_reductions.py" \
    "$testdir/test_sort_and_select.py" \
    "$testdir/test_autograd.py" \
    "$testdir/test_nn.py" \
    "$testdir/test_torch.py"

# Run in a fresh Python process to avoid print-option state leakage.
%__python3 -m pytest $pytest_opts \
    "$testdir/test_torch.py::TestTorch::test_print"

%files
%doc *.md LICENSE
%_bindir/torchrun
%_bindir/torchfrtrace
%python3_sitelibdir/torch/
%python3_sitelibdir/functorch
%python3_sitelibdir/torchgen
%python3_sitelibdir/*.dist-info

%files 	 	-n libtorch-cpu-devel
%_includedir/ATen
%_includedir/c10
%_includedir/caffe2
%_includedir/torch
%_includedir/tensorpipe
%_includedir/libshm.h
%_datadir/cmake/Torch
%_datadir/cmake/Caffe2
%_datadir/cmake/ATen
%_datadir/cmake/Tensorpipe

%files 		-n libtorch-cpu
%_libdir/*.so*

%changelog
* Mon Aug 31 2026 Nikita Shmatko <nash@altlinux.org> 2.12.0-alt1
- Updated to 2.12.0.
- Switched to system pybind11.
- Moved C++ headers to include dir and Cmake files to datadir/cmake.
- Renamed subpackage devel to libtorch-cpu-devel.
- Switched to filtered autogenerated requires.
- Converted the package to an upstream Git-based gear layout.
- Fixed CMake target paths for relocated libraries.
- Turned on tests.
- Used system paths for development files.

* Mon Feb 23 2026 Nikita Shmatko <nash@altlinux.org> 2.10.0-alt1
- Updated to 2.10.0 version.
- Used bundled pybind11 insted of system.
- Vendored mimalloc for better aarch64 memory allocation.
- Minor specfile fixes.

* Thu Feb 12 2026 Nikita Shmatko <nash@altlinux.org> 2.9.1-alt1
- Updated to 2.9.1 version.
- Fixed usage of system fmt library.
- Enabled usage of the system ONNX package.
- Renamed package to python3-module-torch-cpu and
  subpackage libtorch to libtorch-cpu.
- Switched to bundled Gloo instead of the system package.
- Dropped copying of valgrind headers, used system ones.

* Mon Oct 13 2025 Nikita Shmatko <nash@altlinux.org> 2.7.1-alt1
- Initial build for Sisyphus.
