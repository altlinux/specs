# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: fvwm-themes.spec,v 1.2 2005/12/20 08:39:40 eugene Exp $

%define m_p CFLAGS="-O2"

Name: fvwm-themes
Version: 0.7.0
Release: alt2.qa1

Summary: FVWM Themes, configuration framework for FVWM
Summary(ru_RU.UTF-8): Темы для оконного менеджера FVWM
License: GPL
Group: Graphical desktop/FVWM based
Url: http://%name.sourceforge.org/
BuildArch: noarch

Source0: %name-%version.tar.bz2
Source1: %name.wmsession
Source2: %name-extra-%version.tar.bz2
Patch0: %name-menu.patch

Requires: fvwm-base >= 2.5.31
Requires: fvwm-perl >= 2.5.31
Requires: perl >= 5.004
Requires: m4

# required due to /usr/X11R6 -> /usr relocation
Requires: fvwm-base >= 2.5.14-alt1
BuildPreReq: fvwm-base >= 2.5.14-alt1

BuildPreReq: fvwm-perl

# Automatically added by buildreq on Sat Dec 17 2005
BuildRequires: fvwm-base menu xmessage xorg-rgb libX11-devel

%description
FVWM Themes is a powerful configuration framework for FVWM,
designed to be easily extendible and configurable, includes
several pre-built themes, a pack of images and sounds.

%description -l ru_RU.UTF-8
FVWM Themes является мощным окружением для оконного менеджера FVWM,
спроектированным с учетом легкости расширения и конфигурации.
Пакет включает в себя готовые темы, графические и звуковые файлы.

%package extra
Summary: Extra FVWM Themes
Summary(ru_RU.UTF-8): Дополнительные темы для FVWM
Group: Graphical desktop/FVWM based
Requires: %name = %version-%release

%description extra
FVWM Themes is a powerful configuration framework for FVWM,
designed to be easily extendible and configurable, includes
several pre-built themes, a pack of images and sounds.

This package contains 10 more themes for use with the base FVWM Themes
package.

%description -l ru_RU.UTF-8 extra
FVWM Themes является мощным окружением для оконного менеджера FVWM,
спроектированным с учетом легкости расширения и конфигурации.
Пакет включает в себя готовые темы, графические и звуковые файлы.

Данный пакет содержит дополнительные 10 тем для использования наряду
с базовыми.

%prep
%setup -q
%patch0 -p1
perl -pi -e 's,-cronyx-,-\*-,g' locale/ru/*

%build
./configure \
	--prefix=%_prefix \
	--exec-prefix=%_prefix \
	--mandir=%_mandir \
	--sysconfdir=%_sysconfdir/X11
make %m_p

%install
make \
	prefix=$RPM_BUILD_ROOT%_prefix \
	mandir=$RPM_BUILD_ROOT%_mandir \
	ROOT_PREFIX=$RPM_BUILD_ROOT install
%__install -pD -m644 %SOURCE1 $RPM_BUILD_ROOT%_sysconfdir/X11/wmsession.d/10Fvwm-themes
find %buildroot -type f -print0 | xargs -r0 %__subst -p s,%buildroot,,g
%__tar xjf %SOURCE2 -C %buildroot%_datadir/fvwm/themes
%__mv %buildroot%_datadir/fvwm/themes/%name-extra-%version/* %buildroot%_datadir/fvwm/themes/
%__rm -rf %buildroot%_datadir/fvwm/themes/%name-extra-%version
find %buildroot%_datadir/fvwm/themes -type f -print0 | \
	xargs -r0 %__subst -p s,-adobe-,-*-,g
find %buildroot%_datadir/fvwm/themes -type f -print0 | \
	xargs -r0 %__subst -p s,-*-lucida-,-*-serene-,g
find %buildroot%_datadir/fvwm/themes -type f -print0 | \
	xargs -r0 %__subst -p s,-b\&h-lucida-,-*-serene-,g
find %buildroot%_datadir/fvwm/themes -type f -print0 | \
	xargs -r0 %__subst -p s,-*-lucidabright-,-*-times-,g
find %buildroot%_datadir/fvwm/themes -type f -print0 | \
	xargs -r0 %__subst -p s,-*-lucidatypewriter-,-*-serenetypewriter-,g

%post
[ -x %{prefix}/bin/fvwm-themes-menuapp ] && fvwm-themes-menuapp --site --build-menus --remove-popup || true

%files
%_bindir/*
%_sysconfdir/X11/wmsession.d/*
%_sysconfdir/menu-methods/*
%_mandir/man?/*
%_datadir/fvwm/Fvwm*
%_datadir/fvwm/themes-rc*
%_datadir/fvwm/images/
%_datadir/fvwm/locale/
%_datadir/fvwm/sounds/
%dir %_datadir/fvwm/themes
%_datadir/fvwm/themes/afterstep/
%_datadir/fvwm/themes/cde/
%_datadir/fvwm/themes/current/
%_datadir/fvwm/themes/default/
%_datadir/fvwm/themes/luthien/
%_datadir/fvwm/themes/migo/
%_datadir/fvwm/themes/multichoice/
%_datadir/fvwm/themes/olicha/
%_datadir/fvwm/themes/redmond98/
%_datadir/fvwm/themes/redmondxp/
%doc AUTHORS NEWS README TODO
%doc doc/{FAQ,README.1st,colorsets,creating-themes,fvwm-themes.lsm,menus-extra,functions-appbind-extra}

%files extra
%_datadir/fvwm/themes/awol/
%_datadir/fvwm/themes/brushedmetal/
%_datadir/fvwm/themes/e17/
%_datadir/fvwm/themes/mech/
%_datadir/fvwm/themes/minimal/
%_datadir/fvwm/themes/osx/
%_datadir/fvwm/themes/qnx/
%_datadir/fvwm/themes/spruce/
%_datadir/fvwm/themes/unsafe/
%_datadir/fvwm/themes/blackbox/
%_datadir/fvwm/themes/celticbow/
%_datadir/fvwm/themes/ice/
%_datadir/fvwm/themes/metal/
%_datadir/fvwm/themes/nanogui/
%_datadir/fvwm/themes/plainbow/
%_datadir/fvwm/themes/sa/
%_datadir/fvwm/themes/underground/

%changelog
* Wed Apr 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2.qa1
- NMU: Removed obsolete %%update_menus/%%clean_menus calls

* Sun Dec 18 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.7.0-alt2
- Changes from Sergey Vlasov <vsu@> (#8673):
  * Moved all files from /usr/X11R6 to /usr for fvwm-2.5.14-alt1
  * Updated BuildRequires
- %_datadir/fvwm/themes now belongs to package

* Wed Jul 21 2004 Eugene Vlasov <eugvv@altlinux.ru> 0.7.0-alt1
- New version
- Added WM session entry
- Added fvwm-themes-extra

* Tue Jan 08 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.5.0-alt1
- Initial revision.
