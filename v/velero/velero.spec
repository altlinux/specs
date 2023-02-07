%global import_path github.com/vmware-tanzu/velero

Name:     velero
Version:  1.10.1
Release:  alt1

Summary:  Backup and migrate Kubernetes applications and their persistent volumes
License:  Apache-2.0
Group:    Archiving/Backup 
Url:      https://velero.io/
# repacked https://github.com/vmware-tanzu/%name/archive/refs/tags/v%version.tar.gz

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Velero is an open source tool to safely backup and restore, \
perform disaster recovery, and migrate Kubernetes cluster resources \
and persistent volumes.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

pushd $BUILDDIR/src/%import_path
%golang_build ./cmd/%name
%golang_build ./cmd/%name-restore-helper
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Mon Feb 06 2023 Nikolay Burykin <bne@altlinux.org> 1.10.1-alt1
- 1.10.1

* Fri Oct 07 2022 Nikolay Burykin <bne@altlinux.org> 1.9.2-alt1
- Initial build for Sisyphus
