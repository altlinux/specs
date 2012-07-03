Name: isicom
Version: 3.09
Release: alt0.1

Summary: Multitech Intelligent Serial Internal (ISI) Support Tools

License: GPL (not Firmware)
Group: System/Kernel and hardware
Url: http://www.multitech.com/SUPPORT/Families/ISI/drivers.asp

Packager: Vitaly Lipatov <lav@altlinux.ru>

# available from: ftp://ftp.multitech.com/ISI-Cards/Linux/linux22x.tar
# package version unfortunately not mentioned org. package name :-(
Source: ftp://ftp.multitech.com/isi-cards/linux/l309_22x_24x.tar.bz2
Patch0: isicom_3.05-firmld.patch
#Patch1: isicom_3.05-Makefile.patch
ExcludeArch: alpha

%description
ISA-bus Multitech Intelligent Serial Internal (ISI) and Multi-Modem ISI server
card drivers for the following models:
  - ISIHP-2U,
  - ISIHP-2S,
  - ISIHI-2S,
  - ISI608,
  - ISI5634PCI/8,
  - ISI5634PCI/4,
  - ISI4608-PCI,
  - ISI4608,
  - ISI4604-PCI,
  - ISI3334/8e,
  - ISI3334/8,
  - ISI3334/4e,
  - ISI3334/4,
  - ISI2834/4

%prep
%setup -q -n l309_22x_24x
%patch0 -p1
#%patch1 -p1

%build
%make_build firmld

%install
mkdir -p %buildroot/{%_datadir/%name,%_sbindir}
install -m 755 firmld %buildroot/%_sbindir/
install -m 644 *.bin %buildroot/%_datadir/%name

%files
%doc README.TXT
%_sbindir/firmld
%_datadir/%name

%changelog
* Wed Oct 26 2005 Vitaly Lipatov <lav@altlinux.ru> 3.09-alt0.1
- new version
- change packager
- cleanup spec (Url and Source updated)

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.05-alt2
- Rebuilt in new environment

* Mon Mar 11 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.05-alt1
- 3.05
- Fixed firmware load path
- Fixed .spec for ALT Linux Sisyphus

* Sun Jan 14 2001 AEN <aen@logic.ru>
- RE adaptation

* Fri Nov 24 2000 Warly <warly@mandrakesoft.com> 3.0-4mdk
- remove module compilation, already in standard kernel

* Fri May 26 2000 David BAUDENS <baudens@mandrakesoft.com> 3.0-3mdk
- spec-helper
- Don't try to use -preferred-stack-boundary=2 with egcs
- Use %%{_tmppath} for BuildRoot

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0-2mdk
- ExcludeArch: alpha

* Wed Apr  5 2000 Denis Havlik <denis@havlik.org> 3.0-1mdk
- group: System/Kernel and hardware
- new makefile patch
- new description

* Sun Nov 07 1999 John Buswell <john@mandrakesoft.com>
- Build Release

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- sanitized the spec file
