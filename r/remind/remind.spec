%define def_loc MOSCOW
# see patch for a list

Name: remind
Version: 03.01.12
Release: alt2

Summary: Remind is a full-featured calendar/alarm program
License: GPL
Group: Office

URL: http://www.roaringpenguin.com/products/remind
Source0: http://www.roaringpenguin.com/files/download/%name-%version.tar.gz
Source1: remind.desktop
Source100: remind.watch
Patch: remind-03.01.05-alt-customs.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): Полноценный органайзер
Summary(uk_UA.KOI8-U): Повноц╕нний ор╜анайзер

%description
Full-featured calendar/reminder program featuring sophisticated date
calculation, moon phases, sunrise/sunset, Hebrew calendar, alarms,
PostScript output, Tcl/Tk GUI front-end, multilingual messages, and
proper handling of holidays.  Available for UNIX, MS-DOS, OS/2, and
other platforms.  Includes scripts for making a nice WWW calendar
server.

%description -l ru_RU.KOI8-R
Полноценный органайзер с большими возможностями по манипуляции датами,
поддержкой вычисления фаз луны и времени заката/восхода, еврейским
календарем, предупреждениями, выводом в PostScript, дополнительным
графическим интерфейсом и надлежащей поддержкой праздников.
Программа доступна для UNIX, DOS, OS/2 и других платформ.  Включает
скрипты для создания функционального сервера календаринга.

%description -l uk_UA.KOI8-U
Повноц╕нний ор╜анайзер ╕з великими можливостями щодо ман╕пуляц╕╖ датами,
п╕дтримкою обчислення фаз м╕сяця та часу сходу та заходу сонця,
╓врейським календарем, попередженнями, виводом у PostScript, додатковим
граф╕чним ╕нтерфейсом та належною п╕дтримкою свят.  Програма доступна
для UNIX, DOS, OS/2 та ╕нших платформ.  Включа╓ скрипти для створення
функц╕онального серверу календарин╜а.

%package -n tk%name
Summary: TkRemind frontend
Group: Office
Requires: tcllib remind
BuildArch: noarch

%description -n tk%name
This package contains tkremind, the GUI frontend
to remind(1) utility, and Sun's "cm" calendar manager
format convertor.

%prep
%setup
%patch -p1

%build
CFLAGS="%optflags -D%def_loc" %configure 
%make_build

# Known cities (see patch):
# ANADYR ARKHANGELSK ASHKHABAD BAKU BARNAUL CHITA IGARKA KIEV KRASNODAR
# MAGDAGACHI MOSCOW PERM PETROPAVLOVSK RIGA SARATOV TASHKENT VLADIVOSTOK
# VORKUTA YAKUTSK OTTAWA

# TODO: prepare for runtime switching?

%install
# work around broken install target in Makefile -- or my /dev/hands ?
mkdir -p %buildroot{%_bindir,%_man1dir}
%makeinstall
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/rem
%_bindir/rem2ps
%_bindir/remind
%_man1dir/rem.1*
%_man1dir/rem2ps.1*
%_man1dir/remind.1*
#_sysconfdir/cron.daily/*
%doc COPYRIGHT README docs/README.UNIX docs/WHATSNEW www

%files -n tk%name
%_bindir/tkremind
%_bindir/cm2rem.tcl
%_man1dir/tkremind.1*
%_man1dir/cm2rem.1*
%_desktopdir/*

# TODO:
# - un-hardwire city selection (see also #6781)
# - initscript (remind -z)
# - cronjob subpackage?

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 03.01.12-alt2
- added watch file

* Tue Jan 24 2012 Michael Shigorin <mike@altlinux.org> 03.01.12-alt1
- 03.01.12

* Sat Dec 17 2011 Michael Shigorin <mike@altlinux.org> 03.01.11-alt2
- tkremind made noarch

* Sat Dec 17 2011 Michael Shigorin <mike@altlinux.org> 03.01.11-alt1
- 03.01.11

* Tue Apr 12 2011 Michael Shigorin <mike@altlinux.org> 03.01.10-alt1
- 03.01.10
- added missing tkremind dependencies (thx vova1971/narod.ru):
  + tcllib (closes: #25425)
  + remind (closes: #25426)

* Mon Jun 21 2010 Michael Shigorin <mike@altlinux.org> 03.01.09-alt1
- 03.01.09

* Tue Mar 09 2010 Michael Shigorin <mike@altlinux.org> 03.01.08-alt1
- 03.01.08

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 03.01.07-alt4
- split tkremind and cm2rem.tcl into tkremind package

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 03.01.07-alt3
- enhanced categories in desktop file

* Tue Jun 02 2009 Michael Shigorin <mike@altlinux.org> 03.01.07-alt2
- fixed deeply broken desktop file

* Mon Jun 01 2009 Michael Shigorin <mike@altlinux.org> 03.01.07-alt1
- 03.01.07

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 03.01.06-alt2
- applied repocop patch

* Sun Nov 16 2008 Michael Shigorin <mike@altlinux.org> 03.01.06-alt1
- 03.01.06

* Wed Apr 16 2008 Michael Shigorin <mike@altlinux.org> 03.01.05-alt1
- 03.01.05
- updated patch
- remind-all.sh dropped upstream

* Fri Aug 17 2007 Michael Shigorin <mike@altlinux.org> 03.01.00-alt1
- 03.01.00
- updated patch
- macrified default location (alas, it's still build time constant)

* Sat Jan 27 2007 Michael Shigorin <mike@altlinux.org> 03.00.24-alt1
- 03.00.24
- spec macro abuse cleanup
- added freedesktop menu file, removed Debian one

* Sun Sep 18 2005 Michael Shigorin <mike@altlinux.org> 03.00.23-alt1
- 03.00.23
- fixed Url:, thanks to Vitaly Lipatov (lav@)

* Fri Jun 18 2004 Michael Shigorin <mike@altlinux.ru> 03.00.22-alt2
- moved to Office/Time management (#4415); thanks to Vitaly Lipatov (lav@)
  for prompting

* Mon Oct 14 2002 Michael Shigorin <mike@altlinux.ru> 03.00.22-alt1.1
- built with gcc3.2
- updated dependencies

* Sun Apr  7 2002 Michael Shigorin <mike@altlinux.ru> 03.00.22-alt1
- built for ALT
- small fixes (incl. /tmp)
- xUSSR city location data added
