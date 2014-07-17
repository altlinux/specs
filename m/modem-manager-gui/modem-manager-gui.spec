Name:          modem-manager-gui
Summary:       Graphical interface for ModemManager
Summary(de):   Grafische Oberfläche für ModemManager
Summary(ru):   Графический интерфейс для ModemManager
Version:       0.0.16
Release:       alt1

Group:	       System/Configuration/Networking	
License:       GPLv3
URL:           http://linuxonly.ru/cms/page.php?7

Packager:      Andrey Cherepanov <cas@altlinux.org>

# The original download link is a PHP script which points to this file:
Source0:       http://download.tuxfamily.org/gsf/source/%{name}-%{version}.tar.gz
# The German translation has been submitted upstream:
# https://www.transifex.com/projects/p/modem-manager-gui/language/de/
Source1:       %{name}-de.po
Source2:       %{name}-de.1
Source3:       %{name}-ru.1
Source4:       %{name}.ui

Patch1:	       %{name}-fix-bad_elf_symbols.patch

BuildRequires: pkgconfig
BuildRequires: libgtk+3-devel
BuildRequires: glib2-devel
BuildRequires: gdbm-devel
BuildRequires: libnotify-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext-tools

Requires: ModemManager
Requires: NetworkManager

%description
This program is a simple graphical interface for Modem Manager
daemon dbus interface.
Current features:
- View device information: Operator name, Mode, IMEI, IMSI,
  Signal level.
- Send and receive SMS messages with long massages
  concatenation and store messages in database.
- Send USSD requests and read answers in GSM7 and UCS2 formats
  converted to system UTF8 charset.
- Scan available mobile networks.

%description -l de
Dieses Programm ist eine einfache grafische Oberfläche für
die DBus-Schnittstelle des ModemManager-Daemons.
Funktionen:
- Geräteinformationen anzeigen: Name des Netzanbieters, Modus,
  IMEI, IMSI, Signalstärke.
- SMS senden und empfangen, Verkettung langer Nachrichten,
  Speichern der Nachrichten in der Datenbank.
- USSD-Befehle in den Formaten GSM7 und UCS2 senden und
  Antworten empfangen, Umwandlung in den UTF-8-Zeichensatz.
- Nach verfügbaren Mobilnetzwerken suchen.

%description -l ru
Данная программа является простым графическим интерфейсом для
демона Modem Manager, использующим интерфейс dbus.
Текущие возможности:
- Просмотр информации об устройстве: имени оператора, режима работы,
  IMEI, IMSI и уровня сигнала.
- Прием и отправка сообщений SMS с объединением длинных сообщений
  и сохранением сообщений в базе данных.
- Отправка запросов USSD и прием ответов в кодировках GSM7 и UCS2
  с последующей конвертацией в системную кодировку UTF8.
- Сканирование доступных мобильных сетей.

%prep
%setup -q
%patch1 -p2
cp %SOURCE1 ./po/de.po
cp %SOURCE4 src/

%build
%configure
%make_build

%install
%makeinstall INSTALLPREFIX=%buildroot

install -pD %SOURCE2 %buildroot/%_mandir/de/man1/%{name}.1
install -pD %SOURCE3 %buildroot/%_mandir/ru/man1/%{name}.1

%find_lang --with-man %name

%files -f %name.lang
%doc LICENSE AUTHORS Changelog
%_bindir/%name
%_pixmapsdir/%name.png
%_datadir/%name/
%_desktopdir/%name.desktop
%_libdir/%name/
%doc %_man1dir/%name.1.*

%changelog
* Thu Jul 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.0.16-alt1
- Build for Sisyphus (thanks Fedora for spec) (ALT #29225)

