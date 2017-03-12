%define oname caffeine
Name: %oname-ng
Version: 3.4.0
Release: alt2
Summary: Prevent screensaving and powersaving
Group: Graphical desktop/Other
License: GPLv3 and LGPLv3
Url: https://gitlab.com/hobarrera/caffeine-ng
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-devel python3-module-setuptools python3-module-setuptools_scm git
BuildArch: noarch
Obsoletes: %oname
Provides: %oname
Requires: icon-theme-hicolor
#Requires: python3-module-docopt >= 0.6.2
#Requires: python3-module-ewmh >= 0.1.4
#Requires: python3-module-pyxdg >= 0.25
#Requires: python3-module-setproctitle >= 1.1.10
#Requires: python3-module-wheel >= 0.29.0
%add_python3_req_skip gi.repository.Notify

%description
Caffeine is a little daemon that sits in you systray, and prevents the
screensaver from showing up, or the systems from going to sleep. It does so when
an application is fullscreened (eg: youtube), or when you click on the systray
icon (which you can do, when, eg: reading).

This is a fork of Caffeine 2.4, since later versions dropped support for the
systray icon in favour of only automatic detection of fullscreen apps only,
which resulted rather controversial.

The intention of this fork is to also evolve on its own, not only fixing issues,
but also implemented missing features, when relevant.

Caffeine-ng was shortly know as Taurine, a play on its successor's name, since
taurine is a known stimulant, commonly found in energy drinks. However, this
name did not last, since the artwork would not match adequately, and changing it
was undesirable.

%description -l ru_RU.UTF-8
Caffeine - маленькая служба, которая блокирует активацию скринсейвера и переход
компьютера в ждущий режим, когда активное окно находится в полноэкранном режиме
(например: просматриваете YouTube), или при нажатии на значок в системном лотке.

Это форк Caffeine 2.4, так как в более поздних версиях прекращена поддержка
значка в системном лотке в пользу только автоматического обнаружения
полноэкранных приложений.

Цель этого форка самостоятельное развитие, а не только устранение проблем,
реализация недостающих функций, когда это уместно.

Caffeine-ng ранее был известен как Taurine, является его преемником, так как
Taurine является известным стимулятором, обычно встречаются в энергетических
напитков.

%prep
%setup

%build
git config --global user.email "antohami at altlinux.org"
git config --global user.name "Anton Midyukov"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

%python3_build

%install
%python3_install
%find_lang %oname

%files -f %oname.lang
%doc *.rst
%_sysconfdir/xdg/autostart/%oname.desktop
%_bindir/*
%_man1dir/*.1.*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%exclude %_iconsdir/ubuntu-mono-dark
%_pixmapsdir/*
%python3_sitelibdir/*
%_datadir/%oname
%_datadir/glib-2.0/schemas/*

%changelog
* Sun Mar 12 2017 Anton Midyukov <antohami@altlinux.org> 3.4.0-alt2
- Added buildrequires rpm-build-gir.

* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 3.4.0-alt1
- new version 3.4.0

* Tue Jan 03 2017 Anton Midyukov <antohami@altlinux.org> 3.3.8-alt1
- Initial build for ALT Linux Sisyphus.
