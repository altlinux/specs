%def_without check

Name:    vaultwarden_ldap
Version: 2.2.0
Release: alt1

Summary: Automate LDAP invites to Vaultwarden
License: GPLv3+
Group:   Security/Networking
Url:     https://github.com/ViViDboarder/vaultwarden_ldap

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: pkgconfig(openssl)

%description
%summary.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%check
%rust_test --workspace

%files
%doc *.md
%_bindir/*

%changelog
* Wed Jan 21 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus.
