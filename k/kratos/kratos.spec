%global import_path github.com/go-kratos/kratos
Name:    kratos
Version: 2.8.4
Release: alt1

Summary: Your ultimate Go microservices framework for the cloud-native era
License: MIT
Group:   Other
Url:     https://github.com/go-kratos/kratos

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang

%description
Kratos is a microservice-oriented governance framework implemented by golang, 
which offers convenient capabilities to help you quickly build a bulletproof 
application from scratch.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%name
%golang_build cmd/protoc-gen-go-errors
%golang_build cmd/protoc-gen-go-http

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Thu Mar 20 2025 Aleksandr Gamzin <gamzin@altlinux.org> 2.8.4-alt1
- Initial build for Sisyphus
