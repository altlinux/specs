%define _unpackaged_files_terminate_build 1

Name: binsider
Version: 0.2.1
Release: alt1
Summary: Analyze ELF binaries like a boss.
License: Apache-2.0 and MIT 
Group: Development/Ruby
Url:  https://github.com/orhun/binsider
ExclusiveArch: x86_64

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
Binsider can perform static and dynamic analysis, inspect strings, examine
linked libraries, and perform hexdumps, within a terminal user interface.

%prep
%setup -a 1
%patch -p1
rm -fr src/tui/widgets.rs

%build
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%rust_build

%install
%rust_install

%files
%doc README.md LICENSE-*
%_bindir/%name

%changelog
* Thu Jul 02 2025 Pavel Shilov <zerospirit@altlinux.org> 0.2.1-alt1
- Update based on upstream version

* Fri Sep 06 2024 Pavel Shilov <zerospirit@altlinux.org> 0.1.0-alt1
- initial build for Sisyphus
