Name:		pictomir
Version:	0.16.2
Release:	alt1

Summary:	PictoMir education system
License:	GPL / CC BY
Group:		Education

Packager:	Andrey Cherepanov <cas@altlinux.org>

BuildRequires:	qt4-devel >= 4.6.0
BuildRequires:  gcc-c++
BuildRequires:  libqt4-webkit >= 4.6.0
BuildRequires:  phonon-devel
Requires:	icon-theme-hicolor

Source:		%{name}-%{version}.tar
URL:		https://gitorious.org/pictomir
# VCS: 		https://gitorious.org/pictomir/pictomir.git

%description
This package provides a child's icon programming environment
PictoMir for desktops and laptops.
Pictomir integrated development environment
WebKit-based web browser to use within PictoMir

%description -l ru_RU.UTF-8
Программирование пиктограммами для детей
ПиктоМир для настольных компьютеров и ноутбуков.
Среда разработки игр для ПиктоМира
Браузер на основе WebKit для обзора системы ПиктоМир

%prep
%setup -q
qmake-qt4 %name.pro
cd src
lrelease-qt4 src.pro

%build
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot/usr
mkdir -p %buildroot/%_desktopdir
install -m 644 *.desktop %buildroot/%_desktopdir

%files
%_bindir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*.desktop

%changelog
* Sat Jan 24 2015 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt1
- New version

* Tue Jan 10 2012 Eugene Prokopiev <enp@altlinux.ru> 0.15.0-alt2
- closes #26795

* Mon Jan 09 2012 Eugene Prokopiev <enp@altlinux.ru> 0.15.0-alt1
- new version

* Wed Dec 14 2011 Eugene Prokopiev <enp@altlinux.ru> 0.8.0-alt1
- First build for Sisyphus
