Name: grcm
Version: 0.1.6
Release: alt2.qa1

Summary: Gnome Remote Connection Manager
Summary (ru_RU.UTF-8): Диспетчер соединений с удалёнными серверами для Gnome
License: GPL
Group: Networking/Remote access
Url: http://grcm.sourceforge.net
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %name-%version.tar.bz2
Source1: ru.po
Patch0: %name-0.1.5-ru.patch
Patch1: %name-0.1.5-moretypes.patch
BuildRequires: ORBit2-devel glib2-devel gnome-vfs2-devel hostinfo libGConf2-devel libart_lgpl-devel libatk-devel libbonobo2-devel libbonoboui-devel libgnome-devel libgnome-keyring libgnomecanvas-devel libgnomeui-devel libgtk+2-devel libpango-devel libpopt-devel libxml2-devel pkgconfig scrollkeeper

%description
Gnome Remote Connection Manager is a gnome application that stores information
about remote connections. It gives you a GUI program to launch applications
like telnet, shh, or rdesktop. It is highly configurable as to what type of
applications it launches, so you are not limited to the three listed.

%description -l ru_RU.UTF-8
Диспетчер соединений хранит сведения о соединениях с удалёнными серверами и 
предоставляет графический интерфейс для запуска telnet, ssh или rdesktop. 
Программа отличается гибкостью настройки и позволяет запускать различные типы 
клиентов для удалённых серверов, не ограничиваясь тремя перечисленными.    

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cat %SOURCE1 > po/ru.po

%build
%configure
%make_build

%install
%makeinstall

rm -rf %buildroot%_datadir/pixmaps/%name/Makefile*

mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps
mv %buildroot%_datadir/pixmaps/%name/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/
install -D -m 644 %buildroot%_datadir/pixmaps/%name/icon.png %buildroot%_liconsdir/%name.png

# menu; TODO: merge with upstream .desktop file
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=grcm - Remote Connections
Comment=Gnome Remote Connection Manager
Icon=%name
Exec=%name
Terminal=false
Categories=GTK;GNOME;Network;RemoteAccess;
EOF

%find_lang %name

%files -f %name.lang
%doc AUTHORS README
%_bindir/*
%_datadir/gnome/help/%name
%_datadir/omf/%name
%_datadir/pixmaps/%name/*.png
%_datadir/pixmaps/%name/*.xpm
%_iconsdir/hicolor/*/apps/%name.*
%_desktopdir/%name.desktop

%changelog
* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt2.qa1
- NMU: converted menu to desktop file

* Mon Dec 22 2008 Ilya Mashkin <oddity@altlinux.ru> 0.1.6-alt2
- remove deprecated macros from spec

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Mon Jun 07 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.1.5-alt3
- buildfix

* Mon Jun 07 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.1.5-alt2
- Dependencies fixed

* Wed Apr 30 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.1.5-alt1
- ALTLinux build, translation, more preconfigured stuff
