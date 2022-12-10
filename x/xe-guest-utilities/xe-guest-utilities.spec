# spec file for package xe-guest-utilities
#

Name: xe-guest-utilities
Version: 7.31.0
Release: alt1

Summary: Xen Virtual Machine Monitoring Scripts

License: %bsd 2-Clause
Group: System/Servers
Url: https://github.com/xenserver/xe-guest-utilities

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Source1: vendor.tar
Patch0:  %name-%version-%release.patch

Source2: xe-daemon.service
Patch1:  xe-guest-utilities-1.30.0-alt-lsb.patch
Patch2:  xe-guest-utilities-1.30.0-alt-altlinux.patch
Patch3:  xe-guest-utilities-1.31.0-alt-Makefile.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-golang

%description
XenServer guest utilities for unix-like operating systems.

This package contains a daemon for a guest virtual machine to interact
with Citrix Hypervisor and a support utility that submit the distribution
version information and IP address to XenStore.

%package xenstore
Summary: Xen Virtual Machine scripts to interact with XenStore
Group: System/Servers
Requires: %name = %version-%release

%description xenstore
XenServer guest utilities for unix-like operating systems.

This package contais Utilities for interacting with XenStore from withing
a Xen virtual machine.


%prep
%setup
%patch0 -p1

tar xf %SOURCE1
%patch1
%patch2
%patch3

%build
export GO111MODULE=auto
export BUILDDIR="$PWD/build"
export GOPATH="$BUILDDIR:%go_path"

%make_build

%install
# xenstore utils:
mkdir -p -- %buildroot%_bindir
cp build/stage/usr/bin/*  %buildroot%_bindir/

# xe-* daemon:
mkdir -p -- %buildroot%_sbindir
cp build/stage/usr/sbin/*  %buildroot%_sbindir/

# SysVinit init file:
mkdir -p -- %buildroot%_initdir
mv build/stage/etc/init.d/xe-linux-distribution %buildroot%_initdir/xe-daemon
sed -e 's/@BRAND_GUEST@/Xen Guest/' -i %buildroot%_initdir/xe-daemon

# systemd unit file:
mkdir -p -- %buildroot%_unitdir
install -m 644 %SOURCE2 %buildroot%_unitdir/

# udev rule:
mkdir -p -- %buildroot%_udevrulesdir
mv build/stage/etc/udev/rules.d/z10_xen-vcpu-hotplug.rules %buildroot%_udevrulesdir/

%post
%post_service xe-daemon

%preun
%preun_service xe-daemon


%files
%doc README.md CODEOWNERS LICENSE

%_sbindir/xe-*

%config  %_initdir/xe-daemon
%_unitdir/xe-daemon.service
%_udevrulesdir/z10*


%files xenstore
%_bindir/xenstore*


%changelog
* Sat Dec 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 7.31.0-alt1
- New version

* Thu Feb 17 2022 Nikolay A. Fetisov <naf@altlinux.org> 7.30.0-alt1
- Initial build for ALT Linux Sisyphus

