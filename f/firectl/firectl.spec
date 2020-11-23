%global import_path github.com/firecracker-microvm/firectl
Name:     firectl
Version:  0.1.0
Release:  alt1

Summary:  firectl is a command-line tool to run Firecracker microVMs
License:  Apache-2.0
Group:    Other
Url:      https://github.com/firecracker-microvm/firectl

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires: firecracker >= 0.23.0-alt2

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Thu Nov 19 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
