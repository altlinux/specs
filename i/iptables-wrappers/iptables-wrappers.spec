%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

# git rev-list --count v%version..master
%define commit_count 8
# git rev-parse --short master
%define commit_hash c6b9b2d4ee87

Name: iptables-wrappers
Version: 2
Release: alt1.%commit_count.%commit_hash

Summary: Wrapper scripts for using iptables in containers
License: Apache-2.0
Group: System/Kernel and hardware
Url: https://github.com/kubernetes-sigs/iptables-wrappers
Vcs: https://github.com/kubernetes-sigs/iptables-wrappers

Source: %name-%version.tar
Patch0: master-snapshot.patch
Patch1: iptables-wrappers-2-alt-fix-altstyle.patch

BuildRequires: golang >= 1.19

%description
This repository consists of wrapper scripts to help with using iptables
in containers.

Specifically, it provides a wrapper script to select between the two modes
of iptables 1.8 ("legacy" and "nft") at runtime, so that hostNetwork
containers that examine or modify iptables rules will work correctly
regardless of which mode the underlying system is using.

This wrapper is only compatible with Kubernetes 1.17 and newer versions.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
go build -v -x .

%install
mkdir -p %buildroot%_libexecdir/iptables-wrappers
install -m 0755 iptables-wrappers %buildroot%_libexecdir/iptables-wrappers/iptables-wrapper
install -m 0755 iptables-wrapper-installer.sh %buildroot%_libexecdir/iptables-wrappers/iptables-wrapper-installer.sh

%files
%dir %_libexecdir/iptables-wrappers
%_libexecdir/iptables-wrappers/iptables-wrapper
%_libexecdir/iptables-wrappers/iptables-wrapper-installer.sh

%changelog
* Wed Apr 01 2026 Alexander Stepchenko <geochip@altlinux.org> 2-alt1.8.c6b9b2d4ee87
- Initial build.
