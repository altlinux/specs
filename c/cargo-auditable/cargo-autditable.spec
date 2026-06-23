%define _unpackaged_files_terminate_build 1

Name: cargo-auditable
Version: 0.7.5
Release: alt1

Summary: Make production Rust binaries auditable
License: Apache-2.0 or MIT
Group: Development/Tools
Url: https://crates.io/crates/cargo-auditable
Vcs: https://github.com/rust-secure-code/cargo-auditable.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-wasm32-unknown-unknown-target

%description
Know the exact crate versions used to build your Rust executable. Audit
binaries for known bugs or security vulnerabilities in production, at
scale, with zero bookkeeping.

This works by embedding data about the dependency tree in JSON format
into a dedicated linker section of the compiled executable.

Linux, Windows and Mac OS are officially supported. WebAssembly is also
supported starting with v0.6.3. All other ELF targets should work, but
are not tested on CI.

The end goal is to get Cargo itself to encode this information in
binaries. There is an RFC for an implementation within Cargo, for which
this project paves the way: https://github.com/rust-lang/rfcs/pull/2801

%package -n rust-audit-info
Version: 0.5.4
Summary: Command-line tool to extract the dependency trees embedded in binaries by cargo auditable
Group: Development/Tools
Url: https://crates.io/crates/rust-audit-info

%description -n rust-audit-info
Command-line tool to extract the dependency trees embedded in binaries
by cargo auditable.

It takes care of parsing the platform-specific
formats (ELF, PE, Mach-O) and outputs the decompressed JSON.

This tool is intentionally minimal and does not implement vulnerability
scanning on its own. However, it is useful for building your own
vulnerability scanner.

%prep
%setup -a 1
%rust_prep
# Not a member of workspace.
cd rust-audit-info
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

# TODO: add macro option to specify vendor directory.
[source.vendored-sources]
directory = "../vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=2"]

[profile.release]
strip = false
EOF

%build
%rust_build --all-features -p cargo-auditable
# Not a member of workspace.
cd rust-audit-info
%rust_build --all-features -p rust-audit-info

%install
%rust_install cargo-auditable
# Not a member of workspace.
cd rust-audit-info
%rust_install rust-audit-info

%check
%rust_test --all-features -p cargo-auditable

%files -n cargo-auditable
%doc LICENSE-MIT
%doc README.md
%_bindir/cargo-auditable

%files -n rust-audit-info
%doc LICENSE-MIT
%doc rust-audit-info/README.md
%_bindir/rust-audit-info

%changelog
* Mon Jun 22 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.7.5-alt1
- New version (0.7.5).
- Package only MIT license since Apache-2.0 is standard.

* Tue Nov 18 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.7.2-alt1
- New version (0.7.2).

* Tue Aug 05 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.7.0-alt1
- Initial build.
