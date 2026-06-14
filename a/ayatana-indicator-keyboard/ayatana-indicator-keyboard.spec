%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

%def_with check

Name: ayatana-indicator-keyboard
Version: 26.6.2
Release: alt1

Summary: Ayatana Indicator for managing keyboard layout and desktop language
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-keyboard

Source: %name-%version.tar

# sync with version 24.7.2-2 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: ayatana-cmake-modules
BuildRequires: ayatana-indicator-common
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: hicolor-icon-theme
BuildRequires: intltool
BuildRequires: libaccountsservice-devel
BuildRequires: libayatana-common-devel
BuildRequires: libblkid-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libpolkit-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: libXau-devel
BuildRequires: libXdmcp-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxklavier-devel
BuildRequires: libxml2-devel
BuildRequires: mate-themes
BuildRequires: pkg-config
BuildRequires: zlib-devel
BuildRequires: libudev-devel

%if_with check
BuildRequires: ctest
%endif

Requires: matekbd-keyboard-display

%description
This package contains the keyboard indicator, which should show
as an icon in the top panel of indicator aware desktop
environments.

It can be used to switch key layouts or languages, and helps the
user identifying which layouts are currently in use.

%package -n %name-devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description -n %name-devel
%{summary}.

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
       -DENABLE_COVERAGE=OFF
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
%doc COPYING AUTHORS NEWS README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%_datadir/accountsservice/interfaces/org.ayatana.indicator.keyboard.AccountsService.xml
%_datadir/polkit-1/actions/org.ayatana.indicator.keyboard.AccountsService.policy
%_datadir/glib-2.0/schemas/org.ayatana.indicator.keyboard.gschema.xml
%_libdir/libayatana-keyboard-x11.so.*
%_libdir/libayatana-keyboard-lomiri.so.*
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%_iconsdir/hicolor/scalable/status/*
%_iconsdir/ContrastHigh/scalable/status/*
%_datadir/ayatana/indicators/org.ayatana.indicator.keyboard
%_datadir/polkit-1/rules.d/50-org.ayatana.indicator.keyboard.AccountsService.rules
%_userunitdir/%name.service

%files devel
%_libdir/libayatana-keyboard-x11.so
%_libdir/libayatana-keyboard-lomiri.so
%_datadir/dbus-1/interfaces/org.ayatana.indicator.keyboard.AccountsService.xml

%changelog
* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.2-alt1
- New version 26.6.2.

* Fri Jun 12 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.1-alt1
- New version 26.6.1.
- Created -devel package with the corresponding files.

* Tue Jul 22 2025 Nikolay Strelkov <snk@altlinux.org> 24.7.2-alt2
- Packaged library for Lomiri.

* Sat Mar 22 2025 Nikolay Strelkov <snk@altlinux.org> 24.7.2-alt1
- New version 24.7.2.

* Sun Jan 19 2025 Nikolay Strelkov <snk@altlinux.org> 24.7.0-alt2
- Added matekbd-keyboard-display to Requires for the full functionality

* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 24.7.0-alt1
- New version 24.7.0.

* Sun Jan 28 2024 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt3
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + break BuildRequires(pre) to multiple lines
  + do not own dbus, icons, polkit and systemd dirs (thanks to @antohami)
  + do not own /usr/share/ayatana/indicators and /usr/share/accountsservice/interfaces

* Wed Aug 09 2023 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt2
- Removed translations which are ignored by %%find_lang
- Language specific files are declared
- Move service to /usr/libexec for compatibility with MATE Tweak and Debian

* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus
