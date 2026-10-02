%define _unpackaged_files_terminate_build 1

%def_with check

Name: steamguard-cli
Version: 0.18.4
Release: alt1

Summary: Command-line utility for Steam Guard two-factor authentication
License: GPL-3.0-or-later
Group: Security/Networking
URL: https://github.com/dyc3/steamguard-cli
VCS: https://github.com/dyc3/steamguard-cli.git

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust >= 1.96

%description
steamguard-cli is a command-line utility for setting up and using
Steam Guard two-factor authentication. It can generate Steam 2FA
codes, process mobile confirmations, store authentication data
encrypted, use the system keyring, and work with QR codes.

%prep
%setup -a1

%rust_prep

mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[net]
offline = true
EOF

%build
%ifarch i586
export CARGO_PROFILE_RELEASE_LTO=off
%endif

%rust_build \
    --frozen \
    --no-default-features \
    --features qr,keyring

%install
install -Dpm755 target/release/steamguard \
    %buildroot%_bindir/steamguard

ln -s steamguard \
    %buildroot%_bindir/steamguard-cli

%check
%rust_test \
    --workspace \
    --frozen \
    --no-default-features \
    --features qr,keyring

%files
%doc README.md LICENSE
%_bindir/steamguard
%_bindir/steamguard-cli

%changelog
* Thu Oct 02 2026 Timofei Fedotov <sovtouch@altlinux.org> 0.18.4-alt1
- Initial build for ALT Sisyphus.
