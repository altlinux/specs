%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%def_with check

Name: ayatana-indicator-display
Version: 26.6.0
Release: alt1

Summary: Ayatana Indicator for Display configuration
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-display

Source: %name-%version.tar

ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: ayatana-cmake-modules
BuildRequires: ayatana-indicator-common
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: libaccountsservice-devel
BuildRequires: libayatana-common-devel
BuildRequires: libblkid-devel
BuildRequires: libgeoclue2-devel
BuildRequires: libgudev-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: pkg-config
BuildRequires: properties-cpp-devel
BuildRequires: zlib-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xrandr)

%if_with check
BuildRequires: libgtest-devel
BuildRequires: ctest
BuildRequires: qt5-base-devel
BuildRequires: libqtdbustest-devel
BuildRequires: libqtdbusmock-devel
BuildRequires: dbus
BuildRequires: cppcheck
%endif

Requires: xsct

%description
This Ayatana Indicator is designed to be placed on the right side
of a panel and give the user easy control for changing their
display settings.

Ayatana Indicators are only available on desktop environments that
provide a renderer for system indicators (such as MATE, Xfce, Lomiri,
etc.).

%package -n %name-devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description -n %name-devel
%{summary}.

%prep
%setup

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

find %buildroot -type 'f' -name '*.la' -delete -print

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
%doc COPYING AUTHORS INSTALL.md NEWS README README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%_datadir/glib-2.0/schemas/org.ayatana.indicator.display.gschema.xml
%_datadir/ayatana/indicators/org.ayatana.indicator.display
%_iconsdir/hicolor/scalable/status/*.svg
%_userunitdir/%name.service
%_datadir/accountsservice/interfaces/org.ayatana.indicator.display.AccountsService.xml
%_datadir/polkit-1/actions/org.ayatana.indicator.display.AccountsService.policy
%_datadir/polkit-1/rules.d/50-org.ayatana.indicator.display.AccountsService.rules

%files devel
%_datadir/dbus-1/interfaces/org.ayatana.indicator.display.AccountsService.xml

%changelog
* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.0-alt1
- New version 26.6.0.
- Enabled tests.

* Fri Jun 12 2026 Nikolay Strelkov <snk@altlinux.org> 24.5.3-alt1
- New version 24.5.3.
- Created -devel package with the corresponding files.

* Wed May 07 2025 Nikolay Strelkov <snk@altlinux.org> 24.5.2-alt1
- New version 24.5.2.

* Sat Mar 22 2025 Nikolay Strelkov <snk@altlinux.org> 24.5.1-alt1
- New version 24.5.1.

* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 24.5.0-alt1
- New version 24.5.0.

* Sun Jan 28 2024 Nikolay Strelkov <snk@altlinux.org> 22.9.3-alt3
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + break BuildRequires(pre) to multiple lines
  + do not own icons and systemd dirs (thanks to @antohami)
  + do not own /usr/share/ayatana/indicators
  + temporary disable build on ppc64le

* Wed Aug 09 2023 Nikolay Strelkov <snk@altlinux.org> 22.9.3-alt2
- Removed translations which are ignored by %%find_lang
- Language specific files are declared
- Move service to /usr/libexec for compatibility with MATE Tweak and Debian

* Sun Jan 29 2023 Nikolay Strelkov <snk@altlinux.org> 22.9.3-alt1
- Initial build for Sisyphus
