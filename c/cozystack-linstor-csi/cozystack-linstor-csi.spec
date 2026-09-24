%global import_path github.com/piraeusdatastore/linstor-csi
%define _unpackaged_files_terminate_build 1

Name:    cozystack-linstor-csi
Version: 1.11.2
Release: alt1

Summary: CSI plugin for LINSTOR (Cozystack-customized)
License: Apache-2.0
Group:   Other
Url:     https://github.com/piraeusdatastore/linstor-csi
Vcs:     https://github.com/piraeusdatastore/linstor-csi

Source: %name-%version.tar
Source1: vendor.tar
Patch001: 001-relocate-after-clone-restore.diff
Patch002: 002-protocol-c-override-for-dual-attach.diff

Conflicts: linstor-csi

BuildRequires(pre): rpm-macros-golang rpm-macros-systemd
BuildRequires: golang rpm-build-golang

%description
This CSI plugin allows for the use of LINSTOR volumes on Container Orchestrators that implement CSI, such as Kubernetes.

%prep
%setup -a 1
%patch001 -p1
%patch002 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X %import_path/pkg/driver.Version=%version -buildid="

%golang_prepare

%golang_build ./cmd/linstor-csi

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
%gotest ./...

%files
%doc LICENSE README.md
%_bindir/linstor-csi

%changelog
* Thu Sep 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.11.2-alt1
- Initial build for ALT.

