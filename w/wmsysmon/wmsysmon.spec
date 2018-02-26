Name: wmsysmon
Version: 0.7.7
Release: alt2

Packager: Alexey Voinov <voins@altlinux.ru>

Summary: WindowMaker dockapp to show system information
Summary(ru_RU.KOI8-R): Dockapp для WindowMaker. Показывает системную информацию
License: GPL
Group: Graphical desktop/Window Maker
Url:   http://gnugeneration.com/software/wmsysmon/

Source0: %name-%version.tar.bz2
Source1: %name.menu

Patch0: %name-0.7.6-alt-gcc34.patch
Patch1: %name-%version-alt-linux26.patch

# Automatically added by buildreq on Thu Jan 04 2007
BuildRequires: libXext-devel libXpm-devel

%description
wmsysmon, a small dock application for use with
WindowMaker (www.windowmaker.org) to show system information on interrupt
activity, memory use, swap use, and IO.

%description -l ru_RU.KOI8-R
wmsysmon - это маленькое приложение для WindowMaker, которое показывает информацию
о прерываниях, памяти и операциях ввода/вывода.

%prep
%setup -q
%__subst 's/\+=/=/' src/Makefile
%patch0 -p1
%patch1 -p1

%build
%make_build -C src CFLAGS="$RPM_OPT_FLAGS"

%install
install -D -pm755 src/wmsysmon $RPM_BUILD_ROOT%_bindir/%name
install -D -pm644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%doc README ChangeLog
%_bindir/*
%_menudir/*

%changelog
* Fri Nov 06 2009 Alexey Voinov <voins@altlinux.ru> 0.7.7-alt2
- update_menus removed

* Thu Jan 04 2007 Alexey Voinov <voins@altlinux.ru> 0.7.7-alt1
- 0.7.7 (forgotten version?)
- /usr/X11R6 -> /usr
- url fixed
- buildreqs updated
- linux 2.6.x adaptations

* Tue Jan 25 2005 Alexey Voinov <voins@altlinux.ru> 0.7.6-alt4
- gcc-3.4 build fixed
- buildreqs updated

* Fri Oct 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.7.6-alt3
- rebuild with gcc3

* Sat Jun  9 2001 Alexey Voinov <voins@voins.program.ru>
- menu rearranged

* Thu May  7 2001 Alexey Voinov <voins@voins.program.ru>
- initial build

