# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: argc
Version: 1.21.1
Release: alt1
Summary: A Bash CLI framework, also a Bash command runner
License: Apache-2.0 or MIT
Group: Development/Other
Url: https://github.com/sigoden/argc

Source: %name-%version.tar
BuildRequires: rust-cargo

%description
Argc is a powerful Bash framework that simplifies building full-featured
CLIs. It lets you define your CLI through comments, focusing on your core
logic without dealing with argument parsing, usage text, error messages,
and other boilerplate code.

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
cargo build %_smp_mflags --offline --release
for i in bash fish zsh; do
	target/release/%name --argc-completions $i > completions.$i
done
# Examples no need to be accidentally executable these are texts.
chmod a-x examples/*.sh

%install
install -Dp target/release/%name -t %buildroot%_bindir
install -Dpm0644 completions.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dpm0644 completions.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dpm0644 completions.zsh  %buildroot%_datadir/zsh/site-functions/_%name

%check
%buildroot%_bindir/argc --argc-version | grep -Fx '%name %version'
LANG=C.UTF-8 cargo test --release

%files
%doc LICENSE-APACHE LICENSE-MIT README.md docs/*.md examples
%_bindir/argc
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Mon Nov 18 2024 Vitaly Chikunov <vt@altlinux.org> 1.21.1-alt1
- First import v1.21.1-2-g13dbe7d (2024-11-16).
