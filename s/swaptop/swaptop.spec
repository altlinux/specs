%define _unpackaged_files_terminate_build 1

Name: swaptop
Version: 1.0.3
Release: alt1
Summary: swap usage monitor written in rust
License: MIT
Group: Monitoring
Url: https://github.com/luis-ota/swaptop

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
A real-time swap usage monitor for Linux and Windows systems with TUI interface.
Lists processes using swap, displays consumption per-process/per-software,
and provides live-updating graphs.

%prep
%setup -a 1
%autopatch -p1
sed -i 's/^default = \[\]/default = ["linux"]/' Cargo.toml

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
%doc *.md LICENSE
%_bindir/%name

%changelog
* Thu Sep 25 2025 Pavel Shilov <zerospirit@altlinux.org> 1.0.3-alt1
- 1.0.1 -> 1.0.3

* Wed Sep 03 2025 Pavel Shilov <zerospirit@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
