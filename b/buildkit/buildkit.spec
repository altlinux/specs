%global import_path github.com/moby/buildkit
Name:     buildkit
Version:  0.12.2
Release:  alt1

Summary:  BuildKit is a toolkit for converting source code to build artifacts
License:  Apache-2.0
Group:    Other
Url:      https://github.com/moby/buildkit

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires: containerd

%description
BuildKit is a toolkit for converting source code to build artifacts in an
efficient, expressive and repeatable manner.

%prep
%setup
sed 's|/usr/local|/usr|' -i examples/systemd/{system,user}/*.service

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/buildkitd cmd/buildctl

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dm 0644 examples/systemd/system/* -t %buildroot%_unitdir

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/*
%_unitdir/buildkit*
%doc *.md
%doc docs

%changelog
* Mon Sep 11 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.2-alt1
- new version 0.12.2

* Tue Feb 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus
