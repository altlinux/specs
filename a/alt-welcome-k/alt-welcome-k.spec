%define _unpackaged_files_terminate_build 1

Name: alt-welcome-k
Version: 2.4
Release: alt1

Summary: Greeting to Alt Linux for plasma-welcome
License: GPL-2.0-or-later
Group: Graphical desktop/KDE

Requires: plasma-welcome

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kcmutils-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-tools-devel

%description
%summary.

%prep
%setup

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%__mkdir -p %buildroot%_datadir/plasma/plasma-welcome/extra-pages
%__install -Dpm 755 %buildroot%_K6qml/org/kde/plasma/private/welcomedistro/WelcomeToAlt.qml %buildroot%_datadir/plasma/plasma-welcome/extra-pages

%__rm -f %buildroot%_K6qml/org/kde/plasma/private/welcomedistro/{*.qml,kde-qmlmodule.version}

%files -f %name.lang
%_K6qml/org/kde/plasma/private/*/
%_datadir/plasma/plasma-welcome/extra-pages/*.qml

%changelog
* Tue Dec 24 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 2.4-alt1
- Apply the default theme from kdeglobals

* Wed Dec 11 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 2.3-alt1
- Apply the changes after selecting the click type

* Thu Nov 28 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 2.2-alt1
- Use a single click by default

* Thu Nov 28 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 2.1-alt1
- Check if the themeId is empty

* Wed Nov 27 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 2.0-alt1
- Port to KF6
- Add clang-format
- Port qml to Qt6 and add a click type selection
- Port the cmake file to Qt6
- Add a selection of the type of mouse click
- Port to Qt6

* Tue Mar 05 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0-alt2
- Change the path to other QML components

* Fri Mar 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0-alt1
- Initial build for ALT Linux
