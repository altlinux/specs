Name: varmon
Version: 1.2.1
Release: alt1

Summary: RAID management tool for Mylex DAC960/DAC1164 controllers
License: GPL
Group: Monitoring

Url: http://varmon.sourceforge.net
Source0: http://dl.sourceforge.net/varmon/%name-%version.tar.gz
# Source0-md5:	fd251b64ad4976ef8573f0d2a20a02f9
Packager: Ilya Mashkin <oddity@altlinux.org>

BuildRequires: ncurses-devel

Summary(pl): Narzêdzie do zarz±dzania macierzami RAID na kontrolerach Mylex DAC960/DAC1164

%define _sbindir /sbin

%description
VARMon is a free RAID manipulation / management tool for Mylex
DAC960/DAC1164 controller family.

%description -l pl
VARMon to narzêdzie do zarz±dzania i manipulacji macierzami RAID na
kontrolerach Mylex z rodziny DAC960/DAC1164.

%prep
%setup -q

%build
cc %optflags -o varmon varmon.c -Wall -lncurses -I%_includedir/ncurses

%install
install -D varmon %buildroot%_sbindir/varmon

%files
%doc README *.pdf
%_sbindir/varmon

%changelog
* Sun Dec 28 2008 Ilya Mashkin <oddity@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sat Apr 22 2006 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- built for ALT Linux
- spec rev 1.13 borrowed from PLD Linux <feedback@pld-linux.org>;
  these PLD folks worked on it:
  adamg, blues, darekr, glen, gotar, juandon, malekith, misi3k, qboosh
- spec cleanup

* Mon Oct 16 2000 Dragan Stancevic <visitor@valinux.com>
- recreated rpm with the proper credits in the source
- VARMon v. 1.0.2 adds support for the latest DAC driver

* Fri Dec 17 1999 Samuel Flory <sflory@valinux.com>
- Recompiled for 6.1.3
- updated to 1.0.0

* Fri Sep 10 1999 Samuel Flory <sflory@varesearch.com>
- created rpm
