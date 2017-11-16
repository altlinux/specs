%define rname kmousetool

Name: kde5-%rname
Version: 17.08.3
Release: alt1%ubt
%K5init

Summary: %rname is a program that clicks the mouse for you
License: GPLv2
Group: Graphical desktop/KDE
Url: https://www.kde.org/applications/utilities/kmousetool 
Source0: %rname-%version.tar
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
#BuildRequires: extra-cmake-modules git-core gtk-update-icon-cache i586-libxcb kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-knotifications-devel kf5-kxmlgui-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel python3-base qt5-phonon-devel
BuildRequires: extra-cmake-modules libXtst-devel libXext-devel libXt-devel
BuildRequires: kf5-kxmlgui-devel kf5-knotifications-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kauth-devel
BuildRequires: qt5-phonon-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kmousetool
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/kmousetool
%_K5xdgapp/org.kde.kmousetool.desktop
%_K5icon/hicolor/*/*/kmousetool*.*
%_K5data/kmousetool/

%changelog
* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Tue Aug 22 2017 Stanislav Levin <slev@altlinux.org> 17.08.0-alt1%ubt
- Initial build

