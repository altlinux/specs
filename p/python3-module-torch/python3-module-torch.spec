%define pypi_name torch
%def_without check

%def_without system_onnx
%def_with gloo
%def_with tensorpipe
%def_without mpi
%def_without rocm

%define optflags_lto %nil

Name:    python3-module-%pypi_name
Version: 2.7.1
Release: alt1

Summary: Tensors and dynamic neural networks in Python with strong acceleration support (CPU-only)
License: BSD-3-Clause
Group:   Development/ML
URL:     https://pytorch.org/
VCS:     https://github.com/pytorch/pytorch.git

Source: %name-%version.tar
Source1: third_party.tar

Patch0: 0001-disable-submodule-search.patch
Patch1: 0002-fix-system-libs-cmake.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3
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
BuildRequires: libsleef-devel
BuildRequires: FP16-devel
BuildRequires: fxdiv-devel
BuildRequires: libpsimd-devel
BuildRequires: libcpuinfo-devel
BuildRequires: libpthreadpool-devel
BuildRequires: libnumpy-py3-devel
%if_with gloo
BuildRequires: libgloo-devel
%endif
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

# Ignoring packages that unnecessary to work

# coremltools
%add_python3_req_skip coremltools coremltools.converters.mil.input_types coremltools.converters.mil.mil coremltools.models.neural_network

# expecttest
%add_python3_req_skip expecttest

# onnxscript
%add_python3_req_skip onnxscript onnxscript.evaluator onnxscript.function_libs.torch_lib onnxscript.function_libs.torch_lib.ops onnxscript.ir onnxscript.onnx_opset

# optree
%add_python3_req_skip optree

# pytorch_lightning
%add_python3_req_skip pytorch_lightning

# tensorboard
%add_python3_req_skip tensorboard tensorboard.compat tensorboard.compat.proto tensorboard.compat.proto.attr_value_pb2 tensorboard.compat.proto.config_pb2 tensorboard.compat.proto.event_pb2 tensorboard.compat.proto.graph_pb2 tensorboard.compat.proto.node_def_pb2 tensorboard.compat.proto.step_stats_pb2 tensorboard.compat.proto.summary_pb2 tensorboard.compat.proto.tensor_pb2 tensorboard.compat.proto.tensor_shape_pb2 tensorboard.compat.proto.versions_pb2 tensorboard.plugins.custom_scalar tensorboard.plugins.pr_curve.plugin_data_pb2 tensorboard.plugins.projector.projector_config_pb2 tensorboard.plugins.text.plugin_data_pb2 tensorboard.summary.writer.event_file_writer tensorboard.summary.writer.record_writer

# torch
%add_python3_req_skip torch._C._autograd torch._C._distributed_c10d torch._C._distributed_rpc torch._C._dynamo.eval_frame torch._C._dynamo.guards torch._C._functorch torch._C._jit_tree_views torch._C._lazy torch._C._lazy_ts_backend torch._C._monitor torch._C._onnx torch._C._profiler tools.flight_recorder.fr_trace

# torchgen
%add_python3_req_skip torchgen torchgen.model torchgen.utils

# libfb.py.log
%add_python3_req_skip libfb.py.log

%description
%summary.

PyTorch is an optimized tensor library for deep learning using GPUs and CPUs.
This package contains a CPU-only version built for x86_64.

%package devel
Summary: Headers for C/C++, cmake build description and libraries needed for development
Group: Development/ML
Requires: %name = %EVR

%description devel
Although the Python interface is more polished and the primary focus of
development, PyTorch also has a C++ frontend. This package contains the header
to access the C/C++ interface.

%package -n libtorch
Summary: Library which is used by %name
Group: System/Libraries

%description -n libtorch
%summary.

%prep
%setup -a1
%autopatch -p1

#Use system fmt
sed -i -e 's@fmt::fmt-header-only@fmt@' aten/src/ATen/CMakeLists.txt
sed -i -e 's@list(APPEND ATen_HIP_INCLUDE $<TARGET_PROPERTY:fmt,INTERFACE_INCLUDE_DIRECTORIES>)@@' aten/src/ATen/CMakeLists.txt
 
sed -i -e 's@fmt::fmt-header-only@fmt@' third_party/kineto/libkineto/CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' c10/CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' torch/CMakeLists.txt
sed -i -e 's@fmt::fmt-header-only@fmt@' cmake/Dependencies.cmake
sed -i -e 's@fmt::fmt-header-only@fmt@' caffe2/CMakeLists.txt
 
sed -i -e 's@add_subdirectory(${PROJECT_SOURCE_DIR}/third_party/fmt)@#add_subdirectory(${PROJECT_SOURCE_DIR}/third_party/fmt)@' cmake/Dependencies.cmake
sed -i -e 's@set_target_properties(fmt-header-only PROPERTIES INTERFACE_COMPILE_FEATURES "")@#set_target_properties(fmt-header-only PROPERTIES INTERFACE_COMPILE_FEATURES "")@' cmake/Dependencies.cmake
sed -i -e 's@list(APPEND Caffe2_DEPENDENCY_LIBS fmt::fmt-header-only)@#list(APPEND Caffe2_DEPENDENCY_LIBS fmt::fmt-header-only)@' cmake/Dependencies.cmake

# Fix XNNPACK System Library
sed -i -e 's@if(NOT XNNPACK_LIBRARY or NOT microkernels-prod_LIBRARY)@if(NOT XNNPACK_LIBRARY)@' cmake/Dependencies.cmake

# No third_party FXdiv
sed -i -e 's@if(NOT TARGET fxdiv)@if(MSVC AND USE_XNNPACK)@' caffe2/CMakeLists.txt
sed -i -e 's@TARGET_LINK_LIBRARIES(torch_cpu PRIVATE fxdiv)@#TARGET_LINK_LIBRARIES(torch_cpu PRIVATE fxdiv)@' caffe2/CMakeLists.txt

# Use the system valgrind headers
mkdir -p third_party/valgrind-headers
cp %{_includedir}/valgrind/* third_party/valgrind-headers

# Fix installing to /usr/lib64
sed -i -e 's@DESTINATION ${PYTHON_LIB_REL_PATH}@DESTINATION ${CMAKE_INSTALL_PREFIX}/${PYTHON_LIB_REL_PATH}@' caffe2/CMakeLists.txt

%build
%add_optflags -Wno-error=maybe-uninitialized
%add_optflags -Wno-error=array-parameter
%add_optflags -I%{_builddir}/%{name}-%{version}/third_party

export BUILD_CUSTOM_PROTOBUF=OFF
export BUILD_NVFUSER=OFF
export BUILD_SHARED_LIBS=ON
export BUILD_TEST=OFF
export CMAKE_BUILD_TYPE=RelWithDebInfo
export CMAKE_FIND_PACKAGE_PREFER_CONFIG=ON
export CAFFE2_LINK_LOCAL_PROTOBUF=OFF
export INTERN_BUILD_MOBILE=OFF
export USE_DISTRIBUTED=OFF
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
export USE_SYSTEM_ONNX=OFF
export USE_DISTRIBUTED=ON
%if_with tensorpipe
export USE_TENSORPIPE=ON
export TP_BUILD_LIBUV=OFF
%endif
%if_with gloo
export USE_SYSTEM_GLOO=ON
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

%pyproject_build

%install
%pyproject_install

# Install .so files into /usr/lib64 directory
install -Dm755 %buildroot%python3_sitelibdir/torch/lib/lib{c10,torch_cpu,shm,torch_global_deps,torch}.so \
    %buildroot%_libdir/

%files
%doc *.md LICENSE
%_bindir/torchrun
%_bindir/torchfrtrace
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/functorch
%python3_sitelibdir/torchgen
%exclude %python3_sitelibdir/%pypi_name/share
%exclude %python3_sitelibdir/%pypi_name/include
%exclude %python3_sitelibdir/%pypi_name/_inductor/codegen
%exclude %python3_sitelibdir/%pypi_name/utils/benchmark/utils/
%exclude %python3_sitelibdir/torchgen/packaged/ATen/templates
%exclude %python3_sitelibdir/torchgen/packaged/autograd/templates
%python3_sitelibdir/*.dist-info

%files devel
%python3_sitelibdir/%pypi_name/share
%python3_sitelibdir/%pypi_name/include
%python3_sitelibdir/%pypi_name/_inductor/codegen
%python3_sitelibdir/%pypi_name/utils/benchmark/utils/
%python3_sitelibdir/torchgen/packaged/ATen/templates
%python3_sitelibdir/torchgen/packaged/autograd/templates

%files -n libtorch
%_libdir/*.so*

%changelog
* Mon Oct 13 2025 Nikita Shmatko <nash@altlinux.org> 2.7.1-alt1
- Initial build for Sisyphus.
