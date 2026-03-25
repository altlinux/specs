%global import_path github.com/piraeusdatastore/linstor-csi
%define _unpackaged_files_terminate_build 1

Name:    linstor-csi
Version: 1.10.6
Release: alt1

Summary: CSI plugin for LINSTOR
License: Apache-2.0
Group:   Other
Url:     https://github.com/piraeusdatastore/linstor-csi
Vcs:     https://github.com/piraeusdatastore/linstor-csi

Source: %name-%version.tar
Patch:   %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: golang rpm-build-golang

%description
This CSI plugin allows for the use of LINSTOR volumes on Container Orchestrators that implement CSI, such as Kubernetes.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X github.com/piraeusdatastore/linstor-csi/pkg/driver.Version=%version"

%golang_prepare

%golang_build ./cmd/linstor-csi

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Thu Mar 19 2026 Nadezhda Fedorova <fedor@altlinux.org> 1.10.6-alt1
- Initial build for Sisyphus.
