%define soversion 1

Name: whisper-cpp
Version: 1.8.6
Release: alt1

Summary: Port of OpenAI's Whisper model in C/C++
Group: Sound
License: MIT
Url: https://github.com/ggerganov/whisper.cpp

ExcludeArch: %ix86

Source: %name-%version.tar

Patch0: %name-%version.patch
Patch1: whisper-cpp-1.7.5-alt-cmake-fix-destination-pkgconfig.patch
Patch2: whisper-cpp-1.8.4-alt-fix-ggml-lib-names-to-resolve-conflict.patch
Patch3: whisper-cpp-1.8.4-alt-fix-test-segfaults.patch
Patch4: whisper-cpp-1.8.4-alt-change-default-ggml-model.patch

Requires: lib%name%soversion = %EVR
Requires: %name-ggml-base

# cuda won't build using gcc15, gcc14 is required
BuildRequires: cmake gcc-c++ gcc14-c++ git libstdc++-devel-static ctest ccache 
BuildRequires: libavdevice-devel libpostproc-devel libavfilter-devel libswscale-devel
BuildRequires: libswresample-devel libavcodec-devel libavformat-devel libavutil-devel
BuildRequires: vulkan-tools libvulkan-devel glslc glslang spirv-headers
%ifarch x86_64
BuildRequires: nvidia-cuda-toolkit nvidia-cuda-devel-static
%endif

%package -n lib%name%soversion
Summary: Shared libraries for whisper-cpp.
Group: System/Libraries
%ifarch x86_64
%filter_from_requires /debug64(libcuda\.so\.1)/d
%endif

%package -n lib%name-devel
Summary: Development files for lib%name%soversion.
Group: Development/C++
Requires: lib%name%soversion = %EVR

%package -n %name-ggml-base
Summary: Base ggml model.
Group: Other
Requires: %name

%description
High-performance inference of OpenAI's Whisper automatic speech
recognition (ASR) model.

%description -n lib%name%soversion
Contains shared libraries for OpenAI's Whisper automatic speech
recognition (ASR) model.

%description -n lib%name-devel
Contains development files for lib%name%soversion.

%description -n %name-ggml-base
Contains ggml-base.bin model.

%prep
%setup
%autopatch -p1

%build
export CUDAHOSTCXX=/usr/bin/g++-14
%cmake -DWHISPER_BUILD_TESTS=ON \
    -DWHISPER_FFMPEG=ON \
    -DGGML_NATIVE=OFF \
    -DGGML_BACKEND_DL=ON \
    -DGGML_BACKEND_DIR=%_libdir/%name \
    -DDEFAULT_MODEL=%_datadir/%name/ggml-base.bin \
    -DGGML_VULKAN=ON \
    -DCMAKE_CUDA_HOST_COMPILER=/usr/bin/g++-14 \
%ifarch x86_64
    -DGGML_CPU_ALL_VARIANTS=ON \
    -DGGML_CUDA=ON \
%endif
    %nil
%cmake_build

%install
%cmakeinstall_std
install -Dpm644 models/ggml-base.bin -t %buildroot%_datadir/%name

%check
%ifarch x86_64
export GGML_BACKEND_PATH=$PWD/%_cmake__builddir/bin/libggml-cpu-x64.so
%else
export GGML_BACKEND_PATH=$PWD/%_cmake__builddir/bin/libggml-cpu.so
%endif
%ctest

%files
%_bindir/whisper-bench
%_bindir/whisper-cli
%_bindir/whisper-server
%_bindir/whisper-quantize
%_bindir/whisper-vad-speech-segments

%files -n lib%name%soversion
%_libdir/libwhisper.so.%{soversion}*
%_libdir/libggml_whisper.so.*
%_libdir/libggml_base_whisper.so.*
%_libdir/%name/libggml-cpu*.so
%_libdir/%name/libggml-vulkan.so
%ifarch x86_64
%_libdir/%name/libggml-cuda.so
%endif

%files -n lib%name-devel
%_libdir/libwhisper.so
%_libdir/libggml_whisper.so
%_libdir/libggml_base_whisper.so
%_libdir/cmake/*
%_includedir/*
%_libdir/pkgconfig/whisper.pc

%files -n %name-ggml-base
%_datadir/%name/ggml-base.bin

%changelog
* Tue Jun 09 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 1.8.6-alt1
- Updated from 1.8.4 to 1.8.6.

* Tue May 26 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 1.8.4-alt2
- The nvcc-12.9 compiler doesn't support gcc15. gcc14 is required
  to build with CUDA support.

* Thu Mar 26 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 1.8.4-alt1
- New version 1.8.4.
- Added Vulkan GPU support.
- Added CUDA GPU support.

* Tue Sep 23 2025 Evgeniy Gorbanyov <esgor@altlinux.org> 1.7.6-alt1
- New version 1.7.6.

* Tue Jun  3 2025 Evgeniy Gorbanyov <esgor@altlinux.org> 1.7.5-alt1
- Initial build for Sisyphus.
