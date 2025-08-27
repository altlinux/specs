%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: rustlings
Version: 6.5.0
Release: alt1

Summary: Small exercises to get you used to reading and writing Rust code
License: MIT
Group: Development/Documentation
Url: https://rustlings.cool/
Vcs: https://github.com/rust-lang/rustlings

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

Requires: clippy
BuildRequires: /proc
BuildRequires: rust-cargo

%description
This project contains small exercises to get you used to reading
and writing Rust code. This includes reading and responding to
compiler messages!

It is recommended to do the Rustlings exercises in parallel to reading
the official Rust book, the most comprehensive resource for learning
Rust.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE2 .cargo/config.toml

%build
cargo build --release %{?_smp_mflags} --offline

%install
install -Dvm0755 target/release/rustlings %buildroot%_bindir/rustlings

%files
%doc CHANGELOG.md LICENSE README.md
%_bindir/rustlings

%changelog
* Wed Aug 27 2025 Anton Zhukharev <ancieg@altlinux.org> 6.5.0-alt1
- Updated to 6.5.0.

* Mon Apr 28 2025 Anton Zhukharev <ancieg@altlinux.org> 6.4.0-alt2
- Added dependency on clippy.

* Fri Apr 25 2025 Anton Zhukharev <ancieg@altlinux.org> 6.4.0-alt1
- Built for ALT Sisyphus.

