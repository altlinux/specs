%define _unpackaged_files_terminate_build 1

Name: serpl
Version: 0.3.5
Release: alt1
Summary: A simple terminal UI for search and replace.
License: MIT
Group: File tools
Url: https://github.com/yassinebridi/serpl

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
%summary

%prep
%setup
%patch -p1
tar -xf %SOURCE1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
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
* Tue May 12 2026 Pavel Shilov <zerospirit@altlinux.org> 0.3.5-alt1
- Update to new version 0.3.5.

* Sun Aug 03 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus.
