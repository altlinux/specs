# Spec file for gapcmon project

%define version 0.8.9
%define release alt2

Name: gapcmon
Version: %version
Release: %release

Summary: a GUI monitor for apcupsd
Summary(ru_RU.UTF-8): графический монитор состояния ИБП для apcupsd

License: %gpl2plus
Group: Monitoring
Url: http://gapcmon.sourceforge.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: http://prdownloads.sourceforge.net/gapcmon/%name-%version.tar.bz2

Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Source4: %name.desktop

Patch0:  %name-0.8.9-alt-gold.patch

AutoReqProv: yes
BuildPreReq: GConf2 gnome-vfs-devel libgtk+2-devel rpm-build-licenses

%description
A Gtk2/GLib2 GUI application used to monitor UPS devices controlled
by the  APCUPSD package.  The program uses  the  NIS interface from
apcupsd to collect event  and status information for display to the
end-user.

%description -l ru_RU.UTF-8
Графическая утилита для  мониторинга состояния  устройств ИБП,
управляемых демоном apcupsd  из одноимённого пакета. Программа
использует интерфейс NIS демона для сбора сообщений о событиях
и состоянии  ИБП и представляет  их в удобном для пользователя
виде.

%prep
%setup
%patch0

mv -- gapcmon.desktop gapcmon.desktop.orig
cp -- %SOURCE4 gapcmon.desktop

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

# Need it there because of using COPYING in makefile
mv -f -- COPYING COPYING.GPL.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

mkdir -p -- %buildroot%_miconsdir %buildroot%_liconsdir %buildroot%_niconsdir
install -m0644 -- %SOURCE1 %buildroot%_miconsdir/%name.png
install -m0644 -- %SOURCE2 %buildroot%_niconsdir/%name.png
install -m0644 -- %SOURCE3 %buildroot%_liconsdir/%name.png

%files
%doc AUTHORS ChangeLog INSTALL README
%doc --no-dereference COPYING

%exclude %_docdir/%name

%_bindir/%name

%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*
%_pixmapsdir/*.png
%_desktopdir/%name.desktop

%changelog
* Sat May 26 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.9-alt2
- Fix build with --no-copy-dt-needed-entries

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.9-alt1
- New version 0.8.9
- Remove obsolete %%update_menus calls

* Sun Jul 20 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.8-alt1
- New version 0.8.8
- Fix repocop issues on desktop file and icons

* Fri Feb 29 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt1
- New version 0.8.6
  - Added support for displaying current wattage load on UPS
    using eith NOMPOWER or loadpct*rated.wattage
  - Added rated.wattage to preference page

* Sat Aug 11 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.5-alt2
- Fix bug with iconify in KDE (#11565)
- Spec file cleanup

* Tue Mar 27 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.5-alt1
- New version 0.8.5
 * Replace the network routine to use GIOChannels vs gnomeVFS
 * Added ability to start up in icon mode

* Wed Jul 19 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.3-alt1
- New version 0.8.3
 * Added graph color properties page to control.panel notebook

* Mon May 29 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.2-alt1
- Initial build for ALT Linux

* Mon May 29 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.2-alt0
- Initial build
- Fix desktop file

