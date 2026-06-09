%define rname step

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Education
Summary: Interactive physical simulator
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-step = %EVR
Obsoletes: kde5-step < %EVR

Source: %rname-%version.tar
Source10: po-add-ru.po

Patch0: fix-example-saving-error.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-tools-devel
BuildRequires: eigen3 libcln-devel libgsl-devel
BuildRequires: libdiscount-devel
BuildRequires: libqalculate-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel kf6-knotifications-devel kf6-kparts-devel kf6-kplotting-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel

%description
Step is an interactive physical simulator. It works like this:
you place some bodies on the scene, add some forces such as gravity
or springs, then click "Simulate" and Step shows you how your scene
will evolve according to the laws of physics. You can change every
property of bodies/forces in your experiment (even during simulation)
and see how this will change evolution of the experiment. With Step
you can not only learn but feel how physics works!

%prep
%setup -n %rname-%version
%patch0 -p2

sed -i 's|^find_package.*Eigen3.*REQUIRED.*|find_package(Eigen3 REQUIRED)|' CMakeLists.txt


mv po/ru/step.po{,.old}
msgcat --use-first %SOURCE10 po/ru/step.po.old > po/ru/step.po
rm -f po/ru/step.po.old

%build
%K6build -DQT_MAJOR_VERSION=6

%install
%K6install
%K6install_move data step knsrcfiles

%K6find_qtlang %name --all-name
%find_lang %name --with-kde --all-name --append

%files -f %name.lang
%doc LICENSES*
%_datadir/locale/*/LC_SCRIPTS/step/
%_K6bin/step
%_K6data/step/
%_K6data/knsrcfiles/*step*.knsrc
%_K6xdgapp/org.kde.step.desktop
%_K6cfg/step.kcfg
%_K6icon/*/*/apps/step.*
%_K6icon/*/*/actions/step_*.*
%_K6icon/*/*/actions/pointer.*
%_K6xdgmime/*step*.xml
%_datadir/metainfo/*.xml


%changelog
* Tue Jun 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Tue Mar 10 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Oct 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed May 28 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Feb 24 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

