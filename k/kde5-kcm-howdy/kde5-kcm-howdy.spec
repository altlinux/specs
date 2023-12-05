%define _unpackaged_files_terminate_build 1

Name: kde5-kcm-howdy
Version: 0.1.1
Release: alt1

Summary: KDE Workspace 5 Howdy configuration module
License: GPLv3+
Group: Graphical desktop/KDE
Url: https://gitlab.com/golubevan/kcm-howdy

# howdy doesn't support ppc64le
ExcludeArch: ppc64le

Source: %name-%version.tar

%K5init

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: libopencv-devel
BuildRequires: dlib-devel

# needed for dlib
BuildRequires: libgif-devel
BuildRequires: libsqlite3-devel
BuildRequires: libavdevice-devel
BuildRequires: libavfilter-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: liblapack-devel
BuildRequires: libopenblas-devel

Requires: howdy

%description
KDE Workspace 5 Howdy configuration module

%prep
%setup

%build
%K5build -DUSE_AUTO_VECTOR=OFF

%install
%K5install
%K5install_move data kcm_howdy kpackage

%find_lang --with-kde --append --output=%name.lang kcm_howdy

%files -f %name.lang
%_K5xdgapp/kcm_howdy.desktop
%_K5plug/plasma/kcms/systemsettings/kcm_howdy.so
%_K5data/kpackage/kcms/kcm_howdy/
%_K5data/icons/hicolor/scalable/apps/howdy.svg

# auth helper
%_K5libexecdir/kauth/kcm-howdy-auth-helper
%_datadir/dbus-1/system.d/org.kde.kcontrol.kcmhowdy.conf
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmhowdy.policy
%_K5dbus_sys_srv/org.kde.kcontrol.kcmhowdy.service

%changelog
* Tue Dec 05 2023 Anton Golubev <golubevan@altlinux.org> 0.1.1-alt1
- make more proper ScrollViews (ALT #48540)
- use utf-8 for model name (ALT #48538)
- make sure helper is disabled after the error (ALT #48537)
- don't show "Default" button on models tab (ALT #48536)
- fix typo in 'dark_threshold' (ALT #48535)

* Tue Nov 14 2023 Anton Golubev <golubevan@altlinux.org> 0.1.0-alt1
- show preview before face scan
- remove the 'altplace' option
- requires howdy

* Wed Nov 08 2023 Anton Golubev <golubevan@altlinux.org> 0.0.3-alt1
- enable the 'altplace' option
- disable AVX
- refactor

* Wed Oct 25 2023 Anton Golubev <golubevan@altlinux.org> 0.0.2-alt1
- add video preview

* Wed Aug 09 2023 Anton Golubev <golubevan@altlinux.org> 0.0.1-alt1
- Initial build.
