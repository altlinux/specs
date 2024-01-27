# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: git-absorb
Version: 0.6.11
Release: alt1
Summary: git commit --fixup, but automatic
License: BSD-3-Clause
Group: Development/Tools
Url: https://crates.io/crates/git-absorb
Vcs: https://github.com/tummychow/git-absorb

Source: %name-%version.tar
BuildRequires: /proc
BuildRequires: rust-cargo

%description
%summary.

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
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
cargo build %_smp_mflags --offline --release --all-features
for i in bash zsh fish; do
	target/release/git-absorb --gen-completions $i > completion.$i
done

%install
install -Dp target/release/%name -t %buildroot%_bindir
install -Dpm644 Documentation/git-absorb.1 -t %buildroot%_man1dir
install -Dpm644 completion.bash -T %buildroot%_datadir/bash-completion/completions/%name
install -Dpm644 completion.zsh  -T %buildroot%_datadir/zsh/site-functions/_%name
install -Dpm644 completion.fish -T %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
%buildroot%_bindir/git-absorb --version |& grep -Pw '\Q%version\E'

%files
%doc LICENSE.md README.md
%_bindir/git-absorb
%_man1dir/git-absorb.1*
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Sat Jan 27 2024 Vitaly Chikunov <vt@altlinux.org> 0.6.11-alt1
- First import 0.6.11 (2023-11-28).
