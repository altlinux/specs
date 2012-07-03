Name: xrestop
Version: 0.4
Release: alt4

Summary: A 'top' like tool for monitoring X Client server resource usage
License: GPLv2+
Group: Monitoring
Url: http://www.freedesktop.org/wiki/Software/xrestop

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: http://projects.o-hand.com/sources/xrestop/%name-%version.tar.gz

BuildPreReq: libX11-devel libXext-devel libXres-devel libncurses-devel

%description
Xrestop uses the X-Resource extension to provide 'top' like statistics
of each connected X11 client's server side resource usage. It is intended
as a developer tool to aid more efficient server resource usage and debug
server side leakage.

%description -l ru_RU.CP1251
Показывает статистику использования X-клиентами ресурсов X-сервера в
формате, похожем на вывод программы top.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS ChangeLog README

%changelog
* Mon Dec 01 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.4-alt4
- fix buildreqs

* Sun Nov 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.4-alt3
- update Url
- add Packager

* Wed Aug 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.4-alt2
- update buildreqs
- fix Url and Source

* Sat Mar 11 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.4-alt1
- 0.4

* Tue Aug 17 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt1
- new version
- docs packaged

* Wed Dec 24 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt1
- initial build
