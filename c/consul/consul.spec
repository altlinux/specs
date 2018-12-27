%global import_path github.com/hashicorp/consul
Name:     consul
Version:  1.4.0
Release:  alt1

Summary:  Consul is a tool for service discovery and configuration
License:  MPL-2.0
Group:    Other
Url:      https://github.com/hashicorp/consul

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Consul is a distributed, highly available, and data center aware solution to
connect and configure applications across dynamic, distributed infrastructure.

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
* Thu Dec 27 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
