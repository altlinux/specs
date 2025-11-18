%define _unpackaged_files_terminate_build 1

Name: cargo-show-asm
Version: 0.2.54
Release: alt1

Summary: Cargo subcommand showing the assembly, LLVM-IR and MIR generated for Rust code
License: Apache-2.0 or MIT
Group: Development/Other
Url: https://github.com/pacak/cargo-show-asm
Vcs: https://github.com/pacak/cargo-show-asm

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust

%description
A cargo subcommand that displays the Assembly, LLVM-IR, MIR and WASM
generated for Rust source code.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%rust_build --all-features

%install
%rust_install cargo-asm

%check
%rust_test --all-features

%files
%doc LICENSE-*
%_bindir/cargo-asm

%changelog
* Tue Nov 18 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.2.54-alt1
- New version (0.2.54).

* Tue Aug 19 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.2.52-alt1
- New version (0.2.52).

* Tue Jul 29 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.2.51-alt3
- Package licenses.

* Sat Jul 05 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.2.51-alt2
- Enable all features.

* Tue Jul 01 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.2.51-alt1
- Initial build for alt.
