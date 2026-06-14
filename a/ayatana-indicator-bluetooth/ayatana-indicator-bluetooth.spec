%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

Name: ayatana-indicator-bluetooth
Version: 26.6.1
Release: alt1

Summary: Ayatana Indicator for managing Bluetooth devices
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-bluetooth

Source: %name-%version.tar

# sync with version 24.5.0-3 from Debian unstable
Patch: %name-%version-%release.patch

ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: ayatana-cmake-modules
BuildRequires: ayatana-indicator-common
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: libayatana-common-devel
BuildRequires: libblkid-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: vala-tools
BuildRequires: zlib-devel
BuildRequires: libnotify-devel

Requires: ayatana-indicator-common
Requires: blueman
Requires: bluez
Requires: gobject-introspection
Requires: mate-control-center

%description
This Ayatana Indicator exposes bluetooth functionality via the
system indicator API and provides fast user controls for
Bluetooth devices.

%prep
%setup
%patch -p1

%build
%cmake \
  -Denable_tests=Off
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
%doc COPYING AUTHORS INSTALL.md NEWS README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%_datadir/glib-2.0/schemas/org.ayatana.indicator.bluetooth.gschema.xml
%_datadir/ayatana/indicators/org.ayatana.indicator.bluetooth
%_userunitdir/%name.service

%changelog
* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.1-alt1
- New version 26.6.1.

* Tue Jul 22 2025 Nikolay Strelkov <snk@altlinux.org> 24.5.0-alt2
- Added Lomiri greeter support.

* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 24.5.0-alt1
- New version 24.5.0.

* Sun Jan 28 2024 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt3
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + break BuildRequires(pre) to multiple lines
  + do not own systemd dirs (thanks to @antohami)
  + temporary disable build on ppc64le

* Wed Aug 09 2023 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt2
- Removed translations which are ignored by %%find_lang
- Language specific files are declared
- Move service to /usr/libexec for compatibility with MATE Tweak and Debian

* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus
