%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: ayatana-indicator-power
Version: 24.5.3
Release: alt1

Summary: Ayatana Indicator showing power state
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-power

Source: %name-%version.tar

ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: ayatana-cmake-modules
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: libayatana-common-devel
BuildRequires: libnotify-devel
BuildRequires: ayatana-indicator-common
BuildRequires: libblkid-devel
BuildRequires: libjpeg-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libpng-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: libtiff-devel
BuildRequires: zlib-devel

%description
This Ayatana Indicator displays current power management
information and gives the user a way to access power management
preferences.

The Ayatana Indicator provides a generic, multi-desktop-env aware
approach of accessing power information and management features.

%prep
%setup

%build
%cmake \
  -Denable_tests=Off \
  -DENABLE_RDA=Off
%cmake_build

%install
%cmake_install

# these translations are ignored by %%find_lang
rm -fv %buildroot%_datadir/locale/it_CARES/LC_MESSAGES/%name.mo
rm -fv %buildroot%_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/%name.mo

%find_lang %name

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun %name.service

%files -f %name.lang
%doc COPYING AUTHORS NEWS README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%_datadir/glib-2.0/schemas/org.ayatana.indicator.power.gschema.xml
%_datadir/ayatana/indicators/org.ayatana.indicator.power
%_userunitdir/%name.service

%changelog
* Fri Jun 12 2026 Nikolay Strelkov <snk@altlinux.org> 24.5.3-alt1
- New version 24.5.3.

* Sat Mar 22 2025 Nikolay Strelkov <snk@altlinux.org> 24.5.2-alt1
- New version 24.5.2.

* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 24.5.1-alt1
- New version 24.5.1.

* Sun Jan 28 2024 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt3
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + break BuildRequires(pre) to multiple lines
  + do not own systemd dirs (thanks to @antohami)
  + do not own /usr/share/ayatana/indicators
  + temporary disable build on ppc64le

* Wed Aug 09 2023 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt2
- Removed translations which are ignored by %%find_lang
- Language specific files are declared
- Move service to /usr/libexec for compatibility with MATE Tweak and Debian

* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus
