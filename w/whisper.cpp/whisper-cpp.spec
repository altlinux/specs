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

%define soversion 1
%define oldname whisper-cpp

Name: whisper.cpp
Version: 1.9.1
Release: alt4

Summary: Port of OpenAI's Whisper model in C/C++
Group: Sound
License: MIT
Url: https://github.com/ggerganov/whisper.cpp
Vcs: https://github.com/ggml-org/whisper.cpp.git

Provides: %oldname = %EVR
Obsoletes: %oldname < %EVR

ExcludeArch: %ix86

Source: %name-%version.tar

Patch0: %name-%version.patch
Patch1: whisper-cpp-1.8.4-alt-fix-ggml-lib-names-to-resolve-conflict.patch
Patch2: whisper-cpp-1.8.4-alt-change-default-ggml-model.patch
Patch3: whisper-cpp-1.9.1-alt-fix-test-segfaults.patch
Patch4: whisper-cpp-1.9.1-alt-find-backends-without-proc.patch

Requires: libwhisper%soversion = %EVR
Requires: %name-cpu = %EVR

%if_with cuda
Requires: %name-cuda = %EVR
%filter_from_requires /debug64(libcuda\.so\.1)/d
%endif
%if_with vulkan
Requires: %name-vulkan = %EVR
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel-static
BuildRequires: libavcodec-devel
BuildRequires: libavdevice-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libpostproc-devel
BuildRequires: libSDL2-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
%if_with cuda
# cuda requires gcc12
BuildRequires: gcc12-c++
BuildRequires: nvidia-cuda-toolkit nvidia-cuda-devel-static
%endif
%if_with vulkan
BuildRequires: glslang
BuildRequires: glslc
BuildRequires: libvulkan-devel
BuildRequires: spirv-headers
BuildRequires: vulkan-tools
%endif
%{?!_without_check:%{?!_disable_check:
BuildRequires: ctest
}}

%description
High-performance inference of OpenAI's Whisper automatic speech
recognition (ASR) model.

NOTE:
  Only the base ggml models are packaged, in the optional subpackages
  %name-ggml-base (multilingual, used by default) and %name-ggml-base.en
  (English-only). Other models can be downloaded from
  https://huggingface.co/ggerganov/whisper.cpp and passed with the
  -m/--model option.

%package -n libwhisper%soversion
Summary: Shared libraries for %name
Group: System/Libraries
# The CPU backend is the only one required: it always works and is small.
# The CUDA and Vulkan backends are optional, install them explicitly.
Requires: %name-cpu = %EVR
Provides: lib%oldname%soversion = %EVR
Obsoletes: lib%oldname%soversion < %EVR

%description -n libwhisper%soversion
Contains shared libraries for OpenAI's Whisper automatic speech
recognition (ASR) model.

%package -n libwhisper-devel
Summary: Development files for libwhisper%soversion
Group: Development/C++
Requires: libwhisper%soversion = %EVR
Provides: lib%oldname-devel = %EVR
Obsoletes: lib%oldname-devel < %EVR
Conflicts: libllama-devel

%description -n libwhisper-devel
Contains development files for libwhisper%soversion.

%package -n %name-ggml-base
Summary: Whisper base multilingual model in ggml format
Group: Other
BuildArch: noarch

%description -n %name-ggml-base
Contains the ggml-base.bin multilingual model, used by %name tools by
default. The package is optional: models can also be downloaded manually
from https://huggingface.co/ggerganov/whisper.cpp

%package -n %name-ggml-base.en
Summary: Whisper base English-only model in ggml format
Group: Other
BuildArch: noarch

%description -n %name-ggml-base.en
Contains the ggml-base.en.bin English-only model. The package is
optional: models can also be downloaded manually from
https://huggingface.co/ggerganov/whisper.cpp

%package cpu
Summary: %name backend for CPU
Group: Sound
Requires: libwhisper%soversion = %EVR

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

%package stream
Summary: Real-time transcription of audio from microphone
Group: Sound
Requires: libwhisper%soversion = %EVR

%description stream
whisper-stream tool samples the audio every half a second and runs the
transcription continuously.

%package command
Summary: Voice assistant that listens for commands from microphone
Group: Sound
Requires: libwhisper%soversion = %EVR

%description command
whisper-command is a basic voice assistant example: it listens to voice
commands from the microphone and transcribes them.

%prep
%setup
%autopatch -p1

%build
%if_with cuda
export CUDAHOSTCXX=/usr/bin/g++-12
%endif
%cmake -DWHISPER_BUILD_TESTS=ON \
    -DWHISPER_COMMON_FFMPEG=ON \
    -DWHISPER_SDL2=ON \
    -DGGML_NATIVE=OFF \
    -DGGML_BACKEND_DL=ON \
    -DGGML_BACKEND_DIR=%_libdir/%name \
    -DDEFAULT_MODEL=%_datadir/%name/ggml-base.bin \
%if_with vulkan
    -DGGML_VULKAN=ON \
%endif
%if_with cuda
    -DGGML_CUDA=ON \
    -DCMAKE_CUDA_HOST_COMPILER=/usr/bin/g++-12 \
%endif
%ifarch x86_64 riscv64
    -DGGML_CPU_ALL_VARIANTS=ON \
%endif
    %nil
%cmake_build

%install
%cmakeinstall_std
install -Dpm644 models/ggml-base.bin -t %buildroot%_datadir/%name
install -Dpm644 models/ggml-base.en.bin -t %buildroot%_datadir/%name
install -Dpm644 .gear/whisper-server@.service %buildroot%_unitdir/whisper-server@.service
install -Dpm644 .gear/whisper-base.env %buildroot%_sysconfdir/whisper/base.env
install -Dpm644 .gear/whisper-base.en.env %buildroot%_sysconfdir/whisper/base.en.env

# Skip whisper-talk-llama (embeds a copy of llama.cpp) and whisper-lsp.
rm %buildroot%_bindir/whisper-talk-llama
rm %buildroot%_bindir/whisper-lsp

%check
export LD_LIBRARY_PATH=$PWD/%_cmake__builddir/bin PATH+=:$PWD/%_cmake__builddir/bin
%ctest
whisper-bench -m models/ggml-base.bin

%post
%post_systemd 'whisper-server@*.service'

%preun
%preun_systemd 'whisper-server@*.service'

%files
%doc LICENSE README.md .gear/whisper.env.example
%_bindir/whisper-bench
%_bindir/whisper-cli
%_bindir/whisper-server
%_bindir/whisper-quantize
%_bindir/whisper-vad-speech-segments
%_bindir/parakeet-cli
%_bindir/parakeet-quantize
%_unitdir/whisper-server@.service
%dir %_sysconfdir/whisper

%files -n libwhisper%soversion
%_libdir/libwhisper.so.%{soversion}*
%_libdir/libggml_whisper.so.*
%_libdir/libggml_base_whisper.so.*
%_libdir/libparakeet.so.*

%files -n libwhisper-devel
%_libdir/libwhisper.so
%_libdir/libggml_whisper.so
%_libdir/libggml_base_whisper.so
%_libdir/libparakeet.so
%_libdir/cmake/*
%_includedir/*
%_libdir/pkgconfig/whisper.pc
%_libdir/pkgconfig/parakeet.pc

%files -n %name-ggml-base
%_datadir/%name/ggml-base.bin
%config(noreplace) %_sysconfdir/whisper/base.env

%files -n %name-ggml-base.en
%_datadir/%name/ggml-base.en.bin
%config(noreplace) %_sysconfdir/whisper/base.en.env

%files cpu
%_libdir/%name/libggml-cpu*.so

%if_with cuda
%files cuda
%_libdir/%name/libggml-cuda.so
%endif

%if_with vulkan
%files vulkan
%_libdir/%name/libggml-vulkan.so
%endif

%files stream
%_bindir/whisper-stream

%files command
%_bindir/whisper-command

%changelog
* Thu Jul 30 2026 Alexey Shabalin <shaba@altlinux.org> 1.9.1-alt4
- Make the CUDA and Vulkan backends optional: libwhisper0 now requires the
  CPU backend only, so installing the library no longer pulls in the NVIDIA
  and Vulkan stacks.

* Mon Jul 27 2026 Alexey Shabalin <shaba@altlinux.org> 1.9.1-alt3
- Refactor spec to match llama.cpp packaging structure.
- Move gcc12-c++ and vulkan build requirements to their conditional blocks.
- Make ggml model packages optional: the main package no longer requires
  whisper.cpp-ggml-base, models can be downloaded manually instead.
- Package ggml-base.en model as separate optional noarch subpackage.
- Find ggml backends near the executable without /proc (fixes test
  segfaults in hasher, port of the llama.cpp ALT fix).
- Run the full test suite and whisper-bench in %%check.
- Replace whisper-server.service with parametric whisper-server@.service
  (as in llama.cpp): per-instance environment files in /etc/whisper,
  ready-made instances (base, base.en) are shipped with the model packages.
- Build with SDL2: package whisper-stream and whisper-command as separate
  subpackages (whisper-talk-llama and whisper-lsp are not packaged).
- Use WHISPER_COMMON_FFMPEG instead of the deprecated WHISPER_FFMPEG.
- Enable GGML_CPU_ALL_VARIANTS on riscv64 (as in llama.cpp).
- Add .gear/version-up for maintenance with zoryn.

* Tue Jul 21 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 1.9.1-alt2
- Renamed to whisper.cpp (Closes: #59623).
- Added whisper-server.service systemd unit (Closes: #59624).
- Added whisper-cpu, whisper-cuda and whisper-vulkan packages (Closes: #59625).

* Tue Jun 23 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 1.9.1-alt1
- Updated from 1.8.6 to 1.9.1.

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
