%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: ayatana-indicator-sound
Version: 24.5.2
Release: alt2

Summary: Ayatana Indicator for managing system sound
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-sound

Source: %name-%version.tar

Patch: %name-%version-%release.patch

ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: accountsservice
BuildRequires: ayatana-cmake-modules
BuildRequires: ayatana-indicator-common
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: libaccountsservice-gir-devel
BuildRequires: libayatana-common-devel
BuildRequires: libblkid-devel
BuildRequires: libgee0.8-devel
BuildRequires: libjpeg-devel
BuildRequires: libmount-devel
BuildRequires: libnotify-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libpng-devel
BuildRequires: libpolkit-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: libtiff-devel
BuildRequires: libxml2-devel
BuildRequires: vala-tools
BuildRequires: zlib-devel

Requires: gobject-introspection

%description
This Ayatana Indicator is designed to be placed on the right side of a
panel and give the user easy control over the system's sound settings.

Ayatana Indicator Sound provides easy control of the PulseAudio sound
daemon, and integrates well with media players that support the Mpris
protocol.

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
  -DCMAKE_INSTALL_LOCALSTATEDIR=%_localstatedir \
  -Denable_tests=Off \
  -Denable_lomiri_features=Off
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
%doc COPYING AUTHORS INSTALL.md NEWS NEWS.Canonical README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%dir %_datadir/ayatana
%dir %_datadir/ayatana/indicators
%_datadir/ayatana/indicators/org.ayatana.indicator.sound
%_datadir/glib-2.0/schemas/org.ayatana.indicator.sound.gschema.xml
%_userunitdir/%name.service
%_datadir/accountsservice/interfaces/org.ayatana.indicator.sound.AccountsService.xml
%_datadir/polkit-1/actions/org.ayatana.indicator.sound.AccountsService.policy
%_datadir/polkit-1/rules.d/50-org.ayatana.indicator.sound.AccountsService.rules

%files devel
%_datadir/dbus-1/interfaces/org.ayatana.indicator.sound.AccountsService.xml

%changelog
* Fri Jun 12 2026 Nikolay Strelkov <snk@altlinux.org> 24.5.2-alt2
- Created -devel package with the corresponding files.

* Sat Mar 22 2025 Nikolay Strelkov <snk@altlinux.org> 24.5.2-alt1
- New version 24.5.2.

* Fri Jan 17 2025 Nikolay Strelkov <snk@altlinux.org> 24.5.1-alt1
- New version 24.5.1.

* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 24.5.0-alt1
- New version 24.5.0.

* Sun Jan 28 2024 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt3
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + break BuildRequires(pre) to multiple lines
  + do not own dbus, polkit and systemd dirs (thanks to @antohami)
  + do not own /usr/share/accountsservice/interfaces
  + temporary disable build on ppc64le

* Tue Aug 08 2023 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt2
- Removed translations which are ignored by %%find_lang
- Language specific files are declared
- Disown /var/lib/polkit-1 to prevent conflict with polkit-pkla-compat
- Move service to /usr/libexec for compatibility with MATE Tweak and Debian

* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus
