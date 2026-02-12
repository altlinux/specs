%def_without check

Name: repolocli
Version: 0.1.0
Release: alt1

Summary: CLI tool for repology.org

License: GPL-2.0-only
Group: Development/Tools
Url: https://github.com/matthiasbeyer/repolocli

# Source-git: https://github.com/matthiasbeyer/repolocli.git
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: %name.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libssl-devel

%description
Command-line interface for querying repology.org package database.
Allows searching for packages across different repositories
and comparing package versions.

%prep
%setup -a1

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
install -D -m 644 %{SOURCE2} %buildroot%_sysconfdir/xdg/%name.toml

%files
%doc README.md
%_bindir/%name
%config(noreplace) %_sysconfdir/xdg/%name.toml

%changelog
* Sat Feb 07 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial build for ALT Sisyphus
