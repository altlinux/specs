# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: git-delta
Version: 0.18.2
Release: alt1
Summary: A syntax-highlighting pager for git, diff, and grep output
Group: Development/Other
License: MIT
Url: https://github.com/dandavison/delta
Source: %name-%version.tar

BuildRequires: /proc
BuildRequires: rust-cargo
%{?!_without_check:%{?!_disable_check:
BuildRequires: git-core
}}

%description
Code evolves, and we all spend time studying diffs. Delta aims to make
this both efficient and enjoyable: it allows you to make extensive
changes to the layout and styling of diffs, as well as allowing you to
stay arbitrarily close to the default git/diff output.

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
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false
EOF

%build
cargo build %_smp_mflags --offline --release

%install
install -Dp target/release/delta -t %buildroot%_bindir
install -Dpm0644 etc/completion/completion.bash \
		%buildroot%_datadir/bash-completion/completions/delta
install -Dpm0644 etc/completion/completion.zsh \
		%buildroot%_datadir/zsh/site-functions/_delta
install -Dpm0644 etc/completion/completion.fish \
		%buildroot%_datadir/fish/vendor_completions.d/delta.fish

%check
target/release/delta --version | grep -xF 'delta %version'
cargo test %_smp_mflags --release --no-fail-fast -- --test-threads=1

%define _customdocdir %_docdir/%name

%files
%doc LICENSE *.md
%_bindir/delta
%_datadir/bash-completion/completions/delta
%_datadir/zsh/site-functions/_delta
%_datadir/fish/vendor_completions.d/delta.fish

%changelog
* Thu Sep 12 2024 Vitaly Chikunov <vt@altlinux.org> 0.18.2-alt1
- Update to 0.18.2 (2024-09-11).

* Sun Aug 25 2024 Vitaly Chikunov <vt@altlinux.org> 0.18.1-alt1
- Update to 0.18.1 (2024-08-24).

* Sat Aug 17 2024 Vitaly Chikunov <vt@altlinux.org> 0.18.0-alt1
- Update to 0.18.0 (2024-08-16).

* Sun Mar 17 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.0-alt1
- Update to 0.17.0 (2024-03-16).

* Mon Jun 05 2023 Vitaly Chikunov <vt@altlinux.org> 0.16.5-alt1
- Update to 0.16.5 (2023-06-03).

* Mon Dec 19 2022 Vitaly Chikunov <vt@altlinux.org> 0.15.1-alt1
- Update to 0.15.1 (2022-12-03).

* Sun Sep 25 2022 Vitaly Chikunov <vt@altlinux.org> 0.14.0-alt1
- Updated to 0.14.0 (2022-08-31).

* Tue Feb 15 2022 Vitaly Chikunov <vt@altlinux.org> 0.12.0-alt1
- Updated to 0.12.0 (2022-02-14).

* Fri Jan 14 2022 Vitaly Chikunov <vt@altlinux.org> 0.11.3-alt1
- Imported 0.11.3-28-ge9bec95a (2022-01-14).
