Name: dexidp
Version: 2.45.1
Release: alt1

Summary: OpenID Connect identity provider with pluggable connectors
License: Apache-2.0
Group: System/Servers
Url: https://github.com/dexidp/dex

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %name.service
Source3: %name.yaml
Source4: %name.sysusers

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: rpm-macros-systemd
BuildRequires: golang >= 1.25.0
BuildRequires: gcc

Requires(pre): systemd
Requires: ca-certificates

%description
Dex is an identity service that uses OpenID Connect to drive authentication
for other applications. It can delegate authentication to LDAP, SAML,
OpenID Connect and other identity providers.

%prep
%setup -q -a1

%build
export GOPATH="$PWD/.gopath"
export GOCACHE="$PWD/.gocache"
export GOFLAGS="-mod=vendor"
export GOTOOLCHAIN=local
export GOWORK=off
export GOPROXY=off
export GOSUMDB=off
export CGO_ENABLED=1

go build -trimpath -buildvcs=false \
    -ldflags '-X main.version=%version' \
    -o bin/dexidp ./cmd/dex

%install
install -Dm755 bin/dexidp \
    %buildroot%_bindir/dexidp
install -Dm644 %SOURCE2 \
    %buildroot%_unitdir/%name.service

install -Dm640 %SOURCE3 \
    %buildroot%_sysconfdir/%name/config.yaml

install -Dm644 %SOURCE4 \
    %buildroot%_sysusersdir/%name.conf

install -d -m750 \
    %buildroot%_localstatedir/%name

%check
bin/dexidp version | grep -F 'Dex Version: %version'

%pre
%sysusers_create_package %name %SOURCE4

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc LICENSE README.md
%_bindir/dexidp
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %attr(0750,root,dexidp) %_sysconfdir/%name
%config(noreplace) %attr(0640,root,dexidp) %_sysconfdir/%name/config.yaml
%dir %attr(0750,dexidp,dexidp) %_localstatedir/%name

%changelog
* Tue Oct 27 2026 Olesya Shuster <lesyafox@altlinux.org> 2.45.1-alt1
- Initial build for ALT Linux Sisyphus.
