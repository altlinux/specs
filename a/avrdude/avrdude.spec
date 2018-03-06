# -*- rpm-spec -*-
# $Id: avrdude,v 1.2 2005/02/02 09:35:55 grigory Exp $

%def_enable doc

%set_verify_elf_method unresolved=relaxed

Summary: AVRDUDE is software for programming Atmel AVR Microcontrollers.
Name: avrdude
Version: 6.3
Release: alt3
License: GPL
Group: Development/Other
URL: http://www.nongnu.org/avrdude/
Source0: http://download.savannah.gnu.org/releases/avrdude/%name-%version.tar.gz
Patch: avrdude-install-header.patch

BuildRequires(pre): rpm-build-ubt

BuildRequires: gnu-config libtinfo-devel libusb-devel libusb-compat-devel makeinfo
BuildRequires: flex libelf-devel libftdi1-devel libncurses-devel libreadline-devel

%if_enabled doc
BuildRequires: texlive-collection-latexrecommended texi2html texi2dvi
%endif

%package docs
Summary: Documentation for AVRDUDE.
Group: Development/Other
BuildArch: noarch

%package devel
Summary: The AVRDUDE static library with API for other tools.
Group: Development/C
Provides: lib%name-devel = %version-%release
Provides: lib%name-static = %version-%release

%description
AVRDUDE is software for programming Atmel AVR Microcontrollers.

%description docs
Documentation for avrdude in html, postscript and pdf formats.

%description devel
AVRDUDE static library provides API integration for programming Atmel AVR Microcontrollers.

%prep
%setup -q
%patch -p2

%build
%autoreconf
%configure %{subst_enable doc} --enable-parport --enable-linuxgpio
%make

%install
%makeinstall
sed -i 's/^#include "ac_cfg\.h"$/#include <libavrdude_cfg.h>/' %buildroot%_includedir/libavrdude.h
install -T ac_cfg.h %buildroot%_includedir/libavrdude_cfg.h
rm -f %buildroot%_libdir/*.so*

%if_enabled doc
%post

%preun
%endif

%files
%doc AUTHORS ChangeLog* NEWS README doc/TODO
%config %_sysconfdir/%name.conf
%_bindir/*
%_man1dir/*

%if_enabled doc
%_infodir/*

%files docs
%doc doc/avrdude-html/*.html doc/avrdude.ps doc/avrdude.pdf
%endif

%files devel
%_includedir/*.h
%_libdir/*.a

%changelog
* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 6.3-alt3
- NMU: fixed BR: for texlive 2017

* Sun Oct 01 2017 Evgeny Sinelnikov <sin@altlinux.ru> 6.3-alt2%ubt
- Rebuild with libusb-compat-devel due needs for stk500v2 (ALT #33937)

* Thu Jul 27 2017 Evgeny Sinelnikov <sin@altlinux.ru> 6.3-alt1%ubt
- Update to last version with nonstandard speeds on port support (ALT #33688)
- Add avrdude-devel with static development library
- Build with universal build tag (aka ubt macros)

* Sat Jan 09 2016 Grigory Milev <week@altlinux.ru> 6.2-alt1
- new version released

* Tue May 19 2015 Grigory Milev <week@altlinux.ru> 6.1-alt1
- New version released
- flip2 patch obsolete

* Tue Dec 24 2013 Grigory Milev <week@altlinux.ru> 6.0.1-alt2
- Added flip2 bootloaders support (DFU Atmel bootloaders)

* Tue Oct 15 2013 Grigory Milev <week@altlinux.ru> 6.0.1-alt1
- new version released

* Mon Dec 05 2011 Grigory Milev <week@altlinux.ru> 5.11.1-alt1
- new vrsion release, see ChangeLog in docs for detales

* Fri Nov 05 2010 Grigory Milev <week@altlinux.ru> 5.10-alt2
- rebuilded with libusb (bug #24347)

* Thu Nov 04 2010 Grigory Milev <week@altlinux.ru> 5.10-alt1
- new version released
- change make_build to make due troubles with building documentation

* Tue Nov 24 2009 Grigory Milev <week@altlinux.ru> 5.8-alt1
- new version released
- fix dependenses
- remove depricated info install/uninstall scripts

* Fri Mar 27 2009 Grigory Milev <week@altlinux.ru> 5.6-alt1
- New version released
- Added support for USB

* Wed Jan 09 2008 Grigory Milev <week@altlinux.ru> 5.5-alt1
- Update for new version

* Sun Jul 01 2007 Evgeny Sinelnikov <sin@altlinux.ru> 5.3.1-alt1
- Update for new version
- Add enable macros for docs

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 4.4.0-alt1.1
- Rebuilt with libreadline.so.5.

* Tue Feb  1 2005 Grigory Milev <week@altlinux.ru> 4.4.0-alt1
- initial build for ALT Linux

* Wed Aug 27 2003 Theodore A. Roth <troth@openavr.org>
  [Thanks to Artur Lipowski <LAL@pro.onet.pl>]
- Do not build debug package.
- Remove files not packaged to quell RH9 rpmbuild complaints.

* Wed Mar 05 2003 Theodore A. Roth <troth@openavr.org>
- Add docs sub-package.
- Add %post and %preun scriptlets for handling info files.

* Wed Feb 26 2003 Theodore A. Roth <troth@openavr.org>
- Initial build.



