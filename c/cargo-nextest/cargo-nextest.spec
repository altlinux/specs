%def_with check

Name: cargo-nextest
Version: 0.9.148
Release: alt1
Summary: A next-generation test runner for Rust
License: MIT OR Apache-2.0
Group: Development/Tools
Url: https://github.com/nextest-rs/nextest
Vcs: https://github.com/nextest-rs/nextest.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust >= 1.91
BuildRequires: gcc
BuildRequires: /proc
Requires: rust-cargo

%description
Nextest is a next-generation test runner for Rust. It runs tests in parallel,
isolates each test in a separate process, and supports retries, test filtering,
and JUnit reports.

%prep
%setup -a 1
%rust_prep

%build
%rust_build --locked --package cargo-nextest --no-default-features --features default-no-update

%install
%rust_install cargo-nextest

%check
%if_with check
export PATH="$PWD/target/release:$PATH"
cargo nextest run --offline --locked --release --lib --bins \
    --package cargo-nextest --package nextest-filtering \
    --package nextest-metadata --package nextest-runner \
    --no-default-features --features cargo-nextest/default-no-update
%endif

%files
%doc LICENSE-MIT LICENSE-APACHE README.md
%_bindir/cargo-nextest

%changelog
* Wed Oct 14 2026 Anton Farygin <rider@altlinux.org> 0.9.148-alt1
- initial build for ALT Linux
