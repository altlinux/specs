Name: pictomir
Version: 0.16.2
Release: alt3

Summary: PictoMir education system
License: GPL / CC BY
Group: Education

Url: https://gitorious.org/pictomir
# VCS: https://gitorious.org/pictomir/pictomir.git
Source: %name-%version.tar
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: qt4-devel >= 4.6.0
BuildRequires: gcc-c++
BuildRequires: libqt4-webkit-devel >= 1:2.3.4-alt3
BuildRequires: phonon-devel
Requires: icon-theme-hicolor

%description
This package provides a child's icon programming environment.
PictoMir for desktops and laptops.
Pictomir integrated development environment.
WebKit-based web browser to use within PictoMir.

%description -l ru_RU.UTF-8
Программирование пиктограммами для детей.
ПиктоМир для настольных компьютеров и ноутбуков.
Среда разработки игр для ПиктоМира.
Браузер на основе WebKit для обзора системы ПиктоМир.

%prep
%setup
qmake-qt4 %name.pro
cd src
lrelease-qt4 src.pro

%build
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot%_usr
mkdir -p %buildroot/%_desktopdir
install -pm644 *.desktop %buildroot/%_desktopdir

%files
%_bindir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*.desktop

%changelog
* Fri Feb 01 2019 Michael Shigorin <mike@altlinux.org> 0.16.2-alt3
- Fixed BR: (-devel part of libqt4-webkit is actually needed)
- Minor spec cleanup

* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.2-alt2
- Updated build dependencies

* Sat Jan 24 2015 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt1
- New version

* Tue Jan 10 2012 Eugene Prokopiev <enp@altlinux.ru> 0.15.0-alt2
- closes #26795

* Mon Jan 09 2012 Eugene Prokopiev <enp@altlinux.ru> 0.15.0-alt1
- new version

* Wed Dec 14 2011 Eugene Prokopiev <enp@altlinux.ru> 0.8.0-alt1
- First build for Sisyphus
