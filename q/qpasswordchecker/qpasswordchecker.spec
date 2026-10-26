%define daemon_name qpasswordchecker-daemon
%define app_name QPasswordChecker

Name: qpasswordchecker
Version: 0.2.1
Release: alt1

Group: System/Configuration/Other
Summary: Password expiry notification application
License: GPLv3
Url: https://github.com/alxvmr/passwordchecker

#Requires: samba-winbind

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc gcc-c++
BuildRequires: pkgconfig(wbclient)
BuildRequires: qt6-svg-devel qt6-tools-devel libldap-devel libsasl2-devel libwbclient-devel

%description
Qt application and background service for password expiry notifications.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_bindir/%daemon_name
%_desktopdir/%app_name.desktop
%_user_unitdir/qpasswordchecker-daemon-user.service
%_datadir/qpasswordchecker/translations/qpasswordchecker_ru.qm
%_iconsdir/hicolor/*/apps/qpasswordchecker.*

%changelog
* Mon Oct 26 2026 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- fix to start service

* Fri Oct 23 2026 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1
- port to Qt 6
- rename to qpasswordchecker

* Mon Apr 27 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.1-alt1
- Fixes conflicting types error during build.

* Mon Jul 14 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.1.0-alt1
- Rename package: PasswordCheckerSettings to password-checker
- Add processing if the password never expires

* Wed May 21 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.1-alt1
- Init build
