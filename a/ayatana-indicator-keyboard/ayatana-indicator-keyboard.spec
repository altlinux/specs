%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%define libbasename       libayatana-keyboard
# Technically this should be basename-x110, but that would look very weird.
%define backendx11name    %libbasename-x11-0
# Unused, but keep for later.
%define backendlomiriname %libbasename-lomiri0

Name: ayatana-indicator-keyboard
Version: 22.9.0
Release: alt2

Summary: Ayatana Indicator for managing keyboard layout and desktop language
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-keyboard

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd

BuildRequires: ayatana-cmake-modules cmake gcc-c++ intltool libaccountsservice-devel libayatana-common-devel libxkbcommon-devel libxklavier-devel
BuildRequires: ayatana-indicator-common
BuildRequires: glib2-devel
BuildRequires: hicolor-icon-theme
BuildRequires: libblkid-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libpolkit-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: libXau-devel
BuildRequires: libXdmcp-devel
BuildRequires: libxml2-devel
BuildRequires: pkg-config
BuildRequires: zlib-devel

%description
This package contains the keyboard indicator, which should show
as an icon in the top panel of indicator aware desktop
environments.

It can be used to switch key layouts or languages, and helps the
user identifying which layouts are currently in use.

%prep
%setup

%build
%cmake \
  -Denable_tests=Off
%cmake_build

%install
%cmake_install

# Remove libraries targetting lomiri (Ubuntu Touch) for now. We can always
# re-enable it.
rm -rfv "%buildroot%_libdir/"libayatana-keyboard-lomiri.so*

# Move .pkla file to the correct polkit $HOME.
install -d -m '0755' %buildroot%_sharedstatedir/polkit/localauthority/10-vendor.d/
mv %buildroot%_sharedstatedir/polkit{-1,}/localauthority/10-vendor.d/50-org.ayatana.indicator.keyboard.AccountsService.pkla

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
%dir %_datadir/accountsservice/
%dir %_datadir/accountsservice/interfaces/
%_datadir/accountsservice/interfaces/org.ayatana.indicator.keyboard.AccountsService.xml
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/interfaces
%_datadir/dbus-1/interfaces/org.ayatana.indicator.keyboard.AccountsService.xml
%dir %_datadir/polkit-1
%dir %_datadir/polkit-1/actions
%_datadir/polkit-1/actions/org.ayatana.indicator.keyboard.AccountsService.policy
%_datadir/glib-2.0/schemas/org.ayatana.indicator.keyboard.gschema.xml
%_libdir/libayatana-keyboard-x11.so*
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%dir %_sharedstatedir/polkit/
%dir %_sharedstatedir/polkit/localauthority/
%dir %_sharedstatedir/polkit/localauthority/10-vendor.d/
%_sharedstatedir/polkit/localauthority/10-vendor.d/50-org.ayatana.indicator.keyboard.AccountsService.pkla
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/status
%_iconsdir/hicolor/scalable/status/*
%dir %_datadir/ayatana
%dir %_datadir/ayatana/indicators
%_datadir/ayatana/indicators/org.ayatana.indicator.keyboard
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
