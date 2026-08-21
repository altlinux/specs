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

Name: llama.cpp
Version: 10549
Release: alt1
Epoch: 1
Summary: LLM inference in C/C++
License: MIT
Group: Sciences/Computer science
# https://ggml.ai/
Url: https://github.com/ggml-org/llama.cpp
Vcs: https://github.com/ggml-org/llama.cpp.git
ExcludeArch: %ix86
Requires: %name-cpu = %EVR
%if_with cuda
Requires: %name-cuda = %EVR
%filter_from_requires /(libcudart\.so\.12)/d
%filter_from_requires /debug64(libcuda\.so\.1)/d
%endif
%if_with vulkan
Requires: %name-vulkan = %EVR
%endif

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: libcurl-devel
BuildRequires: libgomp-devel
BuildRequires: libssl-devel
BuildRequires: libstdc++-devel-static
%if_with cuda
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
BuildRequires: python3-module-jinja2
BuildRequires: tinyllamas-gguf
}}

%description
Plain C/C++ implementation (of inference of many LLM models) without
dependencies. AVX, AVX2, AVX512, and AMX support for x86 architectures.
Mixed F16/F32 precision. 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and
8-bit integer quantization for faster inference and reduced memory use.
Supports CPU, GPU, and hybrid CPU+GPU inference.

Supported models:

   LLaMA models, Mistral 7B, Mixtral MoE, Falcon, Chinese LLaMA /
   Alpaca and Chinese LLaMA-2 / Alpaca-2, Vigogne (French), Koala,
   Baichuan 1 & 2 + derivations, Aquila 1 & 2, Starcoder models, Refact,
   Persimmon 8B, MPT, Bloom, Yi models, StableLM models, Deepseek models,
   Qwen models, PLaMo-13B, Phi models, GPT-2, Orion 14B, InternLM2,
   CodeShell, Gemma, Mamba, Grok-1, Xverse, Command-R models, SEA-LION,
   GritLM-7B + GritLM-8x7B, OLMo, GPT-NeoX + Pythia,  Snowflake-Arctic
   MoE, Smaug, Poro 34B, Bitnet b1.58 models, Flan T5, Open Elm models,
   ChatGLM3-6b + ChatGLM4-9b + GLMEdge-1.5b + GLMEdge-4b, SmolLM,
   EXAONE-3.0-7.8B-Instruct, FalconMamba Models, Jais, Bielik-11B-v2.3,
   RWKV-6, QRWKV-6, GigaChat-20B-A3B, Trillion-7B-preview, Ling models,
   LFM2 models, Hunyuan models, BailingMoeV2 (Ring/Ling 2.0) models

Multimodal models:

   LLaVA 1.5 models, BakLLaVA, Obsidian, ShareGPT4V, MobileVLM 1.7B/3B
   models, Yi-VL, Mini CPM, Moondream, Bunny, GLM-EDGE, Qwen2-VL,
   LFM2-VL

NOTE:
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
Conflicts: libwhisper-cpp-devel

%description -n libllama-devel
%summary.

%package cpu
Summary: %name tools including backend for CPU
Group: Sciences/Computer science
Requires: libllama = %EVR
Conflicts: %name-convert < %EVR
AutoReqProv: nopython3
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

%package vulkan
Summary: %name backend for GPU
Group: Sciences/Computer science
Requires: %name-cpu = %EVR

%description vulkan
%summary.

%prep
%setup
%autopatch -p1
commit=$(awk '$2=="b%version"{print$1}' .gear/tags/list)
cat <<-EOF >> cmake/build-info.cmake
	set(BUILD_NUMBER %version)
	set(GGML_BUILD_NUMBER %version)
	set(BUILD_COMMIT "${commit::8} [%release]")
EOF
# We do not have Internet access (issues/13371).
perl -00 -ni -e 'print unless /_URL/' tests/test-arg-parser.cpp

%build
%define optflags_debug -g1
# Unless -DCMAKE_SKIP_BUILD_RPATH=yes CMake fails to strip build time RPATH
# from (installed) binaries.
# -Xcompiler=-g1: host-side debug info, otherwise libggml-cuda.so has
# empty .debug_info and 056-debuginfo.brp terminates the build.
export NVCC_PREPEND_FLAGS='-ccbin=g++-12 -Xcompiler=-g1'
%cmake \
	-DCMAKE_SKIP_BUILD_RPATH=yes \
	-DLLAMA_BUILD_TESTS=ON \
	-DGGML_BACKEND_DL=ON \
	-DGGML_BACKEND_DIR=%_libexecdir/llama \
	-DGGML_CPU=ON \
	-DGGML_RPC=ON \
	-DLLAMA_USE_PREBUILT_UI=OFF \
%ifarch x86_64 riscv64
	-DGGML_CPU_ALL_VARIANTS=ON \
%endif
%if_with cuda
	-DGGML_CUDA=ON \
	-DCMAKE_CUDA_ARCHITECTURES='52-virtual;80-virtual' \
%endif
%if_with vulkan
	-DGGML_VULKAN=ON \
%endif
	%nil
grep -E 'LLAMA|GGML' %_cmake__builddir/CMakeCache.txt | sort | tee build-options.txt
%cmake_build
find -name '*.py' | xargs sed -i '1s|#!/usr/bin/env python3|#!%__python3|'
LD_LIBRARY_PATH=%_cmake__builddir/bin %_cmake__builddir/bin/llama-server --completion-bash > llama.bash
LD_LIBRARY_PATH=%_cmake__builddir/bin .gear/gen-manpage %_cmake__builddir/bin/llama-server > llama-server.1

%install
%cmake_install
# Python requirements files.
install -Dpm644 requirements.txt -t %buildroot%_datadir/%name
cp -a requirements -t %buildroot%_datadir/%name
# Additional data.
cp -rp grammars -t %buildroot%_datadir/%name
# Not all examples.
install -Dp examples/*.sh -t %buildroot%_datadir/%name/examples
install -Dp examples/*.py -t %buildroot%_datadir/%name/examples
# We need to run the tests, not install them.
rm %buildroot%_bindir/test-*
# Completions.
install -Dpm644 llama.bash %buildroot%_datadir/bash-completion/completions/llama-server
printf '%%s\n' llama-cli llama-simple llama-run llama-mtmd-cli |
	xargs -ti ln -s llama-server %buildroot%_datadir/bash-completion/completions/{}
install -Dpm644 llama-server.1 -t %buildroot%_man1dir
# Parametric systemd template + config dir (see .gear/llama.env.example).
install -Dpm644 .gear/llama-server@.service %buildroot%_unitdir/llama-server@.service
install -dm755 %buildroot%_sysconfdir/llama

%check
( ! cuobjdump --list-elf %buildroot%_libexecdir/llama/libggml-cuda.so | grep -F -v -e .cubin )
( ! cuobjdump --list-ptx %buildroot%_libexecdir/llama/libggml-cuda.so | grep -F -v -e .sm_80.ptx -e .sm_52.ptx )
# Local path are more useful for debugging becasue they are not stripped by default.
export LD_LIBRARY_PATH=$PWD/%_cmake__builddir/bin PATH+=:$PWD/%_cmake__builddir/bin
llama-server --version
llama-server --version |& grep -Ex 'version: \S+ \(build %version, commit \S+ \[%release\]\)'
# test-eval-callback and test-tokenizers-ggml-vocabs want network.
# test-save-load-state/-state-restore-fragmented require the test-download-model fixture (no network).
# test-thread-safety requires GPU; test-recurrent-state-rollback (MTP) is not runnable w/o CUDA.
# test-generate-models (target test-llama-archs) needs a loadable ggml backend, absent in %check.
%ctest -E 'test-download-model|test-eval-callback|test-tokenizers-ggml-vocabs|test-state-restore-fragmented|test-save-load-state|test-generate-models|test-thread-safety|test-recurrent-state-rollback'
llama-completion -m /usr/share/tinyllamas/stories260K.gguf -p "Hello" -s 42 -n 500 2>/dev/null
llama-completion -m /usr/share/tinyllamas/stories260K.gguf -p "Once upon a time" -s 55 -n 33 2>/dev/null |
	grep "Once upon a time, in a tidy cat, there was a little girl named Lily."

%files

%files -n libllama
# SONAME follows upstream's own versioning (LLAMA_VERSION_BASE/_MAJOR in
# CMakeLists.txt) rather than our build number — no local SOVERSION hacks.
%_libdir/libllama.so.*
%_libdir/libllama-common.so.*
%_libdir/libggml.so.*
%_libdir/libggml-base.so.*
%_libdir/libmtmd.so.*

%files -n libllama-devel
%_libdir/libllama.so
%_libdir/libllama-common.so
%_libdir/libggml.so
%_libdir/libggml-base.so
%_libdir/libmtmd.so
%_includedir/llama*.h
%_includedir/gguf.h
%_includedir/ggml*.h
%_includedir/mtmd*.h
%_cmakedir/ggml
%_cmakedir/llama
%_pkgconfigdir/llama.pc

%post cpu
%post_systemd 'llama-server@*.service'

%preun cpu
%preun_systemd 'llama-server@*.service'

%files cpu
%define _customdocdir %_docdir/%name
%doc LICENSE README.md docs build-options.txt .gear/llama.env.example
%_bindir/llama*
%_bindir/ggml-rpc-server
%_libdir/libllama-*-impl.so
%_unitdir/llama-server@.service
%dir %_sysconfdir/llama
%dir %_datadir/%name
%dir %_datadir/%name/examples
%_datadir/%name/examples/*.sh
%_datadir/%name/examples/*.py
%_datadir/%name/requirements*
%_datadir/%name/grammars
%dir %_libexecdir/llama
%_libexecdir/llama/libggml-cpu*.so
%_libexecdir/llama/libggml-rpc.so
%_datadir/bash-completion/completions/llama-*
%_man1dir/llama-server.1*

%if_with cuda
%files cuda
%dir %_libexecdir/llama
%_libexecdir/llama/libggml-cuda.so
%endif

%if_with vulkan
%files vulkan
%dir %_libexecdir/llama
%_libexecdir/llama/libggml-vulkan.so
%endif

%changelog
* Fri Aug 21 2026 Alexey Shabalin <shaba@altlinux.org> 1:10549-alt1
- Update to b10549.

* Mon Aug 17 2026 Alexey Shabalin <shaba@altlinux.org> 1:10456-alt1
- Update to b10456.

* Fri Aug 14 2026 Alexey Shabalin <shaba@altlinux.org> 1:10430-alt1
- Update to b10430.
- Drop the local SOVERSION sed hacks for libllama/libmtmd/libllama-common.

* Wed Aug 12 2026 Alexey Shabalin <shaba@altlinux.org> 1:10380-alt1
- Update to b10380.

* Thu Jul 23 2026 Alexey Shabalin <shaba@altlinux.org> 1:10103-alt1
- Update to b10103.
- Embed prebuilt WebUI again (ALT#59598).

* Mon Jul 20 2026 Alexey Shabalin <shaba@altlinux.org> 1:10069-alt1
- Update to b10069.

* Wed Jul 15 2026 Anton Farygin <rider@altlinux.org> 1:10015-alt1
- Update to b10015.
- llama-rpc-server renamed to ggml-rpc-server (follow upstream naming).

* Thu Jul 02 2026 Ilya Sorochan <k0tran@altlinux.org> 1:9804-alt2
- NMU: fix riscv64 FTBFS.

* Fri Jun 26 2026 Alexey Shabalin <shaba@altlinux.org> 1:9804-alt1
- Update to b9804.

* Mon Jun 22 2026 Anton Farygin <rider@altlinux.org> 1:9758-alt1
- Update to b9758.

* Fri Jun 19 2026 Alexey Shabalin <shaba@altlinux.org> 1:9728-alt1
- Update to b9728.

* Fri Jun 05 2026 Alexey Shabalin <shaba@altlinux.org> 1:9524-alt1
- Update to b9524.
- Add parametric llama-server@.service systemd unit.

* Wed May 20 2026 Vitaly Chikunov <vt@altlinux.org> 1:9245-alt1
- Update to b9245 (2026-05-20).

* Mon Apr 06 2026 Vitaly Chikunov <vt@altlinux.org> 1:8681-alt1
- Update to b8681 (2026-04-06).

* Sun Mar 22 2026 Vitaly Chikunov <vt@altlinux.org> 1:8470-alt1
- Update to b8470 (2026-03-22).

* Tue Mar 03 2026 Vitaly Chikunov <vt@altlinux.org> 1:8192-alt1
- Update to b8192 (2026-03-03).

* Fri Feb 13 2026 Vitaly Chikunov <vt@altlinux.org> 1:8018-alt1
- Update to b8018 (2026-02-12).

* Sat Jan 24 2026 Vitaly Chikunov <vt@altlinux.org> 1:7819-alt1
- Update to b7819 (2026-01-23).
- Responses API support (partial).

* Sun Dec 14 2025 Vitaly Chikunov <vt@altlinux.org> 1:7388-alt1
- Update to b7388 (2025-12-13).
- llama-cli: New CLI experience (with the old moved to llama-completion).
- llama-server: Live model switching.
- Messages API support.

* Fri Nov 21 2025 Vitaly Chikunov <vt@altlinux.org> 1:7127-alt1
- Update to b7127 (2025-11-21).
- spec: Remove llama.cpp-convert package.
- model: detect GigaChat3-10-A1.8B as deepseek lite.

* Tue Oct 28 2025 Vitaly Chikunov <vt@altlinux.org> 1:6869-alt1
- Update to b6869 (2025-10-28).

* Sat Sep 06 2025 Vitaly Chikunov <vt@altlinux.org> 1:6397-alt1
- Update to b6397 (2025-09-06).
- Python-based model conversion scripts are sub-packaged. Note that they are
  not supported and are provided as-is.

* Sat Aug 09 2025 Vitaly Chikunov <vt@altlinux.org> 1:6121-alt1
- Update to b6121 (2025-08-08).

* Wed Jun 25 2025 Vitaly Chikunov <vt@altlinux.org> 1:5753-alt1
- Update to b5753 (2025-06-24).
- Install an experimental rpc backend and server. The rpc code is a
  proof-of-concept, fragile, and insecure.

* Sat May 10 2025 Vitaly Chikunov <vt@altlinux.org> 1:5332-alt1
- Update to b5332 (2025-05-09), with vision support in llama-server.
- Enable Vulkan backend (for GPU) in llama.cpp-vulkan package.

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
