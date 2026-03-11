Name: navi
Version: 2.24.0
Release: alt1

Summary: An interactive cheatsheet tool for the command-line

License: Apache-2.0
Group: Other
Url: https://github.com/denisidoro/navi

# Source-url: https://github.com/denisidoro/navi.git
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc

Requires: /usr/bin/tldr

%description
An interactive cheatsheet tool for the command-line
so that you won't say the following anymore:

- How to run that command again?
- Oh, it's not in my shell history
- Geez, it's almost what I wanted but I need to change some args

%prep
%setup
tar xf %SOURCE1

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

%files
%doc README.md
%_bindir/%name

%changelog
* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 2.24.0-alt1
- new version (2.24.0) via gear-uupdate
- rewrite as Rust package

* Sun Feb 16 2020 Vitaly Lipatov <lav@altlinux.ru> 0.18.3-alt1
- initial build for ALT Sisyphus
