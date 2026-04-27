# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,unresolved=relaxed,rpath=relaxed

%ifarch x86_64
%def_with cuda
%else
%def_without cuda
%endif
%def_with vulkan

Name: ollama
Version: 0.21.2
Release: alt1
Summary: Get up and running with large language models
License: MIT
Group: Sciences/Computer science
Url: https://ollama.com
Vcs: https://github.com/ollama/ollama
%if_with cuda
# https://bugzilla.altlinux.org/52911
%filter_from_requires /(libcudart\.so\.12)/d
%filter_from_requires /debug64(libcuda\.so\.1)/d
Requires: ollama-cuda = %EVR
%endif
%if_with vulkan
Requires: %name-vulkan = %EVR
%endif
Requires: ollama-cpu = %EVR

ExcludeArch: %ix86
Source: %name-%version.tar
Source3: ollama-user.conf

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: golang
BuildRequires: look
BuildRequires: patchelf
%if_with cuda
BuildRequires: gcc12-c++
BuildRequires: nvidia-cuda-devel-static
%endif
%if_with vulkan
BuildRequires: glslc
BuildRequires: libvulkan-devel
%endif
%{?!_without_check:%{?!_disable_check:
BuildRequires: curl
}}

%description
%summary.
Run OpenAI gpt-oss, DeepSeek-R1, Gemma 3, Llama 4, Mistral, Phi-4,
Qwen 3, and other models, locally.

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
%setup
sed -i '/PRE_INCLUDE_REGEXES/d' CMakeLists.txt

%build
%add_optflags -Wno-unused-function
export NVCC_PREPEND_FLAGS=-ccbin=g++-12
%cmake -DCMAKE_CUDA_ARCHITECTURES='52-virtual;80-virtual' \
       -DGGML_BACKEND_DIR=%_libexecdir/ollama
%cmake_build
go build -v \
	-buildmode=pie \
	-ldflags="
		-X=github.com/ollama/ollama/version.Version=%version
		-X=github.com/ollama/ollama/server.mode=release
	"
find -type f -perm -1 -ls

%install
%cmake_install
install -Dp ollama %buildroot%_bindir/ollama
install -Dpm644 %SOURCE3 %buildroot%_sysusersdir/%name.conf
# HTTP server on 127.0.0.1:11434
install -Dpm644 .gear/%name.service -t %buildroot%_unitdir
mkdir -p %buildroot%_localstatedir/%name
install -Dpm644 models-list.txt tags-list.txt -t %buildroot%_datadir/ollama
install -Dpm644 .gear/completions %buildroot%_datadir/bash-completion/completions/ollama
# Add a RPATH to bypass lib.req false positive error.
find %buildroot%_libexecdir/ollama -name 'libggml-*.so' |
	xargs -trn1 patchelf --set-rpath %_libexecdir/ollama

%check
( ! cuobjdump --list-elf %buildroot%_libexecdir/ollama/libggml-cuda.so | grep -F -v -e .cubin )
( ! cuobjdump --list-ptx %buildroot%_libexecdir/ollama/libggml-cuda.so | grep -F -v -e .sm_80.ptx -e .sm_52.ptx )
cat /proc/loadavg
# We don't have MLX.
rename go go- x/mlxrunner/mlx/generator/main.go
go test -v ./...
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
%dir %_libexecdir/ollama
%_libexecdir/ollama/libggml-base.so
%_libexecdir/ollama/libggml-base.so.*
%_libexecdir/ollama/libggml-cpu*.so
%attr(-,ollama,ollama) %dir %_localstatedir/%name

%if_with cuda
%files cuda
%_libexecdir/ollama/libggml-cuda.so
%endif

%if_with vulkan
%files vulkan
%_libexecdir/ollama/libggml-vulkan.so
%endif

%changelog
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
