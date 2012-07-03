# "internal name"
# i don't want to rename package still
%define iname wmmemmon

Summary: WMMemMon - A dockapp to monitor memory/swap usages
Name: WMMemMon
Version: 1.0.1
Release: alt3
License: GPL
Group: Graphical desktop/Window Maker

Packager: Alexey Voinov <voins@altlinux.ru>

Url: http://www.sh.rim.or.jp/~ssato/dockapp/index.shtml#wmmemmon

Source0: http://www.sh.rim.or.jp/~ssato/src/%iname-%version.tar.bz2
Source1: %iname.menu

# Automatically added by buildreq on Thu Jan 04 2007
BuildRequires: imake libXext-devel libXpm-devel libXt-devel xorg-cf-files

%description
WMMemMon is a program to monitor memory/swap usages. It is a dockapp that is
supported by X window managers such as Window Maker, AfterStep, BlackBox, and
Enlightenment.

The current memory usage is displaied as the outside pie-slices.  The swap usage
is represented by the inside slices. It has an LCD look-alike user interface.
The back-light may be turned on/off by clicking the mouse button over the
appliacation. If the usage hits a certain threshold, an alarm-mode will alert
you by turning back-light on.

%prep
%setup -q -n %iname-%version

%build
%configure
%make_build

%install
install -p -D -m755 src/%iname $RPM_BUILD_ROOT%_bindir/%iname
install -p -D -m644 doc/%iname.1 $RPM_BUILD_ROOT%_man1dir/%iname.1
install -p -D -m644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%iname

%files
%doc README NEWS INSTALL TODO AUTHORS ChangeLog
%_bindir/*
%_man1dir/*
%_menudir/*

%changelog
* Wed Nov 04 2009 Alexey Voinov <voins@altlinux.ru> 1.0.1-alt3
- update_menus removed

* Thu Jan 04 2007 Alexey Voinov <voins@altlinux.ru> 1.0.1-alt2
- /usr/X11R6 -> /usr
- buildreqs updated

* Wed Jun 09 2004 Alexey Voinov <voins@altlinux.ru> 1.0.1-alt1
- new version (1.0.1)

* Mon Mar 10 2003 Alexey Voinov <voins@voins.program.ru> 1.0.0-alt1
- new version (1.0.0)

* Wed Oct 23 2002 Stanislav Ievlev <inger@altlinux.ru> 0.7.0-alt4
- rebuild with gcc3

* Sat Aug 10 2002 Alexey Voinov <voins@voins.program.ru> 0.7.0-alt3
- fixed BuildRequires (thanks to pavel nikitin <np@seman.nsu.ru>
  for reporting)

* Thu May 30 2002 Alexey Voinov <voins@voins.program.ru> 0.7.0-alt2
- iname macro defined
- permissions on wmmemmon executable fixed
- menu updated, so the look will be as before (ignore buffers, ignore
  cached pages)

* Sat May 25 2002 Alexey Voinov <voins@voins.program.ru> 0.7.0-alt1
- new version (0.7.0)
- spec cleanup
- description/summary updated
- url updated

* Sat Jun 9 2001 Alexey Voinov <voins@voins.program.ru>
- menu rearranged

* Thu May 3 2001 Alexey Voinov <voins@voins.program.ru>
- initial build

