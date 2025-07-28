%define _unpackaged_files_terminate_build 1

Name: choose
Version: 1.3.6
Release: alt1

Summary: Human-friendly and fast alternative to cut and (sometimes) awk
License: GPL-3.0
Group: Text tools
Url: https://github.com/theryangeary/choose
Vcs: https://github.com/theryangeary/choose

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: /proc
BuildRequires: rust-cargo

%description
This is choose, a human-friendly and fast alternative to awk and cut.

%prep
%setup -a1
cat << EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build %_smp_mflags --offline --release

%install
install -Dm755 target/release/choose %buildroot%_bindir/choose

%files
%doc readme.md LICENSE
%_bindir/choose

%changelog
* Sun May 04 2025 Maxim Tulskiy <tulskijms@altlinux.org> 1.3.6-alt1
- Initial build for ALT Sisyphus.

