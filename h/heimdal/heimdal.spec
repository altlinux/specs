%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: heimdal
Version: 1.1.2
Release: alt1

Summary: A universal dotfile and system configuration manager
License: MIT
Group: Text tools
Url: https://crates.io/crates/heimdal
Vcs: https://github.com/limistah/heimdal

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires: rust-cargo
BuildRequires: /proc

%description
Heimdal automatically manages your dotfiles, installs packages,
and keeps your development environment in sync across multiple
machines. Built with Rust for performance and reliability.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
cargo build --release --offline -j %__nprocs

%install
install -Dm 755 target/release/heimdal -t %buildroot%_bindir

%files
%_bindir/heimdal

%changelog
* Sat Mar 28 2026 Anton Zhukharev <ancieg@altlinux.org> 1.1.2-alt1
- Packaged for ALT Sisyphus.
