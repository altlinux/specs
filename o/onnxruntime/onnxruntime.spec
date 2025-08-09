%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%add_verify_elf_skiplist %_libdir/libonnxruntime_providers_*.so

%define dnnl_arches x86_64 aarch64

Name: onnxruntime
Version: 1.23.0
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
BuildRequires: pkgconfig(re2)
BuildRequires: protobuf-compiler
BuildRequires: pkgconfig(protobuf)
#BuildRequires: pkgconfig(protobuf-lite)
BuildRequires: cmake(date)
BuildRequires: boost-devel
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(libcpuinfo)
#            : cmake(Microsoft.GSL)
BuildRequires: libmicrosoft-gsl-devel
BuildRequires: libsafeint-cpp-devel
# Cannot use pkgconfig(flatbuffers), too new.
BuildRequires: pkgconfig(pybind11)
# Cannot use cmake(ONNX), no -devel-static, shared libs are useless.
%ifarch %dnnl_arches
BuildRequires: libdnnl-devel
BuildRequires: libgomp-devel
%endif

Source: %name-%version.tar
Patch1: use-system-dnnl.patch

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

%package -n libonnxruntime
Summary: libonnxruntime shared library
Group: Sciences/Computer science

%description -n libonnxruntime
Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI
developers to choose the right tools as their project evolves. ONNX provides an
open source format for AI models, both deep learning and traditional ML. It
defines an extensible computation graph model, as well as definitions of
built-in operators and standard data types.

This package contains the libonnxruntime shared library.

%package -n libonnxruntime-devel
Summary: Development files for onnxruntime
Group: Development/C++

%description -n libonnxruntime-devel
Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI
developers to choose the right tools as their project evolves. ONNX provides an
open source format for AI models, both deep learning and traditional ML. It
defines an extensible computation graph model, as well as definitions of
built-in operators and standard data types.

This package contains development files for libonnxruntime.

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
%setup
%autopatch -p1

# Remove win32 binaries shipped by upstream.
rm -rf cmake/external/git.Win32.2.41.03.patch

# Use system abseil.
subst '/NAMES absl/s!20250512 !!g' cmake/external/abseil-cpp.cmake

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
printf >&2 '%%s\n' "Substituting local copy of 'flatbuffers'."
printf >&2 '%%s: %%s\n' "* Original URL" "$(grep '^flatbuffers;' cmake/deps.txt)"
subst '/^flatbuffers;/s!;[^;]*/archive/refs/tags/!;'"$(pwd)/cmake/"'flatbuffers-!' cmake/deps.txt

# Use bundled ONNX.
# The onnx project does not know how to produce or maintain useful shared libraries.
# See also: https://bugzilla.altlinux.org/55423.
printf >&2 '%%s\n' "Substituting local copy of 'onnx'."
printf >&2 '%%s: %%s\n' "* Original URL" "$(grep '^onnx;' cmake/deps.txt)"
subst '/^onnx;/s!;[^;]*/archive/refs/tags/!;'"$(pwd)/cmake/"'onnx-!' cmake/deps.txt

# Use bundled Eigen3.
printf >&2 '%%s\n' "Substituting local copy of 'eigen'."
printf >&2 '%%s: %%s\n' "* Original URL" "$(grep '^eigen;' cmake/deps.txt)"
subst '/^eigen;/s!;[^;]*/eigen/archive/[^;/]*/eigen-!;'"$(pwd)/cmake/"'eigen-!' cmake/deps.txt

# Use bundled dlpack.
printf >&2 '%%s\n' "Substituting local copy of 'dlpack'."
printf >&2 '%%s: %%s\n' "* Original URL" "$(grep '^dlpack;' cmake/deps.txt)"
subst '/^dlpack;/s!;[^;]*/dlpack/archive/[^;/]*/dlpack-!;'"$(pwd)/cmake/"'dlpack-!' cmake/deps.txt

# Someone at ORT missed the noreturn attribute in their wrapper header.
subst '/static void SafeIntOn[A-Za-z]\+/s!static ![[noreturn]] static !' onnxruntime/core/common/safeint.h

%build
%ifarch %ix86
%add_optflags -msse2
%endif
%ifarch %dnnl_arches
USE_DNNL=ON
%else
USE_DNNL=OFF
%endif
%cmake -Wno-dev -GNinja -S cmake \
  -DCMAKE_CXX_STANDARD=17 \
  -DCMAKE_BUILD_TYPE=None \
  -Donnxruntime_BUILD_SHARED_LIB=ON \
  -Donnxruntime_BUILD_UNIT_TESTS=OFF \
  -Donnxruntime_ENABLE_DLPACK=ON \
  -Donnxruntime_USE_DNNL=$USE_DNNL \
  -DONNX_CUSTOM_PROTOC_EXECUTABLE=%_bindir/protoc \
  -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install
chrpath -d %buildroot%_libdir/libonnxruntime.so.*

%files -n libonnxruntime
%_libdir/libonnxruntime.so.1.23.0
%_libdir/libonnxruntime.so.1

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
%_includedir/onnxruntime/onnxruntime_ep_device_ep_metadata_keys.h
%_includedir/onnxruntime/onnxruntime_float16.h
%_includedir/onnxruntime/onnxruntime_lite_custom_op.h
%_includedir/onnxruntime/onnxruntime_run_options_config_keys.h
%_includedir/onnxruntime/onnxruntime_session_options_config_keys.h

%changelog
* Mon Aug 04 2025 Arseny Maslennikov <arseny@altlinux.org> 1.23.0-alt1
- Initial build for ALT Sisyphus.
  This is a prerelease revision from rel-1.23.0.
  Most execution providers and features are turned off for now.
