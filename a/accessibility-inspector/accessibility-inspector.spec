%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: accessibility-inspector
Version: 26.04.0
Release: alt1

Summary: Inspect your application accessibility tree
License: LGPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/accessibility/accessibility-inspector

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)

BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: libqaccessibilityclient-qt6-devel

%if_with check
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

%prep
%setup
sed -i "s|Categories=.*|Categories=Qt;KDE;Utility;Accessibility;|" org.kde.accessibilityinspector.desktop

%build
%cmake \
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %name --with-kde --all-name --with-man

%check
xvfb-run -a --server-args="-screen 0 1024x768x24+32" %ctest -j1 -VV

%files -f %{name}.lang
%doc README.md
%_K6bin/accessibilityinspector
%_K6lib/libaccessibilityinspector.so.1
%_K6lib/libaccessibilityinspector.so.1.0
%_K6xdgapp/org.kde.accessibilityinspector.desktop
%_K6icon/hicolor/scalable/apps/org.kde.accessibilityinspector.svg
%_K6data/metainfo/org.kde.accessibilityinspector.metainfo.xml
%_K6data/qlogging-categories6/accessibilityinspector.categories

%changelog
* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.0-alt1
- New version 26.04.0.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.3-alt1
- New version 25.12.3.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.2-alt1
- Initial build for Sisyphus
