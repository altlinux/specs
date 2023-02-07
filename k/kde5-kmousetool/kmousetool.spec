%define rname kmousetool

Name: kde5-%rname
Version: 22.12.2
Release: alt1
%K5init no_appdata

Summary: %rname is a program that clicks the mouse for you
License: GPLv2
Group: Graphical desktop/KDE
Url: https://www.kde.org/applications/utilities/kmousetool 
Source0: %rname-%version.tar
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
#BuildRequires: extra-cmake-modules git-core gtk-update-icon-cache i586-libxcb kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-knotifications-devel kf5-kxmlgui-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel python3-base qt5-phonon-devel
BuildRequires: extra-cmake-modules libXtst-devel libXext-devel libXt-devel
BuildRequires: kf5-kxmlgui-devel kf5-knotifications-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kauth-devel kf5-kwindowsystem-devel
BuildRequires: qt5-phonon-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kmousetool
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/kmousetool
%_K5xdgapp/org.kde.kmousetool.desktop
%_K5icon/hicolor/*/*/kmousetool*.*
%_K5data/kmousetool/

%changelog
* Tue Feb 07 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Tue Jan 17 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Tue Sep 20 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Thu May 19 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Tue Jan 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Thu Aug 26 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Fri Jun 11 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Thu May 20 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Fri Mar 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Fri Jan 15 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Mon Dec 21 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Tue Sep 22 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Mon Feb 25 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Tue Aug 22 2017 Stanislav Levin <slev@altlinux.org> 17.08.0-alt1%ubt
- Initial build

