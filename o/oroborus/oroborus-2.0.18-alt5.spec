%define Name Oroborus
Name: oroborus
Version: 2.0.18
Release: alt5.qa1
Summary: Small window manager for the X Window System
Summary(uk_UA.CP1251): Маленький віконний менеджер для X Window System
Summary(ru_RU.CP1251): Маленький оконный менеджер для X Window System
License: GPL
Group: Graphical desktop/Other
URL: http://www.%name.org/
Source0: %name-%version.tar.bz2
Source1: %name-icons.tar.bz2
Source2: start%name
Source3: %{name}rc
Source4: %name.startup
Patch: %name-2.0.18-man.patch

# Automatically added by buildreq on Mon Sep 24 2007
BuildRequires: imake libSM-devel libXext-devel libXpm-devel xorg-cf-files

%description
The main aim of %Name is to be small and light with very few fancy
features, so there are no docks, no taskbars, no root menus and no
icons. These can be added quite easily by either using %Name with
GNOME or using some other applications that provide the required
functionality.

%description -l uk_UA.CP1251
Головна мета %Name - бути маленьким і легким з дуже небагатьма
"модними" властивостями; таким чином немає ніяких доків, панелей задач,
головних меню та значків. Вони можуть бути вельми легко додані шляхом
використання %Name з GNOME або за допомогою інших додатків, які
забезпечують необхідну функціональність.

%description -l ru_RU.CP1251
Главная цель %Name - быть маленьким и лёгким с очень немногими
"модными" свойствами; таким образом нет никаких доков, панелей задач,
главных меню и значков. Они могут быть весьма легко добавлены путём
использования %Name с GNOME или с помощью других приложений,
обеспечивающих необходимую функциональность.


%package themes
Summary: Themes for %Name Window Manager
Summary(uk_UA.CP1251): Теми для віконного менеджера %Name
Summary(ru_RU.CP1251): Темы для оконного менеджера %Name
Group: Graphical desktop/Other
Requires: %name

%description themes
Themes for %Name Window Manager.

%description -l uk_UA.CP1251 themes
Теми для віконного менеджера %Name.

%description -l ru_RU.CP1251 themes
Темы для оконного менеджера %Name.


%prep
%setup -a 1
%patch -p1


%build
%configure
%make_build


%install
%make_install install DESTDIR=%buildroot
install -pD -m 644 %name-64.xpm %buildroot%_iconsdir/hicolor/64x64/apps/%Name.xpm
install -pD -m 644 %name-48.xpm %buildroot%_liconsdir/%name.xpm
install -pD -m 644 %name-32.xpm %buildroot%_niconsdir/%name.xpm
install -pD -m 644 %name-16.xpm %buildroot%_miconsdir/%name.xpm
install -pD -m 0755 %SOURCE2 %buildroot%_bindir/start%name
chmod 755 %buildroot%_bindir/start%name
install -d -m 0755 %buildroot%_x11sysconfdir/%name
install -m 0644 %SOURCE4 %buildroot%_x11sysconfdir/%name/startup
install -m 0755 %SOURCE3 %buildroot%_x11sysconfdir/%name/%{name}rc

# wmsession
install -d -m 0755 %buildroot%_x11sysconfdir/wmsession.d
cat > %buildroot%_x11sysconfdir/wmsession.d/10%name <<__MENU__
NAME=%name
ICON=%_iconsdir/hicolor/64x64/apps/%Name.xpm
EXEC=%_bindir/start%name
DESC=Small yet fully featured window manager.
SCRIPT:
exec %_bindir/start%name
__MENU__


%files
%doc AUTHORS ChangeLog README TODO example.%{name}rc
%_bindir/*
%_man1dir/*
%_man5dir/*
%dir %_datadir/%name
%dir %_datadir/%name/schemes
%dir %_datadir/%name/themes
%_datadir/%name/defaults
%_datadir/%name/schemes/*
%_datadir/%name/themes/%name
%_iconsdir/hicolor/64x64/apps/*.xpm
%_liconsdir/*.xpm
%_niconsdir/*.xpm
%_miconsdir/*.xpm
%_x11sysconfdir/wmsession.d/*
%dir %_x11sysconfdir/%name
%config(noreplace) %_x11sysconfdir/%name/*


%files themes
%_datadir/%name/themes/QNX
%_datadir/%name/themes/agua
%_datadir/%name/themes/beos
%_datadir/%name/themes/cruxish
%_datadir/%name/themes/e017
%_datadir/%name/themes/gorillaworm
%_datadir/%name/themes/next
%_datadir/%name/themes/pillage
%_datadir/%name/themes/platinum
%_datadir/%name/themes/slimline
%_datadir/%name/themes/windows
%_datadir/%name/themes/defold
%_datadir/%name/themes/bluecurve
%_datadir/%name/themes/mkultra
%_datadir/%name/themes/Elberg_Red
%_datadir/%name/themes/Elberg_Green
%_datadir/%name/themes/Elberg_Blue


%changelog
* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.18-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * update_wms for oroborus
  * pixmap-in-deprecated-location for oroborus
  * postclean-05-filetriggers for spec file

* Mon Sep 24 2007 Led <led@altlinux.ru> 2.0.18-alt5
- updated %_x11sysconfdir/%name/startup
- cleaned up spec

* Sat Jun 09 2007 Led <led@altlinux.ru> 2.0.18-alt4
- fixed and cleaned up spec

* Sat Aug 19 2006 Led <led@altlinux.ru> 2.0.18-alt3
- fixed %%files sections

* Fri Jun 16 2006 Led <led@altlinux.ru> 2.0.18-alt2
- changed in %name startup file

* Fri Jun 16 2005 Led <led@altlinux.ru> 2.0.18-alt1
- initial build
- added %name-2.0.18-man.patch
