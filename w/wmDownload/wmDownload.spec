Name: wmDownload
Version: 0.1.2a
Release: alt3

Summary: WindowMaker dockapp that display how much data received
Summary(ru_RU.UTF-8): отображает количество переданых данных
License: GPL
Group: Graphical desktop/Window Maker

Url: http://sourceforge.net/projects/wmdownload/

Source0: %name-%version.tar.gz
Source1: %name.menu

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Wed Oct 28 2009
BuildRequires: libXext-devel libdockapp-devel

%description
wmDownload monitors and displays how much data the user has recieved
on each device since the last machine reboot.

%description -l ru_RU.UTF-8
wmDownload проверяет и отображает, сколько данных пользователь 
получил на каждое устройство с момента последней перезагрузки.

%prep
%setup -q

%build
%make_build CFLAGS="%optflags"

%install
install -D -pm 755 wmDownload %buildroot%_bindir/%name
install -D -pm 644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc BUGS CHANGELOG CREDITS HINTS README TODO
%_bindir/*
%_menudir/*

%changelog
* Wed Oct 28 2009 Igor Zubkov <icesik@altlinux.org> 0.1.2a-alt3
- rebuild

* Sun Oct 25 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.2a-alt2.2
- a friendly repocop NMU: removed post %%update_menus/%%clean_menus

* Tue Mar 20 2007 Igor Zubkov <icesik@altlinux.org> 0.1.2a-alt2.1
- rebuild with new gcc flags (-Wl,--as-needed)
- remove standard COPYING (GPL v2)

* Fri Jan 20 2006 Igor Zubkov <icesik@altlinux.ru> 0.1.2a-alt2
- add url (#8792)
- update buildrequires

* Mon Apr 11 2005 Sir Raorn <raorn@altlinux.ru> 0.1.2a-alt1.1
- Rebuilt with new libdockapp

* Thu Jun 05 2003 Denis Klykvin <nikon@altlinux.ru> 0.1.2a-alt1
- Initial build


