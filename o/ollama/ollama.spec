# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,unresolved=relaxed,rpath=relaxed

%ifarch x86_64
%def_with cuda
%else
%def_without cuda
%endif

Name: ollama
Version: 0.5.13
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
%{?!_without_check:%{?!_disable_check:
BuildRequires: curl
}}

%description
%summary.
Run DeepSeek-R1, Gemma 2, Llama 3.3, Mistral, Phi-4, Qwen 2.5, and other
models, locally.

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

%prep
%setup
%ifnarch x86_64
sed -i /GGML_CPU_ALL_VARIANTS/d CMakeLists.txt
%endif

%build
%add_optflags -Wno-unused-function
export NVCC_PREPEND_FLAGS=-ccbin=g++-12
%cmake -DCMAKE_CUDA_ARCHITECTURES='52-virtual;80-virtual'
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
%if_with cuda
# Remove bundled shared libs.
rm %buildroot%_libexecdir/ollama/cuda_v12/libcu{blas{,Lt},dart}.so*
%endif
install -Dp ollama %buildroot%_bindir/ollama
install -Dpm644 %SOURCE3 %buildroot%_sysusersdir/%name.conf
# HTTP server on 127.0.0.1:11434
install -Dpm644 .gear/%name.service -t %buildroot%_unitdir
mkdir -p %buildroot%_localstatedir/%name
install -Dpm644 models-list.txt tags-list.txt -t %buildroot%_datadir/ollama
install -Dpm644 .gear/completions %buildroot%_datadir/bash-completion/completions/ollama
# Add a RPATH to bypass lib.req false positive error.
find %buildroot%_libexecdir/ollama -name libggml-c*.so |
	xargs -trn1 patchelf --set-rpath %_libexecdir/ollama

%check
{ cuobjdump --list-elf %buildroot%_libexecdir/ollama/cuda_v12/libggml-cuda.so
  cuobjdump --list-ptx %buildroot%_libexecdir/ollama/cuda_v12/libggml-cuda.so
} |& head
cat /proc/loadavg
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
%post_systemd %name.service

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
%_libexecdir/ollama/libggml-cpu*.so
%attr(-,ollama,ollama) %dir %_localstatedir/%name

%if_with cuda
%files cuda
%_libexecdir/ollama/cuda_v12
%endif

%changelog
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
