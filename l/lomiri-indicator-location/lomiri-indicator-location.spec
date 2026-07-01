%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define _libexecdir %_prefix/libexec

Name: lomiri-indicator-location
Version: 26.6.19
Release: alt1

Summary: Indicator controlling access to physical location data
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/indicator-location

Source: %name-%version.tar

# sync with version 25.4.22-2 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(lomiri-url-dispatcher)
BuildRequires: pkgconfig(properties-cpp)
BuildRequires: pkgconfig(systemd)

%if_with check
BuildRequires: ctest
BuildRequires: pkgconfig(gtest)
BuildRequires: dbus
%endif

%description
The Lomiri Location Indicator shows whether the system is using physical
location data and allows the user to control the permissions on its use.

%prep
%setup
%patch -p1

%build
%cmake \
%if_with check
       -Denable_tests=On
%else
       -Denable_tests=Off
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
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING INSTALL MERGE-REVIEW NEWS README
%config %_sysconfdir/xdg/autostart/lomiri-indicator-location.desktop
%_libexecdir/lomiri-indicator-location/lomiri-indicator-location-service
%_datadir/ayatana/indicators/com.lomiri.indicator.location
%_userunitdir/lomiri-indicator-location.service
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-indicator-location.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-indicator-location.mo

%changelog
* Wed Jul 01 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.19-alt1
- New version 26.6.19.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 25.10.2-alt1
- New version 25.10.2.

* Sun Jul 27 2025 Nikolay Strelkov <snk@altlinux.org> 25.4.22-alt1
- Initial build for Sisyphus
