%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: nitrocli
Version: 0.4.1
Release: alt1

Summary: A command line tool for interaction with Nitrokey devices

Group: System/Configuration/Other
License: GPLv3+ CC0-1.0
Url: https://github.com/d-e-s-o/nitrocli

Source: %name-%version.tar

BuildRequires: rust-cargo /proc
BuildRequires: gcc-c++ libhidapi-devel
Requires: gnupg2

%description
Nitrocli is a program that provides a command line interface for
interaction with Nitrokey Pro, Nitrokey Storage, and Librem Key
devices.

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

%build
cargo build %_smp_mflags --offline --release

# generate shell completions
for s in bash fish zsh; do
    target/release/shell-complete $s > %name.$s
done

%install
install -pD -m0755 -t %buildroot%_bindir target/release/%name
install -pD -m0644 -t %buildroot%_man1dir doc/%name.1
# install shell completions
install -pD -m0644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -pD -m0644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -pD -m0644 %name.zsh  %buildroot%_datadir/zsh/site-functions/_%name

%files
%_bindir/%name
%_man1dir/%name.1*
%doc CHANGELOG.md README.md doc/{CONTRIBUTING.md,config.example.toml,packaging.md}
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Mon Nov 04 2024 Andrew Savchenko <bircoph@altlinux.org> 0.4.1-alt1
- Initial version.
