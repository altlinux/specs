%define rname kio-fuse
%ifndef _unitdir_user
%define _unitdir_user %prefix/lib/systemd/user
%endif
%define service_name kio-fuse

Name: kde5-%rname
Version: 5.0.1
Release: alt3
%K5init

Group: Graphical desktop/KDE
Summary: Fuse interface for KIO
Url: http://www.kde.org
License: GPL-3.0-or-later

Requires: /usr/bin/fusermount3

Source: %rname-%version.tar
Patch1: alt-tmpfiles-dir.patch

# Automatically added by buildreq on Thu Sep 02 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libctf-nobfd0 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libxcbutil-keysyms pkg-config python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel rpm-build-file rpm-build-python3 sh4 tzdata
#BuildRequires: appstream extra-cmake-modules git-core glibc-devel-static kf5-kio-devel libfuse3-devel python3-dev qt5-svg-devel qt5-wayland-devel qt5-webengine-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules glibc-devel qt5-base-devel
BuildRequires: libfuse3-devel
BuildRequires: kf5-kio-devel

%description
%{summary}.

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

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DDATA_INSTALL_DIR=%_K5data \
    #

%install
%K5install
%K5install_move data kglobalaccel kconf_update locale
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5libexecdir/kio-fuse
%_K5dbus_srv/org.kde.KIOFuse.service
%_unitdir_user/%service_name.service
/lib/tmpfiles.d/kio-fuse-tmpfiles.conf

%changelog
* Wed Nov 08 2023 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt3
- don't force alternate placement

* Fri Sep 03 2021 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt2
- fix requires

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt1
- initial build (closes: 40679)
