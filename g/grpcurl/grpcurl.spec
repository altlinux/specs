%global import_path github.com/fullstorydev/grpcurl
Name:     grpcurl
Version:  1.7.0
Release:  alt1

Summary:  Like cURL, but for gRPC: Command-line tool for interacting with gRPC servers
License:  MIT
Group:    Other
Url:      https://github.com/fullstorydev/grpcurl

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

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
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Tue Jan 05 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus
