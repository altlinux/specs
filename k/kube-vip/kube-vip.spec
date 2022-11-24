%define _unpackaged_files_terminate_build 1

Name: kube-vip
Version: 0.5.6
Release: alt1

Summary:  Kubernetes Control Plane Virtual IP and Load-Balancer
Group: Networking/Other
License: Apache-2.0
URL: https://github.com/kube-vip/kube-vip

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang rpm-macros-golang

%description
Kubernetes Virtual IP and Load-Balancer for both control plane and Kubernetes services

%prep
%setup
%setup
%patch0 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="github.com/kube-vip/kube-vip"
export GOPATH="%go_path"
export GOFLAGS="-mod=vendor"
%golang_prepare
%golang_build .
rm -rf $BUILDDIR/src

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%files
%doc README.md LICENSE
%_bindir/kube-vip

%changelog
* Thu Nov 24 2022 Egor Ignatov <egori@altlinux.org> 0.5.6-alt1
- 0.5.6

* Sun Oct 23 2022 Egor Ignatov <egori@altlinux.org> 0.5.5-alt1
- First build for ALT
