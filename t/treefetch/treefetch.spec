Name: treefetch
Version: 2.0.0
Release: alt1
License: GPL-3.0

Summary: A plant-based system fetch tool made with Rust

Group: Monitoring

Url: https://github.com/angelofallars/treefetch
Vcs: https://github.com/angelofallars/treefetch.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

%description
A comfy and fast system fetch tool made in Rust.
Tested to be much faster than neofetch and pfetch.
A great pair for cbonsai, to help you get upvotes on your *nix rice.

%prep
%setup -a1

mkdir -p .cargo
cat <<EOF >> .cargo/config.toml
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
%_bindir/%name

%changelog
* Sun Jan 05 2025 Kirill Unitsaev <fiersik@altlinux.org> 2.0.0-alt1
- Initial build
