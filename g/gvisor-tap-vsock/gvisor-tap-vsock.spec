%global _unpackaged_files_terminate_build 1

Name:    gvisor-tap-vsock
Version: 0.7.1
Release: alt1.1

Summary: Go replacement for libslirp and VPNKit
License: Apache-2.0
Group:   System/Configuration/Networking
Url:     https://github.com/containers/gvisor-tap-vsock.git

Source: %name-%version.tar
Patch: ldflags_must_be_empty.patch
Patch1: vendored-u-root-uio-loongarch64.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

BuildRequires: golang

%description
%name is based on the network stack of gVisor. Compared to libslirp,
%name brings a configurable DNS server and
dynamic port forwarding.

%prep
%setup
%patch -p1
%patch1 -p1

%build
%make_build

%install
install -D -m 0755 bin/gvproxy %buildroot%_bindir/gvproxy
install -D -m 0755 bin/gvforwarder %buildroot%_bindir/gvforwarder

%files
%doc LICENSE README.md
%_bindir/gvproxy
%_bindir/gvforwarder

%changelog
* Thu Dec 07 2023 Ivan A. Melnikov <iv@altlinux.org> 0.7.1-alt1.1
- NMU: loongarch64 support

* Tue Dec 05 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.7.1-alt1
- Initial build for ALT 

