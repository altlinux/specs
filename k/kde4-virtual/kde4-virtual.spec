Name:    kde4-virtual
Version: 4.7
Release: alt1

%define smr KDE4 (virtual package)

Packager: Andrey Cherepanov <cas@altlinux.org>
Summary: %smr
License: GPL
Group: Graphical desktop/KDE
URL: http://www.kde.org/

BuildArch: noarch

Source0: %name.list
Source1: kde-virtual.sh

%define kde4_kde   %{expand: %(%SOURCE1 %SOURCE0 kde)}
%define kde4_small %{expand: %(%SOURCE1 %SOURCE0 small)}
%define kde4_mini  %{expand: %(%SOURCE1 %SOURCE0 mini)}
%define kde4_devel %{expand: %(%SOURCE1 %SOURCE0 devel)}

%define dsk %(echo -e "K Desktop Environment 4.x - virtual package\\nto easy select KDE packages during install.")
%define dsk_ru %(echo -e "K Desktop Environment 4.x - виртуальный пакет.\\nОн облегчает выбор пакетов KDE при установке.")

%description
%dsk

%package -n kde4
Summary: %smr
License: GPL
Group: Graphical desktop/KDE
Requires: %kde4_kde
%description -n kde4
%dsk
This package installs all KDE 4.x applications.

%description -n kde4 -l ru_RU.UTF-8
%dsk_ru
Этот пакет устанавливает полный набор приложений KDE 4.x.

%package -n kde4-small
Summary: %smr
License: GPL
Group: Graphical desktop/KDE
Requires: %kde4_small
%description -n kde4-small
%dsk
This package installs most popular KDE 4.x applications.

%description -n kde4-small -l ru_RU.UTF-8
%dsk_ru
Этот пакет устанавливает наиболее популярные приложения KDE 4.x.

%package -n kde4-mini
Summary: %smr
License: GPL
Group: Graphical desktop/KDE
Requires: %kde4_mini
%description -n kde4-mini
%dsk
This package installs mininal set of KDE 4.x applications.

%description -n kde4-mini -l ru_RU.UTF-8
%dsk_ru
Этот пакет устанавливает минимальный набор приложений KDE 4.x.

%package -n kde4-devel
Summary: %smr
License: GPL
Group: Development/KDE and QT
Requires: %kde4_devel
%description -n kde4-devel
%dsk
This package installs development tools for KDE 4.x.

%description -n kde4-devel -l ru_RU.UTF-8
%dsk_ru
Этот пакет устанавливает средства разработки KDE 4.x.

%files -n kde4
%files -n kde4-small
%files -n kde4-mini
%files -n kde4-devel

%changelog
* Wed Sep 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.7-alt1
- fix requires

* Thu Jul 22 2010 Sergey V Turchin <zerg@altlinux.org> 4.4-alt1
- update requires

* Fri Jun 05 2009 Andrey Cherepanov <cas@altlinux.org> 4.2-alt2
- Remove KDE3 requirements by replacing kmail-aegypten-plugins by pinentry-qt (closes: #20335)

* Wed Apr 22 2009 Andrey Cherepanov <cas@altlinux.org> 4.2-alt1
- Initial import
