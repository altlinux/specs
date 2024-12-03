%define _unpackaged_files_terminate_build 1

Name: otree
Version: 0.2.0
Release: alt1
Summary: A command line tool to view objects (JSON/YAML/TOML) in TUI tree widget. 
License: MIT
Group: Terminals
Url: https://github.com/fioncat/otree

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
%summary

%prep
%setup -q
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build


%install
%rust_install

%check
%rust_test 

%files
%_bindir/%name

%changelog
* Wed Sep 04 2024 Pavel Shilov <zerospirit@altlinux.org> 0.2.0-alt1
- initial build for Sisyphus
