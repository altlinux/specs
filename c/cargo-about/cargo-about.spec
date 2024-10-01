%define _unpackaged_files_terminate_build 1

Name: cargo-about
Version: 0.6.4
Release: alt1

Summary: Cargo plugin to generate list of all licenses for a crate
License: Apache-2.0 or MIT
Group: Development/Tools
Url: https://crates.io/crates/cargo-about
Vcs: https://github.com/EmbarkStudios/cargo-about

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: mold

%description
%summary.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE2 .cargo/config.toml

%build
mold -run cargo build %_smp_mflags --release --offline

%install
install -Dvm0644 target/release/cargo-about %buildroot%_bindir/cargo-about

%files
# LICENSE-MIT has copyright
%doc LICENSE-MIT
%_bindir/cargo-about

%changelog
* Tue Oct 01 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.4-alt1
- Updated to 0.6.4.

* Mon Jul 15 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.2-alt1
- Built for ALT Sisyphus.

