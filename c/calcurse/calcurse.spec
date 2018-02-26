Name: calcurse
Version: 2.8
Release: alt1

Summary: Calcurse is a text-based personal organizer
Group: Office
License: GPL
Url: http://culot.org/calcurse/

Source0: %name-%version.tar.gz

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Sat Nov 15 2008
BuildRequires: libncurses-devel

%description
Calcurse is a text-based personal organizer which helps keeping track
of events and everyday tasks. It contains a calendar, a 'todo' list,
and puts your appointments in order. The user interface is
configurable, and one can choose between different color schemes and
layouts.  All of the commands are documented within an online help
system.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO doc/*.html doc/*.css
%_bindir/*
%_man1dir/*

%changelog
* Fri Aug 27 2010 Ilya Mashkin <oddity@altlinux.ru> 2.8-alt1
- 2.8

* Sat Oct 17 2009 Ilya Mashkin <oddity@altlinux.ru> 2.7-alt1
- 2.7

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 2.5-alt1
- 2.5

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 2.3-alt1
- 2.1 -> 2.3

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 2.1-alt1
- 2.0 -> 2.1

* Tue Mar 04 2008 Igor Zubkov <icesik@altlinux.org> 2.0-alt1
- 1.9 -> 2.0

* Wed Oct 24 2007 Igor Zubkov <icesik@altlinux.org> 1.9-alt1
- 1.8 -> 1.9

* Wed May 23 2007 Igor Zubkov <icesik@altlinux.org> 1.8-alt1
- 1.7 -> 1.8

* Wed Feb 21 2007 Igor Zubkov <icesik@altlinux.org> 1.7-alt1
- 1.6 -> 1.7
- clean up build requires

* Mon Oct 23 2006 Igor Zubkov <icesik@altlinux.org> 1.6-alt1
- 1.5 -> 1.6

* Sun Sep 10 2006 Igor Zubkov <icesik@altlinux.org> 1.5-alt1
- 1.4 -> 1.5
- buildreq

* Fri May 19 2006 Igor Zubkov <icesik@altlinux.ru> 1.4-alt1
- 1.4

* Fri Mar 31 2006 Igor Zubkov <icesik@altlinux.ru> 1.3-alt1
- 1.3
- buildreq

* Fri Dec 16 2005 Igor Zubkov <icesik@altlinux.ru> 1.2-alt1
- 1.2

* Sun Oct 30 2005 Igor Zubkov <icesik@altlinux.ru> 1.1-alt1
- Initial build for Sisyphus
