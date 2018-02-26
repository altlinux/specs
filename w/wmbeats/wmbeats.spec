Name: wmbeats
Version: 1.2
Release: alt5.qa1

Packager: Alexey Voinov <voins@altlinux.ru>

Summary: WMBeats displays the time accoridng to Swatch's Internet Time Standard
License: GPL
Group: Graphical desktop/Window Maker

Source0: %name-%version.tar.bz2
Source1: %name.menu

# Automatically added by buildreq on Thu May 08 2008
BuildRequires: libXext-devel libXpm-devel libdockapp-devel

%description
WMBeats displays the time accoridng to Swatch's Internet Time Standard

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
install -D -pm755 wmbeats $RPM_BUILD_ROOT%_bindir/%name
install -D -pm644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%doc README INSTALL ChangeLog
%_bindir/*
%_menudir/*

%changelog
* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmbeats
  * postclean-05-filetriggers for spec file

* Thu May 08 2008 Alexey Voinov <voins@altlinux.ru> 1.2-alt5
- /usr/X11R6 -> /usr
- buildreqs updated

* Wed Apr 13 2005 Alexey Voinov <voins@altlinux.ru> 1.2-alt4
- rebuild with new libdockapp

* Fri Oct 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2-alt3
- rebuild with gcc3

* Sat Jun  9 2001 Alexey Voinov <voins@voins.program.ru>
- menu rearranged

* Thu May  7 2001 Alexey Voinov <voins@voins.program.ru>
- initial build

