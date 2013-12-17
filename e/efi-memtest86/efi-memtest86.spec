%define beta %nil

Name: efi-memtest86
Version: 5.0
Release: alt3

Summary: EFI binary of Passmark Memtest86 V5
License: distributable
Group: System/Kernel and hardware

Url: http://www.memtest86.com
Source0: %name-%version%beta.tar.gz
Source1: README.ALT

# x86 might be added but the sense is quite faint
ExclusiveArch: x86_64

BuildRequires: rpm-macros-uefi
BuildRequires: pesign >= 0.109-alt4

AutoReqProv: no

%define mt86data %_datadir/%name

%description
UEFI implementation of memtest86 V5.0.

NB: these binaries are proprietary (see license.rtf)
distributed under permission (see README.ALT).

Please note that the official build is signed; this shouldn't
intervene in any way but rather provides means to cope with
UEFI SecureBoot (better described as Restricted Boot) firmware
when one can't disable it easily, doesn't want to, or needs not to.

%prep
%setup -n %name

%install
install -pDm644 EFI/MemTest86-x64.efi %buildroot%_efi_bindir/memtest86.efi

mkdir -p %buildroot%mt86data
cp -a EFI/*.{cfg,png,htm,css} %buildroot%mt86data

%pesign -s -i %buildroot%_efi_bindir/memtest86.efi

install %SOURCE1 .

%files
%doc license.rtf README.ALT
%doc guide.pdf
%_efi_bindir/memtest86.efi
%mt86data/

%changelog
* Tue Dec 17 2013 Michael Shigorin <mike@altlinux.org> 5.0-alt3
- updated pesign macros use, reworked binaries installation
- prepare for production signing

* Mon Dec 16 2013 Michael Shigorin <mike@altlinux.org> 5.0-alt2
- pesign with test certs
- added official guide (PDF)

* Wed Dec 11 2013 Michael Shigorin <mike@altlinux.org> 5.0-alt1
- V5.0, thanks upstream

* Thu Nov 28 2013 Michael Shigorin <mike@altlinux.org> 5.0-alt0.1
- initial release based on 20131031 binaries
