Name: wmsm
Version: 0.2.1
Release: alt2.qa1
Summary: System monitor for WindowMaker
License: GPL
Packager: Lebedev Sergey <barabashka@altlinux.org>

Group: Graphical desktop/Window Maker
Url: http://www.unetz.com/schaepe/DOCKAPPS/dockapps.html

Source0: %name-%version.tar.bz2
Source1: %name.menu
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Wed Jul 23 2008
BuildRequires: libXext-devel libXpm-devel



%description
Simple dockapp for WindowMaker
what shows you  CPU, Memory, HardDisk I/O load
and Uptime of your machine.

%prep
%setup -q -n %name-%version

%build
cd wmsm
%make_build
cd ..
%install
mkdir -p %buildroot%_bindir

cd wmsm
%make_install PREFIX=%buildroot%_bindir install
cd ..
install -p -D -m644 %SOURCE1 %buildroot/%_menudir/%name

%files 
%doc INSTALL CHANGELOG COPYING
%_x11bindir/%name
%_menudir/%name

%changelog
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

