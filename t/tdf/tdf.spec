%define _unpackaged_files_terminate_build 1

Name: tdf
Version: 0.4.3
Release: alt1

Summary: A tui-based PDF viewer
License: AGPL-3.0-only
Group: Office
Url: https://github.com/itsjunetime/tdf
VCS: https://github.com/itsjunetime/tdf

# Source-url: https://github.com/itsjunetime/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-%version-ratatui.tar
Source2: %name-%version-ratatui-image.tar
Source3: vendor-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: clang-devel
BuildRequires: gcc-c++
BuildRequires: rust-cargo
BuildRequires: unzip
BuildRequires: fontconfig-devel

%description
Designed to be performant, very responsive, and work well with even very
large PDFs. Built with ratatui.

%prep
%setup -a1 -a2 -a3
%rust_prep
cat >> .cargo/config.toml <<EOF
[source."git+https://github.com/itsjunetime/kittage.git"]
git = "https://github.com/itsjunetime/kittage.git"
replace-with = "vendored-sources"

[source."git+https://github.com/itsjunetime/ratatui-image.git?branch=vb64_on_personal"]
git = "https://github.com/itsjunetime/ratatui-image.git"
branch = "vb64_on_personal"
replace-with = "vendored-sources"

[source."git+https://github.com/itsjunetime/ratatui.git"]
git = "https://github.com/itsjunetime/ratatui.git"
replace-with = "vendored-sources"

[source."git+https://github.com/lukaslihotzki/vb64?branch=update"]
git = "https://github.com/lukaslihotzki/vb64"
branch = "update"
replace-with = "vendored-sources"

[source."git+https://github.com/messense/mupdf-rs.git?rev=2e0fae910fac8048c7008211fc4d3b9f5d227a07"]
git = "https://github.com/messense/mupdf-rs.git"
rev = "2e0fae910fac8048c7008211fc4d3b9f5d227a07"
replace-with = "vendored-sources"
EOF

cargo-vendor-checksum --vendor vendor --all --ignore-missing

%build
%rust_build --no-default-features

%install
%rust_install

%files
%_bindir/%name

%changelog
* Mon Nov 10 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 0.4.3-alt1
- initial build for ALT Linux
