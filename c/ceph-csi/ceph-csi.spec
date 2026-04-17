%define _unpackaged_files_terminate_build 1

%global import_path github.com/ceph/ceph-csi

%define git_commit f8b8b1416793ceaf6e01592b77f438e8b4c3b6b8
%define ceph_version_string squid

Name: ceph-csi
Version: 3.15.1
Release: alt1

Summary: CSI driver for Ceph
License: Apache-2.0
Group: Other
Url: https://github.com/ceph/ceph-csi
Vcs: https://github.com/ceph/ceph-csi

ExcludeArch: %ix86 %arm %mips32 ppc

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24
BuildRequires: librbd-devel
BuildRequires: libcephfs-devel

%description
Ceph CSI plugins implement an interface between a CSI-enabled
Container Orchestrator (CO) and Ceph clusters. They enable dynamically
provisioning Ceph volumes and attaching them to workloads.

Independent CSI plugins are provided to support RBD and CephFS backed volumes.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export TAGS="%ceph_version_string,ceph_preview"
export LDFLAGS="-X %import_path/internal/util.GitCommit=%git_commit \
                -X %import_path/internal/util.DriverVersion=v%version"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/

mv "$BUILDDIR/bin/cmd" "$BUILDDIR/bin/cephcsi"

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc README.md
%_bindir/cephcsi

%changelog
* Mon Mar 02 2026 Alexander Stepchenko <geochip@altlinux.org> 3.15.1-alt1
- Initial build.
