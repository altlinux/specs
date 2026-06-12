%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: ayatana-indicator-a11y
Version: 25.4.1
Release: alt1

Summary: Ayatana Indicator for Accessibility Settings
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-a11y

Source: %name-%version.tar

Patch: %name-%version-%release.patch

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
BuildRequires: libsystemd-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel

Requires: onboard
Requires: orca
Requires: magnus

%description
This Ayatana Indicator provides quick access to accessibility related assistance applications such as the screen reader or an on-screen keyboard.

The provided accessibility indicator should show as an icon in the top panel of indicator aware desktop environments. It can be used to toggle and access various accessibility features.

Ayatana Indicators are only available on desktop environments that provide a renderer for system indicators (such as MATE, Xfce, Lomiri, etc.).

%package -n %name-devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description -n %name-devel
%{summary}.

%prep
%setup

%build
%cmake
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
%doc COPYING AUTHORS INSTALL.md NEWS ChangeLog README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%dir %_libexecdir/%name/
%_libexecdir/%name/%{name}-service
%_datadir/ayatana/indicators/org.ayatana.indicator.a11y
%_datadir/glib-2.0/schemas/org.ayatana.indicator.a11y.gschema.xml
%_userunitdir/%name.service
%_datadir/accountsservice/interfaces/org.ayatana.indicator.a11y.AccountsService.xml
%_datadir/polkit-1/actions/org.ayatana.indicator.a11y.AccountsService.policy
%_localstatedir/polkit-1/localauthority/10-vendor.d/50-org.ayatana.indicator.a11y.AccountsService.pkla
%_datadir/polkit-1/rules.d/50-org.ayatana.indicator.a11y.AccountsService.rules
%_iconsdir/hicolor/scalable/status/*

%files devel
%_datadir/dbus-1/interfaces/org.ayatana.indicator.a11y.AccountsService.xml

%changelog
* Fri Jun 12 2026 Nikolay Strelkov <snk@altlinux.org> 25.4.1-alt1
- New version 25.4.1.
- Created -devel package with the corresponding files.

* Sat Apr 12 2025 Nikolay Strelkov <snk@altlinux.org> 25.4.0-alt1
- New version 25.4.0.

* Sat Mar 22 2025 Nikolay Strelkov <snk@altlinux.org> 24.4.2-alt1
- New version 24.4.2.

* Sun Jan 19 2025 Nikolay Strelkov <snk@altlinux.org> 24.4.1-alt1
- Initial build for Sisyphus
