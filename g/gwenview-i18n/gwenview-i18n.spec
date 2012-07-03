Name: gwenview-i18n
Version: 1.4.2
Release: alt3
Summary: Language support for gwenview.
License: GPL
Group: Graphical desktop/KDE
URL: http://gwenview.sourceforge.net

Packager: Valery Inozemtsev <shrek@altlinux.ru>

BuildArch: noarch

Source0: %name-%version.tar.bz2

PreReq: gwenview = %version

# Automatically added by buildreq on Mon Sep 18 2006
BuildRequires: gcc-c++ kdelibs-devel libXext-devel libXt-devel libjpeg-devel qt3-designer xml-utils

%description
Language support for gwenview.

%prep
%setup -q

%build
%K3configure
%make_build

%install
%K3install

%K3find_lang --with-kde --output=%name.lang gwenview

%files -f %name.lang
%lang(pt_BR) %_K3doc/pt_BR/gwenview

%changelog
* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt3
- Prepare package for noarch

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt2
- Adapt to new KDE3 placement

* Wed Sep 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Mon Nov 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Mon Sep 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0
