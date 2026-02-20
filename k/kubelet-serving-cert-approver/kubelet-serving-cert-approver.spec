%define _unpackaged_files_terminate_build 1

%global import_path github.com/alex1989hu/kubelet-serving-cert-approver

Name: kubelet-serving-cert-approver
Version: 0.10.3
Release: alt1

Summary: Kubelet Serving TLS Certificate Signing Request Approver
License: Apache-2.0
Group: Other
Url: https://github.com/alex1989hu/kubelet-serving-cert-approver
Vcs: https://github.com/alex1989hu/kubelet-serving-cert-approver

Source: %name-%version.tar

Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
Kubelet Serving Certificate Approver is a custom approving controller
which approves kubernetes.io/kubelet-serving Certificate Signing Request
that kubelet use to serve TLS endpoints.

%prep
%setup
%patch -p1

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
%doc *.md
%_bindir/kubelet-serving-cert-approver

%changelog
* Fri Feb 20 2026 Alexander Stepchenko <geochip@altlinux.org> 0.10.3-alt1
- Initial build.
