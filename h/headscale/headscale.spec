%define _unpackaged_files_terminate_build 1

%global import_path github.com/juanfont/headscale

Name: headscale
Version: 0.28.0
Release: alt1

Summary: An open source, self-hosted implementation of the Tailscale control server
License: BSD-3-Clause
Group: Other
Url: https://headscale.net/stable
Vcs: https://github.com/juanfont/headscale

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.26

%description
Tailscale is a modern VPN built on top of Wireguard.
It works like an overlay network between the computers of your
networks - using NAT traversal.

Everything in Tailscale is Open Source, except the GUI clients for
proprietary OS (Windows and macOS/iOS), and the control server.

The control server works as an exchange point of Wireguard public keys for
the nodes in the Tailscale network. It assigns the IP addresses of
the clients, creates the boundaries between each user, enables sharing
machines between users, and exposes the advertised routes of your nodes.

A Tailscale network (tailnet) is private network which Tailscale assigns
to a user in terms of private users or an organisation.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export LDFLAGS="-X main.version=v%version"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/headscale

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -pDm 0644 packaging/systemd/headscale.service %buildroot%_unitdir/headscale.service
install -pDm 0644 config-example.yaml %buildroot%_sysconfdir/headscale/config.yaml

install -d %buildroot%_localstatedir/headscale

%pre
groupadd --system --force headscale > /dev/null 2>&1 ||:
useradd --system \
  --gid headscale \
  --no-create-home \
  --home-dir %_localstatedir/headscale \
  --shell /sbin/nologin \
  --comment 'Headscale default user' \
  headscale > /dev/null 2>&1 ||:

%post
%post_systemd headscale.service

%preun
%preun_systemd headscale.service

%files
%doc README.md CHANGELOG.md
%_bindir/headscale
%_unitdir/headscale.service
%dir %_sysconfdir/headscale
%config(noreplace) %_sysconfdir/headscale/config.yaml
%attr(775, headscale, headscale) %dir %_localstatedir/headscale

%changelog
* Sun Mar 01 2026 Alexander Stepchenko <geochip@altlinux.org> 0.28.0-alt1
- Initial build.
