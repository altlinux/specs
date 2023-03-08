%define oname caffeine
Name: %oname-ng
Version: 4.0.2
Release: alt2
Summary: Prevent screensaving and powersaving
Group: Graphical desktop/Other
License: GPLv3 and LGPLv3
Url: https://codeberg.org/WhyNotHugo/caffeine-ng

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3(setuptools) python3(setuptools_scm) python3(wheel)
BuildRequires: git-core

Obsoletes: %oname =< %EVR
Provides: %oname

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

%description -l ru_RU.UTF-8
Caffeine - маленькая служба, которая блокирует активацию скринсейвера и переход
компьютера в ждущий режим, когда активное окно находится в полноэкранном режиме
(например: просматриваете YouTube), или при нажатии на значок в системном лотке.

Это форк Caffeine 2.4, так как в более поздних версиях прекращена поддержка
значка в системном лотке в пользу только автоматического обнаружения
полноэкранных приложений.

Цель этого форка самостоятельное развитие, а не только устранение проблем,
реализация недостающих функций, когда это уместно.

%prep
%setup
%autopatch -p1

%build
git config --global user.email "user at altlinux.org"
git config --global user.name "user"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

%pyproject_build

%install
%pyproject_install

mv %buildroot%python3_sitelibdir%prefix/* %buildroot%prefix/
mv %buildroot%python3_sitelibdir%_sysconfdir %buildroot/

%find_lang %oname

# remove unused icons
rm -r %buildroot%_iconsdir/ubuntu-mono-dark

%files -f %oname.lang
%doc *.rst
%_sysconfdir/xdg/autostart/%oname.desktop
%_bindir/*
%_man1dir/*.1.*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_pixmapsdir/*
%python3_sitelibdir/*
#_datadir/%oname
%_datadir/glib-2.0/schemas/*

%changelog
* Thu Mar 09 2023 Anton Midyukov <antohami@altlinux.org> 4.0.2-alt2
- switch to use AyatanaAppindicator

* Mon Feb 13 2023 Anton Midyukov <antohami@altlinux.org> 4.0.2-alt1
- new version 4.0.2
- Update Url

* Thu Jun 23 2022 Anton Midyukov <antohami@altlinux.org> 3.5.1-alt1
- new version 3.5.1
- cleeanup spec

* Tue Mar 19 2019 Anton Midyukov <antohami@altlinux.org> 3.4.2-alt2
- fix freezing on exit (Closes: 36003)
- Update Url

* Sun Feb 03 2019 Anton Midyukov <antohami@altlinux.org> 3.4.2-alt1
- new version 3.4.2

* Fri Jul 28 2017 Anton Midyukov <antohami@altlinux.org> 3.4.0-alt3
- Added missing requires.

* Sun Mar 12 2017 Anton Midyukov <antohami@altlinux.org> 3.4.0-alt2
- Added buildrequires rpm-build-gir.

* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 3.4.0-alt1
- new version 3.4.0

* Tue Jan 03 2017 Anton Midyukov <antohami@altlinux.org> 3.3.8-alt1
- Initial build for ALT Linux Sisyphus.
