# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%ifarch x86_64_cuda_tested
%def_with cuda
%else
%def_without cuda
%endif

Name: ollama
Version: 0.4.4
Release: alt1
Summary: Get up and running with large language models
License: MIT
Group: Sciences/Computer science
Url: https://ollama.com
Vcs: https://github.com/ollama/ollama
%if_with cuda
Requires: libcuda
%endif

ExclusiveArch: aarch64 x86_64
Source: %name-%version.tar
Source3: ollama-user.conf

BuildRequires(pre): rpm-macros-systemd
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: golang
%if_with cuda
BuildRequires: gcc12-c++
BuildRequires: nvidia-cuda-devel-static
%endif

%description
%summary.
Using llama.cpp backend.

Note: You should have at least 8 GB of RAM available to run the 7B models,
16 GB to run the 13B models, and 32 GB to run the 33B models.

%prep
%setup

%build
export NPROCS="%__nprocs"
# First step builds several llama.cpp servers in
# ./llm/build/linux/*/*/bin/ (gzipped).
export OLLAMA_SKIP_PATCHING=1
%if_with cuda
# NVCC cannot compile using gcc-13: https://github.com/ggerganov/llama.cpp/issues/8000
export OLLAMA_CUSTOM_CUDA_DEFS="-DCMAKE_CUDA_HOST_COMPILER=gcc-12"
export CUDA_LIB_DIR=%_libdir
%endif
export GOFLAGS='-buildmode=pie'
go generate ./...
go build -v \
	-buildmode=pie \
	-ldflags="
	-X=github.com/ollama/ollama/version.Version=%version
	-X=github.com/ollama/ollama/server.mode=release
	"

%install
install -Dp ollama %buildroot%_bindir/ollama
install -Dpm644 %SOURCE3 %buildroot%_sysusersdir/%name.conf
# HTTP server on 127.0.0.1:11434
install -Dpm644 .gear/%name.service -t %buildroot%_unitdir
mkdir -p %buildroot%_localstatedir/%name
install -Dpm644 models-list.txt tags-list.txt -t %buildroot%_datadir/ollama
install -Dpm644 .gear/completions %buildroot%_datadir/bash-completion/completions/ollama

%check
go test ./...
%buildroot%_bindir/ollama --version |& grep -Pw 'version is \Q%version\E$'

%pre
%sysusers_create_package %name %SOURCE3

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md docs examples
%_bindir/ollama
%_datadir/ollama
%_datadir/bash-completion/completions/ollama
%_unitdir/%name.service
%_sysusersdir/%name.conf
%attr(-,ollama,ollama) %dir %_localstatedir/%name

%changelog
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
