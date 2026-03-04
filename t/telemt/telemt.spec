Name: telemt
Version: 3.0.15
Release: alt1

Summary: MTProxy for Telegram on Rust + Tokio

License: TELEMT UL 1
Group: Networking/Other
Url: https://github.com/telemt/telemt

# Source-url: https://github.com/telemt/telemt.git
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: %name.toml
Source3: %name.service

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Fast, secure Telegram MTProto proxy server implementation written in Rust
using the Tokio async runtime. Supports all official MTProto proxy modes
(Classic, Secure, Fake TLS), replay attack protection, traffic masking,
and Middle-End proxy mode.

%prep
%setup
tar -xf %{SOURCE1} -C .

mkdir -p .cargo
cat >> .cargo/config <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install
install -Dm0644 %{SOURCE2} %buildroot%_sysconfdir/%name.toml
install -Dm0644 %{SOURCE3} %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%config(noreplace) %_sysconfdir/%name.toml
%_unitdir/%name.service

%changelog
* Wed Mar 04 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.15-alt1
- new version 3.0.15

* Tue Feb 17 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- initial build for ALT Sisyphus
