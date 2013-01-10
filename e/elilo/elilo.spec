Name: elilo
Version: 3.14
Release: alt1.592

Summary: EFI Linux Loader
License: GPL v2+
Group: System/Kernel and hardware

Url: http://elilo.sourceforge.net
Source0: http://downloads.sourceforge.net/elilo/%name-%version-all.tar.gz
Source1: debian.eliloalt.man8
Source2: elilo.conf.man5

BuildRequires: gnu-efi >= 3.0d
BuildRequires: rpm-macros-uefi

# archdep BRs aren't straightforward at all but can be avoided here
ExclusiveArch: x86_64

%ifarch x86_64
BuildRequires: sbsigntools alt-uefi-keys-private
%endif

Summary(pl.UTF-8): Linuksowy bootloader dla platform EFI

%description
ELILO is an EFI Linux boot loader for IA-64 (IPF), IA-32 (x86)
and x86_64 EFI-based platforms.

%description -l pl.UTF-8
ELILO to linuksowy bootloader dla platform IA-64 (IPF), IA-32 (x86)
oraz x86_64 opartych na EFI.

%package signed
Summary: EFI Linux Loader (pre-signed binary)
License: GPL v2+
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description signed
This package holds the pre-signed binary of ELILO
to cope with UEFI SecureBoot (rather Restricted Boot).

%prep
%setup -c
tar xf %name-%version-source.tar.gz

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
# autocreates signed.manifest
%_efi_sign %buildroot%_efi_bindir/elilo.efi
%endif

%files
%doc %version-release-notes.txt elilo/{ChangeLog,README*,TODO}
%doc elilo/docs/*.txt elilo/examples
%_sbindir/eliloalt
%_efi_bindir/elilo.efi
%_man8dir/eliloalt.8*
%_man5dir/elilo.conf.5*

%ifarch x86_64
%files -f signed.manifest signed
%endif

%changelog
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
