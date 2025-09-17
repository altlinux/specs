# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: codex
Version: 0.36.0
Release: alt1
Summary: Lightweight coding agent that runs in terminal
License: Apache-2.0
Group: Development/Other
Url: https://github.com/openai/codex
Requires: git-core
Requires: ripgrep

ExcludeArch: %ix86

Source: %name-%version.tar
BuildRequires: help2man
BuildRequires: openssl-devel
BuildRequires: rust-cargo

%description
The default model is gpt-oss:20b which is supposed to be run locally with
ollama. Other models can be configured, see config.md for details.

When using with ollama it's important to increase its context limit by
setting in /etc/sysconfig/ollama:

    OLLAMA_CONTEXT_LENGTH=131072

Warning: The tool is provided experimentally without warranty of
functionality, performance, or availability. Features may change, regress,
or fail without notice; use at your own risk. The tool is provided solely
as a showcase and proof-of-concept, without upstream support.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/nornagon/ratatui?branch=nornagon-v0.29.0-patch"]
git = "https://github.com/nornagon/ratatui"
branch = "nornagon-v0.29.0-patch"
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
cargo build --manifest-path=codex-rs/Cargo.toml %_smp_mflags --offline --release

%install
install -Dp %name-rs/target/release/%name -t %buildroot%_bindir
mkdir -p %buildroot%_datadir/bash-completion/completions \
	 %buildroot%_datadir/fish/vendor_completions.d \
	 %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish
%buildroot%_bindir/%name completion zsh  > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_man1dir
help2man -N %buildroot%_bindir/%name > %buildroot%_man1dir/%name.1

%check
PATH=%buildroot%_bindir:$PATH
codex --version | grep -Fx '%name-cli %version'
# Test sandboxing.
! codex debug landlock touch a || exit 2
  codex debug landlock --full-auto touch a
  rm a
! codex debug landlock --full-auto touch ../a || exit 2
! grep -i 'Update available|api.github.com' %buildroot%_bindir/%name || exit 3

%files
%define _customdocdir %_docdir/%name
%doc CHANGELOG.md LICENSE README.md docs
%_bindir/codex
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_man1dir/codex.1*

%changelog
* Tue Sep 16 2025 Vitaly Chikunov <vt@altlinux.org> 0.36.0-alt1
- Experimental update to rust-v0.36.0 (2025-09-15).
- Disabled unsolicited remote version check and upgrade banner.
- Allow to disable --oss mode with --oss=false, which is required for API
  access to any models except gpt-oss via local Ollama.

* Sat Sep 06 2025 Vitaly Chikunov <vt@altlinux.org> 0.30.0-alt1
- Experimental import rust-v0.30.0 (2025-09-05).
