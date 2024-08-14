%define rname drkonqi
%define _unit_nedodir %{expand: %(dirname %_unitdir)}
%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif
%add_python3_path %_K6data/drkonqi/gdb/python/gdb_preamble/
%add_python3_req_skip gdb gdb.FrameDecorator

Name: %rname
Version: 6.1.2
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Crash Handler
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf6-kirigami
#Requires: systemd-coredump
#Requires: python3(psutil) python3(pygdbmi) python3(sentry_sdk)

Provides: plasam5-drkonqi = 1:%version-%release
Obsoletes: plasam5-drkonqi < 1:%version-%release

Source: %rname-%version.tar
Patch1: alt-enable-debuginfod-support.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-systemd
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: libssl-devel libsystemd-devel
BuildRequires: pkgconfig(polkit-qt6-1)
BuildRequires: kf6-kcrash-devel kf6-ki18n-devel kf6-kidletime-devel kf6-kio-devel kf6-knotifications-devel
BuildRequires: kf6-kwallet-devel kf6-kwindowsystem-devel kf6-syntax-highlighting-devel kf6-kitemmodels-devel
BuildRequires: kf6-kpackage-devel kf6-kdeclarative-devel kf6-kstatusnotifieritem-devel

%description
The KDE Crash Handler.

%package -n plasma5-drkonqi
Group: Graphical desktop/KDE
Summary: Compatibility package
Epoch: 1
Requires: drkonqi >= %version-%release
%description -n plasma5-drkonqi
Compatibility package.

%prep
%setup -n %rname-%version
%autopatch -p1

%build
%K6build \
    -DSYSTEMD_UNIT_INSTALL_DIR=%_unit_nedodir \
    -DSYSTEMD_USER_UNIT_INSTALL_DIR=%_userunitdir \
    -DWITH_GDB12:BOOL=ON \
    -DWITH_PYTHON_VENDORING:BOOL=OFF \
    #

%install
%K6install
%K6install_move data drkonqi
%find_lang %name --all-name

%files -n plasma5-drkonqi

%files -f %name.lang
%doc LICENSES/*
%_K6bin/drkonqi*
%_K6exec/drkonqi*
%_K6libexecdir/drkonqi*
%_K6plug/drkonqi/
%_K6data/drkonqi/
%_K6xdgapp/*drkonqi*.desktop
%_unitdir/*drkonqi*
%_unitdir/*.wants/*drkonqi*
%_userunitdir/*drkonqi*
%_userunitdir/*.wants/*drkonqi*
%_datadir/qlogging-categories6/*.*categories
%_datadir/polkit-1/actions/*drkonqi*.policy
%_K6dbus_sys_srv/*drkonqi*.service
%_K6dbus/system.d/*drkonqi*.conf

%changelog
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

