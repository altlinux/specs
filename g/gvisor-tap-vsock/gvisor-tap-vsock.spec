%global import_path github.com/containers/gvisor-tap-vsock
%global _unpackaged_files_terminate_build 1

Name:    gvisor-tap-vsock
Version: 0.9.0
Release: alt1

Summary: Go replacement for libslirp and VPNKit
License: Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
Group:   System/Configuration/Networking
Url:     https://github.com/containers/gvisor-tap-vsock

Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

BuildRequires: golang >= 1.26

# tests deps
BuildRequires: rpm-build-vm
BuildRequires: iproute2

%description
A replacement for libslirp and VPNKit, written in pure Go.
It is based on the network stack of gVisor. Compared to
libslirp, gvisor-tap-vsock brings a configurable DNS server
and dynamic port forwarding.

%prep
%setup

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export LDFLAGS="-X %import_path/pkg/types.gitVersion=%version"

%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif

%golang_prepare

%golang_build cmd/gvproxy

export CGO_ENABLED=0
%golang_build cmd/vm

%install
export BUILDDIR="$PWD/.gopath"

%golang_install

mv %buildroot%_bindir/vm %buildroot%_bindir/gvforwarder

rm -rf -- %buildroot%go_root

%check
export GOFLAGS="-mod=vendor"
export GOCACHE="$PWD/.gocache"

# TestDNS and "default system DNS server" resolve redhat.com via the
# real network, which is not available during the build
vm-run --sbin --heredoc <<'EOF'
ip link set lo up
go test -count=1 \
	$(go list ./cmd/gvproxy ./pkg/... | grep -v services/dns)
go test -count=1 -skip '^TestDNS$' ./pkg/services/dns \
	-ginkgo.skip 'default system DNS server'
EOF

%files
%doc LICENSE README.md
%_bindir/gvproxy
%_bindir/gvforwarder

%changelog
* Fri Oct 09 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.9.0-alt1
- 0.8.8 -> 0.9.0
- Enable tests.

* Wed Feb 25 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.8.8-alt1
- 0.7.4 -> 0.8.8

* Tue Aug 20 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.7.4-alt1
- 0.7.3 -> 0.7.4
- Removed outdated patch (from 0.7.1-alt1.1)

* Tue Apr 16 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.7.3-alt1
- 0.7.1 -> 0.7.3 

* Thu Dec 07 2023 Ivan A. Melnikov <iv@altlinux.org> 0.7.1-alt1.1
- NMU: loongarch64 support

* Tue Dec 05 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.7.1-alt1
- Initial build for ALT 
