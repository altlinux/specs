Name: openvpn-multi-authentication-plugin
Version: 1.0.1
Release: alt1

Summary: Multi-provider authentication plugin for OpenVPN
License: GPL-3.0-only
Group: System/Servers
Url: https://github.com/osenchenko/openvpn-multi-authentication-plugin

Source0: %name-%version.tar
Source1: vendor-auth-service.tar
Source2: vendor-radius-client.tar
Source3: vendor-openvpn-plugin.tar
Source4: Cargo.lock
Source5: openvpn-auth-service.service
Source6: auth-service.yml
Source7: openvpn-plugin.yml
Source8: openvpn-auth-service.sysusers

Patch0: 0001-update-go-module-version.patch

BuildRequires: rpm-build-golang rpm-build-rust
BuildRequires: gcc pkg-config libssl-devel openvpn-devel
BuildRequires(pre): rpm-macros-systemd
Requires: openvpn ca-certificates

%description
OpenVPN authentication plugin with LDAP/LDAPS and RADIUS support.
The package includes the Rust authentication plugin,
the Go authentication service and the RADIUS test client.

%prep
%setup -q -a1 -a2 -a3

%patch0 -p1

cp %SOURCE4 openvpn-plugin/Cargo.lock

find auth-service/vendor radius-client/vendor -type f -name '*.py' \
    -exec sed -i '1{/^#!.*python/d;}' {} +

mkdir -p openvpn-plugin/.cargo

cat > openvpn-plugin/.cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[net]
offline = true
EOF

%build
export GO111MODULE=on
export GOWORK=off
export GOTOOLCHAIN=local
export CGO_ENABLED=0
export GOFLAGS="-mod=vendor -trimpath -buildvcs=false"
export GOPROXY=off
export GOSUMDB=off
export GOCACHE="$PWD/.gocache"

export CARGO_HOME="$PWD/.cargo-home"
export CARGO_TARGET_DIR="$PWD/openvpn-plugin/target"

cd auth-service
go build -tags=safe -o auth-service ./cmd/auth-service

cd ../radius-client
go build -o radius-client .

cd ../openvpn-plugin
cargo build --release --frozen --lib

%install
install -Dm755 auth-service/auth-service \
    %buildroot%_bindir/auth-service

install -Dm755 radius-client/radius-client \
    %buildroot%_bindir/radius-client

install -Dm755 openvpn-plugin/target/release/libopenvpn_auth_plugin.so \
    %buildroot%_libdir/libopenvpn_auth_plugin.so

install -Dm644 %SOURCE5 \
    %buildroot%_unitdir/openvpn-auth-service.service

install -d -m750 %buildroot%_sysconfdir/%name

install -m640 %SOURCE6 \
    %buildroot%_sysconfdir/%name/auth-service.yml

install -m600 %SOURCE7 \
    %buildroot%_sysconfdir/%name/openvpn-plugin.yml

install -Dm644 %SOURCE8 \
    %buildroot%_sysusersdir/openvpn-auth-service.conf

%post
%post_systemd openvpn-auth-service.service

%preun
%preun_systemd openvpn-auth-service.service

%files
%doc LICENSE README.md
%_bindir/auth-service
%_bindir/radius-client
%_libdir/libopenvpn_auth_plugin.so
%_unitdir/openvpn-auth-service.service
%_sysusersdir/openvpn-auth-service.conf

%dir %attr(0750,root,openvpn-auth) %_sysconfdir/%name
%config(noreplace) %attr(0640,root,openvpn-auth) %_sysconfdir/%name/auth-service.yml
%config(noreplace) %attr(0600,root,root) %_sysconfdir/%name/openvpn-plugin.yml

%changelog
* Tue Oct 27 2026 Olesya Shuster <lesyafox@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux Sisyphus.
