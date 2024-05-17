# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: just
Version: 1.26.0
Release: alt1.1
Summary: Just a command runner
License: CC0-1.0
Group: Development/Other
Url: https://just.systems/
Vcs: https://github.com/casey/just

Source: %name-%version.tar
BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: cargo-vendor-checksum diffstat

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

%check
cargo test %_smp_mflags --release --offline --no-fail-fast
PATH=%buildroot%_bindir:$PATH
cat > justfile <<EOF
_help:
	@just --list
version:
	just --version
EOF
just | grep -Ez '^Available recipes:\s*version\s$'
just version | grep -Fx '%name %version'

%files
%define _customdocdir %_docdir/%name
%doc LICENSE *.md examples
%_bindir/just
%_man1dir/just.1*
%_datadir/bash-completion/completions/just
%_datadir/zsh/site-functions/_just
%_datadir/fish/vendor_completions.d/just.fish

%changelog
* Fri May 17 2024 Ivan A. Melnikov <iv@altlinux.org> 1.26.0-alt1.1
- Drop obsolete loongarch64 fix.

* Thu May 16 2024 Vitaly Chikunov <vt@altlinux.org> 1.26.0-alt1
- Update to 1.26.0 (2024-05-14).

* Wed Mar 13 2024 Vitaly Chikunov <vt@altlinux.org> 1.25.2-alt1
- Update to 1.25.2 (2024-03-10).

* Tue Jan 16 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.22.1-alt2
- NMU: fixed FTBFS on LoongArch.

* Tue Jan 09 2024 Vitaly Chikunov <vt@altlinux.org> 1.22.1-alt1
- Update to 1.22.1 (2024-01-08).

* Sat Jun 10 2023 Vitaly Chikunov <vt@altlinux.org> 1.14.0-alt1
- First import 1.14.0-1-gf329046 (2023-06-10).
