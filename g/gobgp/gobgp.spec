%global _unpackaged_files_terminate_build 1
%global import_path github.com/osrg/gobgp/v4

Name:    gobgp
Version: 4.7.0
Release: alt1

Summary: BGP implementation in Go - command line client
License: Apache-2.0
Group:   Networking/Other
Url:     https://osrg.github.io/gobgp
Vcs:     https://github.com/osrg/gobgp

Source:  %name-%version.tar
Source1: vendor.tar
Source2: gobgpd.service
Source3: gobgpd.sysconfig
Source4: gobgpd.conf

ExcludeArch: %ix86

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): rpm-macros-systemd
BuildRequires: golang >= 1.24.5

%description
GoBGP is an open source BGP implementation designed from scratch for
modern environment and implemented in a modern programming language,
the Go Programming Language.

This package contains gobgp, the command line client for gobgpd.

%package -n gobgpd
Summary: BGP implementation in Go - daemon
Group: Networking/Other

%description -n gobgpd
This package contains gobgpd, the BGP daemon.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0
export GOFLAGS="-buildmode=pie"

%golang_prepare
%golang_build ./cmd/gobgp ./cmd/gobgpd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

# place daemon binary to sbin
mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/gobgpd %buildroot%_sbindir/gobgpd

install -pD -m644 %SOURCE2 %buildroot%_unitdir/gobgpd.service
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/gobgpd
install -pD -m640 %SOURCE4 %buildroot%_sysconfdir/gobgpd/gobgpd.conf
mkdir -p %buildroot%_localstatedir/gobgpd

%check
export CGO_ENABLED=0
%gotest \
    ./cmd/gobgp \
    ./pkg/apiutil \
    ./pkg/config/... \
    ./pkg/packet/...

%pre -n gobgpd
getent group _gobgpd >/dev/null || groupadd -r _gobgpd
getent passwd _gobgpd >/dev/null || \
    useradd -r -g _gobgpd -d %_localstatedir/gobgpd -s /dev/null \
    --no-create-home -c "GoBGP Routing Daemon" _gobgpd

%post -n gobgpd
%post_service gobgpd

%preun -n gobgpd
%preun_service gobgpd

%files
%doc README.md
%_bindir/gobgp

%files -n gobgpd
%doc docs/sources/*
%_sbindir/gobgpd
%_unitdir/gobgpd.service
%config(noreplace) %_sysconfdir/sysconfig/gobgpd
%dir %attr(0750,root,_gobgpd) %_sysconfdir/gobgpd
%config(noreplace) %attr(0640,root,_gobgpd) %_sysconfdir/gobgpd/gobgpd.conf
%dir %attr(1770,root,_gobgpd) %_localstatedir/gobgpd

%changelog
* Mon Oct 19 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 4.7.0-alt1
- Initial build for ALT.


