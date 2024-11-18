%define _unpackaged_files_terminate_build 1

Name: kio-admin
Version: 24.11.80
Release: alt1
%K6init

Summary: Manage files as administrator using the admin:// KIO protocol
License: (GPL-2.0-only or GPL-3.0-only) and BSD-3-Clause and CC0-1.0 and FSFAP
Group: Graphical desktop/KDE
URL: https://invent.kde.org/system/kio-admin
VCS: https://invent.kde.org/system/kio-admin.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kio-devel
BuildRequires: qt6-declarative-devel
BuildRequires: libpolkitqt6-qt6-devel
BuildRequires: libvulkan-devel

%description
kio-admin implements a new protocol "admin:///" which gives administrative access
to the entire system. This is achieved by talking, over dbus, with a root-level
helper binary that in turn uses existing KIO infrastructure to run file://
operations in root-scope.

%prep
%setup

%build
%K6cmake -DQT_MAJOR_VERSION=6
%K6build

%install
%K6install
%find_lang %name --all-name

%files -f %name.lang
%doc README.* LICENSES/*
%dir %_K6plug/kf6/kfileitemaction/
%_K6plug/kf6/kfileitemaction/%name.so
%dir %_K6plug/kf6/kio/
%_K6plug/kf6/kio/admin.so
%_K6exec/%name-helper
%_K6dbus/system.d/*kio*.conf
%_K6dbus_sys_srv/*kio*.service
%_datadir/metainfo/*kio*.xml
%_datadir/polkit-1/actions/*kio*.policy

%changelog
* Mon Nov 18 2024 Anton Kurachenko <srebrov@altlinux.org> 24.11.80-alt1
- Initial build for Sisyphus.
