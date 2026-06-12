%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: ayatana-indicator-datetime
Version: 26.6.0
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

# for Lomiri
BuildRequires: pkgconfig(lomiri-url-dispatcher)
BuildRequires: pkgconfig(lomiri-sounds)
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kcalcore-devel
BuildRequires: pkgconfig(lomiri-schemas)
BuildRequires: pkgconfig(libmkcal-qt5)

Requires: ayatana-indicator-datetime-common

%description
This Ayatana Indicator provides a combined calendar, clock, alarm
and event management tool.

%package -n ayatana-indicator-datetime-common
Summary: Common files used by both Ayatana/Lomiri Indicator Datetime variants
Group: Graphical desktop/Other
BuildArch: noarch

%description -n ayatana-indicator-datetime-common
Ayatana / Lomiri Indicator Datetime are two variants of the Ayatana
Datetime Indicator built for different use cases. They provide a
combined calendar, clock, alarm and event management tool for common
desktop environments and for the Lomiri operating environment.

This package contains files used by both variants.

%package -n lomiri-indicator-datetime
Summary: Lomiri Indicator providing clock and calendar
Group: Graphical desktop/Other
Requires: ayatana-indicator-datetime-common

%description -n lomiri-indicator-datetime
This Lomiri Indicator provides a combined calendar, clock, alarm and
event management tool.

This variant of the datetime indicator is targeted for being used on
Lomiri, this indicator supports phone devices.

This variant of the datetime indicator has been built for using
msyncd (mkcal) as ICS data storage backend.

%prep
%setup

%build
%cmake -B build_a \
       -Denable_tests=Off \
       -Denable_lomiri_features=Off
cmake --build "build_a" -j%__nprocs

%cmake -B build_l \
       -Denable_tests=Off \
       -DENABLE_LOMIRI_FEATURES=ON
cmake --build "build_l" -j%__nprocs

%install
export DESTDIR="%buildroot"
cmake --install "build_a" --verbose
cmake --install "build_l" --verbose

find %buildroot -type f -name "*.la" -delete -print

# these translations are ignored by %%find_lang
rm -fv %buildroot%_datadir/locale/it_CARES/LC_MESSAGES/%name.mo
rm -fv %buildroot%_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/%name.mo

%find_lang %name

%post -n ayatana-indicator-datetime
%systemd_user_post %name.service
%post -n lomiri-indicator-datetime
%systemd_user_post lomiri-indicator-datetime.service

%preun -n ayatana-indicator-datetime
%systemd_user_preun %name.service
%preun -n lomiri-indicator-datetime
%systemd_user_preun lomiri-indicator-datetime.service

%postun -n ayatana-indicator-datetime
%systemd_user_postun %name.service
%postun -n lomiri-indicator-datetime
%systemd_user_postun lomiri-indicator-datetime.service

%files
%config %_sysconfdir/xdg/autostart/%name.desktop
%_userunitdir/%name.service
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service

%files -n ayatana-indicator-datetime-common -f %name.lang
%doc COPYING AUTHORS INSTALL.md NEWS NEWS.Canonical README.md
%_datadir/glib-2.0/schemas/org.ayatana.indicator.datetime.gschema.xml
%_datadir/ayatana/indicators/org.ayatana.indicator.datetime

%files -n lomiri-indicator-datetime
%dir %_libexecdir/lomiri-indicator-datetime
%_libexecdir/lomiri-indicator-datetime/lomiri-indicator-datetime-service
%_userunitdir/lomiri-indicator-datetime.service

%changelog
* Fri Jun 12 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.0-alt1
- New version 26.6.0.

* Sun Jul 20 2025 Nikolay Strelkov <snk@altlinux.org> 25.4.0-alt2
- Enable Lomiri support.

* Sat Apr 12 2025 Nikolay Strelkov <snk@altlinux.org> 25.4.0-alt1
- New version 25.4.0.

* Sat Mar 22 2025 Nikolay Strelkov <snk@altlinux.org> 24.5.1-alt1
- New version 24.5.1.

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
