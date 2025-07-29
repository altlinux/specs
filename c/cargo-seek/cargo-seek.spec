%define _unpackaged_files_terminate_build 1

Name: cargo-seek
Version: 0.1.0
Release: alt1
Summary: A terminal user interface for searching, adding and installing cargo crates.
License: MIT
Group: Development/Tools
Url: https://owasp.org/www-project-amass/

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: pkgconfig(openssl)

%description
%summary

%prep
%setup -a 1
%autopatch -p1

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
%doc README.md LICENSE
%_bindir/%name

%changelog
* Tue Jul 29 2025 Pavel Shilov <zerospirit@altlinux.org> 0.1.0-alt1
- Initial build for Alt.
