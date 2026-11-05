%define _unpackaged_files_terminate_build 1
%define bcr_rev 0218c15e571f233d1cb3efc7660a218b8e36933b

%define rules_rust_data %_datadir/bazel/rules_rust/%version
%define license_prefix Apache-2.0 AND MIT AND BSD-3-Clause AND

Name: bazel-rules-rust
Version: 0.75.0
Release: alt1

Summary: Rust rules and source-built Cargo generator for Bazel
License: %license_prefix MPL-2.0 AND Unicode-3.0 AND Unicode-DFS-2016
Group: Development/Tools
URL: https://github.com/bazelbuild/rules_rust
VCS: https://github.com/bazelbuild/rules_rust.git

Source0: rules_rust-%version.tar
Source1: bcr-0218c15.tar.gz
Source2: cargo-vendor-%version.tar
Source3: install-source.py
Patch0: %name-alt.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: python3
BuildRequires: rpm-build-python3

Requires: rust-cargo

# The registry cache contains build inputs and maintainer generators.
%add_findreq_skiplist %_datadir/bazel/rules_rust/registry/*
%add_findprov_skiplist %_datadir/bazel/rules_rust/registry/*

# This manual Bazel target regenerates upstream checksum tables.
%add_findreq_skiplist %rules_rust_data/util/fetch_shas/fetch_shas.py
%add_findprov_skiplist %rules_rust_data/util/fetch_shas/fetch_shas.py

%define rules_rust_testdir %rules_rust_data/test
%define rules_rust_analyzer_dir %rules_rust_testdir/rust_analyzer
%define rules_rust_crate_tests %rules_rust_data/crate_universe/tests
%define rules_rust_local_path %rules_rust_crate_tests/integration/local_path
%add_findreq_skiplist %rules_rust_data/.github/workflows/release_prep.sh
%add_findreq_skiplist %rules_rust_local_path/vendor_edit_test.sh
%add_findreq_skiplist %rules_rust_testdir/clippy/clippy_failure_tester.sh
%add_findreq_skiplist %rules_rust_testdir/query_test_binary.sh
%add_findreq_skiplist %rules_rust_analyzer_dir/flycheck_clippy_test_runner.sh
%add_findreq_skiplist %rules_rust_analyzer_dir/partial_failure_test_runner.sh
%add_findreq_skiplist %rules_rust_analyzer_dir/rust_analyzer_test_runner.sh
%add_findreq_skiplist %rules_rust_testdir/rustfmt/rustfmt_failure_tester.sh
%add_findreq_skiplist %rules_rust_testdir/vscode/vscode_test_runner.sh
%add_findreq_skiplist %rules_rust_data/util/repin_all.sh
%description
The cargo-bazel 0.18.0 generator is built from the complete rules_rust
release with the system Rust toolchain and locked offline Cargo sources.
It generates Bazel targets from Cargo packages and dependency metadata.

%package source
Summary: Complete rules_rust source module and registry metadata
License: Apache-2.0
Group: Development/Tools

BuildArch: noarch

%description source
Complete upstream rules, Rust code, tests and pinned Bazel Central Registry
metadata for rules_rust %version. Consumers provide Bazel, Rust toolchains
and transitive modules. The native generator can be selected through
CARGO_BAZEL_GENERATOR_URL=file:///usr/bin/cargo-bazel and the upstream
CARGO_BAZEL_GENERATOR_SHA256 setting.

%prep
%setup -q -n rules_rust-%version
%autopatch -p1
tar -xf %SOURCE2 -C crate_universe
cd crate_universe
%rust_prep

%build
cd crate_universe
export CARGO_NET_OFFLINE=true
%rust_build --locked --package cargo-bazel

%install
cd crate_universe
%rust_install cargo-bazel
cd ..
mkdir bcr-registry
tar -xzf %SOURCE1 --strip-components=1 \
    -C bcr-registry \
    bazel-central-registry-%bcr_rev/bazel_registry.json \
    bazel-central-registry-%bcr_rev/modules

python3 %SOURCE3 . \
    %buildroot%_datadir/bazel/rules_rust/%version licenses \
    %_defaultdocdir/%name-%version
install -d %buildroot%_datadir/bazel/rules_rust/distdir
install -pm644 %SOURCE0 \
    %buildroot%_datadir/bazel/rules_rust/distdir/rules_rust-%version.tar

%check
cd crate_universe
export CARGO_NET_OFFLINE=true
export REPOSITORY_NAME=rules_rust
export CARGO_TOML=rules_rust/crate_universe/Cargo.toml
export VERSION_BZL=rules_rust/crate_universe/version.bzl
export CARGO=%_bindir/cargo
export RUSTC=%_bindir/rustc
export RUNFILES_DIR="$PWD/test-runfiles"
mkdir -p "$RUNFILES_DIR"
ln -s "$(dirname "$PWD")" "$RUNFILES_DIR/rules_rust"
export TEST_TMPDIR="$(mktemp -d)"
# Upstream skips network-dependent cases offline; preserve their diagnostics.
%rust_test --locked --package cargo-bazel -- \
    --nocapture --test-threads=1
./target/release/cargo-bazel --version
cd ..
tar -xOf %SOURCE1 \
    bazel-central-registry-%bcr_rev/modules/rules_rust/%version/MODULE.bazel \
        | \
    cmp - MODULE.bazel

%files
%doc LICENSE.txt licenses
%_bindir/cargo-bazel

%files source
%_datadir/bazel/rules_rust

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 0.75.0-alt1
- Initial build for ALT.
