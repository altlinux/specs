%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%def_with check

Name: ayatana-indicator-printers
Version: 26.6.0
Release: alt1

Summary: Ayatana Indicator showing active print jobs
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-printers

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: ayatana-cmake-modules
BuildRequires: ayatana-indicator-common
BuildRequires: cmake
BuildRequires: intltool
BuildRequires: libaccounts-glib-devel
BuildRequires: libayatana-common-devel
BuildRequires: libcups-devel
BuildRequires: libdbus-devel
BuildRequires: libdbusmenu-gtk3-devel
BuildRequires: libpcre2-devel
BuildRequires: libsystemd-devel

%if_with check
BuildRequires: ctest
BuildRequires: dbus
%endif

%description
This Ayatana Indicator is designed to let you view and control
active print jobs.

Use an indicator plugin for your desktop environment or a desktop
environment that natively supports indicators to provide this
indicator to the user.

%prep
%setup

%build
%add_optflags -std=gnu17
%cmake \
       -DCMAKE_INSTALL_LOCALSTATEDIR=%_localstatedir \
%if_with check
       -DENABLE_TESTS=ON \
%else
       -DENABLE_TESTS=OFF \
%endif
       -DENABLE_COVERAGE=OFF
%cmake_build

%install
%cmake_install

find %buildroot -type f -name "*.la" -delete -print

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
%doc COPYING AUTHORS AUTHORS.Canonical NEWS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%_datadir/ayatana/indicators/org.ayatana.indicator.printers
%_userunitdir/%name.service

%changelog
* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.0-alt1
- New version 26.6.0.
- Enabled tests.

* Fri Jun 12 2026 Nikolay Strelkov <snk@altlinux.org> 23.10.2-alt1
- New version 23.10.2.

* Thu Apr 23 2026 Nikolay Strelkov <snk@altlinux.org> 23.10.1-alt2
- Fixed FTBFS caused by gcc15.

* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 23.10.1-alt1
- New version 23.10.1.

* Sun Jan 28 2024 Nikolay Strelkov <snk@altlinux.org> 22.2.0-alt3
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + break BuildRequires(pre) to multiple lines
  + do not own systemd dirs (thanks to @antohami)

* Wed Aug 09 2023 Nikolay Strelkov <snk@altlinux.org> 22.2.0-alt2
- Removed translations which are ignored by %%find_lang
- Language specific files are declared
- Move service to /usr/libexec for compatibility with MATE Tweak and Debian

* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.2.0-alt1
- Initial build for Sisyphus
