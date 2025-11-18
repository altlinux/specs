%define _unpackaged_files_terminate_build 1
%def_with check

Name: cargo-llvm-cov
Version: 0.6.21
Release: alt1

Summary: Cargo subcommand to easily use LLVM source-based code coverage
License: Apache-2.0 or MIT
Group: Development/Tools
Url: https://crates.io/crates/cargo-llvm-cov
Vcs: https://github.com/taiki-e/cargo-llvm-cov.git

# Unsupported due explicit use of x64 integer types.
ExcludeArch: i586

Source: %name-%version.tar
Source1: vendor.tar

# Cargo.lock required for vendored test-helper dependency.
Patch: cargo-llvm-cov-0.6.19-alt-missing_cargo_lock.patch
# Sets paths to used llvm tools by environment variables.
Patch1: cargo-llvm-cov-0.6.19-alt-paths_to_llvm_tools.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: git
BuildRequires: llvm
BuildRequires: llvm-common

%description
%summary.

This is a wrapper around rustc -C instrument-coverage and provides:
Generate very precise coverage data.
Support cargo test, cargo run, and cargo nextest with command-line
interface compatible with cargo.
Support for proc-macro, including coverage of UI tests.
Fast because it does not introduce extra layers between rustc, cargo,
and llvm-tools.

%prep
%setup -a 1
%autopatch -p1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/taiki-e/test-helper.git?rev=f38a7f5"]
git = "https://github.com/taiki-e/test-helper.git"
rev = "f38a7f5"
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
# Required for some tests.
git init -q
git config user.name "rpmbuild"
git config user.email "<rpmbuild>"
git add .

%build
export LLVM_COV_PATH=%_bindir/llvm-cov
export LLVM_PROFDATA_PATH=%_bindir/llvm-profdata
%rust_build

%install
%rust_install

%check
export LLVM_COV_PATH=%_bindir/llvm-cov
export LLVM_PROFDATA_PATH=%_bindir/llvm-profdata
%rust_test

%files
%doc LICENSE-*
%_bindir/cargo-llvm-cov

%changelog
* Fri Oct 24 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.6.21-alt1
- New version (0.6.21).

* Tue Sep 09 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.6.19-alt1
- Initial build.
