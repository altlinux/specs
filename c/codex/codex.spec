# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: codex
Version: 0.141.0
Release: alt3
Summary: Lightweight coding agent that runs in terminal
License: Apache-2.0
Group: Development/Other
Url: https://github.com/openai/codex
Vcs: https://github.com/openai/codex.git
Requires: bubblewrap
Requires: git-core
Requires: ripgrep

ExcludeArch: %ix86

Source: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: README.alt
Patch1: %name-%version-%release.patch
BuildRequires: help2man
BuildRequires: openssl-devel
BuildRequires: rust-cargo
BuildRequires: libcap-devel

%description
Codex CLI is a coding agent from OpenAI that runs locally on your computer.

%prep
%setup -a1
%patch1 -p1
# .gear/ is excluded from the source tarball/diff, so bring the ALT readme in.
cp -p %SOURCE2 README.alt
set -C
cat > .cargo/config.toml <<EOF
[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[target.loongarch64-unknown-linux-gnu]
rustflags = ["-Ccode-model=medium"]

[profile.release]
strip = false
lto = false
codegen-units = 16
EOF
# Disable OOB updates.
perl -0777 -pi -e 's/(pub fn get_upgrade_version\b[^{]+).*?^}/\1 { None }/sm and $x++;
	END { die unless $x }' codex-rs/tui/src/updates.rs

%build
RUST_BACKTRACE=full \
cargo build \
	--config=.cargo/vendor-config.toml \
	--manifest-path=codex-rs/Cargo.toml \
	%_smp_mflags --offline --release \
	-p codex-cli

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
! codex sandbox linux --full-auto touch a || exit 2
# bwrap: No permissions to create a new namespace, likely because the kernel
#  does not allow non-privileged user namespaces. On e.g. debian this can be
#  enabled with 'sysctl kernel.unprivileged_userns_clone=1'.

%files
%define _customdocdir %_docdir/%name
%doc CHANGELOG.md LICENSE README.md docs README.alt
%_bindir/codex
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_man1dir/codex.1*

%changelog
* Mon Jun 29 2026 Ilya Sorochan <k0tran@altlinux.org> 0.141.0-alt3
- Fix linker error on loongarch64.

* Mon Jun 22 2026 Alexey Shabalin <shaba@altlinux.org> 0.141.0-alt2
- Rework packaging for zoryn.

* Fri Jun 19 2026 Alexey Shabalin <shaba@altlinux.org> 0.141.0-alt1
- Update to rust-v0.141.0.
- Re-apply the downstream Code Mode stub (keep rusty_v8 out of the build).

* Sat Apr 25 2026 Vitaly Chikunov <vt@altlinux.org> 0.125.0-alt1
- Update to rust-v0.125.0 (2026-04-24).

* Tue Mar 24 2026 Vitaly Chikunov <vt@altlinux.org> 0.116.0-alt1
- Update to rust-v0.116.0 (2026-03-19).

* Sat Feb 07 2026 Vitaly Chikunov <vt@altlinux.org> 0.98.0-alt1
- Update to rust-v0.98.0 (2026-02-05).

* Sun Feb 01 2026 Vitaly Chikunov <vt@altlinux.org> 0.93.0-alt1
- Update to rust-v0.93.0 (2026-01-30).

* Sat Jan 17 2026 Vitaly Chikunov <vt@altlinux.org> 0.87.0-alt1
- Update to rust-v0.87.0 (2026-01-16).

* Sat Jan 10 2026 Vitaly Chikunov <vt@altlinux.org> 0.80.0-alt1
- Update to rust-v0.80.0 (2026-01-09).

* Sun Dec 21 2025 Vitaly Chikunov <vt@altlinux.org> 0.77.0-alt1
- Update to rust-v0.77.0 (2025-12-20).
- --oss is broken, use Responses API via config (see README.alt).

* Sun Nov 23 2025 Vitaly Chikunov <vt@altlinux.org> 0.63.0-alt1
- Experimental update to rust-v0.63.0 (2025-11-21).
- The behavior of the --oss option is restored, and by default it's turned
  off. This is because --oss is Ollama-API-centric, and to use other OSS
  engines (such as llama.cpp) we need OpenAI-API mode. Also, this will allow
  users to follow how-tos more closely.

* Tue Sep 16 2025 Vitaly Chikunov <vt@altlinux.org> 0.36.0-alt1
- Experimental update to rust-v0.36.0 (2025-09-15).
- Disabled unsolicited remote version check and upgrade banner.
- Allow to disable --oss mode with --oss=false, which is required for API
  access to any models except gpt-oss via local Ollama.

* Sat Sep 06 2025 Vitaly Chikunov <vt@altlinux.org> 0.30.0-alt1
- Experimental import rust-v0.30.0 (2025-09-05).
