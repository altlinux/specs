%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

%def_with check

Name: ayatana-indicator-session
Version: 26.6.1
Release: alt1

Summary: Ayatana Indicator showing session management, status and user switching
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-session

Source: %name-%version.tar

# sync with version 24.5.1-2 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: ayatana-cmake-modules
BuildRequires: ayatana-indicator-common
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: hicolor-icon-theme
BuildRequires: intltool
BuildRequires: libayatana-common-devel
BuildRequires: libblkid-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: zlib-devel

%if_with check
BuildRequires: libgtest-devel
BuildRequires: ctest
BuildRequires: dbus
%endif

%description
This indicator is designed to be placed on the right side of a
panel and give the user easy control for changing their instant
message status. Switching to another user. Starting a guest
session. Or controlling the status of their own session.

It requires some way to be hosted into a panel. For the MATE Panel
the appropriate package is mate-indicator-applet.

%prep
%setup
%patch -p1

%build
%cmake \
%if_with check
       -DENABLE_TESTS=ON \
%else
       -DENABLE_TESTS=OFF \
%endif
       -DENABLE_COVERAGE=OFF \
       -DENABLE_RDA=OFF
%cmake_build

%install
%cmake_install

# these translations are ignored by %%find_lang
rm -fv %buildroot%_datadir/locale/it_CARES/LC_MESSAGES/%name.mo
rm -fv %buildroot%_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/%name.mo

%find_lang %name

%check
%ctest -j1 -VV

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun %name.service

%files -f %name.lang
%doc COPYING NEWS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%_iconsdir/*/*/*/*
%_datadir/glib-2.0/schemas/org.ayatana.indicator.session.gschema.xml
%_datadir/ayatana/indicators/org.ayatana.indicator.session
%_userunitdir/%name.service

%changelog
* Mon Jun 15 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.1-alt1
- New version 26.6.1.

* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.0-alt1
- New version 26.6.0.
- Enabled tests.

* Tue Jul 22 2025 Nikolay Strelkov <snk@altlinux.org> 24.5.1-alt2
- Adapted for Lomiri.

* Sat Apr 12 2025 Nikolay Strelkov <snk@altlinux.org> 24.5.1-alt1
- New version 24.5.1.

* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 24.5.0-alt1
- New version 24.5.0.

* Sun Jan 28 2024 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt3
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + break BuildRequires(pre) to multiple lines
  + do not own icons and systemd dirs (thanks to @antohami)
  + do not own /usr/share/ayatana/indicators

* Wed Aug 09 2023 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt2
- Removed translations which are ignored by %%find_lang
- Language specific files are declared
- Move service to /usr/libexec for compatibility with MATE Tweak and Debian

* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus
