# -*- rpm-spec -*-
# $Id: avrdude,v 1.2 2005/02/02 09:35:55 grigory Exp $

%def_enable doc

Summary: AVRDUDE is software for programming Atmel AVR Microcontrollers.
Name: avrdude
Version: 5.11.1
Release: alt1
License: GPL
Group: Development/Other
URL: http://savannah.nongnu.org/projects/avrdude
Source0: %name-%version.tar.gz

BuildRequires: flex libncurses-devel libreadline-devel libusb-compat-devel

%if_enabled doc
BuildRequires: tetex-core tetex-dvips tetex-latex
%endif

%package docs
Summary: Documentation for AVRDUDE.
Group: Development/Other
BuildArch: noarch

%description
AVRDUDE is software for programming Atmel AVR Microcontrollers.

%description docs
Documentation for avrdude in html, postscript and pdf formats.

%prep
%setup -q

%build
%configure %{subst_enable doc} --enable-parport
%make

%install
%makeinstall

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

%changelog
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



