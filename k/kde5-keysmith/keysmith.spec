%define rname keysmith

Name: kde5-%rname
Version: 23.08.5
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Two-factor authenticator
Url: http://www.kde.org
License: GPL-3.0-or-later

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Apr 03 2024 (-bi)
# optimized out: bash5 cmake cmake-modules debugedit elfutils fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libctf-nobfd0 libdouble-conversion3 libfreetype-devel libglvnd-devel libgpg-error libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-svg libqt5-widgets libqt5-x11extras libsasl2-3 libssl-devel libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbcommon-devel pkg-config python3 python3-base python3-dev python3-module-setuptools qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 sh5 tzdata xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream extra-cmake-modules kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-kwindowsystem-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libsodium-devel libxcb-render-util-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel libxkbcommon-x11-devel libxkbfile-devel python3-module-mpl_toolkits qt5-imageformats qt5-quickcontrols2-devel qt5-svg-devel qt5-virtualkeyboard-devel qt5-wayland-devel qt5-webengine-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: libsodium-devel
BuildRequires: qt5-quickcontrols2-devel qt5-svg-devel
BuildRequires: kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-kwindowsystem-devel

%description
Keysmith is an application to generate two-factor authentication (2FA)
tokens when logging in to your (online) accounts.

%prep
%setup -n %rname-%version

%build
%K5build \
    -DKF_IGNORE_PLATFORM_CHECK=ON \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/keysmith
%_K5xdgapp/org.kde.keysmith.desktop
%_K5icon/*/*/*/keysmith.*
%_datadir/metainfo/*.xml

%changelog
* Wed Apr 03 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- initial build
