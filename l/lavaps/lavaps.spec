Name: lavaps
Version: 2.7
Release: alt3

Summary: a lava lamp of currently running processes
License: GPL
Group: Toys

Url: http://www.isi.edu/~johnh/SOFTWARE/LAVAPS/
Source0: http://www.isi.edu/~johnh/SOFTWARE/LAVAPS/%name-%version.tar.gz
Source1: %name.xpm
Source2: %name.desktop
Patch: lavaps_2.7-4.2.diff

Summary(ru_RU.KOI8-R): отображение запущенных процессов
Summary(uk_UA.KOI8-U): в╕дображення наявних процес╕в

# Automatically added by buildreq on Wed Nov 09 2011
# optimized out: GConf ORBit2-devel fontconfig fontconfig-devel glib2-devel gnome-vfs gnome-vfs-devel libGConf-devel libICE-devel libSM-devel libX11-devel libart_lgpl-devel libatk-devel libavahi-glib libbonobo-devel libbonoboui-devel libcairo-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgnome-devel libgnome-keyring libgnomecanvas-devel libgpg-error libgtk+2-devel libpango-devel libpopt-devel libstdc++-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators pkg-config xorg-xproto-devel
BuildRequires: gcc-c++ imake libXext-devel libgnomeui-devel perl-Pod-Parser perl-XML-Parser perl-devel tcl xorg-cf-files

%description
Lavaps is an interactive process-tracking program like ``top'', but
with a much different attitude.  Rather than presenting lots of
specific info in digital form, it tries to present certain important
information in a graphical analog form.  The idea is that you can run
it in the background and get a rough idea of what's happening to your
system without devoting much concentration to the task.

%description -l ru_RU.KOI8-R
Lavaps - интерактивная программа отслеживания состояния процессов
наподобие top, но представляющая не точные цифровые данные,
а "ощущение" в графическом виде.

%description -l uk_UA.KOI8-U
Lavaps - ╕нтерактивна програма в╕дсл╕дковування стану процес╕в
на кшталт top, але надаюча не цифров╕ дан╕, а "в╕дчуття"
у граф╕чному вигляд╕.

%prep
%setup
%patch -p1

%build
sed -i 's|\(^DEFS = \)|\1-DUSE_NON_CONST |' Makefile.in
%configure
# apparently SMP-incompatible build
make

%install
%makeinstall
install -pDm644 %SOURCE1 %buildroot%_niconsdir/%name.xpm
install -pDm644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
%find_lang %name

%files -f %name.lang
%doc README
%_bindir/*
%_man1dir/*
%_niconsdir/*
%_desktopdir/*
%_sysconfdir/gconf/schemas/*

%changelog
* Wed Nov 09 2011 Michael Shigorin <mike@altlinux.org> 2.7-alt3
- applied debian patch to fix FTBFS:
  + superfluous header included
  + g++ tweaks
- replaced legacy debian menufile with a fd.o one from opensuse
- minor spec cleanup
- buildreq

* Mon Feb 06 2006 Michael Shigorin <mike@altlinux.org> 2.7-alt2
- s/XFree86-devel-static/XFree86-devel/

* Tue Mar 01 2005 Michael Shigorin <mike@altlinux.ru> 2.7-alt1
- 2.7
- added translations and gconf schemas
- marked build stage as SMP-incompatible

* Sun Aug 15 2004 Michael Shigorin <mike@altlinux.ru> 2.6-alt1
- 2.6 (minor bugfixes)

* Fri Jun 11 2004 Michael Shigorin <mike@altlinux.ru> 2.5-alt1
- 2.5

* Fri Sep 26 2003 Michael Shigorin <mike@altlinux.ru> 2.4-alt1
- 2.4 (minor bugfixes)

* Fri Jul 18 2003 Michael Shigorin <mike@altlinux.ru> 2.3-alt2
- buildreq run and several specific requires added by hand

* Wed Jul 16 2003 Michael Shigorin <mike@altlinux.ru> 2.3-alt1
- 2.3

* Thu Sep 26 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.20-alt2
- rebuilt with tcl 8.4

* Tue Jul 23 2002 Michael Shigorin <mike@altlinux.ru> 1.20-alt1
- built for ALT Linux
