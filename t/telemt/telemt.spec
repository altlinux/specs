Name: telemt
Version: 3.4.22
Release: alt1

Summary: MTProxy for Telegram on Rust + Tokio

License: TELEMT LICENSE 3.3
Group: Networking/Other
Url: https://github.com/telemt/telemt

# Source-url: https://github.com/telemt/telemt.git
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml
Source3: %name.service

ExcludeArch: %ix86

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
install -Dm0644 %{SOURCE2} %buildroot%_sysconfdir/%name/config.toml
install -Dm0644 %{SOURCE3} %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/config.toml
%_unitdir/%name.service
%doc README.md docs/

%changelog
* Sun Jul 05 2026 Vitaly Lipatov <lav@altlinux.ru> 3.4.22-alt1
- new version 3.4.22
- fix License field to match upstream (TELEMT LICENSE 3.3)

* Sun Jun 21 2026 Vitaly Lipatov <lav@altlinux.ru> 3.4.18-alt1
- new version 3.4.18

* Fri May 22 2026 Vitaly Lipatov <lav@altlinux.ru> 3.4.12-alt1
- new version 3.4.12

* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 3.4.10-alt1
- new version (3.4.10)

* Wed Apr 01 2026 Vitaly Lipatov <lav@altlinux.ru> 3.3.35-alt1
- new version 3.3.35
- telemt.service: add LimitNOFILE=65536 (altbug #58405)

* Thu Mar 26 2026 Vitaly Lipatov <lav@altlinux.ru> 3.3.32-alt1
- new version 3.3.32
- remove config.full.toml (removed upstream, replaced by docs/CONFIG_PARAMS.en.md)
- add docs/ to package

* Thu Mar 12 2026 Vitaly Lipatov <lav@altlinux.ru> 3.3.16-alt1
- new version 3.3.16

* Thu Mar 05 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.15-alt3
- config.toml: enable IPv6 by default
- telemt.service: add WorkingDirectory, StateDirectory, DynamicUser
- telemt.service: add CAP_NET_BIND_SERVICE for port 443

* Wed Mar 04 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.15-alt2
- move config to /etc/telemt/config.toml (match --init path)
- add config.full.toml as full configuration reference

* Wed Mar 04 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.15-alt1
- new version 3.0.15

* Tue Feb 17 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- initial build for ALT Sisyphus
