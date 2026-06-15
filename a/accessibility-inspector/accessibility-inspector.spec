%define _stripped_files_terminate_build 1
%def_disable testing

%define rname accessibility-inspector
%define accessibilityinspector_sover 1
%define libaccessibilityinspector libaccessibilityinspector%accessibilityinspector_sover

Name: %rname
Version: 26.04.2
Release: alt2
%K6init

Group: Graphical desktop/KDE
Summary: Inspect your application accessibility tree
License: LGPL-2.0-or-later
Url: https://invent.kde.org/accessibility/accessibility-inspector

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: pkgconfig(Qt6) pkgconfig(Qt6Qml)
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: libqaccessibilityclient-qt6-devel

%if_with testing
BuildRequires: ctest
BuildRequires: icon-theme-breeze
BuildRequires: xauth
BuildRequires: xvfb-run
%endif

Requires: plasma6-breeze
Requires: icon-theme-breeze

%description
Accessibility Inspector is as the name suggests an inspector for your
application accessibility tree. It lets you check all the items exposed
via At-SPI, too.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Conflicts: accessibility-inspector < 26.04.2-alt2
%description common
%name common package

%package -n %libaccessibilityinspector
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libaccessibilityinspector
%name library

%prep
%setup
sed -i "s|Categories=.*|Categories=Qt;KDE;Utility;Accessibility;|" org.kde.accessibilityinspector.desktop

%build
%K6build \
%if_enabled testing
    -DBUILD_TESTING=ON \
%else
    -DBUILD_TESTING=OFF \
%endif
    #

%install
%K6install

%find_lang %name --with-kde --all-name

%check
%if_enabled testing
xvfb-run -a --server-args="-screen 0 1024x768x24+32" %ctest -j1 -VV
%endif

%files common -f %name.lang

%files
%doc README.md
%_K6bin/accessibilityinspector
%_K6xdgapp/*accessibilityinspector*.desktop
%_K6icon/*/*/apps/*accessibilityinspector*
%_K6data/metainfo/*accessibilityinspector*.xml
%_K6data/qlogging-categories6/*accessibilityinspector*.categories

%files -n %libaccessibilityinspector
%_K6lib/libaccessibilityinspector.so.%accessibilityinspector_sover
%_K6lib/libaccessibilityinspector.so.*

%changelog
* Mon Jun 15 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt2
- fix packaging

* Fri Jun 05 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.2-alt1
- New version 26.04.2.

* Thu May 07 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.1-alt1
- New version 26.04.1.

* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.0-alt1
- New version 26.04.0.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.3-alt1
- New version 25.12.3.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.2-alt1
- Initial build for Sisyphus
