%define _unpackaged_files_terminate_build 1

Name: feroxbuster
Version: 2.13.1
Release: alt1

Summary: feroxbuster is a tool designed to perform Forced Browsing
License: MIT
Group: Security/Networking
Url: https://epi052.github.io/feroxbuster-docs/overview/
Vcs: https://github.com/epi052/feroxbuster

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: perl-IPC-Cmd
Requires: seclists

%description
feroxbuster uses brute force combined with a wordlist to search
for unlinked content in target directories. These resources may
store sensitive information about web applications and operational systems,
such as source code, credentials, internal network addressing, etc...

%prep
%setup -a1
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
root = "%buildroot%prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false

# Incorrect linker specs causing failure on aarch64/armh:
#   error: linker 'aarch64-linux-gnu-gcc' not found
[target.'cfg(all())']
linker = "gcc"
EOF
sed -i '/armv7-unknown/,/gnueabihf-gcc/d;/aarch64-unknown/,/gnu-gcc/d' .cargo/config.toml

%build
cargo build %_smp_mflags --offline --release

%install
cargo install %_smp_mflags --offline --no-track --path .
install -Dm 644 shell_completions/%name.bash \
    %buildroot/%_datadir/bash-completion/completions/%name
install -Dm 644 shell_completions/%name.fish \
    %buildroot/%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 644 shell_completions/_%name \
    %buildroot/%_datadir/zsh/site-functions/_%name

%files
%doc README* docs LICENSE
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Tue Mar 03 2026 Denis Rastyogin <gerben@altlinux.org> 2.13.1-alt1
- Initial build for ALT Sisyphus.
