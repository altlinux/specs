%define _unpackaged_files_terminate_build 1
%def_with check

Name: tailcat
Version: 0.7.0
Release: alt1

Summary: Netcat-like tool over Tailscale's data plane, without its control plane
License: BSD-3-Clause
Group: Networking/Other
VCS: https://github.com/tailscale/tailcat
Url: https://github.com/tailscale/tailcat

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%if_with check
BuildRequires: openssh-clients
BuildRequires: /dev/pts
BuildRequires: /proc
%endif

%description
Tailcat is a remix of Tailscale open source pieces to act like netcat, but over
Tailscale's data plane, without Tailscale's control plane. One side runs a
tailcat server and gets back a short tailcat address, the other side passes
that address to the tailcat client to connect. All traffic between the two is
encrypted end-to-end with WireGuard. The connection bootstraps through a DERP
relay, then NAT traversal upgrades it to a direct peer-to-peer UDP connection
when possible.

Besides plain pipes, tailcat can forward ports, serve SSH, SFTP and files,
act as a SOCKS5 proxy or an exit node. No Tailscale account and no root access
are needed: it does not alter the routing tables or DNS of the machine.

%prep
%setup -a1
%patch0 -p1

%build
LDFLAGS="-X main.version=%version-%release"
%gobuild -tags "$(cat build-tags.txt)" -o ./bin/tailcat ./cmd/tailcat

%install
install -vDm 755 ./bin/tailcat \
        %buildroot%_bindir/tailcat

%check
[ "$(./bin/tailcat version)" = "%version-%release" ]
# The test harness must stay untagged (see cmd/tailcat/e2e_test.go),
# TestForwardToExitNodeTarget is flaky in sandboxes (see forward_test.go)
%gotest -count=1 -timeout 30m -skip TestForwardToExitNodeTarget ./...

%files
%doc LICENSE README.md INSTALL.md
%_bindir/tailcat

%changelog
* Thu Oct 08 2026 Egor Ignatov <egori@altlinux.org> 0.7.0-alt1
- First build for ALT.
