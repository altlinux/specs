Name:    obah
Version: 0.1.1
Release: alt1

Summary: OpenVR bindings TUI for xrizer, VapoR, OpenComposite
License: MIT
Group:   Other
URL:     https://github.com/galister/obah

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

ExcludeArch: %ix86

%description
%summary

%prep
%setup -a1
%rust_prep

cat >> .cargo/config.toml <<EOF
[source."git+https://codeberg.org/CosmicHarper/vdf-rs.git?rev=fc6dcbea9eb13cacb98dea40063f6f56cde6e145"]
git = "https://codeberg.org/CosmicHarper/vdf-rs.git"
rev = "fc6dcbea9eb13cacb98dea40063f6f56cde6e145"
replace-with = "vendored-sources"
EOF

%build
%rust_build

%install
%rust_install

%files
%doc LICENSE.txt README.md
%_bindir/%name

%changelog
* Wed Sep 23 2026 Sergey Palcheh <minergenon@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus
