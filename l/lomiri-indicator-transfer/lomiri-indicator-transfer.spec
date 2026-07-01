%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_without check

%define _libexecdir %_prefix/libexec

Name: lomiri-indicator-transfer
Version: 1.2.1
Release: alt1

Summary: Lomiri Indicator showing transfers
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-indicator-transfer

Source: %name-%version.tar

# sync with version 1.2.0-2 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(properties-cpp)
BuildRequires: pkgconfig(click-0.4)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(dbustest-1)
BuildRequires: pkgconfig(gtest)
BuildRequires: ayatana-cmake-modules

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: dbus-test-runner
%endif

%description
Indicator that shows file/data transfers in the indicator bar of the
Lomiri operating shell.

This package provides the indicator service itself.

%package download-manager
Summary: Download manager plugin for Lomiri's Transfer Indicator
Group: Graphical desktop/Other
Requires: lomiri-indicator-transfer = %{version}-%{release}
Requires: liblomiri-indicator-transfer = %{version}-%{release}

%description download-manager
Indicator that shows file/data transfers in the indicator bar of the
Lomiri operating shell.

This package contains the associated download manager.

%package -n lib%{name}
Summary: Shared library used by Lomiri's Transfer Indicator and plugins
Group: System/Libraries

%description -n lib%{name}
Indicator that shows file/data transfers in the indicator bar of the
Lomiri operating shell.

This package contains a shared library used by Lomiri Indicator
Transfer.

%package -n lib%{name}-devel
Summary: Development files for lomiri-indicator-transfer
Group: Development/C++
Requires: liblomiri-indicator-transfer = %{version}-%{release}

%description -n lib%{name}-devel
Indicator that shows file/data transfers in the indicator bar of the
Lomiri operating shell.

This package contains development headers for the shared library of
Lomiri Indicator Transfer.

%prep
%setup
%patch -p1

%build
%cmake \
%if_with check
       -Denable_tests=On
%else
       -Denable_tests=On
%endif
%cmake_build

%install
%cmake_install

%find_lang %name

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun %name.service

%check
%ctest -j1 -VV -E cppcheck

%files -f %{name}.lang
%doc AUTHORS ChangeLog HACKING MERGE-REVIEW README TODO
%config %_sysconfdir/xdg/autostart/lomiri-indicator-transfer.desktop
%_userunitdir/lomiri-indicator-transfer.service
%dir %_libexecdir/lomiri-indicator-transfer
%_libexecdir/lomiri-indicator-transfer/lomiri-indicator-transfer-service
%_datadir/ayatana/indicators/com.lomiri.indicator.transfer
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-indicator-transfer.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-indicator-transfer.mo

%files download-manager
%_libexecdir/lomiri-indicator-transfer/libdmtransfers.so

%files -n lib%{name}
%_libdir/liblomiri-indicator-transfer.so.1
%_libdir/liblomiri-indicator-transfer.so.1.0.0

%files -n lib%{name}-devel
%dir %_includedir/lomiri-indicator-transfer
%dir %_includedir/lomiri-indicator-transfer/transfer
%_includedir/lomiri-indicator-transfer/transfer/model.h
%_includedir/lomiri-indicator-transfer/transfer/source.h
%_includedir/lomiri-indicator-transfer/transfer/transfer.h
%_libdir/liblomiri-indicator-transfer.so
%_pkgconfigdir/lomiri-indicator-transfer.pc

%changelog
* Wed Jul 01 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt1
- New version 1.2.1.

* Sun Jul 27 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
