%define _unpackaged_files_terminate_build 1

Name: ayatana-indicator-sound
Version: 22.9.0
Release: alt1

Summary: Ayatana Indicator for managing system sound
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-sound

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd

BuildRequires: ayatana-cmake-modules cmake gcc-c++ intltool libaccountsservice-gir-devel libayatana-common-devel libgee0.8-devel libnotify-devel libpulseaudio-devel libxml2-devel vala-tools
BuildRequires: accountsservice
BuildRequires: ayatana-indicator-common
BuildRequires: libblkid-devel
BuildRequires: libjpeg-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libpng-devel
BuildRequires: libpolkit-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: libtiff-devel
BuildRequires: zlib-devel

Requires: gobject-introspection

%description
This Ayatana Indicator is designed to be placed on the right side of a 
panel and give the user easy control over the system's sound settings. 

Ayatana Indicator Sound provides easy control of the PulseAudio sound 
daemon, and integrates well with media players that support the Mpris 
protocol.

%prep
%setup

%build
%cmake \
  -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir \
  -DCMAKE_INSTALL_LOCALSTATEDIR=%_localstatedir \
  -Denable_tests=Off                              \
  -Denable_lomiri_features=Off
%cmake_build

%install
%cmake_install

# Move .pkla file to the correct polkit $HOME.
mkdir -p %buildroot%_localstatedir/polkit-1/localauthority/10-vendor.d/
mv -v %buildroot%_localstatedir/lib/polkit-1/localauthority/10-vendor.d/50-org.ayatana.indicator.sound.AccountsService.pkla %buildroot%_localstatedir/polkit-1/localauthority/10-vendor.d/

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun %name.service

%files
%doc COPYING AUTHORS INSTALL.md NEWS NEWS.Canonical README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%_libexecdir/%name/
%dir %_datadir/ayatana
%dir %_datadir/ayatana/indicators
%_datadir/ayatana/indicators/org.ayatana.indicator.sound
%_datadir/glib-2.0/schemas/org.ayatana.indicator.sound.gschema.xml
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/interfaces
%_datadir/dbus-1/interfaces/org.ayatana.indicator.sound.AccountsService.xml
%_userunitdir/%name.service
%dir %_datadir/accountsservice/
%dir %_datadir/accountsservice/interfaces/
%_datadir/accountsservice/interfaces/org.ayatana.indicator.sound.AccountsService.xml
%_datadir/polkit-1/actions/org.ayatana.indicator.sound.AccountsService.policy
%dir %_localstatedir/polkit-1/
%dir %_localstatedir/polkit-1/localauthority/
%dir %_localstatedir/polkit-1/localauthority/10-vendor.d/
%_localstatedir/polkit-1/localauthority/10-vendor.d/50-org.ayatana.indicator.sound.AccountsService.pkla
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus
