%define rname kcolorchooser

Name: kde5-%rname
Version: 22.12.2
Release: alt1
%K5init altplace no_appdata

Group: Graphics
Summary: Color Chooser
Url: http://www.kde.org
License: MIT

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Oct 21 2022 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kwidgetsaddons-devel libctf-nobfd0 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-devel rpm-build-file rpm-build-python3 sh4 tzdata
#BuildRequires: appstream extra-cmake-modules gtk4-update-icon-cache kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kxmlgui-devel lua5.3 python3-module-setuptools python3-module-zope qt5-imageformats qt5-svg-devel qt5-wayland-devel qt5-webengine-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kxmlgui-devel

%description
Color selector and palette editor.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5charselect
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5charselect
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/kcolorchooser
%_K5xdgapp/*kcolorchooser*.desktop
%_K5icon/*/*/apps/*kcolorchooser*

%changelog
* Tue Feb 07 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Tue Jan 17 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Fri Oct 21 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- initial build
