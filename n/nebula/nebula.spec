Name: nebula
Version: 1.10.3
Release: alt1

Summary: Scalable overlay networking tool with a focus on performance, simplicity and security
License: MIT
Group: Networking/Other
Url: https://github.com/slackhq/nebula
VCS: https://github.com/slackhq/nebula

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %name.service
Source3: README.alt
Source4: %name@.service

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc
BuildRequires: golang >= 1.25

Requires: %name-cert = %EVR

%description
Nebula is a scalable overlay networking tool with a focus on performance,
simplicity and security. It lets you seamlessly connect computers anywhere
in the world. Nebula is portable, and runs on Linux, OSX, Windows, iOS,
and Android.

Nebula incorporates a number of existing concepts like encryption, security
groups, certificates, and tunneling, and combines them into a single tool
that creates an encrypted, authenticated overlay network.

%package cert
Summary: Nebula PKI certificate authority and signing tool
Group: Networking/Other

%description cert
nebula-cert is a command line utility for creating Nebula certificate
authorities and signing host certificates used by Nebula nodes.

%prep
%setup -q
%setup -q -T -D -a 1
cp -p %SOURCE3 .

%build
export CGO_ENABLED=0
export GOFLAGS="-mod=vendor -trimpath"
LDFLAGS="-X main.Build=%version"

go build -ldflags "$LDFLAGS" -o nebula        ./cmd/nebula
go build -ldflags "$LDFLAGS" -o nebula-cert   ./cmd/nebula-cert

%install
install -Dm755 nebula        %buildroot%_sbindir/nebula
install -Dm755 nebula-cert   %buildroot%_bindir/nebula-cert
install -Dm644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm644 %SOURCE4 %buildroot%_unitdir/%name@.service

install -dm750 %buildroot%_sysconfdir/%name
install -Dm640 examples/config.yml %buildroot%_sysconfdir/%name/config.yml.example
sed -i \
    -e 's|^\(  ca: \)/etc/nebula/ca.crt|\1/run/credentials/%name.service/ca.crt|' \
    -e 's|^\(  cert: \)/etc/nebula/host.crt|\1/run/credentials/%name.service/host.crt|' \
    -e 's|^\(  key: \)/etc/nebula/host.key|\1/run/credentials/%name.service/host.key|' \
    %buildroot%_sysconfdir/%name/config.yml.example

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md README.alt CHANGELOG.md LICENSE AUTHORS SECURITY.md LOGGING.md
%_sbindir/nebula
%_unitdir/%name.service
%_unitdir/%name@.service
%dir %attr(0750,root,root) %_sysconfdir/%name
%config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/config.yml.example

%files cert
%_bindir/nebula-cert

%changelog
* Sun May 24 2026 Anton Farygin <rider@altlinux.org> 1.10.3-alt1
- initial build for ALT Linux
