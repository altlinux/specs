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
Version: 0.1.44
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
Source1: llama.cpp-0.tar
Source2: kompute-0.tar
Source3: ollama-user.conf

BuildRequires(pre): rpm-macros-systemd
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: golang
%if_with cuda
BuildRequires: gcc12-c++
BuildRequires: nvidia-cuda-devel-static
%endif

%description
%summary.
Using llama.cpp backend.

%prep
%setup
tar xf %SOURCE1 -C llm
tar xf %SOURCE2 -C llm/llama.cpp
# Build process requires git repo to repeatedly patch and restore different
# modifications to llama.cpp
cd llm/llama.cpp
git init -q
git config user.name "$USER"
git config user.email "$USER"
git add -Af .
git commit -q -m "$PWD"
git tag "%version-%release"

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

%check
# Running gpu test destroys %%buildroot https://github.com/ollama/ollama/issues/5129
TMPDIR=$TMPDIR/tmp
mkdir $TMPDIR
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
%_unitdir/%name.service
%_sysusersdir/%name.conf
%attr(-,ollama,ollama) %dir %_localstatedir/%name

%changelog
* Thu Jun 20 2024 Vitaly Chikunov <vt@altlinux.org> 0.1.44-alt1
- First import v0.1.44 (2024-06-13).
