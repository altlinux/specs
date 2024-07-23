# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: llama.cpp
Version: 3441
Release: alt1
Epoch: 1
Summary: LLM inference in C/C++
License: MIT
Group: Sciences/Computer science
Url: https://github.com/ggerganov/llama.cpp
Requires: libllama = %EVR

ExclusiveArch: aarch64 x86_64
Source: %name-%version.tar

AutoReqProv: nopython3
Requires: python3
Requires: python3(argparse)
Requires: python3(glob)
Requires: python3(os)
Requires: python3(pip)
Requires: python3(struct)
%add_findreq_skiplist %_datadir/%name/examples/*

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libopenblas-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: ctest
BuildRequires: tinyllamas-gguf
}}

%description
Plain C/C++ implementation (of inference of many LLM models) without
dependencies. AVX, AVX2 and AVX512 support for x86 architectures.
Mixed F16/F32 precision. 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and
8-bit integer quantization for faster inference and reduced memory use.
Runs on the CPU.

Supported models:

   LLaMA, LLaMA 2, Mistral 7B, Mixtral MoE, Falcon, Chinese LLaMA /
   Alpaca and Chinese LLaMA-2 / Alpaca-2, Vigogne (French), Koala,
   Baichuan 1 & 2 + derivations, Aquila 1 & 2, Starcoder models, Refact,
   Persimmon 8B, MPT, Bloom, Yi models, StableLM models, Deepseek models,
   Qwen models, PLaMo-13B, Phi models, GPT-2, Orion 14B, InternLM2,
   CodeShell, Gemma, Mamba, Grok-1, Xverse, Command-R models, SEA-LION,
   GritLM-7B + GritLM-8x7B, OLMo, GPT-NeoX + Pythia

Multimodal models:

   LLaVA 1.5 models, BakLLaVA, Obsidian, ShareGPT4V, MobileVLM 1.7B/3B
   models, Yi-VL, Mini CPM, Moondream, Bunny

NOTE 1: You will need to:

  pip3 install -r /usr/share/llama.cpp/requirements.txt

for data format conversion scripts to work.

NOTE 2:
  MODELS ARE NOT PROVIDED. You need to download them from original
  sites and place them into "./models" directory.

  For example, LLaMA downloaded via public torrent link is 220 GB.

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

%prep
%setup
cat <<-EOF >> cmake/build-info.cmake
	set(BUILD_NUMBER %version)
	set(BUILD_COMMIT "%release")
EOF
sed -i '/lib\/pkgconfig/s/lib/${CMAKE_INSTALL_LIBDIR}/' CMakeLists.txt
sed -i '/POSITION_INDEPENDENT_CODE/s/PROPERTIES/& SOVERSION 0.0.%version/' ggml/src/CMakeLists.txt src/CMakeLists.txt
sed -i 's/@PROJECT_VERSION@/0.0.%version/' cmake/llama.pc.in

%build
# Unless -DCMAKE_SKIP_BUILD_RPATH=yes CMake fails to strip build time RPATH
# from (installed) binaries.
%cmake \
	-DCMAKE_SKIP_BUILD_RPATH=yes \
	-DGGML_BLAS=ON \
	-DGGML_BLAS_VENDOR=OpenBLAS \
	-DLLAMA_CURL=ON \
	-DLLAMA_BUILD_TESTS=OFF \
	%nil
grep -E 'LLAMA|GGML' %_cmake__builddir/CMakeCache.txt | sort | tee build-options.txt
%cmake_build
find -name '*.py' | xargs sed -i '1s|#!/usr/bin/env python3|#!%__python3|'

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

# llava belongs to examples which we don't install.
rm %buildroot%_libdir/libllava_shared.so

%check
export LD_LIBRARY_PATH=$PWD/%_cmake__builddir/src:$PWD/%_cmake__builddir/ggml/src
%_cmake__builddir/bin/llama-cli --version |& grep -Fx 'version: %version (%release)'
# test-eval-callback wants network.
%ctest -j1 -E test-eval-callback
PATH=%buildroot%_bindir:$PATH
llama-cli -m %_datadir/tinyllamas/stories260K.gguf -p "Hello" -s 42 -n 500
llama-cli -m %_datadir/tinyllamas/stories260K.gguf -p "Once upon a time" -s 55 -n 33 |
	grep 'Once upon a time, there was a boy named Tom. Tom had a big box of colors.'

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md docs build-options.txt
%_bindir/llama-*
%_bindir/convert*.py
%_datadir/%name

%files -n libllama
%_libdir/libggml.so.0.0.%version
%_libdir/libllama.so.0.0.%version

%files -n libllama-devel
%_includedir/ggml*.h
%_includedir/llama.h
%_cmakedir/llama
%_pkgconfigdir/llama.pc
%_libdir/libggml.so
%_libdir/libllama.so

%changelog
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
