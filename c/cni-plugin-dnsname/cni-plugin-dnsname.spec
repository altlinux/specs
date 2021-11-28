%define oname dnsname
%define _libexecdir /usr/libexec
%define cni_dir %_libexecdir/cni
%global _unpackaged_files_terminate_build 1
%global import_path github.com/containers/dnsname

Name:     cni-plugin-%oname
Version:  1.3.1
Release:  alt1

Summary:  Dnsname cni plugin for podman
License:  Apache-2.0
Group:    System/Configuration/Other
# https://github.com/containers/dnsname
Url:      https://github.com/containers/dnsname

Source:   %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: /proc

Requires: dnsmasq
Requires: cni-plugins

%description
This plugin sets up the use of dnsmasq on a given CNI network so that Pods
can resolve each other by name.  When configured, the pod and its IP address
are added to a network specific hosts file that dnsmasq reads in.
Similarly, when a pod is removed from the network, it will remove the entry
from the hosts file.  Each CNI network will have its own dnsmasq instance.

%prep
%setup

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export GIT_COMMIT=%release

%golang_prepare

pushd .gopath/src/%import_path
%make_build PREFIX=%_prefix 
popd


%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"

pushd .gopath/src/%import_path
%make DESTDIR=%buildroot PREFIX=%_prefix install
popd

%files
%doc README.md README_PODMAN.md
%cni_dir/dnsname

%changelog
* Sun Nov 28 2021 Alexey Shabalin <shaba@altlinux.org> 1.3.1-alt1
- new version 1.3.1

* Tue Dec 08 2020 Alexey Shabalin <shaba@altlinux.org> 1.1.1-alt1
- Initial build

