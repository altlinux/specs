Name: uefi-utils
Version: 0.1
Release: alt1

Summary: Various (U)EFI utilities
License: GPLv2+
Group: System/Kernel and hardware

Url: https://github.com/fpmurphy/UEFI-Utilities
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: rpm-macros-uefi
BuildRequires: pesign >= 0.109-alt4
BuildRequires: gnu-efi

ExclusiveArch: x86_64

%description
%summary

%package listcerts
Summary: List UEFI SecureBoot certificates
Group: System/Kernel and hardware

%description listcerts
This UEFI binary helps inspect
the Restricted Boot certs installed.

%prep
%setup
sed -i 's,gnuefi/,,g' */Makefile

%build
cd listcerts
make CFLAGS="-fPIC -U_FORTIFY_SOURCE -fno-stack-protector"

%install
install -pDm644 listcerts/listcerts.efi %buildroot%_efi_bindir/listcerts.efi

%ifarch x86_64
%pesign -s -i %buildroot%_efi_bindir/listcerts.efi
%endif

%files listcerts
%_efi_bindir/listcerts.efi
%doc listcerts/README

%changelog
* Wed Jun 11 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release
  + listcerts only
  + proposed by Matt Lewandowsky

