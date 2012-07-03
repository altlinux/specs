%define oname beep
Name: beep-speaker
Version: 1.2.2
Release: alt1

Summary: Beep the pc speaker any number of ways

License: GPL
Group: Sound
Url: http://www.johnath.com/beep/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.johnath.com/beep/%oname-%version.tar.bz2
Patch0: beep_1.2.2-17.diff

%description
Beep allows the user to control the pc-speaker with precision,
allowing different sounds to indicate different events. While it
can be run quite happily on the commandline, it's intended place
of residence is within shell/perl scripts, notifying the user when
something interesting occurs. Of course, it has no notion of
what's interesting, but it's real good at that notifying part.

%prep
%setup -q -n %oname-%version
%patch0 -p1

%build
gcc %optflags -Wall -o beep beep.c

%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_man1dir
install -m 755 beep %buildroot/%_bindir/
gunzip beep.1.gz
install -m 644 beep.1 %buildroot%_man1dir/

%files
%doc CHANGELOG CREDITS README
%_bindir/beep
%_man1dir/*

%changelog
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

