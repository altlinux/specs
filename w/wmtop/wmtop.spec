Name: wmtop
Version: 0.84
Release: alt5

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Dock-app that is a mini graphical version of the cpu monitoring utility top
License: GPL
Group: Graphical desktop/Window Maker

URL: http://wmtop.sourceforge.net/
Source0: http://dl.sf.net/wmtop/wmtop-%version.tar.bz2
Source1: wmtop.menu

# Automatically added by buildreq on Wed Dec 17 2008
BuildRequires: libXext-devel libXpm-devel

%description
wmtop maintains a view of the 3 top CPU (or memory) consuming processes
displaying the amount of CPU used as a horizontal bar. It's a kind of mini
'top'.

%prep
%setup

%build
%make_build CC="gcc %optflags" linux

%install
install -p -D -m755 wmtop %buildroot%_bindir/wmtop
install -p -D -m644 %SOURCE1 %buildroot%_menudir/wmtop

%files
%doc README CHANGES
%_bindir/wmtop
%_menudir/*

%changelog
* Wed Dec 17 2008 Victor Forsyuk <force@altlinux.org> 0.84-alt5
- Remove obsolete install time scripts.

* Thu Jun 07 2007 Victor Forsyuk <force@altlinux.org> 0.84-alt4
- Rebuild to move from /usr/X11R6 to /usr.
- Add URL and source location.
- Refresh build requirements.

* Fri Feb 13 2004 Alexey Dyachenko <alexd@altlinux.ru> 0.84-alt3
- rebuild 
- update build requires

* Mon Jan 27 2003 Alexey Dyachenko <alexd@altlinux.ru> 0.84-alt2
- rebuild 
- fix wrong packager name

* Fri Aug 16 2002 Alexey Dyachenko <dyachenko@fromru.com> 0.84-alt1
- initial build
