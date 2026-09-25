# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,unresolved=relaxed,rpath=relaxed

# Upstream looks for runtime payloads in ../lib/ollama relative to
# /usr/bin/ollama (see ml/path.go); keep the upstream layout.
%define ollama_libdir %_prefix/lib/ollama

%ifarch x86_64
%def_with cuda
%else
%def_without cuda
%endif
%def_with vulkan

Name: ollama
Version: 0.34.4
Release: alt2
Summary: Get up and running with large language models
License: MIT
Group: Sciences/Computer science
URL: https://ollama.com
VCS: https://github.com/ollama/ollama

%if_with cuda
# https://bugzilla.altlinux.org/52911
%filter_from_requires /(libcudart\.so\.%cuda_major)/d
%filter_from_requires /debug64(libcuda\.so\.1)/d
Requires: ollama-cuda = %EVR
%endif

%if_with vulkan
Requires: %name-vulkan = %EVR
%endif
Requires: ollama-cpu = %EVR

ExcludeArch: %ix86

Source: %name-%version.tar
Source1: vendor.tar
Source3: ollama-user.conf
Source4: %name.service
Source5: completions
Source6: models-list.txt
Source7: tags-list.txt
# ALT: Do not auto-install third-party agents from the internet; point the
# user at installation instructions instead.
Patch: alt-no-autoinstall-agents.patch
# gcc < 14 does not support the +sme feature modifier in -march (p11 aarch64)
Patch1: alt-llama-gcc13-no-sme.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd
BuildRequires: rpm-build-golang
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: look
BuildRequires: patchelf

%if_with cuda
BuildRequires(pre): rpm-macros-cuda-toolkit
BuildRequires: %cuda_buildreq
BuildRequires: nvidia-cuda-devel-static
%endif

%if_with vulkan
BuildRequires: glslc
BuildRequires: libvulkan-devel
BuildRequires: spirv-headers
%endif

%{?!_without_check:%{?!_disable_check:
BuildRequires: curl
}}

%description
Ollama lets you use open models with your coding agents
so you can spend less while keeping your data private.

This is a meta-package.

%package cpu
Summary: The main ollama package with CPU runner
Group: Sciences/Computer science

%description cpu
%summary.

%package cuda
Summary: Ollama runner for NVIDIA GPU
Group: Sciences/Computer science
Requires: libnvidia-ptxjitcompiler
Requires: ollama-cpu = %EVR

%description cuda
%summary.

%package vulkan
Summary: Ollama runner for GPU
Group: Sciences/Computer science
Requires: ollama-cpu = %EVR

%description vulkan
%summary.

%prep
%setup -a 1
%autopatch -p1
# Do not bundle CUDA runtime libraries; the system toolkit is used instead.
sed -i '/PRE_INCLUDE_REGEXES/d' llama/server/CMakeLists.txt
# Do not strip the Go binary (brp-debuginfo forbids stripped files).
sed -i 's/"-s -w /"/' cmake/local.cmake

%build
%add_optflags -Wno-unused-function
# ExternalProject sub-builds (llama-server, GPU backends) do not inherit
# %%optflags from the top-level configure; pass them via the environment so
# the libraries carry debug info (brp-debuginfo requirement).
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
# Offline build: use the vendored llama.cpp (see .gear/merge-up.d/) instead
# of fetching it with CMake FetchContent. The Sisyphus llama.cpp package
# cannot be used: ollama pins an exact commit (LLAMA_CPP_VERSION) that the
# repo package never matches, and the build compiles ollama's compat sources
# into the llama target from the source tree, not an installed library.
# The compat patch is already applied to the vendored tree.
export OLLAMA_LLAMA_CPP_SOURCE=$PWD/vendor/llama.cpp
backends=
%if_with cuda
backends=cuda_v%cuda_major
%endif
%if_with vulkan
backends="${backends:+$backends;}vulkan"
%endif
# The superbuild (cmake/local.cmake) builds the Go binary, llama-server,
# CPU backend variants and the requested GPU backends, and stages them all
# under OLLAMA_LIB_DIR for %cmake_install.
%cmake -DOLLAMA_VERSION:STRING=%version \
	-DOLLAMA_LLAMA_BACKENDS:STRING="$backends" \
%if_with cuda
	%cuda_cmake_flags \
%endif
	%nil
%cmake_build

%install
%cmake_install
install -Dpm644 %SOURCE3 %buildroot%_sysusersdir/%name.conf
# HTTP server on 127.0.0.1:11434
install -Dpm644 %SOURCE4 -t %buildroot%_unitdir
mkdir -p %buildroot%_localstatedir/%name
install -Dpm644 %SOURCE6 %SOURCE7 -t %buildroot%_datadir/ollama
install -Dpm644 %SOURCE5 %buildroot%_datadir/bash-completion/completions/ollama
# Add a RPATH to bypass lib.req false positive error and to let GPU backend
# modules in runner subdirectories find the base libraries.
find %buildroot%ollama_libdir -name 'libggml-*.so*' |
	xargs -trn1 patchelf --set-rpath %ollama_libdir

%check
%if_with cuda
( ! cuobjdump --list-elf %buildroot%ollama_libdir/cuda_v%cuda_major/libggml-cuda.so | grep -F -v -e .cubin )
# SASS for every arch, PTX only for the newest one (e.g. .sm_121.ptx or
# arch-specific .sm_121a.ptx).
( ! cuobjdump --list-ptx %buildroot%ollama_libdir/cuda_v%cuda_major/libggml-cuda.so | grep -F -v -e .sm_%cuda_arch_max )
%endif
cat /proc/loadavg
# We don't have MLX.
rename go go- mlx/generator/main.go
# TestCodexAppCountsOnlyOllamaRequestsInRegularProfile is flaky in the gyle
# build environment (passes on host and in local hasher): the request-count
# cursor skips session files whose mtime precedes the reset timestamp,
# which is sensitive to filesystem timestamp granularity.
go test -v ./... -skip 'TestCodexAppCountsOnlyOllamaRequestsInRegularProfile'
%buildroot%_bindir/ollama --version | grep -Fx 'Warning: client version is %version'
ldd %buildroot%_bindir/ollama
%buildroot%_bindir/ollama serve &
sleep 1
curl -sSf http://127.0.0.1:11434/api/version | grep '"version":"%version"'
curl -sSf http://127.0.0.1:11434/api/tags
curl -sSf http://127.0.0.1:11434/api/ps
kill %%?ollama

%pre cpu
%sysusers_create_package %name %SOURCE3

%post cpu
# We need to restart the server after all backends are installed, not in the
# middle of installs to avoid loading wrong DSO. But, just installing/removing
# a GPU backend won't trigger server restart. Upgrading a GPU backend will
# trigger the server restart via strict dependence on CPU backend.
%post_systemd_postponed %name.service

%preun cpu
%preun_systemd %name.service

%files

%files cpu
%define _customdocdir %_docdir/%name
%doc LICENSE README.md docs SECURITY.md
%_bindir/ollama
%_datadir/ollama
%_datadir/bash-completion/completions/ollama
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %ollama_libdir
%ollama_libdir/llama-*
%ollama_libdir/*.so*
%ollama_libdir/*LICENSE*
%attr(-,ollama,ollama) %dir %_localstatedir/%name

%if_with cuda
%files cuda
%ollama_libdir/cuda_v%cuda_major
%endif

%if_with vulkan
%files vulkan
%ollama_libdir/vulkan
%endif

%changelog
* Fri Sep 25 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.34.4-alt2
- Skip llama.cpp SME CPU backend variants when building with gcc < 14
  (+sme is not supported there; fixes aarch64 build in p11).

* Thu Sep 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.34.4-alt1
- Updated to version 0.34.4.

* Wed Sep 23 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.34.3-alt1
- Updated to version 0.34.3.

* Sun Sep 20 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.34.2-alt1
- Updated to version 0.34.2.
- Build the source tarball from the pristine upstream tag; all ALT-owned
  files (vendor.tar, service, completions, models/tags lists) now enter
  the src.rpm as explicit sources.
- Build llama-server from the vendored pinned llama.cpp: upstream removed
  the in-tree ggml backend and now fetches llama.cpp with CMake
  FetchContent (pin: LLAMA_CPP_VERSION), which is impossible in the
  offline build environment.
- Install runtime payloads into /usr/lib/ollama with per-runner
  subdirectories (cuda_v13, vulkan) per the new upstream layout.
- Do not auto-install third-party coding agents (openclaw, pi, hermes,
  claude, etc.) from the internet; point at install instructions instead.

* Tue Sep 15 2026 Mikhail Tergoev <fidel@altlinux.org> 0.23.4-alt2
- Rebuild with nvidia-cuda-toolkit 13.2.1 using rpm-macros-cuda-toolkit.

* Thu May 14 2026 Vitaly Chikunov <vt@altlinux.org> 0.23.4-alt1
- Update to v0.23.4 (2026-05-12).

* Wed May 13 2026 Vitaly Chikunov <vt@altlinux.org> 0.23.3-alt1
- Update to v0.23.3 (2026-05-11).

* Mon Apr 27 2026 Vitaly Chikunov <vt@altlinux.org> 0.21.2-alt1
- Update to v0.21.2 (2026-04-23).

* Sun Apr 05 2026 Vitaly Chikunov <vt@altlinux.org> 0.20.2-alt1
- Update to v0.20.2 (2026-04-03).

* Tue Mar 10 2026 Vitaly Chikunov <vt@altlinux.org> 0.17.7-alt1
- Update to v0.17.7 (2026-03-05).

* Mon Mar 02 2026 Vitaly Chikunov <vt@altlinux.org> 0.17.5-alt1
- Update to v0.17.5 (2026-03-01).

* Thu Feb 26 2026 Vitaly Chikunov <vt@altlinux.org> 0.17.1-alt1
- Experimental update to v0.17.1 (2026-02-25).

* Sat Feb 07 2026 Vitaly Chikunov <vt@altlinux.org> 0.15.6-alt1
- Update to v0.15.6 (2026-02-06).

* Sun Jan 25 2026 Vitaly Chikunov <vt@altlinux.org> 0.15.1-alt1
- Update to v0.15.1 (2026-01-24).

* Wed Jan 14 2026 Vitaly Chikunov <vt@altlinux.org> 0.14.0-alt1
- Update to v0.14.0 (2026-01-13).

* Wed Jan 07 2026 Vitaly Chikunov <vt@altlinux.org> 0.13.5-alt1
- Update to v0.13.5 (2025-12-18).

* Fri Dec 12 2025 Vitaly Chikunov <vt@altlinux.org> 0.13.3-alt1
- Update to v0.13.3 (2025-12-11).

* Sat Nov 15 2025 Vitaly Chikunov <vt@altlinux.org> 0.12.11-alt1
- Update to v0.12.11 (2025-11-13).

* Sun Nov 09 2025 Vitaly Chikunov <vt@altlinux.org> 0.12.10-alt1
- Update to v0.12.10 (2025-11-05).
- Enable Vulkan GPU runner (ollama-vulkan).

* Sun Nov 02 2025 Vitaly Chikunov <vt@altlinux.org> 0.12.9-alt1
- Update to v0.12.9 (2025-10-31).

* Sun Oct 26 2025 Vitaly Chikunov <vt@altlinux.org> 0.12.3-alt1
- Update to v0.12.3 (2025-09-25).

* Mon Sep 15 2025 Vitaly Chikunov <vt@altlinux.org> 0.11.11-alt1
- Update to v0.11.11 (2025-09-12).

* Sat Sep 06 2025 Vitaly Chikunov <vt@altlinux.org> 0.11.10-alt1
- Update to v0.11.10 (2025-09-04).

* Sat Aug 30 2025 Vitaly Chikunov <vt@altlinux.org> 0.11.8-alt1
- Update to v0.11.8 (2025-08-28).

* Tue Aug 26 2025 Vitaly Chikunov <vt@altlinux.org> 0.11.7-alt1
- Update to v0.11.7 (2025-08-22).

* Thu Aug 21 2025 Vitaly Chikunov <vt@altlinux.org> 0.11.6-alt1
- Update to v0.11.6 (2025-08-19) with gpt-oss and flash attention fixes.

* Fri Aug 08 2025 Vitaly Chikunov <vt@altlinux.org> 0.11.4-alt1
- Update to v0.11.4 (2025-08-07).

* Thu Jun 19 2025 Vitaly Chikunov <vt@altlinux.org> 0.9.2-alt1
- Update to v0.9.2 (2025-06-18).

* Sun Jun 15 2025 Vitaly Chikunov <vt@altlinux.org> 0.9.1-alt1
- Update to v0.9.1 (2025-06-14).

* Mon May 26 2025 Vitaly Chikunov <vt@altlinux.org> 0.7.1-alt1
- Update to v0.7.1 (2025-05-22). [With llama.cpp b5359, 2025-05-12].
- With new engine for multimodal models.

* Mon May 05 2025 Vitaly Chikunov <vt@altlinux.org> 0.6.8-alt1
- Update to v0.6.8 (2025-05-03). [With llama.cpp b5237, 2025-04-30].
- Mostly a bugfix release.

* Sat May 03 2025 Vitaly Chikunov <vt@altlinux.org> 0.6.7-alt1
- Update to v0.6.7 (2025-04-30). [With llama.cpp b5162, 2025-04-20].

* Fri Mar 28 2025 Vitaly Chikunov <vt@altlinux.org> 0.6.3-alt1
- Update to v0.6.3 (2025-03-26). Primarily focused on Gemma 3 improvements.

* Sat Mar 15 2025 Vitaly Chikunov <vt@altlinux.org> 0.6.1-alt1
- Update to v0.6.1 (2025-03-14).

* Wed Mar 12 2025 Vitaly Chikunov <vt@altlinux.org> 0.6.0-alt1
- Update to v0.6.0 (2025-03-11).

* Fri Mar 07 2025 Vitaly Chikunov <vt@altlinux.org> 0.5.13-alt1
- Update to v0.5.13 (2025-03-03).
- Enable NVIDIA GPU runner (ollama-cuda).

* Sat Feb 15 2025 Vitaly Chikunov <vt@altlinux.org> 0.5.11-alt1
- Update to v0.5.11 (2025-02-13).
- Split the package into meta-package (ollama) and runner (ollama-cpu).

* Sat Jan 18 2025 Vitaly Chikunov <vt@altlinux.org> 0.5.7-alt1
- Update to v0.5.7 (2025-01-16).

* Sat Dec 07 2024 Vitaly Chikunov <vt@altlinux.org> 0.5.1-alt1
- Update to v0.5.1 (2024-12-06).

* Sat Nov 23 2024 Vitaly Chikunov <vt@altlinux.org> 0.4.4-alt1
- Update to v0.4.4 (2024-11-22).

* Fri Nov 22 2024 Vitaly Chikunov <vt@altlinux.org> 0.4.3-alt1
- Update to v0.4.3 (2024-11-21).
- Add bash-completion support.

* Sun Oct 27 2024 Vitaly Chikunov <vt@altlinux.org> 0.3.14-alt1
- Update to v0.3.14 (2024-10-17).

* Tue Oct 08 2024 Vitaly Chikunov <vt@altlinux.org> 0.3.12-alt1
- Update to v0.3.12 (2024-09-24). (Fixes CVE-2024-45436).

* Tue Jun 25 2024 Vitaly Chikunov <vt@altlinux.org> 0.1.46-alt1
- Update to v0.1.46 (2024-06-24).

* Thu Jun 20 2024 Vitaly Chikunov <vt@altlinux.org> 0.1.44-alt1
- First import v0.1.44 (2024-06-13).
