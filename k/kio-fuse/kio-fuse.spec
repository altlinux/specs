%define rname kio-fuse
%ifndef _user_unitdir
%define _user_unitdir %prefix/lib/systemd/user
%endif
%define service_name kio-fuse

Name: %rname
Version: 5.1.0
Release: alt10
%K6init

Group: Graphical desktop/KDE
Summary: Fuse interface for KIO
Url: http://www.kde.org
License: GPL-3.0-or-later

Requires: /usr/bin/fusermount3
Provides:  kde5-kio-fuse = %EVR
Obsoletes: kde5-kio-fuse < %EVR

Source: %rname-%version.tar
Patch1: alt-tmpfiles-dir.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules glibc-devel qt6-declarative-devel
BuildRequires: libfuse3-devel
BuildRequires: kf6-kio-devel

%description
%{summary}.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
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
%K6build \
    -DQT_MAJOR_VERSION=6 \
    -DDATA_INSTALL_DIR=%_K6data \
    #

%install
%K6install
%K6install_move data kglobalaccel kconf_update locale
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6libexecdir/kio-fuse
%_K6dbus_srv/org.kde.KIOFuse.service
%_user_unitdir/%service_name.service
/lib/tmpfiles.d/kio-fuse-tmpfiles.conf

%changelog
* Thu Nov 14 2024 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt10
- build with KF6 (closes: 52037)

* Wed Mar 13 2024 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- new version

* Wed Nov 08 2023 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt3
- don't force alternate placement

* Fri Sep 03 2021 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt2
- fix requires

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt1
- initial build (closes: 40679)
