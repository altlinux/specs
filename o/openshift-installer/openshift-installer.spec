%global import_path github.com/openshift/installer
Name:     openshift-installer
Version:  0.16.1
Release:  alt2

Summary:  Install an OpenShift 4.x cluster
License:  Apache-2.0
Group:    Other
Url:      https://github.com/openshift/installer

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang libvirt-devel

ExcludeArch: %ix86 armh

%description
%summary

%prep
%setup

%build
export GO111MODULE=auto
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

pushd .build/src/%import_path
export TAGS=libvirt
%golang_build cmd/openshift-install
popd

$BUILDDIR/bin/openshift-install > completion-bash


%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
install -Dm644 completion-bash %buildroot/%_datadir/bash-completion/completions/openshift-install

%files
%_bindir/*
%_datadir/bash-completion/completions/openshift-install
%doc *.md

%changelog
* Tue Feb 23 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.1-alt2
- Set GO111MODULE=auto to fix build with go 1.16

* Thu Sep 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.1-alt1
- Initial build for Sisyphus
