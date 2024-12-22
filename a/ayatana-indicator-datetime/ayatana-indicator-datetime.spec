%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: ayatana-indicator-datetime
Version: 24.5.0
Release: alt1

Summary: Ayatana Indicator providing clock and calendar
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-datetime

Source: %name-%version.tar

ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: accountsservice
BuildRequires: ayatana-cmake-modules
BuildRequires: ayatana-indicator-common
BuildRequires: cmake
BuildRequires: evolution-data-server-devel
BuildRequires: gcc-c++
BuildRequires: gstreamer1.0-devel
BuildRequires: intltool
BuildRequires: libaccounts-glib-devel
BuildRequires: libayatana-common-devel
BuildRequires: libblkid-devel
BuildRequires: libbrotli-devel
BuildRequires: libgcrypt-devel
BuildRequires: libjpeg-devel
BuildRequires: libmessaging-menu-devel
BuildRequires: libmount-devel
BuildRequires: libnghttp2-devel
BuildRequires: libnotify-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libpsl-devel
BuildRequires: libselinux-devel
BuildRequires: libsqlite3-devel
BuildRequires: libtiff-devel
BuildRequires: libuuid-devel
BuildRequires: properties-cpp-devel
BuildRequires: systemd-devel

%description
This Ayatana Indicator provides a combined calendar, clock, alarm
and event management tool.

%prep
%setup

%build
%cmake \
  -Denable_tests=Off \
  -Denable_lomiri_features=OFF
%cmake_build

%install
%cmake_install

find %buildroot -type f -name "*.la" -delete -print

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
%doc COPYING AUTHORS INSTALL.md NEWS NEWS.Canonical README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%_datadir/glib-2.0/schemas/org.ayatana.indicator.datetime.gschema.xml
%_datadir/ayatana/indicators/org.ayatana.indicator.datetime
%_userunitdir/%name.service

%changelog
* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 24.5.0-alt1
- New version 24.5.0.

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
