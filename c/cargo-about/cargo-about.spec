%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: cargo-about
Version: 0.7.1
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

%description
%summary.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE2 .cargo/config.toml

%build
cargo build --release %{?_smp_mflags} --offline

%install
install -Dvm0755 target/release/cargo-about %buildroot%_bindir/cargo-about

%files
# LICENSE-MIT has copyright
%doc LICENSE-MIT
%_bindir/cargo-about

%changelog
* Thu Mar 20 2025 Anton Zhukharev <ancieg@altlinux.org> 0.7.1-alt1
- Updated to 0.7.1.

* Wed Feb 26 2025 Anton Zhukharev <ancieg@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Fri Nov 29 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.6-alt1
- Updated to 0.6.6.

* Wed Oct 02 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.4-alt2
- Fixed wrong permissions of cargo-about binary.

* Tue Oct 01 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.4-alt1
- Updated to 0.6.4.

* Mon Jul 15 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.2-alt1
- Built for ALT Sisyphus.

