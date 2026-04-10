%define _unpackaged_files_terminate_build 1

Name: otree
Version: 0.6.5
Release: alt1
Summary: A command line tool to view objects (JSON/YAML/TOML) in TUI tree widget. 
License: MIT
Group: Terminals
Url: https://github.com/fioncat/otree

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
%summary

%prep
%setup -a 1
%patch -p1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF

[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/fioncat/tui-rs-tree-widget?branch=main#407fd9005271d93ae2411ec0231a51e7f5e070f9"]
git = "https://github.com/fioncat/tui-rs-tree-widget"
branch = "main"
rev = "407fd9005271d93ae2411ec0231a51e7f5e070f9"
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
%doc README.md
%_bindir/%name

%changelog
* Fri Apr 10 2026 Pavel Shilov <zerospirit@altlinux.org> 0.6.5-alt1
- 0.6.4 -> 0.6.5

* Fri Feb 20 2026 Pavel Shilov <zerospirit@altlinux.org> 0.6.4-alt1
- 0.6.3 -> 0.6.4

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 0.6.3-alt1
- 0.6.2 -> 0.6.3

* Tue Oct 21 2025 Pavel Shilov <zerospirit@altlinux.org> 0.6.2-alt1
- 0.6.1 -> 0.6.2

* Tue Aug 26 2025 Pavel Shilov <zerospirit@altlinux.org> 0.6.1-alt1
- 0.5.0 -> 0.6.1

* Mon Aug 18 2025 Pavel Shilov <zerospirit@altlinux.org> 0.5.0-alt1
- 0.4.0 -> 0.5.0

* Thu Jul 03 2025 Pavel Shilov <zerospirit@altlinux.org> 0.4.0-alt1
- Update version based on upstream

* Wed Sep 04 2024 Pavel Shilov <zerospirit@altlinux.org> 0.2.0-alt1
- initial build for Sisyphus
