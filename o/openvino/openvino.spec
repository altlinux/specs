%define _unpackaged_files_terminate_build 1

# Library soversion is computed by upstream from the version:
# 2026.4.0 -> "26" "4" "0" -> libopenvino.so.2640 (cmake/developer_package/version.cmake).
%define sover 2640
%define plugindir %_libdir/openvino-%version

%def_with python
%def_without check

Name: openvino
Version: 2026.4.0
Release: alt1

Summary: Open source toolkit for optimizing and deploying AI inference
License: Apache-2.0
Group: Sciences/Computer science
Url: https://docs.openvino.ai/
Vcs: https://github.com/openvinotoolkit/openvino

ExclusiveArch: x86_64

Source: %name-%version.tar
Source1: ovc
Source2: %name-%version-submodule-src-plugins-intel_cpu-thirdparty-onednn.tar
Source3: %name-%version-submodule-src-plugins-intel_cpu-thirdparty-mlas.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: ittapi-devel-static
BuildRequires: level-zero-npu-extensions-devel
BuildRequires: libze-devel
BuildRequires: libxbyak-devel
BuildRequires: opencl-headers
BuildRequires: opencl-cpp-headers
BuildRequires: ocl-icd-devel
BuildRequires: libpugixml-devel
BuildRequires: libprotobuf-devel
BuildRequires: protobuf-compiler
BuildRequires: libflatbuffers-devel
BuildRequires: libsnappy-devel
BuildRequires: libonnx-devel
BuildRequires: nlohmann-json-devel
BuildRequires: tbb-devel
BuildRequires: zlib-devel
%if_with python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: pybind11-devel
BuildRequires: python3-module-pybind11
BuildRequires: python3-module-numpy
BuildRequires: python3-module-setuptools
%endif
%if_with check
BuildRequires: ctest
%endif

%description
OpenVINO is an open-source toolkit for optimizing and deploying deep learning
models from cloud to edge. It accelerates deep learning inference across
various use cases, such as generative AI, video, audio, and language with
models from popular frameworks like PyTorch, TensorFlow, ONNX, and more.
Convert and optimize models, and deploy across a mix of Intel hardware and
environments, on-premises and on-device, in the browser or in the cloud.

%package -n lib%name%sover
Summary: OpenVINO Runtime library
Group: System/Libraries

%description -n lib%name%sover
OpenVINO is an open-source toolkit for optimizing and deploying deep learning
models.

This package contains OpenVINO Runtime core libraries (C++ and C API).
Device plugins are loaded at runtime and packaged separately.

%package -n lib%name-devel
Summary: Development files for OpenVINO Runtime
Group: Development/C++
# OpenVINOConfig.cmake looks for TBB
Requires: tbb-devel

%description -n lib%name-devel
This package contains header files, CMake and pkg-config files for
developing applications that use OpenVINO Runtime.

%package plugins
Summary: OpenVINO Runtime virtual device plugins
Group: System/Libraries

%description plugins
This package contains the virtual device plugins for OpenVINO Runtime:
AUTO, MULTI, HETERO and BATCH.

%package plugin-intel-cpu
Summary: Intel CPU plugin for OpenVINO Runtime
Group: System/Libraries

%description plugin-intel-cpu
This package contains the Intel CPU plugin for OpenVINO Runtime, which
enables inference on x86-64 CPUs.

%package plugin-intel-gpu
Summary: Intel GPU plugin for OpenVINO Runtime
Group: System/Libraries

%description plugin-intel-gpu
This package contains the Intel GPU plugin for OpenVINO Runtime, which
enables inference on Intel integrated and discrete GPUs via OpenCL.

%package plugin-intel-npu
Summary: Intel NPU plugin for OpenVINO Runtime
Group: System/Libraries

%description plugin-intel-npu
This package contains the Intel NPU plugin for OpenVINO Runtime, which
enables inference on Intel Neural Processing Units via Level Zero.

%package -n lib%name-ir-frontend%sover
Summary: OpenVINO IR frontend
Group: System/Libraries

%description -n lib%name-ir-frontend%sover
This package contains the OpenVINO frontend for reading models in
OpenVINO IR format.

%package -n lib%name-onnx-frontend%sover
Summary: OpenVINO ONNX frontend
Group: System/Libraries

%description -n lib%name-onnx-frontend%sover
This package contains the OpenVINO frontend for reading ONNX models.

%package -n lib%name-paddle-frontend%sover
Summary: OpenVINO PaddlePaddle frontend
Group: System/Libraries

%description -n lib%name-paddle-frontend%sover
This package contains the OpenVINO frontend for reading PaddlePaddle models.

%package -n lib%name-pytorch-frontend%sover
Summary: OpenVINO PyTorch frontend
Group: System/Libraries

%description -n lib%name-pytorch-frontend%sover
This package contains the OpenVINO frontend for converting PyTorch models.

%package -n lib%name-tensorflow-frontend%sover
Summary: OpenVINO TensorFlow frontend
Group: System/Libraries

%description -n lib%name-tensorflow-frontend%sover
This package contains the OpenVINO frontend for reading TensorFlow models.

%package -n lib%name-tensorflow-lite-frontend%sover
Summary: OpenVINO TensorFlow Lite frontend
Group: System/Libraries

%description -n lib%name-tensorflow-lite-frontend%sover
This package contains the OpenVINO frontend for reading TensorFlow Lite
models.

%package -n lib%name-gguf-frontend%sover
Summary: OpenVINO GGUF frontend
Group: System/Libraries

%description -n lib%name-gguf-frontend%sover
OpenVINO frontend for loading models in GGUF format.

%if_with python
%package -n python3-module-%name
Summary: Python bindings for OpenVINO Runtime
Group: Development/Python3
# Python modules import torch, tensorflow, PIL etc. only when converting
# models from these frameworks, so python dependencies are listed by hand.
AutoReq: yes, nopython3
Requires: python3-module-numpy
# plugins are loaded at runtime; CPU is the device available everywhere
Requires: %name-plugin-intel-cpu = %EVR

%description -n python3-module-%name
OpenVINO is an open-source toolkit for optimizing and deploying deep learning
models.

This package contains Python 3 bindings for OpenVINO Runtime.

%package tools
Summary: OpenVINO model converter
Group: Sciences/Computer science
Requires: python3-module-%name = %EVR

%description tools
This package contains ovc, the OpenVINO model converter, which converts
models from ONNX, TensorFlow, TensorFlow Lite, PaddlePaddle and PyTorch
formats to OpenVINO IR.
%endif

%prep
%setup -a2 -a3
%autopatch -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
	-DCPACK_GENERATOR=RPM \
	-DENABLE_CLANG_FORMAT=OFF \
	-DENABLE_NCC_STYLE=OFF \
	-DENABLE_CPPLINT=OFF \
	-DENABLE_LTO=OFF \
	-DOV_STRIP_BINARIES=OFF \
	-DENABLE_TESTS=OFF \
	-DENABLE_SAMPLES=OFF \
	-DENABLE_TEMPLATE=OFF \
	-DENABLE_JS=OFF \
	-DENABLE_WHEEL=OFF \
	-DENABLE_PYTHON=%{?_with_python:ON}%{!?_with_python:OFF} \
	-DPython3_EXECUTABLE=%__python3 \
	-DENABLE_INTEL_CPU=ON \
	-DENABLE_MLAS_FOR_CPU=ON \
	-DENABLE_INTEL_GPU=ON \
	-DENABLE_ONEDNN_FOR_GPU=OFF \
	-DENABLE_INTEL_NPU=ON \
	-DENABLE_INTEL_NPU_INTERNAL=OFF \
	-DENABLE_INTEL_NPU_COMPILER=OFF \
	-DENABLE_PROFILING_ITT=BASE \
	-DENABLE_PLUGINS_XML=OFF \
	-DENABLE_SYSTEM_TBB=ON \
	-DENABLE_TBBBIND_2_5=OFF \
	-DENABLE_SYSTEM_PUGIXML=ON \
	-DENABLE_SYSTEM_FLATBUFFERS=ON \
	-DENABLE_SYSTEM_OPENCL=ON \
	-DENABLE_SYSTEM_PROTOBUF=ON \
	-DProtobuf_USE_STATIC_LIBS=OFF \
	-DENABLE_SYSTEM_SNAPPY=ON \
	-DENABLE_SYSTEM_LEVEL_ZERO=ON \
	-DENABLE_OV_ONNX_FRONTEND=ON \
	-DENABLE_OV_PADDLE_FRONTEND=ON \
	-DENABLE_OV_IR_FRONTEND=ON \
	-DENABLE_OV_PYTORCH_FRONTEND=ON \
	-DENABLE_OV_TF_FRONTEND=ON \
	-DENABLE_OV_TF_LITE_FRONTEND=ON \
	-DENABLE_OV_JAX_FRONTEND=OFF \
	%nil
%cmake_build

%install
%cmake_install
%if_with python
install -Dm755 %SOURCE1 %buildroot%_bindir/ovc
%endif
# upstream per-component copyright files (licenses are packaged via %%doc)
rm -r %buildroot%_datadir/doc
# samples sources are not packaged
rm -r %buildroot%_datadir/openvino

%check
%ctest

%files -n lib%name%sover
%doc LICENSE README.md
%_libdir/libopenvino.so.%sover
%_libdir/libopenvino.so.%version
%_libdir/libopenvino_c.so.%sover
%_libdir/libopenvino_c.so.%version
%dir %plugindir

%files plugins
%plugindir/libopenvino_auto_plugin.so
%plugindir/libopenvino_auto_batch_plugin.so
%plugindir/libopenvino_hetero_plugin.so

%files plugin-intel-cpu
%plugindir/libopenvino_intel_cpu_plugin.so

%files plugin-intel-gpu
%plugindir/libopenvino_intel_gpu_plugin.so
%plugindir/cache.json

%files plugin-intel-npu
%plugindir/libopenvino_intel_npu_plugin.so

%files -n lib%name-ir-frontend%sover
%_libdir/libopenvino_ir_frontend.so.%sover
%_libdir/libopenvino_ir_frontend.so.%version

%files -n lib%name-onnx-frontend%sover
%_libdir/libopenvino_onnx_frontend.so.%sover
%_libdir/libopenvino_onnx_frontend.so.%version

%files -n lib%name-paddle-frontend%sover
%_libdir/libopenvino_paddle_frontend.so.%sover
%_libdir/libopenvino_paddle_frontend.so.%version

%files -n lib%name-pytorch-frontend%sover
%_libdir/libopenvino_pytorch_frontend.so.%sover
%_libdir/libopenvino_pytorch_frontend.so.%version

%files -n lib%name-tensorflow-frontend%sover
%_libdir/libopenvino_tensorflow_frontend.so.%sover
%_libdir/libopenvino_tensorflow_frontend.so.%version

%files -n lib%name-tensorflow-lite-frontend%sover
%_libdir/libopenvino_tensorflow_lite_frontend.so.%sover
%_libdir/libopenvino_tensorflow_lite_frontend.so.%version

%files -n  lib%name-gguf-frontend%sover
%_libdir/libopenvino_gguf_frontend.so.%sover
%_libdir/libopenvino_gguf_frontend.so.%version

%files -n lib%name-devel
%_includedir/openvino
%_libdir/libopenvino.so
%_libdir/libopenvino_c.so
%_libdir/libopenvino_onnx_frontend.so
%_libdir/libopenvino_paddle_frontend.so
%_libdir/libopenvino_pytorch_frontend.so
%_libdir/libopenvino_tensorflow_frontend.so
%_libdir/libopenvino_tensorflow_lite_frontend.so
%_libdir/libopenvino_gguf_frontend.so
%_libdir/cmake/openvino%version
%_pkgconfigdir/openvino.pc

%if_with python
%files -n python3-module-%name
%python3_sitelibdir/openvino
%exclude %python3_sitelibdir/openvino/tools/ovc

%files tools
%_bindir/ovc
%python3_sitelibdir/openvino/tools/ovc
%endif

%changelog
* Wed Sep 23 2026 Artem Krasovskiy <aibure@altlinux.org> 2026.4.0-alt1
- Initial build for Sisyphus.
