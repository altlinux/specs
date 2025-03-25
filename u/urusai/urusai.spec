%global import_path github.com/calpa/urusai
Name:    urusai
Version: 1.0.1
Release: alt1

Summary: Go implementation of noisy HTTP/DNS traffic generator
License: MIT
Group:   Other
Url:     https://github.com/calpa/urusai

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

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
%doc *.md
%_bindir/*

%changelog
* Wed Mar 19 2025 Aleksandr Gamzin <gamzin@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
