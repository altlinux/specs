# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: just
Version: 1.14.0
Release: alt1
Summary: Just a command runner
License: CC0-1.0
Group: Development/Other
Url: https://just.systems/
Vcs: https://github.com/casey/just

Source: %name-%version.tar
BuildRequires: /proc
BuildRequires: rust-cargo

%description
just is a handy way to save and run project-specific commands.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false
EOF


%build
cargo build %_smp_mflags --offline --release

%install
install -Dp target/release/just -t %buildroot%_bindir
install -Dpm0644 completions/just.bash %buildroot%_datadir/bash-completion/completions/just
install -Dpm0644 completions/just.zsh  %buildroot%_datadir/zsh/site-functions/_just
install -Dpm0644 completions/just.fish %buildroot%_datadir/fish/vendor_completions.d/just.fish
install -Dpm0644 man/just.1 -t %buildroot%_man1dir

%define _customdocdir %_docdir/%name

%files
%doc LICENSE *.md examples
%_bindir/just
%_man1dir/just.1*
%_datadir/bash-completion/completions/just
%_datadir/zsh/site-functions/_just
%_datadir/fish/vendor_completions.d/just.fish

%changelog
* Sat Jun 10 2023 Vitaly Chikunov <vt@altlinux.org> 1.14.0-alt1
- First import 1.14.0-1-gf329046 (2023-06-10).
