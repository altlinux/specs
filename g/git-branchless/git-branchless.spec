# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: git-branchless
Version: 0.10.0
Release: alt1
Summary: High-velocity, monorepo-scale workflow for Git
License: MIT or Apache-2.0
Group: Development/Tools
Url: https://github.com/arxanas/git-branchless

Source: %name-%version.tar
BuildRequires: git
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(zlib)
BuildRequires: rust-cargo

%description
git-branchless is a suite of tools which enhances Git in several ways.

%prep
%setup
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
sed -i '/rusqlite/s/"bundled",\?//' Cargo.toml

%build
cargo build %_smp_mflags --offline --release --all-features

%install
install -Dp target/release/%name -t %buildroot%_bindir
target/release/%name install-man-pages %buildroot%_mandir

%check
%buildroot%_bindir/git-branchless --version |& grep -Fx '%name-opts %version'
ldd %buildroot%_bindir/git-branchless | grep -Fw libsqlite3.so
ldd %buildroot%_bindir/git-branchless | grep -Fw libz.so
ldd %buildroot%_bindir/git-branchless
# Rebuilds because cargo.
export TEST_GIT=$(which git) TEST_GIT_EXEC_PATH=$(git --exec-path)
cargo test --release -- \
	      --skip=test_next_ambiguous_interactive \
	      --skip=test_switch_abort \
	      --skip=test_switch_auto_switch_interactive \
	      --skip=test_switch_auto_switch_interactive_disabled \
	      --skip=test_switch_pty \
	      --skip=test_switch_pty_branch \
	      --skip=test_switch_pty_initial_query

%files
%define _customdocdir %_docdir/%name
%doc CHANGELOG.md LICENSE-APACHE LICENSE-MIT README.md
%doc wiki
%_bindir/git-branchless
%_man1dir/git-branchless*.1*

%changelog
* Tue Oct 15 2024 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt1
- Update to v0.10.0 (2024-10-14).
- spec: Build with vendored libgit2(1.8.1) as our libgit2(1.7.2) is too old.

* Sat Oct 12 2024 Vitaly Chikunov <vt@altlinux.org> 0.9.0-alt1
- First import v0.9.0 (2024-05-26).
