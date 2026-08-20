# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%ifarch x86_64
%def_with cuda
%else
%def_without cuda
%endif
%def_with vulkan

%define backenddir %_libdir/%name
%define soversion 0

Name: transcribe.cpp
Version: 0.1.3
Release: alt3

Summary: Speech-to-text (ASR) inference in C/C++
License: MIT
Group: Sound
Url: https://github.com/handy-computer/transcribe.cpp
Vcs: https://github.com/handy-computer/transcribe.cpp.git
ExcludeArch: %ix86

Source: %name-%version.tar
Patch0: %name-%version.patch
Patch1: transcribe.cpp-0.1.3-alt-rename-ggml-libs.patch
Patch2: transcribe.cpp-0.1.3-alt-backend-dir.patch

Requires: libtranscribe%soversion = %EVR
Requires: %name-cpu = %EVR
%if_with cuda
Requires: %name-cuda = %EVR
%filter_from_requires /(libcudart\.so\.12)/d
%filter_from_requires /debug64(libcuda\.so\.1)/d
%endif
%if_with vulkan
Requires: %name-vulkan = %EVR
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
%if_with cuda
# cuda requires gcc12
BuildRequires: gcc12-c++
BuildRequires: nvidia-cuda-devel-static
%endif
%if_with vulkan
BuildRequires: glslc
BuildRequires: libvulkan-devel
BuildRequires: spirv-headers
%endif
%{?!_without_check:%{?!_disable_check:
BuildRequires: ctest
}}

%description
High-performance inference of speech-to-text (ASR) models in C/C++ on the
ggml runtime, with the ggml CPU kernels for all supported instruction set
variants and CUDA and Vulkan backends for GPU inference.

Supported model families: Parakeet, Canary, Canary-Qwen, Whisper, GigaAM,
Moonshine (batch and streaming), Qwen3-ASR, Cohere Transcribe, SenseVoice,
FunASR Nano, Nemotron Speech Streaming, Granite Speech, Voxtral (batch and
realtime), MedASR.

NOTE:
  MODELS ARE NOT PROVIDED. GGUF models can be downloaded from Hugging Face
  (https://huggingface.co/handy-computer) and passed with the -m/--model
  option.

%package -n libtranscribe%soversion
Summary: Shared library for %name
Group: System/Libraries
# The CPU backend is the only one required: it always works and is small.
# The CUDA and Vulkan backends are optional, install them explicitly.
Requires: %name-cpu = %EVR

%description -n libtranscribe%soversion
%summary.

%package -n libtranscribe-devel
Summary: Development files for libtranscribe%soversion
Group: Development/C
Requires: libtranscribe%soversion = %EVR

%description -n libtranscribe-devel
Contains the public header (transcribe.h and the per-family extension
headers), the ABI digest and the link manifest transcribe-link.json.

The manifest is the machine-readable link interface for non-CMake
consumers: it is what the Rust -sys crate consumes when TRANSCRIBE_DIR
points at a system prefix (TRANSCRIBE_DIR=%prefix), instead of building a
private copy of the library from source.

%package cpu
Summary: %name backend for CPU
Group: Sound
Requires: libtranscribe%soversion = %EVR

%description cpu
%summary.

%package cuda
Summary: %name backend for NVIDIA GPU
Group: Sound
Requires: %name-cpu = %EVR
Requires: libnvidia-ptxjitcompiler

%description cuda
%summary.

%package vulkan
Summary: %name backend for GPU
Group: Sound
Requires: %name-cpu = %EVR

%description vulkan
%summary.

%prep
%setup
%autopatch -p1

%build
%if_with cuda
# -Xcompiler=-g1: host-side debug info, otherwise the CUDA backend module has
# an empty .debug_info and 056-debuginfo.brp terminates the build (as in
# llama.cpp).
%define optflags_debug -g1
export NVCC_PREPEND_FLAGS='-ccbin=g++-12 -Xcompiler=-g1'
%endif
# Unless -DCMAKE_SKIP_BUILD_RPATH=yes CMake leaves the build time RPATH in the
# binaries, which are installed from the build tree (upstream has no install
# rules for the CLI and the tools).
%cmake \
	-DCMAKE_SKIP_BUILD_RPATH=yes \
	-DCMAKE_INSTALL_LIBDIR=%_lib \
	-DTRANSCRIBE_INSTALL=ON \
	-DTRANSCRIBE_BUILD_SHARED=ON \
	-DTRANSCRIBE_BUILD_TESTS=ON \
	-DTRANSCRIBE_BUILD_EXAMPLES=ON \
	-DTRANSCRIBE_BUILD_TOOLS=ON \
	-DTRANSCRIBE_GGML_BACKEND_DL=ON \
	-DGGML_BACKEND_DIR=%backenddir \
	-DGGML_NATIVE=OFF \
%ifarch x86_64 riscv64
	-DGGML_CPU_ALL_VARIANTS=ON \
%endif
%if_with cuda
	-DTRANSCRIBE_CUDA=ON \
	-DCMAKE_CUDA_ARCHITECTURES='52-virtual;80-virtual' \
%endif
%if_with vulkan
	-DTRANSCRIBE_VULKAN=ON \
%endif
	%nil
grep -E '^TRANSCRIBE|^GGML' %_cmake__builddir/CMakeCache.txt | sort | tee build-options.txt
%cmake_build

%install
%cmake_install
# Upstream installs the library, the headers and the link manifest only; the
# CLI, the bench and the quantizer are built from examples/ and tools/.
install -Dp %_cmake__builddir/bin/transcribe-cli -t %buildroot%_bindir
install -Dp %_cmake__builddir/bin/transcribe-quantize -t %buildroot%_bindir
install -Dp %_cmake__builddir/bin/transcribe-bench -t %buildroot%_bindir
# The bundled ggml installs its own public headers and CMake package into the
# system-wide locations, where they collide with llama.cpp and whisper.cpp.
# transcribe.h is a one-header public surface (callers never include ggml.h),
# so the ggml development files are not packaged.
rm -f %buildroot%_includedir/ggml*.h %buildroot%_includedir/gguf.h
rm -rf %buildroot%_cmakedir/ggml
rmdir --ignore-fail-on-non-empty %buildroot%_cmakedir

%check
%if_with cuda
# Only the virtual architectures asked for above, nothing else (as in llama.cpp).
( ! cuobjdump --list-elf %buildroot%backenddir/libggml-cuda.so | grep -F -v -e .cubin )
( ! cuobjdump --list-ptx %buildroot%backenddir/libggml-cuda.so | grep -F -v -e .sm_80.ptx -e .sm_52.ptx )
%endif
# %backenddir does not exist at build time, so the library falls back to
# scanning the directory it lives in itself (src/), while the build puts the
# backend modules into bin/ — colocate them for the test run.
cp -a %_cmake__builddir/bin/libggml-*.so %_cmake__builddir/src/
export LD_LIBRARY_PATH=$PWD/%_cmake__builddir/src:$PWD/%_cmake__builddir/ggml/src
export PATH=$PWD/%_cmake__builddir/bin:$PATH
%ctest

%files -n libtranscribe%soversion
%_libdir/libtranscribe.so.*
%_libdir/libggml_transcribe.so.*
%_libdir/libggml_base_transcribe.so.*

%files -n libtranscribe-devel
%_includedir/transcribe.h
%_includedir/transcribe.abihash
%_includedir/transcribe
%_libdir/libtranscribe.so
%_libdir/libggml_transcribe.so
%_libdir/libggml_base_transcribe.so
%_libdir/transcribe-link.json

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md THIRD-PARTY-LICENSES.md docs build-options.txt
%_bindir/transcribe-cli
%_bindir/transcribe-quantize
%_bindir/transcribe-bench

%files cpu
%dir %backenddir
%backenddir/libggml-cpu*.so

%if_with cuda
%files cuda
%dir %backenddir
%backenddir/libggml-cuda*.so
%endif

%if_with vulkan
%files vulkan
%dir %backenddir
%backenddir/libggml-vulkan*.so
%endif

%changelog
* Thu Jul 30 2026 Alexey Shabalin <shaba@altlinux.org> 0.1.3-alt3
- Make the CUDA and Vulkan backends optional: libtranscribe0 now requires
  the CPU backend only, so installing the library no longer pulls in the
  NVIDIA and Vulkan stacks.

* Wed Jul 29 2026 Alexey Shabalin <shaba@altlinux.org> 0.1.3-alt2
- Build without BLAS.

* Tue Jul 28 2026 Alexey Shabalin <shaba@altlinux.org> 0.1.3-alt1
- Initial build for ALT Sisyphus.
