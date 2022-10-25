# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed
# elflint is relaxed because of
#   section [18] '.debug_gdb_scripts' has wrong flags: expected none, is ALLOC|MERGE|STRINGS

Name: sequoia-sq
Version: 0.27.0
Release: alt1
Summary: A command-line frontend for Sequoia
License: GPL-2.0-or-later
Group: File tools
Url: https://sequoia-pgp.org/
Vcs: https://gitlab.com/sequoia-pgp/sequoia
# Docs: https://docs.sequoia-pgp.org/sq/

Source: %name-%version.tar
BuildRequires: clang-devel
BuildRequires: libnettle-devel
BuildRequires: libssl-devel
BuildRequires: rust-cargo
BuildRequires: /proc

%description
A command-line frontend for Sequoia, an implementation of OpenPGP.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
quiet = false
verbose = true

[install]
root = "%buildroot%_prefix"

[profile.release]
strip = false
EOF

%build
# Workaround for:
#
#   error: unused return value of `Box::<T>::from_raw` that must be used
#     --> openpgp/src/crypto/mem.rs:162:13
#      |
#  162 |             Box::from_raw(self.0);
#      |             ^^^^^^^^^^^^^^^^^^^^^^
#      |
#      = note: `-D unused-must-use` implied by `-D warnings`
#      = note: call `drop(from_raw(ptr))` if you intend to drop the `Box`
#
# And it should be RUSTFLAGS env to override [target.'cfg(all())'].rustflags
export RUSTFLAGS="-Adead_code"

# Required to generate and [mis[place shell completions.
export CARGO_TARGET_DIR=$PWD/target

cargo build %_smp_mflags --offline --release --bins -p sequoia-sq

%install
install -Dp target/release/sq -t %buildroot%_bindir/
install -Dp sq/man-sq-autocrypt/*.1 -t %buildroot%_man1dir/
install -Dp target/_sq     -t %buildroot%_datadir/zsh/site-functions/
install -Dp target/sq.fish -t %buildroot%_datadir/fish/vendor_completions.d/
install -Dp target/sq.bash -t %buildroot%_datadir/bash-completion/completions/

%check
PATH=$PATH:%buildroot%_bindir
sq --version
sq key generate -u julia@example.org -e julia.secret.pgp
sq key extract-cert julia.secret.pgp -o julia.public.pgp
sq inspect julia.public.pgp
echo "The quick brown fox jumps over the lazy dog." > message
sq encrypt --recipient-cert julia.public.pgp message --compression zlib -o message.pgp
sq decrypt --recipient-key julia.secret.pgp message.pgp --dump | diff message -
K=$(sq packet decrypt --recipient-key julia.secret.pgp --dump-session-key message.pgp 2>&1 |
    grep -Po 'Session key: \K.*')
sq packet dump --session-key "$K" message.pgp -x

%files
%_bindir/sq
%_man1dir/*.1*
%_datadir/zsh/site-functions/_*
%_datadir/fish/vendor_completions.d/*.fish
%_datadir/bash-completion/completions/*.bash

%changelog
* Mon Oct 24 2022 Vitaly Chikunov <vt@altlinux.org> 0.27.0-alt1
- First import sq/v0.27.0 (2022-07-19).
