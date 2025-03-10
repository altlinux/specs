# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%ifarch x86_64
%def_with cuda
%else
%def_without cuda
%endif

Name: llama.cpp
Version: 4855
Release: alt1
Epoch: 1
Summary: LLM inference in C/C++
License: MIT
Group: Sciences/Computer science
Url: https://github.com/ggerganov/llama.cpp
ExcludeArch: %ix86
Requires: %name-cpu = %EVR
%if_with cuda
Requires: %name-cuda = %EVR
%filter_from_requires /(libcudart\.so\.12)/d
%filter_from_requires /debug64(libcuda\.so\.1)/d
%endif

Source: %name-%version.tar
Source1: kompute-0.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libgomp-devel
BuildRequires: libstdc++-devel-static
%if_with cuda
BuildRequires: gcc12-c++
BuildRequires: nvidia-cuda-devel-static
%endif
%{?!_without_check:%{?!_disable_check:
BuildRequires: ctest
BuildRequires: tinyllamas-gguf
}}

%description
Plain C/C++ implementation (of inference of many LLM models) without
dependencies. AVX, AVX2, AVX512, and AMX support for x86 architectures.
Mixed F16/F32 precision. 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and
8-bit integer quantization for faster inference and reduced memory use.
Supports CPU, GPU, and hybrid CPU+GPU inference.

Supported models:

   LLaMA, LLaMA 2, Mistral 7B, Mixtral MoE, Falcon, Chinese LLaMA /
   Alpaca and Chinese LLaMA-2 / Alpaca-2, Vigogne (French), Koala,
   Baichuan 1 & 2 + derivations, Aquila 1 & 2, Starcoder models, Refact,
   Persimmon 8B, MPT, Bloom, Yi models, StableLM models, Deepseek models,
   Qwen models, PLaMo-13B, Phi models, GPT-2, Orion 14B, InternLM2,
   CodeShell, Gemma, Mamba, Grok-1, Xverse, Command-R models, SEA-LION,
   GritLM-7B + GritLM-8x7B, OLMo, GPT-NeoX + Pythia,  Snowflake-Arctic
   MoE, Smaug, Poro 34B, Bitnet b1.58 models, Flan T5, Open Elm models,
   ChatGLM3-6b + ChatGLM4-9b + GLMEdge-1.5b + GLMEdge-4b, SmolLM,
   EXAONE-3.0-7.8B-Instruct, FalconMamba Models, Jais, Bielik-11B-v2.3,
   RWKV-6, QRWKV-6, GigaChat-20B-A3B

Multimodal models:

   LLaVA 1.5 models, BakLLaVA, Obsidian, ShareGPT4V, MobileVLM 1.7B/3B
   models, Yi-VL, Mini CPM, Moondream, Bunny, GLM-EDGE, Qwen2-VL

NOTE 1: For data format conversion script to work you will need to:

  pip3 install -r /usr/share/llama.cpp/requirements.txt

NOTE 2:
  MODELS ARE NOT PROVIDED. You'll need to download them from the original
  sites (or Hugging Face Hub).

Overall this is all raw and EXPERIMENTAL, no warranty, no support.

%package -n libllama
Summary: Shared libraries for llama.cpp
Group: System/Libraries

%description -n libllama
%summary.

%package -n libllama-devel
Summary: Development files for llama.cpp
Group: Development/C
Requires: libllama = %EVR

%description -n libllama-devel
%summary.

%package cpu
Summary: %name tools including backend for CPU
Group: Sciences/Computer science
Requires: libllama = %EVR
AutoReqProv: nopython3
Requires: python3
Requires: python3(argparse)
Requires: python3(glob)
Requires: python3(os)
Requires: python3(pip)
Requires: python3(struct)
%add_findreq_skiplist %_datadir/%name/examples/*

%description cpu
%summary.

%package cuda
Summary: %name backend for NVIDIA GPU
Group: Sciences/Computer science
Requires: libnvidia-ptxjitcompiler
Requires: %name-cpu = %EVR

%description cuda
%summary.

%prep
%setup
tar xf %SOURCE1 -C ggml/src/ggml-kompute
cat <<-EOF >> cmake/build-info.cmake
	set(BUILD_NUMBER %version)
	set(GGML_BUILD_NUMBER %version)
	set(BUILD_COMMIT "%release")
EOF
sed -i '/POSITION_INDEPENDENT_CODE/s/PROPERTIES/& SOVERSION 0.0.%version/' ggml/src/CMakeLists.txt src/CMakeLists.txt
sed -i 's/POSITION_INDEPENDENT_CODE/SOVERSION 0.0.%version &/' ggml/cmake/ggml-config.cmake.in

%build
# Unless -DCMAKE_SKIP_BUILD_RPATH=yes CMake fails to strip build time RPATH
# from (installed) binaries.
export NVCC_PREPEND_FLAGS=-ccbin=g++-12
%cmake \
	-DCMAKE_SKIP_BUILD_RPATH=yes \
	-DLLAMA_BUILD_TESTS=ON \
	-DLLAMA_CURL=ON \
	-DGGML_BACKEND_DL=ON \
	-DGGML_CPU=ON \
%ifarch x86_64
	-DGGML_CPU_ALL_VARIANTS=ON \
%endif
%if_with cuda
	-DGGML_CUDA=ON \
	-DCMAKE_CUDA_ARCHITECTURES='52-virtual;80-virtual' \
%endif
	%nil
grep -E 'LLAMA|GGML' %_cmake__builddir/CMakeCache.txt | sort | tee build-options.txt
%cmake_build
find -name '*.py' | xargs sed -i '1s|#!/usr/bin/env python3|#!%__python3|'
LD_LIBRARY_PATH=%_cmake__builddir/bin %_cmake__builddir/bin/llama-cli --completion-bash > llama.bash

%install
%cmake_install
# Python requirements files.
install -Dpm644 requirements.txt -t %buildroot%_datadir/%name
cp -a requirements -t %buildroot%_datadir/%name
# Additional data.
cp -rp prompts -t %buildroot%_datadir/%name
cp -rp grammars -t %buildroot%_datadir/%name
# Not all examples.
install -Dp examples/*.sh -t %buildroot%_datadir/%name/examples
install -Dp examples/*.py -t %buildroot%_datadir/%name/examples
# We need to run the tests, not install them.
rm %buildroot%_bindir/test-*
# Completions.
install -Dpm644 llama.bash %buildroot%_datadir/bash-completion/completions/llama-cli
printf '%%s\n' llama-server llama-simple llama-run |
	xargs -ti ln -s llama-cli %buildroot%_datadir/bash-completion/completions/{}

%check
# Local path are more useful for debugging becasue they are not stripped by default.
%dnl export LD_LIBRARY_PATH=%buildroot%_libdir:%buildroot%_libexecdir/llama PATH+=:%buildroot%_bindir
export LD_LIBRARY_PATH=$PWD/%_cmake__builddir/bin PATH+=:$PWD/%_cmake__builddir/bin
llama-cli --version
llama-cli --version |& grep -Fx 'version: %version (%release)'
# test-eval-callback wants network.
%ctest -j1 -E test-eval-callback
llama-cli -m %_datadir/tinyllamas/stories260K.gguf -p "Hello" -s 42 -n 500
llama-cli -m %_datadir/tinyllamas/stories260K.gguf -p "Once upon a time" -s 55 -n 33 |
	grep 'Once upon a time, there was a boy named Tom. Tom had a big box of colors.'

%files

%files -n libllama
%_libdir/libllama.so.0.0.%version
%_libdir/libggml.so.0.0.%version
%_libdir/libggml-base.so.0.0.%version

%files -n libllama-devel
%_libdir/libllama.so
%_libdir/libggml.so
%_libdir/libggml-base.so
%_includedir/llama*.h
%_includedir/gguf.h
%_includedir/ggml*.h
%_cmakedir/ggml
%_cmakedir/llama
%_pkgconfigdir/llama.pc

%files cpu
%define _customdocdir %_docdir/%name
%doc LICENSE README.md docs build-options.txt
%_bindir/llama-*
%_bindir/convert*.py
%_datadir/%name
%dir %_libexecdir/llama
%_libexecdir/llama/libggml-cpu*.so
%_datadir/bash-completion/completions/llama-*

%if_with cuda
%files cuda
%dir %_libexecdir/llama
%_libexecdir/llama/libggml-cuda.so
%endif

%changelog
* Mon Mar 10 2025 Vitaly Chikunov <vt@altlinux.org> 1:4855-alt1
- Update to b4855 (2025-03-07).
- Enable CUDA backend (for NVIDIA GPU) in llama.cpp-cuda package.
- Disable BLAS backend (issues/12282).
- Install bash-completions.

* Tue Jul 23 2024 Vitaly Chikunov <vt@altlinux.org> 1:3441-alt1
- Update to b3441 (2024-07-23).
- spec: Package libllama and libllama-devel (ALT#50962).
- spec: Use upstream install procedure; as a consequence, some binary names are
  changed.

* Mon Jun 03 2024 Vitaly Chikunov <vt@altlinux.org> 1:3072-alt1.20240603
- Update to b3072 (2024-06-03).
- The version scheme now matches the upstream build number more closely,
  instead of using the commit date.
- Build with libcurl and OpenBLAS support.

* Tue May 28 2024 Vitaly Chikunov <vt@altlinux.org> 20240527-alt1
- Update to b3012 (2024-05-27).

* Mon Feb 26 2024 Vitaly Chikunov <vt@altlinux.org> 20240225-alt1
- Update to b2259 (2024-02-25).

* Fri Oct 20 2023 Vitaly Chikunov <vt@altlinux.org> 20231019-alt1
- Update to b1400 (2023-10-19).
- Install experimental converters (convert- prefixed tools).

* Sun Jul 30 2023 Vitaly Chikunov <vt@altlinux.org> 20230728-alt1
- Update to master-8a88e58 (2023-07-28).

* Sun May 14 2023 Vitaly Chikunov <vt@altlinux.org> 20230513-alt1
- Build master-bda4d7c (2023-05-13).

* Wed Apr 19 2023 Vitaly Chikunov <vt@altlinux.org> 20230419-alt1
- Build master-6667401 (2023-04-19).
