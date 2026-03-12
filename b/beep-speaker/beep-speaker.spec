Name: beep-speaker
Version: 1.4.12
Release: alt1

Summary: Beep the pc speaker any number of ways

License: GPL-2.0-only
Group: Sound
Url: https://github.com/spkr-beep/beep

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/spkr-beep/beep/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

%description
Beep allows the user to control the pc-speaker with precision,
allowing different sounds to indicate different events. While it
can be run quite happily on the commandline, it's intended place
of residence is within shell/perl scripts, notifying the user when
something interesting occurs. Of course, it has no notion of
what's interesting, but it's real good at that notifying part.

%prep
%setup

%build
%make_build prefix=%prefix CFLAGS="%optflags" CPPFLAGS=""

%install
%makeinstall_std prefix=%prefix
rm -rf %buildroot%_datadir/doc/beep

%files
%doc CREDITS.md NEWS.md README.md
%_bindir/beep
%_man1dir/*

%changelog
* Thu Mar 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1.4.12-alt1
- new version (1.4.12) via gear-uupdate
- updated upstream URL to github.com/spkr-beep/beep
- updated build to use upstream Makefile

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- new version 1.3 (with rpmrb script)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Mar 30 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- initial build for ALT Linux Sisyphus

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.2.2-7mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-7mdv2007.0
+ Revision: 101615
- Import beep

* Tue Jun 27 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-7mdv2007.0
- added one patch by debian

* Sat May 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-6mdk
- rebuild

* Thu Apr 08 2004 Michael Scherer <misc@mandrake.org> 1.2.2-5mdk
- Build release

