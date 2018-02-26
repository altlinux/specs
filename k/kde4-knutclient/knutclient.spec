%define _iskde 1

%define rname knutclient
Name:      kde4-%rname
Version:   1.0.4
Release:   alt1

Group:     Monitoring
Summary:   A GUI client for NUT
Summary(ru_RU.UTF-8): Графический интерфейс для NUT
Url:       http://www.knut.prynych.cz/
#Url:       http://code.google.com/p/knut/
License:   GPLv2

#Requires:  nut

Source: %rname-%version.tar
BuildRequires: gcc-c++ kde4libs-devel libupsclient-devel

%description
Knutclient is a visual KDE client for UPS systems using NUT - Network UPS Tools.

%description -l ru_RU.UTF-8
Knutclient - это графический KDE-клиент системы работы с источниками
бесперебойного питания NUT (Network UPS Tools, Инструментарий сетевых
ИБП)

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname

%files -f %rname.lang
%_K4bindir/%rname
%_K4xdg_apps/%rname.desktop
%_K4apps/%rname
%_K4iconsdir/*/*/apps/%{rname}*.*

%changelog
* Wed Dec 29 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt1
- new version

* Tue Nov 09 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt0.M51.1
- built for M51

* Tue Nov 09 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- initial build

