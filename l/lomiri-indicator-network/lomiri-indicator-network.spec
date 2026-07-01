%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# TODO do something with C++17 requirement for gtest
%def_without check

%define _libexecdir %_prefix/libexec

Name: lomiri-indicator-network
Version: 1.99.0
Release: alt1

Summary: Systems settings menu service - Network indicator
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-indicator-network

Source: %name-%version.tar

# sync with version 1.1.1-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ayatana-cmake-modules
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(ofono)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(lomiri-url-dispatcher)
BuildRequires: pkgconfig(systemd)
BuildRequires: qt5-declarative-devel
BuildRequires: pkgconfig(qofono-qt5)
BuildRequires: doxygen

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /usr/bin/dbus-test-runner
BuildRequires: /usr/bin/xvfb-run
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: pkgconfig(libgmenuharness)
%endif

Requires: suru-icon-theme
Requires: NetworkManager-openvpn
Requires: NetworkManager-pptp

%description
The Lomiri-indicator-network service is responsible for exporting the system
settings menu through D-Bus.

This indicator is basically an Ayatana system indicator, but it has been
specifically been designed for the Lomiri Operating Environment. If you
try using it with another desktop environment, note that you are on
unexplored territory.

%package -n lib%{name}
Summary: Lomiri Connectivity Qt API
Group: System/Libraries

%description -n lib%{name}
Lomiri Connectivity API - Qt bindings.

This package contains the share library.

%package -n %{name}-devel
Summary: Lomiri Connectivity Qt API - development files
Group: Development/Other
Requires: lib%{name} = %{version}-%{release}

%description -n %{name}-devel
Lomiri Connectivity API - Qt bindings.

This package contains development files to develop against the Qt
library.

%package -n %{name}-doc
Summary: Lomiri Connectivity API - documentation
Group: Documentation
BuildArch: noarch

%description -n %{name}-doc
Lomiri Connectivity API.

This package contains developer documentation.

%prep
%setup
%patch -p1

%build
%cmake \
       -W no-dev \
       -Dqmlplugindump_exe=%_qt5_bindir/qmlplugindump \
%if_with check
       -DENABLE_TESTS=ON \
%else
       -DENABLE_TESTS=OFF \
%endif
       -DENABLE_COVERAGE=OFF \
       -DENABLE_UBUNTU_COMPAT=ON
%cmake_build

%install
%cmake_install

%find_lang %{name}

%post
%systemd_user_post lomiri-indicator-network-secret-agent.service
%systemd_user_post lomiri-indicator-network.service

%preun
%systemd_user_preun lomiri-indicator-network-secret-agent.service
%systemd_user_preun lomiri-indicator-network.service

%postun
%systemd_user_postun lomiri-indicator-network-secret-agent.service
%systemd_user_postun lomiri-indicator-network.service

%check
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING.LGPL MERGE-REVIEW NEWS README.md
%_xdgconfigdir/autostart/lomiri-indicator-network.desktop
%_userunitdir/lomiri-indicator-network-secret-agent.service
%_userunitdir/lomiri-indicator-network.service
%dir %_libexecdir/lomiri-indicator-network/
%_libexecdir/lomiri-indicator-network/lomiri-indicator-network-secret-agent
%_libexecdir/lomiri-indicator-network/lomiri-indicator-network-service
%_datadir/glib-2.0/schemas/com.lomiri.indicator.network.gschema.xml
%_datadir/unity/indicators/com.lomiri.indicator.network
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-indicator-network.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-indicator-network.mo
%dir %_qt5_qmldir/Lomiri/Connectivity
%_qt5_qmldir/Lomiri/Connectivity/libconnectivity-qml.so
%_qt5_qmldir/Lomiri/Connectivity/qmldir
%dir %_qt5_qmldir/Ubuntu/Connectivity
%_qt5_qmldir/Ubuntu/Connectivity/libconnectivity-qml-ubuntu-compat.so
%_qt5_qmldir/Ubuntu/Connectivity/qmldir
%_datadir/dbus-1/services/com.lomiri.connectivity1.service

%files -n lib%{name}
%_libdir/liblomiri-connectivity-qt1.so.1*

%files -n %{name}-devel
%_libdir/liblomiri-connectivity-qt1.so
%_pkgconfigdir/lomiri-connectivity-qt1.pc
%dir %_includedir/connectivity-api
%_includedir/connectivity-api/*

%files -n %{name}-doc
%dir %_datadir/doc/lomiri-indicator-network
%_datadir/doc/lomiri-indicator-network/*

%changelog
* Wed Jul 01 2026 Nikolay Strelkov <snk@altlinux.org> 1.99.0-alt1
- New version 1.99.0.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- New version 1.2.0.

* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.2-alt1
- New version 1.1.2.

* Mon Jul 14 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
