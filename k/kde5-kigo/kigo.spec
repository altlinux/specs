%define rname kigo

Name: kde5-%rname
Version: 22.12.3
Release: alt1
%K5init no_appdata

Summary: %rname is an open-source implementation of the popular Go game
License: GPLv2
Group: Games/Boards
Url: https://www.kde.org/applications/games/kigo
Source0: %rname-%version.tar
Requires: gnugo
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules
BuildRequires: qt5-declarative-devel qt5-svg-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kcrash-devel kf5-kdoctools-devel
BuildRequires: kf5-knewstuff-devel kf5-kio-devel kf5-ktextwidgets-devel
BuildRequires: kde5-libkdegames-devel

%description
%rname is an open-source implementation of the popular Go game. Go is a
strategic board game for two players. It is also known as igo (Japanese), weiqi
or wei ch'i (Chinese) or baduk (Korean). Go is noted for being rich in strategic
complexity despite its simple rules. The game is played by two players who
alternately place black and white stones (playing pieces, now usually made of
glass or plastic) on the vacant intersections of a grid of 19x19 lines (9x9 or
13x13 for easier games).

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data %rname knsrcfiles
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/%rname
%_K5xdgapp/org.kde.%{rname}.desktop
%_K5icon/hicolor/*/*/%{rname}*.*
%_K5data/%{rname}/
%_K5cfg/%{rname}.kcfg
%_K5data/knsrcfiles/*%{rname}*.knsrc
%_datadir/qlogging-categories5/*.*categories

%changelog
* Tue Mar 07 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt1
- new version

* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Fri Jan 20 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Wed Sep 21 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Tue Jul 12 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Mon May 23 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Sat Mar 05 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Tue Jan 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Tue Aug 31 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Fri Jul 09 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Thu May 27 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Fri Mar 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Tue Dec 22 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Thu Oct 15 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Wed Aug 19 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Fri Mar 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Fri Aug 30 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Fri Mar 22 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Fri Jul 27 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Mon May 28 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Fri Nov 17 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Mon Aug 28 2017 Stanislav Levin <slev@altlinux.org> 17.08.0-alt1%ubt
- Initial build

