%define _unpackaged_files_terminate_build 1

Name: ngrrram
Version: 1.0.3
Release: alt1
Summary: A TUI tool to help you type faster and learn new layouts
License: GPL-3.0
Group: Games/Educational
Url: https://github.com/wintermute-cell/ngrrram

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
ngrrram is a CLI tool to practice typing ngrams
(n adjacent symbols in particular order)
to improve your typing speed and/or learn new keyboard layouts effectively.

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

%check
%rust_test

%files
%doc README.md
%_bindir/%name

%changelog
* Thu Dec 19 2024 Pavel Shilov <zerospirit@altlinux.org> 1.0.3-alt1
- initial build for Sisyphus
