%define _unpackaged_files_terminate_build 1

Name: keroberos
Version: 2026.4
Release: alt1

Summary: An application to track, manage, and visualize your TCG collection
License: MIT
Group: Games/Cards
Url: https://github.com/hecrj/keroberos
Vcs: https://github.com/hecrj/keroberos.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libssl-devel
BuildRequires: pkg-config

%description
An application to track, manage, and visualize your TCG collection.

%prep
%setup -a1
%rust_prep
cat >> .cargo/config.toml <<EOF

[source."git+https://github.com/iced-rs/iced.git?rev=4255f613b887c3362214edd128acb8d2722bd0de"]
git = "https://github.com/iced-rs/iced.git"
rev = "4255f613b887c3362214edd128acb8d2722bd0de"
replace-with = "vendored-sources"

[source."git+https://github.com/iced-rs/winit.git?rev=05b8ff17a06562f0a10bb46e6eaacbe2a95cb5ed"]
git = "https://github.com/iced-rs/winit.git"
rev = "05b8ff17a06562f0a10bb46e6eaacbe2a95cb5ed"
replace-with = "vendored-sources"

[source."git+https://github.com/hecrj/iced_fontello.git?rev=e3652a7f9048f99d3ca85ff3f11b3c61cfa391d6"]
git = "https://github.com/hecrj/iced_fontello.git"
rev = "e3652a7f9048f99d3ca85ff3f11b3c61cfa391d6"
replace-with = "vendored-sources"

[source."git+https://github.com/hecrj/iced_palace.git?rev=7b908e7e636837baa40879d569363b5d87f27a80"]
git = "https://github.com/hecrj/iced_palace.git"
rev = "7b908e7e636837baa40879d569363b5d87f27a80"
replace-with = "vendored-sources"

[source."git+https://github.com/iced-rs/cryoglyph.git?rev=1d68895e9c4c9b73739f826e81c2e3012c155cce"]
git = "https://github.com/iced-rs/cryoglyph.git"
rev = "1d68895e9c4c9b73739f826e81c2e3012c155cce"
replace-with = "vendored-sources"
EOF
# This is necessary to resolve dependency source conflicts.
cargo update --offline

%build
export RUSTFLAGS="-Copt-level=3"
%rust_build

%install
%rust_install keroberos

%check
%rust_test

%files
%doc LICENSE README.md
%_bindir/keroberos

%changelog
* Tue Jul 07 2026 Mikhail Nogin <joycap@altlinux.org> 2026.4-alt1
- Initial built for Sisyphus.
