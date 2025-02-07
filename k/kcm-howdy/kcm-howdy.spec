%define _unpackaged_files_terminate_build 1

%define rname kcm-howdy

Name: %rname
Version: 6.0.2
Release: alt1

Summary: KDE Workspace 6 Howdy configuration module
License: GPLv3+
Group: Graphical desktop/KDE
Url: https://gitlab.com/golubevan/kcm-howdy

Provides: kde5-kcm-howdy = %EVR
Obsoletes: kde5-kcm-howdy < %EVR

# howdy doesn't support ppc64le
ExcludeArch: ppc64le

Source: %name-%version.tar

%K6init

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: kf6-kcmutils-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: libopencv-devel
BuildRequires: dlib-devel
BuildRequires: libsystemd-devel

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

%define module_config_file %_xdgconfigdir/%rname/%rname.ini

%description
KDE Workspace 6 Howdy configuration module

%prep
%setup

%build
%K6build \
    -DUSE_AUTO_VECTOR=OFF \
    -DMODULE_CONFIG_FILE="%module_config_file"

%install
%K6install
%K6install_move data kcm_howdy kpackage

%find_lang --with-kde --append --output=%name.lang kcm_howdy

%post
# Get the minimum UID from login.defs
UID_MIN=$(awk '/^UID_MIN/ {print $2}' /etc/login.defs 2>/dev/null)
sed -i "s/^minimum-uid=.*/minimum-uid=$UID_MIN/" %module_config_file

%files -f %name.lang
%config %module_config_file
%_K6xdgapp/kcm_howdy.desktop
%_K6plug/plasma/kcms/systemsettings/kcm_howdy.so
%_K6data/icons/hicolor/scalable/apps/howdy.svg

# auth helper
%_K6exec/kauth/kcm-howdy-auth-helper
%_datadir/dbus-1/system.d/org.kde.kcontrol.kcmhowdy.conf
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmhowdy.policy
%_K6dbus_sys_srv/org.kde.kcontrol.kcmhowdy.service

%changelog
* Thu Feb 06 2025 Anton Golubev <golubevan@altlinux.org> 6.0.2-alt1
- import OpenBLAS via PkgConfig (fix FTBFS)

* Wed Jan 29 2025 Anton Golubev <golubevan@altlinux.org> 6.0.1-alt1
- reset the user interface after an action error

* Fri Jan 24 2025 Anton Golubev <golubevan@altlinux.org> 6.0.0-alt1
- rename package kde5-kcm-howdy -> kcm-howdy
- port to kde6
- correct the maximum height of the models table (ALT #48540)
- correctly display model id in preview (ALT #50758)
- check the ID_INFRARED_CAMERA property (ALT #50757)

* Wed Jun 05 2024 Anton Golubev <golubevan@altlinux.org> 0.1.3-alt1
- better display of labels in dark theme
- get MIN_UID from login.defs when installing and updating

* Tue Apr 16 2024 Anton Golubev <golubevan@altlinux.org> 0.1.2-alt1
- add initial setup wizard
- recommend IR cameras (ALT #48796)
- improve font scaling in preview
- add the ability to test only one model
- edit other users models

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
