%define rname kronometer

Name: kde5-%rname
Version: 2.3.0
Release: alt3
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: Stopwatch application by KDE
Url: https://invent.kde.org/utilities/kronometer
Vcs: https://invent.kde.org/utilities/kronometer.git
License: GPLv2+

Source: %rname-%version.tar
Source1: po.tar
Patch: %name-%version-alt-add-translations.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kauth-devel kf5-kdoctools-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-ki18n-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel

%description
Kronometer is a simple stopwatch application.

%prep
%setup -a1 -n %rname-%version
%autopatch -p1

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
* Wed Apr 24 2024 Anton Kurachenko <srebrov@altlinux.org> 2.3.0-alt3
- Added translations.

* Wed Feb 07 2024 Anton Kurachenko <srebrov@altlinux.org> 2.3.0-alt2
- Changed project homepage link.

* Fri Jul 21 2023 Anton Kurachenko <srebrov@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus.
