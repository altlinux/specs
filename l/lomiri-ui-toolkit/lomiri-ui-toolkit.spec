%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# NOTE: tests are running long, some fail
%def_without check

%define lomiri_intver 5.5.0

Name: lomiri-ui-toolkit
Version: 1.3.5906
Release: alt1

Summary: Qt Components for Lomiri
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-ui-toolkit

Source: %name-%version.tar

# sync with version 1.3.5110+dfsg-2 from Debian unstable + fix qmlscene issues
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-declarative-devel
BuildRequires: pkgconfig(Qt5Feedback)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickTest)
BuildRequires: qt5-qtsystems-devel
BuildRequires: qt5-qtsystems-private-devel
BuildRequires: pkgconfig(Qt5Organizer)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(lttng-ust)
BuildRequires: qt5-base-devel-static

%filter_from_requires /python3(autopilot.*)/d
%filter_from_requires /python3(distutils)/d

Requires: qt5-declarative-devel

# qt5/qml/Qt/labs/folderlistmodel/qmldir, qt5/qml/QtQml/Models.2/qmldir, qt5/qml/QtQuick/Layouts/qmldir
Requires: libqt5-qml
# qt5/qml/QtFeedback/qmldir
Requires: qt5-feedback
# qt5/qml/QtGraphicalEffects/private/qmldir, qt5/qml/QtGraphicalEffects/qmldir
Requires: qt5-graphicaleffects
# qt5/qml/QtQuick/Window.2/qmldir, qt5/qml/QtQuick.2/qmldir
Requires: libqt5-quick
# qt5/qml/QtQuick/XmlListModel/qmldir
Requires: libqt5-xmlpatterns

%if_with check
BuildRequires: /proc
BuildRequires: /usr/bin/xauth
BuildRequires: /usr/bin/xvfb-run
BuildRequires: accountsservice
BuildRequires: dbus
BuildRequires: dbus-test-runner
BuildRequires: qt5-graphicaleffects
BuildRequires: qt5-feedback
BuildRequires: suru-icon-theme
BuildRequires: fonts-ttf-google-noto-sans
%endif

%description
This project consists of a set of QML components to ease the creation of
beautiful applications in QML for Lomiri.
QML alone lacks built-in components for basic widgets like Button, Slider,
Scrollbar, etc, meaning a developer has to build them from scratch. This
toolkit aims to stop this duplication of work, supplying beautiful components
ready-made and with a clear and consistent API.
These components are fully themeable so the look and feel can be easily
customized. Resolution independence technology is built in so UIs are scaled
to best suit the display.

%package devel
Summary: Lomiri-ui-toolkit development files
Group: Development/KDE and QT
Requires: %name = %version-%release

%description devel
This package contains development files needed for lomiri-ui-toolkit.

%package -n python3-module-lomiriuitoolkit
Summary: Python3 files for Lomiri-ui-toolkit
Requires: %name = %version-%release
Group: Development/Python
BuildArch: noarch

%description -n python3-module-lomiriuitoolkit
Python3 files for Lomiri-ui-toolkit.

%package doc
Summary: Documentation for Lomiri-ui-toolkit
Group: Documentation
BuildArch: noarch

%description doc
Documentation for Lomiri-ui-toolkit.

%package examples
Summary: Examples for Lomiri-ui-toolkit
Group: Development/KDE and QT
Requires: %name = %version-%release

%description examples
Examples for Lomiri-ui-toolkit.

%prep
%setup
%patch -p1
sed -i '/DEFINES += _FORTIFY_SOURCE=2/d' features/lomiri_common.prf

%build
lrelease-qt5 lomiri-sdk.pro
%qmake_qt5 lomiri-sdk.pro \
           CONFIG+=ubuntu-uitk-compat \
           CONFIG+=nostrip \
           CONFIG+=debian_build

pushd tests/autopilot
%pyproject_build
popd

%make_build

sed -i "s/Qt5 = 5/Qt5/g" lib/pkgconfig/*.pc

%install
%makeinstall_std INSTALL_ROOT=%buildroot

mkdir -p %buildroot%_bindir
mv -v %buildroot%_datadir/qt5/bin/lomiri-ui-toolkit-launcher %buildroot%_bindir/
mv -v %buildroot%_datadir/qt5/bin/lomiri-app-launch-tracepoints %buildroot%_bindir/
mv -v %buildroot%_datadir/qt5/bin/lomiri-app-launch-profiler-lttng %buildroot%_bindir/
mv -v %buildroot%_datadir/qt5/bin/lomiri-appstart-profile %buildroot%_bindir/
mv -v %buildroot%_datadir/qt5/bin/lomiri-appstart-test %buildroot%_bindir/

rm -rfv %buildroot%_qt5_qmldir/Extinct

pushd tests/autopilot
%pyproject_install
mv -v lomiriuitoolkit/{tests,_custom_proxy_objects} -t %buildroot%python3_sitelibdir_noarch/lomiriuitoolkit/
popd

%find_lang %name
%find_lang %{name}-gallery

%check
xvfb-run make -j1 check

%files -f %{name}.lang
%doc COPYING AUTHORS ChangeLog COPYING.CC-BY-SA-3.0 README.md
%_libdir/libLomiriGestures.so.*
%_libdir/libLomiriMetrics.so.*
%_libdir/libLomiriToolkit.so.*
%dir %_qt5_plugindir/lomiri
%dir %_qt5_plugindir/lomiri/metrics
%_qt5_plugindir/lomiri/metrics/*.so
%dir %_qt5_qmldir/Lomiri
%_qt5_qmldir/Lomiri/Components/
%_qt5_qmldir/Lomiri/Layouts/
%_qt5_qmldir/Lomiri/Metrics/
%_qt5_qmldir/Lomiri/PerformanceMetrics/
%_qt5_qmldir/Lomiri/Test/
%dir %_qt5_qmldir/Ubuntu
%_qt5_qmldir/Ubuntu/Components/
%_qt5_qmldir/Ubuntu/Layouts/
%_qt5_qmldir/Ubuntu/Metrics/
%_qt5_qmldir/Ubuntu/PerformanceMetrics/
%_qt5_qmldir/Ubuntu/Test/
%exclude %_datadir/qt5/share/locale/it_CARES/LC_MESSAGES/lomiri-ui-toolkit.mo
%exclude %_datadir/qt5/share/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-ui-toolkit.mo

%files devel
%doc CODING
%_bindir/lomiri-*
%_libdir/libLomiriGestures.so
%_libdir/libLomiriMetrics.so
%_libdir/libLomiriToolkit.so
%_libdir/*.prl
%_libdir/pkgconfig/*.pc
%dir %_libdir/lomiri-ui-toolkit
%_libdir/lomiri-ui-toolkit/apicheck
%_qt5_archdatadir/mkspecs/modules/*.pri
%_includedir/qt5/LomiriGestures/
%_includedir/qt5/LomiriMetrics/
%_includedir/qt5/LomiriToolkit/

%files -n python3-module-lomiriuitoolkit
%doc README.md
%dir %python3_sitelibdir_noarch/lomiriuitoolkit
%python3_sitelibdir_noarch/lomiriuitoolkit/*.py
%python3_sitelibdir_noarch/lomiriuitoolkit/_custom_proxy_objects/
%python3_sitelibdir_noarch/lomiriuitoolkit/__pycache__/
%python3_sitelibdir_noarch/lomiriuitoolkit/tests/
%python3_sitelibdir_noarch/lomiriuitoolkit-%{version}.dist-info/

%files doc
%doc COPYING.CC-BY-SA-3.0
%_qt5_docdir/*.qch
%_datadir/doc/lomiri-ui-toolkit/

%files examples -f %{name}-gallery.lang
%dir %_qt5_examplesdir/lomiri-ui-toolkit
%dir %_qt5_examplesdir/lomiri-ui-toolkit/examples
%_qt5_examplesdir/lomiri-ui-toolkit/examples/calculator/
%_qt5_examplesdir/lomiri-ui-toolkit/examples/customtheme/
%_qt5_examplesdir/lomiri-ui-toolkit/examples/jokes/
%_qt5_examplesdir/lomiri-ui-toolkit/examples/locale/
%_qt5_examplesdir/lomiri-ui-toolkit/examples/lomiri-ui-toolkit-gallery/
%_qt5_examplesdir/lomiri-ui-toolkit/examples/unit-converter/
%exclude %_datadir/qt5/share/locale/it_CARES/LC_MESSAGES/lomiri-ui-toolkit-gallery.mo
%exclude %_datadir/qt5/share/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-ui-toolkit-gallery.mo

%changelog
* Sat May 16 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.5906-alt1
- New version 1.3.5906.

* Wed Apr 22 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.5905-alt1
- New version 1.3.5905.

* Tue Mar 31 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.5904-alt1
- New version 1.3.5904.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.5903-alt1
- New version 1.3.5903.

* Fri Dec 26 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.5902-alt1
- New version 1.3.5902.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.5901-alt1
- New version 1.3.5901.

* Thu Dec 04 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.5900-alt1
- New version 1.3.5900.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.5110-alt1
- Initial build for Sisyphus
