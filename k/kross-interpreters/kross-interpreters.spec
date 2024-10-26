%define rname kross-interpreters

Name: %rname
Version: 24.08.2
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Kross interpreters
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-declarative-devel qt5-script-devel
BuildRequires: python-devel rpm-build-python
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdesignerplugin-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kross-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
%summary.

%package -n kross-python
Group: Development/KDE and QT
Summary: Kross plugin for python
#Requires: %name-common >= %EVR
Provides:  kde5-kross-python = %EVR
Obsoletes: kde5-kross-python < %EVR
%description -n kross-python
Python plugin for the Kross archtecture in KDE.

%prep
%setup -n %rname-%version
%{!?_enable_kross-falcon:rm -rf falcon}
%{!?_enable_kross-ruby:rm -rf ruby}
%{!?_enable_kross-java:rm -rf java}

%build
%K5build

%install
%K5install


%files -n kross-python
%_K5plug/krosspython.so

%changelog
* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build
