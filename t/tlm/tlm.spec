%define _unpackaged_files_terminate_build 1
%global import_path github.com/github.com/yusufcanb/tlm

Name: tlm
Version: 1.1        
Release: alt1
Summary: Local CLI Copilot, powered by CodeLLaMa   
License: Apache-2.0
Group: Terminals
URL: https://github.com/yusufcanb/tlm
Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch
ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
Requires: ollama

%description
tlm is your CLI companion which requires nothing except your workstation.
It uses most efficient and powerful CodeLLaMa in your local environment to
provide you the best possible command line suggestions.

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/%name


%changelog
* Thu Dec 26 2024 Pavel Shilov <zerospirit@altlinux.org> 1.1-alt1
- Initial build for Sisyphus
