%define import_path github.com/go-delve/delve
%global _unpackaged_files_terminate_build 1

Name:           delve
Version:        1.23.0
Release:        alt1

Summary:        Delve is a debugger for the Go programming language
License:        MIT
Group:          Development/Other
URL:            https://github.com/go-delve/delve
Source:         %name-%version.tar

ExcludeArch: ppc64le
ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.19
BuildRequires: /proc

%description
The goal of the project is to provide a simple, full
featured debugging tool for Go. Delve should be easy
to invoke and easy to use.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
%golang_build cmd/dlv

$BUILDDIR/bin/dlv completion bash > dlv.bash
$BUILDDIR/bin/dlv completion zsh > dlv.zsh
$BUILDDIR/bin/dlv completion fish > dlv.fish

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dm 644 dlv.bash %buildroot%_datadir/bash-completion/completions/dlv
install -Dm 644 dlv.zsh %buildroot%_datadir/zsh/site-functions/_dlv
install -Dm 644 dlv.fish %buildroot%_datadir/fish/vendor_completions.d/dlv.fish

%files
%doc *.md LICENSE
%_bindir/dlv
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/_*
%_datadir/fish/vendor_completions.d/*.fish

%changelog
* Tue Aug 06 2024 Nadezhda Fedorova <fedor@altlinux.org> 1.23.0-alt1
- Initial build for ALTLinux.
