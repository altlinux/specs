%define rname kimagemapeditor

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Development/Other
Summary: An HTML imagemap editor
Url: http://www.kde.org
License: GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides:  kde5-kimagemapeditor = %EVR
Obsoletes: kde5-kimagemapeditor < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules
BuildRequires: qt6-wayland-devel qt6-webengine-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdoctools-devel kf6-kguiaddons-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kparts-devel kf6-ktextwidgets-devel

%description
An HTML imagemap editor.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kimagemapeditor
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6bin/kimagemapeditor
%_K6plug/kf6/parts/*kimagemapeditor*.so
%_K6xdgapp/org.kde.kimagemapeditor.desktop
%_K6icon/*/*/actions/*.*
%_K6icon/*/*/apps/kimagemapeditor.*
%_K6data/kimagemapeditor/
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*kimagemapeditor*.xml

%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

