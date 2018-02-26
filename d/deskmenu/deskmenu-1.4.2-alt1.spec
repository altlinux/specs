Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%define Name DeskMenu
Name: deskmenu
Version: 1.4.2
Release: alt1.1
Summary: Root menu program for Window Manager
Summary(uk_UA.CP1251): Главное меню для віконного менеджера
Summary(ru_RU.CP1251): Главное меню для оконного менеджера
License: GPL
Group: Graphical desktop/Other
URL: http://www.oroborus.org/
Source0: %{name}_%version.tar.bz2
Source1: %name.menu-method.gz

# Automatically added by buildreq on Fri Jun 16 2006
BuildRequires: fontconfig libgtk+2-devel
BuildRequires: libXext-devel libXt-devel xorg-cf-files

%description
%Name is a root menu program for Window Manager which is activated
by clicking the root window.

%description -l uk_UA.CP1251
%Name - головне меню для віконного менеджера, активізується кліком
кнопкою мишки.

%description -l ru_RU.CP1251
%Name - главное меню для оконного менеджера, активизирующееся кликом
кнопкой мышки.


%prep
%setup -q -n %name-%version
subst 's/\r//g' README


%build
%configure
%make_build


%install
%make_install install DESTDIR=%buildroot
install -d -m 0755 %buildroot%_sysconfdir/menu-methods
gzip -dc -- %SOURCE1 > %buildroot%_sysconfdir/menu-methods/%name
chmod 755 %buildroot%_sysconfdir/menu-methods/%name
gzip --best --stdout > changelog.gz


%files
%doc AUTHORS README example_rc changelog.* debian/README.Debian
%_bindir/%name
%_man1dir/*
%_sysconfdir/menu-methods/*


%changelog
* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for deskmenu

* Fri Jun 16 2006 Led <led@altlinux.ru> 1.4.2-alt1
- initial build
