Name: wmtop
Version: 0.84
Release: alt7

Summary: Dock-app that is a mini graphical version of the cpu monitoring utility top
License: GPL
Group: Graphical desktop/Window Maker

Url: http://wmtop.sourceforge.net/
Source0: http://dl.sf.net/wmtop/%name-%version.tar.bz2
Source1: wmtop.menu
Packager: Victor Forsyuk <force@altlinux.org>

# Automatically added by buildreq on Wed Dec 17 2008
BuildRequires: libXext-devel libXpm-devel

%description
wmtop maintains a view of the 3 top CPU (or memory) consuming processes
displaying the amount of CPU used as a horizontal bar.
It's a kind of mini 'top'.

%prep
%setup
sed -i 's,^FLAGS.*,& -std=gnu89,' Makefile

%build
%make_build CC="gcc %optflags" linux

%install
install -pDm755 wmtop %buildroot%_bindir/wmtop
install -pDm644 %SOURCE1 %buildroot%_menudir/wmtop

%files
%doc README CHANGES
%_bindir/wmtop
%_menudir/*

%changelog
* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 0.84-alt7
- gcc5 FTBFS workaround (-std=gnu89)

* Tue Oct 15 2013 Michael Shigorin <mike@altlinux.org> 0.84-alt6
- fixed menu file

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.84-alt5.qa1
- NMU: rebuilt for debuginfo.

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
