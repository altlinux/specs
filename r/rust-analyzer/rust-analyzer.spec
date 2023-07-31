%define _unpackaged_files_terminate_build 1

Name: rust-analyzer
Version: 2023.07.31
Release: alt1

Summary: A Rust compiler front-end for IDEs
License: MIT or Apache-2.0
Group: Development/Tools

Url: https://rust-analyzer.github.io/
VCS: https://github.com/rust-lang/rust-analyzer

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rust rust-cargo

%description
rust-analyzer is a modular compiler frontend for the Rust language. It
is a part of a larger rls-2.0 effort to create excellent IDE support
for Rust.

%prep
%setup
%patch0 -p1

mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --release %{?_smp_mflags} --all-targets --offline 

%install
install -D -m755 target/release/rust-analyzer %buildroot%_bindir/rust-analyzer

%files
%doc LICENSE-MIT LICENSE-APACHE README.md
%_bindir/rust-analyzer

%changelog
* Mon Jul 31 2023 Egor Ignatov <egori@altlinux.org> 2023.07.31-alt1
- First build for ALT
