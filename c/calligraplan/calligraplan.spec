%define oname calligra-plan

%define sover 4
%define libcalligraplankernel libcalligraplankernel%sover
%define libcalligraplanmodels libcalligraplanmodels%sover
%define libcalligraplanui libcalligraplanui%sover
%define libcalligraplankundo2 libcalligraplankundo2%sover
%define libcalligraplanmain libcalligraplanmain%sover
%define libcalligraplanodf libcalligraplanodf%sover
%define libcalligraplanplugin libcalligraplanplugin%sover
%define libcalligraplanprivate libcalligraplanprivate%sover
%define libcalligraplanstore libcalligraplanstore%sover
%define libcalligraplanwidgets libcalligraplanwidgets%sover
%define libcalligraplanwidgetutils libcalligraplanwidgetutils%sover
%define libcalligraplanportfolioprivate libcalligraplanportfolioprivate%sover
%define libcalligraplantjscheduler libcalligraplantjscheduler%sover
%define libcalligraplanworkprivate libcalligraplanworkprivate%sover

Name: calligraplan
Version: 4.0.1
Release: alt1
Epoch: 0
%K6init

Group: Office
Summary: A project planner
License: GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later
Url: https://www.calligra.org/plan/

Requires: %oname-common >= %EVR

Source: http://download.kde.org/stable/calligra/%version/calligraplan-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-svg-devel
BuildRequires: libqca-qt6-devel
BuildRequires: zlib-devel libvulkan-devel libcups-devel
BuildRequires: kf6-karchive-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kcmutils-devel
BuildRequires: kf6-kio-devel kf6-knotifications-devel kf6-kparts-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-kholidays-devel
BuildRequires: kf6-kitemmodels-devel kf6-kcalendarcore-devel kf6-kdoctools-devel
BuildRequires: plasma6-activities-devel
BuildRequires: kde6-kdiagram-devel

%description
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package -n %oname
Group: Office
Summary: A project planner
Requires: %oname-common >= %EVR
%description -n %oname
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package -n %oname-common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description -n %oname-common
%name common package

%package -n %oname-devel
Group: Development/KDE and QT
Summary: Header files and libraries needed for %name development
Conflicts: libflake-devel
%description -n %oname-devel
Header files and libraries needed for %name development

%package -n %libcalligraplankernel
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplankernel
%name library

%package -n %libcalligraplanmodels
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanmodels
%name library

%package -n %libcalligraplanui
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanui
%name library

%package -n %libcalligraplankundo2
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplankundo2
%name library

%package -n %libcalligraplanmain
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanmain
%name library

%package -n %libcalligraplanodf
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanodf
%name library

%package -n %libcalligraplanplugin
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanplugin
%name library

%package -n %libcalligraplanprivate
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanprivate
%name library

%package -n %libcalligraplanstore
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanstore
%name library

%package -n %libcalligraplanwidgets
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanwidgets
%name library

%package -n %libcalligraplanwidgetutils
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanwidgetutils
%name library

%package -n %libcalligraplanportfolioprivate
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanportfolioprivate
%name library

%package -n %libcalligraplantjscheduler
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplantjscheduler
%name library

%package -n %libcalligraplanworkprivate
Summary: %name library
Group: System/Libraries
Requires: %oname-common >= %EVR
%description -n %libcalligraplanworkprivate
%name library

%prep
%setup

%build
%K6build \
    -DPACKAGERS_BUILD=OFF \
    -DBUILD_TESTING=OFF \
    -DTEMPLATES_INSTALL_DIR:PATH=%_K6tmpl \
    #

%install
%K6install

## unpackaged files
rm -frv %buildroot/%_datadir/locale/x-test/

%find_lang --with-kde --all-name %name

%files -n %oname-common -f %name.lang
%_K6icon/*/*/*/*
%_K6xdgmime/*plan*.xml

%files -n %oname-devel
%_K6link/lib*.so

%files -n %oname
%dir %_K6plug/calligraplan/
%dir %_K6plug/calligraplan/parts/
%dir %_K6plug/calligraplan/formatfilters/
%dir %_K6plug/calligraplan/schedulers/
%config(noreplace) %_K6xdgconf/calligraplan*rc
%_K6bin/calligraplan*
%_K6plug/calligraplan/
%_datadir/calligraplan/
%_datadir/calligraplanwork/
%_K6data/kxmlgui?/calligraplan*/
%_K6cfg/calligraplansettings.kcfg
%_K6cfg/calligraplanworksettings.kcfg
%_K6xdgapp/org.kde.calligraplan*.desktop
%_datadir/metainfo/*calligraplan*.xml

%files -n %libcalligraplankernel
%_K6lib/libcalligraplankernel.so.%sover
%_K6lib/libcalligraplankernel.so.*
%files -n %libcalligraplanmodels
%_K6lib/libcalligraplanmodels.so.%sover
%_K6lib/libcalligraplanmodels.so.*
%files -n %libcalligraplanui
%_K6lib/libcalligraplanui.so.%sover
%_K6lib/libcalligraplanui.so.*
%files -n %libcalligraplankundo2
%_K6lib/libcalligraplankundo2.so.%sover
%_K6lib/libcalligraplankundo2.so.*
%files -n %libcalligraplanmain
%_K6lib/libcalligraplanmain.so.%sover
%_K6lib/libcalligraplanmain.so.*
%files -n %libcalligraplanodf
%_K6lib/libcalligraplanodf.so.%sover
%_K6lib/libcalligraplanodf.so.*
%files -n %libcalligraplanplugin
%_K6lib/libcalligraplanplugin.so.%sover
%_K6lib/libcalligraplanplugin.so.*
%files -n %libcalligraplanprivate
%_K6lib/libcalligraplanprivate.so.%sover
%_K6lib/libcalligraplanprivate.so.*
%files -n %libcalligraplanstore
%_K6lib/libcalligraplanstore.so.%sover
%_K6lib/libcalligraplanstore.so.*
%files -n %libcalligraplanwidgets
%_K6lib/libcalligraplanwidgets.so.%sover
%_K6lib/libcalligraplanwidgets.so.*
%files -n %libcalligraplanwidgetutils
%_K6lib/libcalligraplanwidgetutils.so.%sover
%_K6lib/libcalligraplanwidgetutils.so.*
%files -n %libcalligraplanportfolioprivate
%_K6lib/libcalligraplanportfolioprivate.so.%sover
%_K6lib/libcalligraplanportfolioprivate.so.*
%files -n %libcalligraplantjscheduler
%_K6lib/libcalligraplantjscheduler.so.%sover
%_K6lib/libcalligraplantjscheduler.so.*
%files -n %libcalligraplanworkprivate
%_K6lib/libcalligraplanworkprivate.so.%sover
%_K6lib/libcalligraplanworkprivate.so.*

%changelog
* Mon Jan 12 2026 Sergey V Turchin <zerg@altlinux.org> 0:4.0.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 0:3.3.0-alt2
- fix build requries

* Thu Jan 30 2025 Sergey V Turchin <zerg@altlinux.org> 0:3.3.0-alt1
- new version

* Wed Aug 26 2020 Sergey V Turchin <zerg@altlinux.org> 0:3.2.2-alt1
- new version

* Fri Aug 23 2019 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt7
- fix build with new kcalcore

* Thu Aug 15 2019 Oleg Solovyov <mcpain@altlinux.org> 0:3.1.0-alt6
- Fixed build

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt5.qa1
- NMU: remove rpm-build-ubt from BR:

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt4.qa1
- NMU: applied repocop patch

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0:3.1.0-alt4
- Fixed build with new Qt.

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt3
- NMU: added url

* Tue Mar 20 2018 Oleg Solovyov <mcpain@altlinux.org> 0:3.1.0-alt2%ubt
- split libs
- rename packages

* Tue Mar 13 2018 Oleg Solovyov <mcpain@altlinux.org> 0:3.1.0-alt1%ubt
- initial build for ALT
