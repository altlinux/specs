Name: wmgtemp
Version: 1.1
Release: alt1

Summary: Dock app for WindowMaker that displays the CPU and SYS temperatures
License: Artistic
Group: Graphical desktop/Window Maker

URL: http://www.fluxcode.net/
Source0: http://www.fluxcode.net/%name-%version.tar.gz
Source1: %name.menu

# Automatically added by buildreq on Wed Oct 20 2010
BuildRequires: libXext-devel libXpm-devel libsensors3-devel

%description
wmgtemp graphically displays the CPU and System temperatures using the lm_sensors package.
It was originally intended to work with the VIA686A chipset but an increasing list of
sensors are being supported. It displays the CPU and System temperature values, a scaling
graph of temperature history, and high-temperature warning lights.

%prep
%setup

%build
cd src
%make_build CCFLAGS="%optflags"

%install
install -p -D -m755 src/%name $RPM_BUILD_ROOT%_bindir/%name
install -p -D -m644 %name.1 $RPM_BUILD_ROOT%_man1dir/%name.1
install -p -D -m644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%_bindir/*
%_man1dir/*
%_menudir/*

%changelog
* Wed Oct 20 2010 Victor Forsiuk <force@altlinux.org> 1.1-alt1
- 1.1 (this version built with libsensors3).
- License is actually Artistic, not GPL.

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.7-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmgtemp
  * postclean-05-filetriggers for spec file

* Thu May 08 2008 Alexey Voinov <voins@altlinux.ru> 0.7-alt3
- /usr/X11R6 -> /usr
- buildreq fixed

* Mon Dec 29 2003 Alexey Voinov <voins@altlinux.ru> 0.7-alt2
- rebuild with new libsensors

* Sat Aug 23 2003 Alexey Voinov <voins@altlinux.ru> 0.7-alt1
- new version (0.7)
- rebuild with new libsensors

* Wed Oct 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt3
- rebuild with gcc3

* Mon Oct  1 2001 Alexey Voinov <voins@voins.program.ru> 0.5-alt2
- auto buildreqs added

* Sun Sep 30 2001 Alexey Voinov <voins@voins.program.ru> 0.5-alt1
- initial build

