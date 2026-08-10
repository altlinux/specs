%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%add_verify_elf_skiplist %_libdir/libonnxruntime_providers_*.so

%define dnnl_arches x86_64 aarch64

%define soname 1

Name: onnxruntime
Version: 1.28.0
Release: alt1

Summary: Cross-platform, high performance inference and training machine-learning accelerator

License: MIT
Group: Sciences/Computer science
URL: https://github.com/microsoft/onnxruntime

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.28.0
BuildRequires: chrpath
BuildRequires: ninja-build
BuildRequires: gcc-c++ >= 9.1
BuildRequires: libabseil-cpp-devel
# Do NOT add libflatbuffers-devel here: spec uses bundled flatbuffers,
# and system flatbuffers-config.cmake lacks the flatbuffers::flatbuffers target.
BuildRequires: pkgconfig(re2)
BuildRequires: protobuf-compiler
BuildRequires: pkgconfig(protobuf)
BuildRequires: cmake(date)
BuildRequires: boost-devel
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(libcpuinfo)
#            : cmake(Microsoft.GSL)
BuildRequires: libmicrosoft-gsl-devel
BuildRequires: libsafeint-cpp-devel
# Cannot use pkgconfig(flatbuffers), too new.
BuildRequires: pkgconfig(pybind11)
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pip
BuildRequires: python3-module-packaging
BuildRequires: python3-module-numpy
BuildRequires: libnumpy-py3-devel
# Cannot use cmake(ONNX), no -devel-static, shared libs are useless.
%ifarch %dnnl_arches
BuildRequires: libdnnl-devel
BuildRequires: libgomp-devel
%endif

Source: %name-%version.tar
Source1: %name-%version-cmake-external-onnx.tar
Source2: %name-%version-cmake-external-flatbuffers.tar
Source3: %name-%version-cmake-external-eigen.tar
Source4: %name-%version-cmake-external-dlpack.tar
Patch1: use-system-dnnl.patch

# The bundled onnxruntime.transformers model-conversion tooling needs heavy
# optional dependencies (torch, transformers, diffusers, tensorrt, ...) and its
# scripts confuse the python3 requires scanner; do not ship it.  The remaining
# optional imports below are used lazily by onnxruntime.tools/quantization.
%add_python3_req_skip onnx_ir onnxruntime.quantization.execution_providers onnxruntime_extensions ort_flatbuffers_py.fbs torch
%add_python3_req_skip torch._C._onnx torch.distributed torch.nn.functional torch.onnx torch.onnx.symbolic_helper torch.profiler
%add_python3_req_skip torch.utils.cpp_extension torch.utils.data transformers transformers.cache_utils
# The kept transformers/*.py helpers use sibling-style imports; ml_dtypes is
# optional and not packaged in Sisyphus.
%add_python3_req_skip float16 fusion_utils ml_dtypes onnx_model

%description
Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI
developers to choose the right tools as their project evolves. ONNX provides an
open source format for AI models, both deep learning and traditional ML. It
defines an extensible computation graph model, as well as definitions of
built-in operators and standard data types. Currently we focus on the
capabilities needed for inferencing (scoring).

ONNX Runtime inference can enable faster customer experiences and lower costs,
supporting models from deep learning frameworks such as PyTorch and
TensorFlow/Keras as well as classical machine learning libraries such as
scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime is compatible with different
hardware, drivers, and operating systems, and provides optimal performance by
leveraging hardware accelerators where applicable alongside graph optimizations
and transforms.

%package -n libonnxruntime%soname
Summary: libonnxruntime shared library
Group: System/Libraries
Obsoletes: libonnxruntime <= 1.24.4-alt1

%description -n libonnxruntime%soname
Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI
developers to choose the right tools as their project evolves. ONNX provides an
open source format for AI models, both deep learning and traditional ML. It
defines an extensible computation graph model, as well as definitions of
built-in operators and standard data types.

This package contains the libonnxruntime shared library.

%package -n libonnxruntime-devel
Summary: Development files for onnxruntime
Group: Development/C++
Requires: libonnxruntime%soname = %EVR

%description -n libonnxruntime-devel
Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI
developers to choose the right tools as their project evolves. ONNX provides an
open source format for AI models, both deep learning and traditional ML. It
defines an extensible computation graph model, as well as definitions of
built-in operators and standard data types.

This package contains development files for libonnxruntime.

%package -n python3-module-onnxruntime
Summary: Python 3 bindings for onnxruntime
Group: Development/Python3

%description -n python3-module-onnxruntime
Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI
developers to choose the right tools as their project evolves. ONNX provides an
open source format for AI models, both deep learning and traditional ML. It
defines an extensible computation graph model, as well as definitions of
built-in operators and standard data types.

This package contains the Python 3 bindings for onnxruntime.

%package -n libonnxruntime-providers
Summary: Execution provider plugins for onnxruntime
Group: Sciences/Computer science

%description -n libonnxruntime-providers
Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI
developers to choose the right tools as their project evolves. ONNX provides an
open source format for AI models, both deep learning and traditional ML. It
defines an extensible computation graph model, as well as definitions of
built-in operators and standard data types.

This package contains the "execution providers" for this onnxruntime, built
as loadable plugin shared objects.

%prep
%setup -a1 -a2 -a3 -a4
%autopatch -p1

# Remove win32 binaries shipped by upstream.
rm -rf cmake/external/git.Win32.2.41.03.patch

# Use system abseil.
subst '/NAMES absl/s![0-9]\{8\} !!g' cmake/external/abseil-cpp.cmake

# Use system nlohmann-json.
subst '/NAMES nlohmann_json/s!3.10 !!g' cmake/external/onnxruntime_external_deps.cmake

# Patch Boost detection, which worked well for us in 1.22.1.
subst '/^if(NOT TARGET Boost::mp11)/ifind_package(Boost REQUIRED)' cmake/external/onnxruntime_external_deps.cmake
subst '/^if(NOT TARGET Boost::mp11)/iadd_library(Boost::mp11 ALIAS Boost::headers)' cmake/external/onnxruntime_external_deps.cmake

# Use system SafeInt.hpp.
subst '/NAMES "SafeInt.hpp"/s!)! PATHS "%_includedir/safeint")!g' cmake/external/onnxruntime_external_deps.cmake

# Use bundled flatbuffers. :(((
# To load and store structured data, onnxruntime ships generated development
# headers and modules that use flatbuffers/flatbuffers.h when onnxruntime is
# compiled. The headers and modules take care to check exact version of
# flatbuffers.h; even later versions won't cut it.
# We cannot take the risk that the same schema, if regenerated by a newer
# flatc, will produce cxx code that cannot read ONNX files or serializes data
# in a way incompatible to the world.
# The source tree is passed via FETCHCONTENT_SOURCE_DIR_FLATBUFFERS in %%build.

# Use bundled ONNX from Source1 (cmake/external/onnx).
# The onnx project does not know how to produce or maintain useful shared libraries.
# See also: https://bugzilla.altlinux.org/55423.
# The source tree is passed via FETCHCONTENT_SOURCE_DIR_ONNX in %%build.

# Use bundled Eigen3.
# The source tree is passed via FETCHCONTENT_SOURCE_DIR_EIGEN3 in %%build.

# Use bundled dlpack.
# The source tree is passed via FETCHCONTENT_SOURCE_DIR_DLPACK in %%build.

# FetchContent applies PATCH_COMMAND only to downloaded sources; the trees
# from Source2-Source4 are pre-unpacked, so apply ORT patches here.
patch -p1 -d cmake/external/flatbuffers < cmake/patches/flatbuffers/flatbuffers.patch
patch -p1 -d cmake/external/eigen < cmake/patches/eigen/s390x-build.patch
patch -p1 -d cmake/external/eigen < cmake/patches/eigen/s390x-build-werror.patch

# Someone at ORT missed the noreturn attribute in their wrapper header.
subst '/static void SafeIntOn[A-Za-z]\+/s!static ![[noreturn]] static !' onnxruntime/core/common/safeint.h

%build
%ifarch %ix86
# -msse2 is required by mlas x86 kernels. -U__SSE2__ keeps abseil headers on
# the portable hash-table group implementation, matching the system abseil
# (built without SSE2); otherwise linking fails with undefined references to
# absl::container_internal::PrepareInsertLarge and friends.
%add_optflags -msse2 -U__SSE2__
%endif
%ifarch %dnnl_arches
USE_DNNL=ON
%else
USE_DNNL=OFF
%endif
%cmake -Wno-dev -GNinja -S cmake \
  -DCMAKE_CXX_STANDARD=20 \
  -DCMAKE_BUILD_TYPE=None \
  -Donnxruntime_BUILD_SHARED_LIB=ON \
  -Donnxruntime_ENABLE_PYTHON=ON \
  -Donnxruntime_BUILD_UNIT_TESTS=OFF \
  -Donnxruntime_ENABLE_DLPACK=ON \
  -Donnxruntime_USE_DNNL=$USE_DNNL \
  -DONNX_CUSTOM_PROTOC_EXECUTABLE=%_bindir/protoc \
  -DFETCHCONTENT_SOURCE_DIR_ONNX:PATH="$(pwd)/cmake/external/onnx" \
  -DFETCHCONTENT_SOURCE_DIR_FLATBUFFERS:PATH="$(pwd)/cmake/external/flatbuffers" \
  -DFETCHCONTENT_SOURCE_DIR_EIGEN3:PATH="$(pwd)/cmake/external/eigen" \
  -DFETCHCONTENT_SOURCE_DIR_DLPACK:PATH="$(pwd)/cmake/external/dlpack" \
  -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install
chrpath -d %buildroot%_libdir/libonnxruntime.so.*

# The wheel must be built from the cmake build dir, where
# onnxruntime_python.cmake assembled the python package tree.
pushd %_cmake__builddir
%__python3 ../setup.py bdist_wheel
%__python3 -m pip install --no-deps --no-index --ignore-installed \
  --root %buildroot dist/onnxruntime-%version-*.whl
popd

# Do not ship the model-conversion tooling (see the note above), but keep
# the few modules that onnxruntime.quantization imports at runtime.
find %buildroot%python3_sitelibdir/onnxruntime/transformers -mindepth 1 -maxdepth 1 \
  ! -name '__init__.py' ! -name 'onnx_utils.py' ! -name 'fusion_utils.py' \
  ! -name 'onnx_model.py' ! -name 'float16.py' ! -name '__pycache__' \
  -exec rm -rf {} +
rm -rf %buildroot%python3_sitelibdir/onnxruntime/transformers/__pycache__

%files -n libonnxruntime%soname
%_libdir/libonnxruntime.so.%version
%_libdir/libonnxruntime.so.%soname

%files -n python3-module-onnxruntime
%_bindir/onnxruntime_test
%python3_sitelibdir/onnxruntime/
%python3_sitelibdir/onnxruntime-%version.dist-info/

%files -n libonnxruntime-providers
%_includedir/onnxruntime/provider_options.h
%_includedir/onnxruntime/*_provider_*.h
%_includedir/onnxruntime/core/providers/resource.h
%_includedir/onnxruntime/core/providers/custom_op_context.h
%_libdir/libonnxruntime_providers_*.so

%files -n libonnxruntime-devel
%_pkgconfigdir/libonnxruntime.pc
%_libdir/cmake/onnxruntime
%_libdir/libonnxruntime.so
%_includedir/onnxruntime/onnxruntime_c_api.h
%_includedir/onnxruntime/onnxruntime_cxx_api.h
%_includedir/onnxruntime/onnxruntime_cxx_inline.h
%_includedir/onnxruntime/onnxruntime_ep_c_api.h
%_includedir/onnxruntime/onnxruntime_env_config_keys.h
%_includedir/onnxruntime/onnxruntime_ep_device_ep_metadata_keys.h
%_includedir/onnxruntime/onnxruntime_float16.h
%_includedir/onnxruntime/onnxruntime_lite_custom_op.h
%_includedir/onnxruntime/onnxruntime_run_options_config_keys.h
%_includedir/onnxruntime/onnxruntime_session_options_config_keys.h
%_includedir/onnxruntime/onnxruntime_error_code.h
%_includedir/onnxruntime/onnxruntime_experimental_c_api.h
%_includedir/onnxruntime/onnxruntime_experimental_c_api.inc
%_includedir/onnxruntime/onnxruntime_experimental_cxx_api.h


%changelog
* Thu Aug 06 2026 Anton Farygin <rider@altlinux.org> 1.28.0-alt1
- 1.24.4 -> 1.28.0
- fixed libonnxruntime updating (closes: #60109)
- built python3 module (closes: #58623)
- excluded the bundled model-conversion tooling from the python3 module
  (it needs torch/transformers/diffusers and breaks dependency generation)

* Wed Apr 08 2026 Anton Farygin <rider@altlinux.org> 1.24.4-alt1
- 1.23.0 -> 1.24.4

* Mon Aug 04 2025 Arseny Maslennikov <arseny@altlinux.org> 1.23.0-alt1
- Initial build for ALT Sisyphus.
  This is a prerelease revision from rel-1.23.0.
  Most execution providers and features are turned off for now.
