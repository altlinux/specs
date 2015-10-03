Name: wmsm
Version: 0.2.1
Release: alt3

Summary: System monitor for WindowMaker
License: GPL
Group: Graphical desktop/Window Maker

Url: http://repo.or.cz/w/dockapps.git
Source0: %name-%version.tar.bz2
Source1: %name.menu
Patch: %name-%version-%release.patch
Packager: Lebedev Sergey <barabashka@altlinux.org>

# Automatically added by buildreq on Wed Jul 23 2008
BuildRequires: libXext-devel libXpm-devel

%description
Simple dockapp for WindowMaker
what shows you  CPU, Memory, HardDisk I/O load
and Uptime of your machine.

%prep
%setup
sed -i 's,^CFLAGS.*,& -std=gnu89,' wmsm/Makefile

%build
cd wmsm
%make_build
cd ..

%install
mkdir -p %buildroot%_bindir
cd wmsm
%make_install PREFIX=%buildroot%_bindir install
cd ..
install -pDm644 %SOURCE1 %buildroot%_menudir/%name

%files 
%doc CHANGELOG COPYING
%_bindir/%name
%_menudir/%name

%changelog
* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 0.2.1-alt3
- gcc5 FTBFS workaround (-std=gnu89)
- minor spec cleanup
- updated Url:

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.1-alt2.qa2
- NMU: rebuilt for debuginfo.

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.1-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmsm
  * postclean-05-filetriggers for spec file

* Wed Jul 23 2008 Lebedev Sergey <barabashka@altlinux.org> 0.2.1-alt2
- fixed buildreq

* Tue May 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.1-alt1
- 0.2.1 release.

* Mon Nov 01 2004 Sergey Lebedev <barabashka@altlinux.ru> 0.2.0-alt1
- first build 

