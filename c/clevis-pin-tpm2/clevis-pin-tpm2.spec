Name: clevis-pin-tpm2
Version: 0.5.5
Release: alt1

Summary: Clevis PIN for unlocking with TPM2 supporting Authorized Policies

License: MIT
Group: System/Configuration/Hardware
Url: https://github.com/fedora-iot/clevis-pin-tpm2
VCS: https://github.com/fedora-iot/clevis-pin-tpm2

# Source-url: https://github.com/fedora-iot/clevis-pin-tpm2/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): /proc rpm-build-rust
BuildRequires: clang-devel libssl-devel libtpm2-tss-devel

%description
%summary.

%prep
%setup -a1
%patch -p1

sed -i 's|/tss2/tss2|/tss2|g' \
  vendor/tss-esapi-sys/build.rs

%rust_prep

%build
%rust_build

%install
%rust_install
ln -s %_bindir/%name %buildroot%_bindir/clevis-encrypt-tpm2plus
ln -s %_bindir/%name %buildroot%_bindir/clevis-decrypt-tpm2plus

%files
%doc LICENSES/ README.md
%_bindir/%name
%_bindir/clevis-encrypt-tpm2plus
%_bindir/clevis-decrypt-tpm2plus

%changelog
* Tue May 05 2026 Leontiy Volodin <lvol@altlinux.org> 0.5.5-alt1
- New version 0.5.5.

* Wed Mar 04 2026 Leontiy Volodin <lvol@altlinux.org> 0.5.4-alt1
- New version 0.5.4.
- Added VCS tag.

* Wed Sep 13 2023 Leontiy Volodin <lvol@altlinux.org> 0.5.3-alt1
- Initial build for ALT Sisyphus.
- Needed for clevis 19.
