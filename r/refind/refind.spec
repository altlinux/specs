Name: refind
Version: 0.11.2
Release: alt1

Summary: EFI boot manager software
License: GPLv3
Group: System/Base

Url: http://www.rodsbooks.com/refind/
# https://git.code.sf.net/p/refind/code
Source: %name-%version.tar 
Source1: altlinux_altinst.png
Source2: altlinux_live.png
Source3: altlinux_rescue.png
Source4: os_altlinux.png

BuildRequires: gnu-efi >= 3.0.6-alt1
BuildRequires: unzip
BuildRequires: rpm-macros-uefi
BuildRequires: pesign >= 0.109-alt4
Requires: efibootmgr
Obsoletes: refind-signed

ExclusiveArch: x86_64

%define refind_lib %_efi_bindir
%define refind_data %_datadir/%name

%description
A graphical boot manager for EFI- and UEFI-based computers, such as all
Intel-based Macs and recent (most 2011 and later) PCs. rEFInd presents a
boot menu showing all the EFI boot loaders on the EFI-accessible
partitions, and optionally BIOS-bootable partitions on Macs. EFI-compatbile
OSes, including Linux, provide boot loaders that rEFInd can detect and
launch. rEFInd can launch Linux EFI boot loaders such as ELILO, GRUB
Legacy, GRUB 2, and 3.3.0 and later kernels with EFI stub support. EFI
filesystem drivers for ext2/3/4fs, ReiserFS, HFS+, and ISO-9660 enable
rEFInd to read boot loaders from these filesystems, too. rEFInd's ability
to detect boot loaders at runtime makes it very easy to use, particularly
when paired with Linux kernels that provide EFI stub support.

Please note that the official build is signed; this shouldn't
intervene in any way but rather provides means to cope with
UEFI SecureBoot (better described as Restricted Boot) firmware
when one can't disable it easily, doesn't want to, or needs not to.

%prep
%setup

%build
make gnuefi EFICRT0=%_libdir GNUEFILIB=%_libdir
make fs_gnuefi EFICRT0=%_libdir GNUEFILIB=%_libdir

%install
mkdir -p %buildroot{%refind_lib{,/drivers_%_efi_arch},%refind_data}

%ifarch x86_64
# don't feed macros with complicated expressions, esp. in the loop
for i in refind/refind*.efi drivers_%_efi_arch/*_x64.efi; do
	%pesign -s -i $i
done
%endif

install -pm644 refind/refind*.efi %buildroot%refind_lib/
cp -a drivers_%_efi_arch/*.efi %buildroot%refind_lib/drivers_%_efi_arch/

cp -a icons/ %buildroot%refind_data/
install -pDm644 %SOURCE1 %buildroot%refind_data/icons/altlinux/altinst.png
install -pDm644 %SOURCE2 %buildroot%refind_data/icons/altlinux/live.png
install -pDm644 %SOURCE3 %buildroot%refind_data/icons/altlinux/rescue.png
install -pDm644 %SOURCE4 %buildroot%refind_data/icons/os_altlinux.png

%files
%doc docs/*
%doc NEWS.txt COPYING.txt LICENSE.txt README.txt CREDITS.txt
%refind_lib
%refind_data

%changelog
* Sun Nov 26 2017 Anton Farygin <rider@altlinux.ru> 0.11.2-alt1
- 0.11.2
- icons converted to png (refind default format)

* Wed Mar 01 2017 Michael Shigorin <mike@altlinux.org> 0.6.12-alt4
- FTBFS workaround: use gcc4.7

* Tue Dec 17 2013 Michael Shigorin <mike@altlinux.org> 0.6.12-alt3
- built with gnu-efi 3.0r to be sure
- memtest86 support backported from 0.7.4
- added ALT-specific boot action icons
- updated pesign macros use, reworked binaries installation
- prepare for production signing

* Mon Jul 29 2013 Michael Shigorin <mike@altlinux.org> 0.6.12-alt2
- built with gnu-efi 3.0u

* Wed Jul 03 2013 Michael Shigorin <mike@altlinux.org> 0.6.12-alt1
- 0.6.12

* Wed May 08 2013 Michael Shigorin <mike@altlinux.org> 0.6.10-alt1
- 0.6.10

* Mon Apr 29 2013 Michael Shigorin <mike@altlinux.org> 0.6.9-alt1
- 0.6.9

* Tue Mar 19 2013 Michael Shigorin <mike@altlinux.org> 0.6.8-alt1
- 0.6.8

* Tue Feb 05 2013 Michael Shigorin <mike@altlinux.org> 0.6.7-alt1
- 0.6.7

* Wed Jan 30 2013 Michael Shigorin <mike@altlinux.org> 0.6.6-alt1
- 0.6.6

* Thu Jan 17 2013 Michael Shigorin <mike@altlinux.org> 0.6.5-alt1
- 0.6.5
- dropped os_altlinux icon (merged upstream)

* Sat Jan 12 2013 Michael Shigorin <mike@altlinux.org> 0.6.4-alt1
- initial build for ALT Linux Sisyphus
- stripped upstream installation helpers (too smart for a package)
- added os_altlinux icon

* Sun Jan 6 2013 R Smith <rodsmith@rodsbooks.com> - 0.6.3-2
- Fixed accidental inclusion of "env" as part of installation script

* Sun Jan 6 2013 R Smith <rodsmith@rodsbooks.com> - 0.6.3
- Created spec file for 0.6.3 release
