%define cargo_prep %nil
%define cargo_build %rust_build
%define cargo_install %rust_install

Name: matrix-authentication-service
Version: 1.14.0
Release: alt1

Summary: OAuth 2.0 and OpenID Connect authentication server for Matrix

License: AGPL-3.0-only
Group: Networking/Other
URL: https://github.com/element-hq/matrix-authentication-service
# Source-url: https://github.com/element-hq/matrix-authentication-service.git
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: mas.service
Source3: mas.sysusers
Source4: mas-share.tar.gz

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: cmake gcc-c++
Requires: ca-certificates

%description
Matrix Authentication Service (MAS) is an OAuth 2.0 and OpenID Connect
provider designed for use with Matrix homeservers such as Synapse.

It provides user authentication, session management, and upstream
identity provider integration for the Matrix ecosystem.

Requires PostgreSQL >= 13 as a database backend.

%prep
%setup -a1

# Patch default paths from /usr/local/share to /usr/share
sed -i 's|/usr/local/share/mas-cli|/usr/share/mas-cli|g' \
    crates/config/src/sections/templates.rs \
    crates/config/src/sections/policy.rs \
    crates/config/src/sections/http.rs

# Reduce memory usage during linking: disable LTO and use more codegen units
sed -i '/^\[profile.release\]/,/^$/{
    s/^codegen-units = 1/codegen-units = 16/
    s/^lto = true/lto = false/
}' Cargo.toml

%cargo_prep

cat <<EOF >> .cargo/config.toml

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export VERGEN_GIT_DESCRIBE="v%version"
%cargo_build --bin mas-cli --no-default-features --features docker

%install
install -Dm0755 target/release/mas-cli %buildroot%_bindir/mas-cli
install -Dm0644 %SOURCE2 %buildroot%_unitdir/mas.service
install -Dm0644 %SOURCE3 %buildroot%_sysusersdir/mas.conf

# Install prebuilt share data (templates, translations, frontend assets, policy)
mkdir -p %buildroot%_datadir/mas-cli
tar xzf %SOURCE4 -C %buildroot%_datadir/mas-cli/ --strip-components=1

# Config directory
mkdir -p %buildroot%_sysconfdir/mas

%pre
%sysusers_create_inline u _mas - "Matrix Authentication Service" /nonexistent /usr/sbin/nologin

%files
%doc README.md LICENSE
%_bindir/mas-cli
%_unitdir/mas.service
%_sysusersdir/mas.conf
%dir %_sysconfdir/mas
%_datadir/mas-cli/

%changelog
* Fri Apr 03 2026 Vitaly Lipatov <lav@altlinux.ru> 1.14.0-alt1
- initial build for ALT Sisyphus
- added ca-certificates requirement
- fixed default HTTP assets path
