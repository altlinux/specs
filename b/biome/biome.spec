%global _unpackaged_files_terminate_build 1
%def_with check

Name: biome
Version: 2.6.3
Release: alt1
Summary: A fast formatter, linter and analyzer for web projects
License: MIT or Apache-2.0
Group: Development/Tools
URL: https://biomejs.dev
VCS: https://github.com/biomejs/biome

Source: %name-%version.tar
Source1: vendor.tar
Patch: biome-disable-upgrade.patch

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: git-core
%endif

%description
Biome is a fast formatter, linter and analyzer for web projects.
It supports JavaScript, TypeScript, JSX, JSON, CSS and other web
languages, providing consistent formatting and code quality checks.

%prep
%setup -a1
%patch -p1

%build
export BIOME_VERSION=%version
export CARGO_PROFILE_RELEASE_STRIP=false
# Disable LTO: fat LTO exceeds available memory during linking.
export CARGO_PROFILE_RELEASE_LTO=thin
%rust_build -p biome_cli --locked --config vendor/config.toml

%install
%rust_install

%check
export CARGO_PROFILE_RELEASE_STRIP=false
export CARGO_PROFILE_RELEASE_LTO=thin
# RPM owns the binary: self-upgrade must be absent from help and rejected by the parser.
# BIOME_BINARY blocks self-updating if the command is accidentally restored.
target/release/biome --help > biome-help.log
if grep -Eq '^[[:space:]]+upgrade([[:space:]]|$)' biome-help.log; then
    cat biome-help.log
    exit 1
fi
if BIOME_BINARY=disabled target/release/biome upgrade > upgrade.log 2>&1; then
    cat upgrade.log
    exit 1
fi
grep -F 'no such command or positional: `upgrade`' upgrade.log
%rust_test -p biome_cli --offline --locked --config vendor/config.toml -- \
    --skip cases::help::upgrade_help

%files
%_bindir/%name
%doc LICENSE-MIT LICENSE-APACHE

%changelog
* Sat Oct 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.6.3-alt1
- Updated to version 2.6.3.

* Sat Oct 17 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.5.15-alt1
- Initial build for ALT.
