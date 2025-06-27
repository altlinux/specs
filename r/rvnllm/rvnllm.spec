# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: rvnllm
Version: 0.1.7
Release: alt1
Summary: LLM model introspection and diffing for GGUF and safetensors
License: MIT
Group: Other
Url: https://rvnllm.com/
Vcs: https://github.com/rvnllm/rvnllm

ExcludeArch: %ix86
Source: %name-%version.tar
BuildRequires: python3-base
BuildRequires: rust-cargo

%description
%summary.

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

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF
# We obliged to include it.
cp -a /usr/share/license/MIT LICENSE.MIT

%build
cargo build %_smp_mflags --offline --release --all-features

%install
install -Dp target/release/rvn-{diff,info} -t %buildroot%_bindir

%files
%doc LICENSE.MIT README.md
%_bindir/rvn-diff
%_bindir/rvn-info

%changelog
* Wed Jun 18 2025 Vitaly Chikunov <vt@altlinux.org> 0.1.7-alt1
- Experimental import v0.1.7-8-g302eae7 (2025-06-17).
