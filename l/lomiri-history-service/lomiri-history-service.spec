%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_without check

%define _libexecdir %_prefix/libexec

Name: lomiri-history-service
Version: 0.7
Release: alt1

Summary: History service to store messages and calls
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-history-service

Source: %name-%version.tar

# sync with version 0.6-2 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5Contacts)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: libphonenumber-devel
BuildRequires: pkgconfig(TelepathyQt5)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(systemd)
BuildRequires: ayatana-cmake-modules
BuildRequires: /usr/bin/lcov
BuildRequires: /usr/bin/gcovr
BuildRequires: libtelepathy-mission-control

%if_with check
BuildRequires: ctest
BuildRequires: dbus-test-runner
BuildRequires: dconf
BuildRequires: /usr/bin/xvfb-run
BuildRequires: /usr/bin/gnome-keyring-daemon
%endif

%description
A service to record the messages that are sent and received and the calls
that are made in the Ubuntu Touch platform.

This package contains the history service daemon that watches for
Telepathy events and stores.

This package contains some tools to be used with the history service.

%package -n lib%{name}
Group: System/Libraries
Summary: History service to store messages and calls - client library

%description -n lib%{name}
A service to record the messages that are sent and received and the calls
that are made in the Ubuntu Touch platform.

This package contains the client library to access the data stored by the
history service.

%package -n lib%{name}-devel
Group: Development/KDE and QT
Summary: History service to store messages and calls - development files
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
A service to record the messages that are sent and received and the calls
that are made in the Ubuntu Touch platform.

This package contains the development files for the history service client
library.

%prep
%setup
%patch -p1

%build
%cmake \
       -DQMAKE_EXECUTABLE=/usr/bin/qmake-qt5 \
       -DENABLE_COVERAGE=OFF \
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%post
%systemd_user_post lomiri-history-daemon.service

%preun
%systemd_user_preun lomiri-history-daemon.service

%postun
%systemd_user_postun lomiri-history-daemon.service

%check
%ctest -j1 -VV

%files
%doc AUTHORS ChangeLog COPYING README.md TODO
%_bindir/lomiri-history-maketextevents
%_bindir/lomiri-history-makevoiceevents
%_userunitdir/lomiri-history-daemon.service
%_libdir/lomiri-history-service/plugins/libsqlitehistoryplugin.so
%_qt5_qmldir/Lomiri/History/liblomirihistory-qml.so
%_qt5_qmldir/Lomiri/History/qmldir
%_libexecdir/lomiri-history-daemon
%_datadir/dbus-1/services/com.lomiri.HistoryService.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.HistoryDaemonObserver.service
%_datadir/telepathy/clients/LomiriHistoryDaemonObserver.client

%files -n lib%{name}
%_libdir/liblomirihistoryservice.so.*

%files -n lib%{name}-devel
%dir %_includedir/lomiri-history-service
%dir %_includedir/lomiri-history-service/History
%_includedir/lomiri-history-service/History/*
%_libdir/liblomirihistoryservice.so
%_pkgconfigdir/lomiri-history-service.pc

%changelog
* Wed Jul 01 2026 Nikolay Strelkov <snk@altlinux.org> 0.7-alt1
- New version 0.7.

* Thu Jul 17 2025 Nikolay Strelkov <snk@altlinux.org> 0.6-alt1
- Initial build for Sisyphus
