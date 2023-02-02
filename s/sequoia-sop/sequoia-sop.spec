# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed
# elflint is relaxed because of
#   section [18] '.debug_gdb_scripts' has wrong flags: expected none, is ALLOC|MERGE|STRINGS

Name: sequoia-sop
Version: 0.27.3
Release: alt1
Summary: An implementation of the Stateless OpenPGP Interface using Sequoia
License: GPL-2.0-or-later
Group: File tools
Url: https://sequoia-pgp.org/
Vcs: https://gitlab.com/sequoia-pgp/sequoia-sop

Source: %name-%version.tar
BuildRequires: clang-devel
BuildRequires: libnettle-devel
BuildRequires: rust-cargo
BuildRequires: /proc

%description
sqop tool implements the Stateless OpenPGP Command Line Interface (SOP)
using the Sequoia OpenPGP implementation and provides encryption,
decryption, signature creation and verification, and basic key and
certificate management with a convenient git-style subcommand interface.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
quiet = false
verbose = true

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[env]
RUST_BACKTRACE = "full"

[net]
offline = true

[profile.release]
strip = false
EOF

%build
# Required to generate and [mis[place shell completions.
export CARGO_TARGET_DIR=$PWD/target

cargo build %_smp_mflags --release --all-features

%install
install -Dp target/release/sqop -t %buildroot%_bindir/
install -Dp man-sqop/*.1 -t %buildroot%_man1dir/
install -Dp target/_sqop     -t %buildroot%_datadir/zsh/site-functions/
install -Dp target/sqop.fish -t %buildroot%_datadir/fish/vendor_completions.d/
install -Dp target/sqop.bash -t %buildroot%_datadir/bash-completion/completions/

%check
cargo test %_smp_mflags --release --no-fail-fast --all-features

# A small functional test from README.md to be sure.
PATH=$PATH:%buildroot%_bindir
sqop version --extended
sqop generate-key julia@example.org | tee julia.secret.pgp
sqop extract-cert < julia.secret.pgp | tee julia.public.pgp
echo 'a message' > message
sqop encrypt julia.public.pgp < message | tee message.pgp
sqop decrypt julia.secret.pgp < message.pgp | diff message -
sqop sign julia.secret.pgp < message | tee message.asc
sqop verify message.asc julia.public.pgp < message
! sqop verify message.asc julia.public.pgp <<<"wrong message"

%files
%_bindir/sqop
%_man1dir/*.1*
%_datadir/zsh/site-functions/_*
%_datadir/fish/vendor_completions.d/*.fish
%_datadir/bash-completion/completions/*.bash

%changelog
* Thu Feb 02 2023 Vitaly Chikunov <vt@altlinux.org> 0.27.3-alt1
- Update to v0.27.3 (2023-01-18).

* Mon Oct 24 2022 Vitaly Chikunov <vt@altlinux.org> 0.27.1-alt1
- First import v0.27.1 (2022-07-20).
