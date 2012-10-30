Name: elilo
Version: 3.14
Release: alt1.5

Summary: EFI Linux Boot Loader
License: GPL v2+
Group: System/Kernel and hardware

Url: http://elilo.sourceforge.net
Source0: http://downloads.sourceforge.net/elilo/%name-%version-all.tar.gz
Source1: debian.eliloalt.man8
Source2: elilo.conf.man5

BuildRequires: gnu-efi >= 3.0d
ExclusiveArch: %ix86 x86_64 ia64

Summary(pl.UTF-8): Linuksowy bootloader dla platform EFI

%description
ELILO is the EFI Linux boot loader for IA-64 (IPF), IA-32 (x86)
and x86_64 EFI-based platforms.

%description -l pl.UTF-8
ELILO to linuksowy bootloader dla platform IA-64 (IPF), IA-32 (x86)
oraz x86_64 opartych na EFI.

%prep
%setup -c
tar xf elilo-%version-source.tar.gz

%build
%make -C elilo -j1 \
	ARCH=$(arch | sed -e 's/i.86/ia32/') \
	OPTIMFLAGS="%optflags" \
	EFICRT0=%_libdir \
	EFILIB=%_libdir \
	GNUEFILIB=%_libdir

%install
install -pDm755 elilo/tools/eliloalt %buildroot%_sbindir/eliloalt
install -pDm644 elilo/elilo.efi %buildroot%_libdir/efi/elilo.efi
install -pDm644 %SOURCE1 %buildroot%_man8dir/eliloalt.8
install -pDm644 %SOURCE2 %buildroot%_man5dir/elilo.conf.5

%files
%doc %version-release-notes.txt elilo/{ChangeLog,README*,TODO}
%doc elilo/docs/*.txt elilo/examples
%_sbindir/eliloalt
%_libdir/efi/elilo.efi
%_man8dir/eliloalt.8*
%_man5dir/elilo.conf.5*

%changelog
* Tue Oct 30 2012 Michael Shigorin <mike@altlinux.org> 3.14-alt1.5
- moved elilo.efi from /boot/efi into %_libdir/efi:
  there's no warranty that the ESP is there at the package install time
  still working around an overmounted situation is no good at all
- robbed opensuse package of debian manpages as well
- minor spec cleanup

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 3.14-alt1
- built for Sisyphus; these PLD people worked on the spec:
  baggins glen qboosh
