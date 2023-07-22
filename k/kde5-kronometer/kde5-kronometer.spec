%define rname kronometer

Name: kde5-%rname
Version: 2.3.0
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: Stopwatch application by KDE
Url: http://www.kde.org
License: GPLv2+

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kauth-devel kf5-kdoctools-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-ki18n-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel

%description
Kronometer is a simple stopwatch application.

%prep
%setup -n %rname-%version

%build
%K5build 

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K5bin/%rname
%_K5xdgapp/*.desktop
%_K5icon/*/*/*/%rname.*
%_datadir/kf5/config.kcfg/%rname.*

%changelog
* Fri Jul 21 2023 Anton Kurachenko <srebrov@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus.
