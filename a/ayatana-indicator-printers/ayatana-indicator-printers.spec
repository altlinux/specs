%define _unpackaged_files_terminate_build 1

Name: ayatana-indicator-printers
Version: 22.2.0
Release: alt1

Summary: Ayatana Indicator showing active print jobs
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-printers

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd

BuildRequires: libaccounts-glib-devel libayatana-indicator3-devel libcups-devel libdbusmenu-gtk3-devel mate-common
BuildRequires: ayatana-indicator-common
BuildRequires: libdbus-devel
BuildRequires: libsystemd-devel

%description
This Ayatana Indicator is designed to let you view and control
active print jobs.

Use an indicator plugin for your desktop environment or a desktop
environment that natively supports indicators to provide this
indicator to the user.

%prep
%setup

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static \
  --disable-gcov
%make_build V=1

%install
%makeinstall_std
find %buildroot -type f -name "*.la" -delete -print

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun %name.service

%files
%doc COPYING AUTHORS AUTHORS.Canonical NEWS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%_libexecdir/%name/
%dir %_libdir/ayatana-indicators3
%dir %_libdir/ayatana-indicators3/7
%_libdir/ayatana-indicators3/7/libayatana-printersmenu.so
%_userunitdir/%name.service
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.2.0-alt1
- Initial build for Sisyphus
