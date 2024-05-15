Name: alt-uefi-certs
Version: 3.0
Release: alt1

Summary: A set of ALT Linux certificates to verify UEFI binaries
License: Public domain
Group: System/Kernel and hardware

Url: http://en.altlinux.org/UEFI_SecureBoot_mini-HOWTO
Source: %name-%version.tar

BuildRequires: rpm-macros-uefi >= 0.5
BuildArch: noarch

Obsoletes: alt-uefi-keys alt-uefi-keys-private

%description
This package contains ALT Linux UEFI SB CA certificate
corresponding to the private key that is now used to sign
ALT Linux UEFI bootloaders to cope with UEFI SecureBoot regime
(aka "Restricted Boot").

This can be enrolled by the user so that ALT shim and
subsequent bootloaders are accepted by firmware
without Microsoft's certificates.

See also:
http://mjg59.dreamwidth.org/20303.html
http://www.rodsbooks.com/efi-bootloaders/secureboot.html
%url

%prep
%setup

%build

%install
install -pDm644 altlinux-ca.cer %buildroot%_efi_keydir/altlinux.cer

%files
%_efi_keydir/altlinux.cer

%changelog
* Wed May 08 2024 Egor Ignatov <egori@altlinux.org> 3.0-alt1
- replace ALT UEFI SB CA 2021 with ALT Linux Secure Boot CA 2024

* Tue Aug 03 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.0-alt1
- replaced ALT UEFI SB CA 2013 certificate with ALT UEFI SB CA 2021

* Mon Apr 22 2019 Michael Shigorin <mike@altlinux.org> 1.0-alt2
- oops, it's still used in mkimage
- updated Url:

* Wed Dec 11 2013 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- dropped test crypto material
- added ALT UEFI SB CA 2013 certificate
- renamed the package from alt-uefi-keys to alt-uefi-certs
  as there are no keys within it anymore

* Wed Jan 09 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

