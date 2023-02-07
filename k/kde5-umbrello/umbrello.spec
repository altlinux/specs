%define rname umbrello

#%ifarch %e2k ppc64le
#%def_disable qtwebengine
#%else
#%def_enable qtwebengine
#%endif

Name: kde5-%rname
Version: 22.12.2
Release: alt1
%K5init no_appdata

Group: Graphical desktop/KDE
Summary: UML Modeller
Url: http://www.kde.org
License: GPL-2.0 and LGPL-2.1 and FDL-1.2

AutoProv: yes noshell nopython nopython2 nopython3 noperl noruby noqml notcl nomaven nogir novala

Source: %rname-%version.tar
Patch1: alt-no-webkit.patch

# Automatically added by buildreq on Thu Jan 14 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms libxml2-devel pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-gir ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libxslt-devel python-module-google qt5-svg-devel rpm-build-python3 rpm-build-ruby xsltproc
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-svg-devel qt5-tools
#%if_enabled qtwebengine
#BuildRequires: qt5-webengine-devel
#%else
#BuildRequires: qt5-webkit-devel
#%endif
#BuildRequires: llvm-devel llvm-devel-static clang-devel clang-devel-static
BuildRequires: libxslt-devel xsltproc
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-kcrash-devel kf5-kdelibs4support-devel kf5-syntax-highlighting-devel

%description
Umbrello UML Modeller is a UML diagramming tool for KDE.
UML lets you create models of object orientated software systems in a
standard language.

%prep
%setup -n %rname-%version
#%if_enabled qtwebengine
#%patch1 -p1
#%endif

# disable unittests
sed -i 's|\(.*add_subdirectory.*unittests.*\)|#\1|' CMakeLists.txt
# python shebang
sed -i '/^#!\/usr\/bin\/env/s|python|%__python3|' umbrello/headings/heading.py

%build
%add_optflags -I%_K5inc/KWindowSystem
%K5build \
    -DBUILD_KF5=ON \
    #

%install
%K5install
%K5install_move data umbrello umbrello5
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_bindir/*
%_K5bin/*
%_K5data/umbrello*/
%_K5icon/hicolor/*/apps/umbrello.*
%_K5icon/hicolor/*/mimetypes/application-x-uml.*
%_K5xdgapp/org.kde.umbrello*.desktop


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

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt3
- build with qtwebkit on e2k and ppc64le

* Wed Jan 19 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt2
- build without qtwebkit

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

* Wed Feb 17 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt2
- update build requries

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Fri Jan 22 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt3
- disable unittests

* Fri Jan 22 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt2
- remove buildrequires to llvm, so don't build tests

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

* Mon Nov 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
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

* Mon Dec 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2
- fix compile with new Qt

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Fri Jun 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Thu May 04 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1
- new version

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Mon Dec 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- initial build
