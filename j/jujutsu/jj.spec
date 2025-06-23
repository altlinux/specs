# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: jujutsu
Version: 0.30.0
Release: alt1
Summary: An experimental Git-compatible VCS that is both simple and powerful
License: Apache-2.0
Group: Development/Other
Url: https://jj-vcs.github.io/jj/
Vcs: https://github.com/jj-vcs/jj
Provides: jj = %EVR

Source: %name-%version.tar
BuildRequires: rust-cargo
BuildRequires: openssl-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: git-core
BuildRequires: gnupg2
BuildRequires: jq
BuildRequires: openssh-common
%ifarch x86_64 aarch64
BuildRequires: taplo
%endif
}}

%description
Jujutsu is a powerful version control system for software projects. You
use it to get a copy of your code, track changes to the code, and finally
publish those changes for others to see and use. It is designed from
the ground up to be easy to use-whether you're new or experienced,
working on brand new projects alone, or large scale software projects
with large histories and teams.

Jujutsu is unlike most other systems, because internally it abstracts
the user interface and version control algorithms from the storage
systems used to serve your content. This allows it to serve as a VCS
with many possible physical backends, that may have their own data or
networking models-like Mercurial or Breezy, or hybrid systems like
Google's cloud-based design, Piper/CitC.

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

%build
cargo build %_smp_mflags --offline --release --all-features
target/release/jj util completion bash > _bash
target/release/jj util completion fish > _fish
target/release/jj util completion zsh  > _zsh
target/release/jj util install-man-pages .

%install
install -Dp target/release/jj -t %buildroot%_bindir
install -Dpm644 _bash %buildroot%_datadir/bash-completion/completions/jj
install -Dpm644 _fish %buildroot%_datadir/fish/vendor_completions.d/jj.fish
install -Dpm644 _zsh  %buildroot%_datadir/zsh/site-functions/_jj
install -Dpm644 man1/*.1 -t %buildroot%_man1dir

%check
%buildroot%_bindir/jj -V | grep -Fx 'jj %version'
# gpgsm tests require gnupg 2.4.4
cargo test --release -- \
	--skip test_gpg::gpgsm_signing_roundtrip \
	--skip test_gpg::gpgsm_signing_roundtrip_explicit_key

%files
%define _customdocdir %_docdir/%name
%doc AUTHORS CHANGELOG.md LICENSE README.md SECURITY.md docs
%_bindir/jj
%_man1dir/jj*.1*
%_datadir/bash-completion/completions/jj
%_datadir/zsh/site-functions/_jj
%_datadir/fish/vendor_completions.d/jj.fish

%changelog
* Mon Jun 23 2025 Vitaly Chikunov <vt@altlinux.org> 0.30.0-alt1
- First import v0.30.0 (2025-06-04).
