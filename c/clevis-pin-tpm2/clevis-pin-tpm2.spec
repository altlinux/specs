Name: clevis-pin-tpm2
Version: 0.5.3
Release: alt1

Summary: Clevis PIN for unlocking with TPM2 supporting Authorized Policies

License: MIT
Group: System/Configuration/Hardware
Url: https://github.com/fedora-iot/clevis-pin-tpm2

Source: %url/archive/v%version/%name-%version.tar.gz
Source1: vendor.tar

BuildRequires(pre): /proc rpm-build-rust
BuildRequires: clang-devel libssl-devel libtpm2-tss-devel

%description
%summary.

%prep
%setup -a1

sed -i 's|/tss2/tss2|/tss2|g' \
  vendor/tss-esapi-sys/build.rs

mkdir -p .cargo
cat >> .cargo/config <<EOF
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

%install
cargo install %_smp_mflags --offline --no-track --path .
ln -s %_bindir/%name %buildroot%_bindir/clevis-encrypt-tpm2plus
ln -s %_bindir/%name %buildroot%_bindir/clevis-decrypt-tpm2plus

%files
%doc LICENSE README.md
%_bindir/%name
%_bindir/clevis-encrypt-tpm2plus
%_bindir/clevis-decrypt-tpm2plus

%changelog
* Wed Sep 13 2023 Leontiy Volodin <lvol@altlinux.org> 0.5.3-alt1
- Initial build for ALT Sisyphus.
- Needed for clevis 19.
