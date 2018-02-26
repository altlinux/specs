Name: settitle
Summary: Set Screen or Xterm window title
Version: 0.0.5
Release: alt2
License: GPL
Group: System/Base

Packager: Denis Smirnov <mithraen@altlinux.ru>

Url: http://sisyphus.ru/ru/srpm/Sisyphus/settitle

Source: %name-%version.tar

%description
%summary

%prep
%setup
%build
%make all
%install
%makeinstall
%files
%_bindir/is_screen
%_bindir/settitle
%changelog
* Tue Oct 06 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.5-alt2
- add Url tag

* Thu Nov 20 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.5-alt1
- fix is_screen in screen-bce term
- cleanup spec

* Sun Nov 16 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1
- fix crash if TERM not set

* Fri Nov 14 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.3-alt1
- fix TERM=screen-bce support

* Fri Feb 29 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.2-alt1
- package binary files :)

* Sun Feb 24 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus

