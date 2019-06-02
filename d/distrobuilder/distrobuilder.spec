%global import_path github.com/lxc/distrobuilder
Name:     distrobuilder
Version:  0.0.0.0.1
# 0, number of commits, hash of commit, alt release
Release:  alt0.428.06a6a8e.1

Summary:  System container image builder for LXC and LXD
License:  Apache-2.0
Group:    Other
Url:      https://github.com/lxc/distrobuilder

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
%golang_build distrobuilder

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot/%_datadir/%name
cp -r doc/examples %buildroot/%_datadir/%name

%files
%_bindir/*
%doc *.md
%_datadir/%name

%changelog
* Sun Jun 02 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.0.0.0.1-alt0.428.06a6a8e.1
- Initial build for Sisyphus
