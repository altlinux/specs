Name: alt-uefi-keys
Version: 0.1
Release: alt1

Summary: A set of ALT Linux keys to sign UEFI binaries
License: Public domain
Group: System/Kernel and hardware

Url: http://www.altlinux.org/UEFI
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: rpm-macros-uefi
BuildArch: noarch

%description
This package contains a test set of keys generated for signing
ALT Linux bootloaders to operate under UEFI SecureBoot regime
(aka "Restricted Boot").

These are aimed to be enrolled manually by the user so the
private part is also included (note that there's a possibility
of malware being signed with it but that's negligible at this
experimental stage and the next one will be different).

See also:
http://mjg59.dreamwidth.org/20303.html
http://www.rodsbooks.com/efi-bootloaders/secureboot.html

%package private
Summary: The private part of UEFI SB signing keys
License: Public domain
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description private
This package holds the private part (the one used for signing).

%prep
%setup

%build

%install
install -pDm644 MOK.key %buildroot%_efi_keydir/altlinux.key
install -pDm644 MOK.crt %buildroot%_efi_keydir/altlinux.crt
install -pDm644 MOK.cer %buildroot%_efi_keydir/altlinux.cer

%files
%_efi_keydir/altlinux.crt
%_efi_keydir/altlinux.cer

%files private
%_efi_keydir/altlinux.key

%changelog
* Wed Jan 09 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

