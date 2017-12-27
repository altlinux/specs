Name: elilo
Version: 3.16
Release: alt1

Summary: EFI Linux Loader
License: GPL v2+
Group: System/Kernel and hardware

Url: http://elilo.sourceforge.net
Source0: http://downloads.sourceforge.net/elilo/%name-%version-all.tar.gz
Source1: debian.eliloalt.man8
Source2: elilo.conf.man5

BuildRequires: rpm-macros-uefi
BuildRequires: pesign >= 0.109-alt4
BuildRequires: gnu-efi

ExclusiveArch: x86_64

Obsoletes: elilo-signed

%description
ELILO is an EFI Linux boot loader for IA-64 (IPF), IA-32 (x86)
and x86_64 EFI-based platforms.

This package might hold pre-signed ELILO binary
to cope with UEFI SecureBoot (rather Restricted Boot).

%description -l pl.UTF-8
ELILO to linuksowy bootloader dla platform IA-64 (IPF), IA-32 (x86)
oraz x86_64 opartych na EFI.

%prep
%setup -c
tar xf %name-%version-source.tar.gz
mv elilo-%version-source elilo

%build
%make -C elilo -j1 \
	ARCH=$(arch | sed -e 's/i.86/ia32/') \
	OPTIMFLAGS="%optflags" \
	EFICRT0=%_libdir \
	EFILIB=%_libdir \
	GNUEFILIB=%_libdir

%install
install -pDm755 elilo/tools/eliloalt %buildroot%_sbindir/eliloalt
install -pDm644 elilo/elilo.efi %buildroot%_efi_bindir/elilo.efi
install -pDm644 %SOURCE1 %buildroot%_man8dir/eliloalt.8
install -pDm644 %SOURCE2 %buildroot%_man5dir/elilo.conf.5

%ifarch x86_64
%pesign -s -i %buildroot%_efi_bindir/elilo.efi
%endif

%files
%doc %version-release-notes.txt elilo/{ChangeLog,README*,TODO}
%doc elilo/docs/*.txt elilo/examples
%_sbindir/eliloalt
%_efi_bindir/elilo.efi
%_man8dir/eliloalt.8*
%_man5dir/elilo.conf.5*

%changelog
* Fri Nov 24 2017 Anton Farygin <rider@altlinux.ru> 3.16-alt1
- 3.16

* Wed Mar 01 2017 Michael Shigorin <mike@altlinux.org> 3.14-alt1.59265358
- FTBFS workaround: use gcc4.7

* Tue Dec 17 2013 Michael Shigorin <mike@altlinux.org> 3.14-alt1.5926535
- build with gnu-efi 3.0r to be sure
- prepare for production signing

* Wed Nov 20 2013 Michael Shigorin <mike@altlinux.org> 3.14-alt1.592653
- build with current gnu-efi
- pesign with ALT key

* Mon Jul 29 2013 Michael Shigorin <mike@altlinux.org> 3.14-alt1.59265
- built with gnu-efi 3.0u

* Thu Feb 28 2013 Michael Shigorin <mike@altlinux.org> 3.14-alt1.5926
- built with gnu-efi 3.0t

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 3.14-alt1.592
- signing is only relevant for x86_64 (just as ALT ELILO)

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 3.14-alt1.59
- introduced signed subpackage
- use rpm-macros-uefi

* Tue Oct 30 2012 Michael Shigorin <mike@altlinux.org> 3.14-alt1.5
- moved elilo.efi from /boot/efi into %_libdir/efi:
  there's no warranty that the ESP is there at the package install time
  still working around an overmounted situation is no good at all
- robbed opensuse package of debian manpages as well
- minor spec cleanup

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 3.14-alt1
- built for Sisyphus; these PLD people worked on the spec:
  baggins glen qboosh
