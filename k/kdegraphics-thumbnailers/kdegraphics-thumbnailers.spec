%define rname kdegraphics-thumbnailers

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Graphics Thumbnailers
Url: http://www.kde.org
License: GPL-2.0-or-later and LGPL-2.0-or-later

# for PDF/PS
Requires: /usr/bin/gs

Provides:  kde5-graphics-thumbnailers = %EVR
Obsoletes: kde5-graphics-thumbnailers < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kde6-libkdcraw-devel kde6-libkexiv2-devel
BuildRequires: kf6-karchive-devel kf6-kio-devel

%description
%summary.


%prep
%setup -n %rname-%version

%build
%K6build \
    -DDISABLE_MOBIPOCKET=ON \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6plug/kf?/thumbcreator/*thumb*.so
%_datadir/metainfo/*thumb*.xml

%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

