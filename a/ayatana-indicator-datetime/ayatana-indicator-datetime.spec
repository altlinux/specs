%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: ayatana-indicator-datetime
Version: 22.9.0
Release: alt2

Summary: Ayatana Indicator providing clock and calendar
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-datetime

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd

BuildRequires: ayatana-cmake-modules cmake evolution-data-server-devel gcc-c++ gstreamer1.0-devel intltool libaccounts-glib-devel libayatana-common-devel libmessaging-menu-devel libnotify-devel libuuid-devel properties-cpp-devel
BuildRequires: accountsservice
BuildRequires: ayatana-indicator-common
BuildRequires: libblkid-devel
BuildRequires: libbrotli-devel
BuildRequires: libgcrypt-devel
BuildRequires: libjpeg-devel
BuildRequires: libmount-devel
BuildRequires: libnghttp2-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libpsl-devel
BuildRequires: libselinux-devel
BuildRequires: libsqlite3-devel
BuildRequires: libtiff-devel
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
%dir %_datadir/ayatana
%dir %_datadir/ayatana/indicators
%_datadir/ayatana/indicators/org.ayatana.indicator.datetime
%dir %_prefix/lib/systemd
%dir %_userunitdir
%_userunitdir/%name.service

%changelog
* Wed Aug 09 2023 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt2
- Removed translations which are ignored by %%find_lang
- Language specific files are declared
- Move service to /usr/libexec for compatibility with MATE Tweak and Debian

* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus
