%define rname kalgebra

%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Education
Summary: Graph Calculator
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf6-kirigami
Provides:  kde5-kalgebra = %EVR
Obsoletes: kde5-kalgebra < %EVR

Source: %rname-%version.tar
Source10: po-add-ru.po
Patch0: alt-add-display-imported-commands.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-svg-devel qt6-declarative-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: libGLU-devel libreadline-devel
BuildRequires: libncursesw-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel  kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel 
BuildRequires: kf6-kpackage-devel
BuildRequires: plasma6-lib-devel
BuildRequires: analitza-devel

%description
KAlgebra is an application that can replace your graphing calculator.
It has numerical, logical, symbolic, and analysis features that let you calculate
mathematical expressions on the console and graphically plot the results in 2D or 3D.
KAlgebra is rooted in the Mathematical Markup Language (MathML);
however, one does not need to know MathML to use KAlgebra.

%prep
%setup -n %rname-%version
%patch0 -p1

mv po/ru/kalgebra.po{,.old}
msgcat --use-first %SOURCE10 po/ru/kalgebra.po.old > po/ru/kalgebra.po
rm -f po/ru/kalgebra.po.old

%build
%K6build

%install
%K6install
%K6install_move data plasma kalgebramobile
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/*algebra*
%_K6xdgapp/*algebra*.desktop
%_K6icon/*/*/apps/*algebra.*
%if_enabled qtwebengine
%_K6data/plasma/plasmoids/org.kde.graphsplasmoid/
%_datadir/katepart?/syntax/kalgebra.xml
%endif
%_datadir/metainfo/*.xml


%changelog
* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

