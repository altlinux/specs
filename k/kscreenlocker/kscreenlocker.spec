%define rname kscreenlocker

%def_disable seccomp
%def_enable kcheckpass

%define sover 6
%define libkscreenlocker libkscreenlocker%sover

Name: %rname
Version: 6.7.2
Release: alt1
#Epoch: 2
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Screen Locker
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: plasma6-layer-shell-qt

Provides: plasma5-kscreenlocker = 2:%version-%release
Obsoletes: plasma5-kscreenlocker < 2:%version-%release

Source: %rname-%version.tar
%if_enabled kcheckpass
Source2: kcheckpass.tar
%endif
Source10: pam-kde6-screenlocker
Source11: pam-kde6-fingerprint
Source12: pam-kde6-smartcard
#
Source20: po-ru-add-kscreenlocker_greet.po

Patch1: alt-def-screenlocker.patch
%if_enabled kcheckpass
Patch2: alt-pam-support.patch
%endif
Patch3: alt-pam-service.patch
Patch4: alt-dont-respond.patch
Patch5: alt-disable-noninteractive.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: glibc-devel
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel qt6-declarative-devel
BuildRequires: libpam-devel libwayland-client-devel libwayland-server-devel
BuildRequires: libXi-devel libxcb-devel libxcbutil-keysyms-devel libxcbutil-devel
%if_enabled seccomp
BuildRequires: libseccomp-devel
%endif
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel
BuildRequires: kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdeclarative-devel kf6-kirigami-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-ksvg-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kidletime-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kpackage-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel  kf6-solid-devel kf6-sonnet-devel
BuildRequires: plasma6-lib-devel plasma6-layer-shell-qt-devel plasma6-libkscreen-devel

%description
%summary

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-kscreenlocker-common = 2:%version-%release
Obsoletes: plasma5-kscreenlocker-common < 2:%version-%release
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: plasma5-kscreenlocker-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkscreenlocker
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libkscreenlocker
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1
%if_enabled kcheckpass
%patch2 -p1
%endif
#patch3 -p1
%patch4 -p1
#patch5 -p1

%if_enabled kcheckpass
tar xf %SOURCE2 kcheckpass/
mv kcheckpass/authenticator.* greeter/
mv kcheckpass/config-unix.h.cmake ./
%endif

mkdir bin_fake
ln -s /bin/true bin_fake/loginctl

msgcat --use-first %SOURCE20 po/ru/kscreenlocker_greet.po > po/ru/kscreenlocker_greet.po.tmp
cat po/ru/kscreenlocker_greet.po.tmp > po/ru/kscreenlocker_greet.po
rm -f po/ru/kscreenlocker_greet.po.tmp

%build
export PATH=$PWD/bin_fake:$PATH
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #
# KSCREENLOCKER_PAM_SERVICE
# KSCREENLOCKER_PAM_PASSWORD_SERVICE
# KSCREENLOCKER_PAM_FINGERPRINT_SERVICE
# KSCREENLOCKER_PAM_SMARTCARD_SERVICE

%install
%K6install
%K6install_move data kconf_update ksmserver kpackage
%find_lang %name --all-name

# Install kde pam configuration files
install -d -m 0755 %buildroot/%_sysconfdir/pam.d/
install -m 0644 %SOURCE10 %buildroot/%_sysconfdir/pam.d/kde
install -m 0644 %SOURCE11 %buildroot/%_sysconfdir/pam.d/kde-fingerprint
install -m 0644 %SOURCE12 %buildroot/%_sysconfdir/pam.d/kde-smartcard

%files common -f %name.lang
%doc COPYING
%_datadir/qlogging-categories6/*.*categories

%files
%config(noreplace) %_sysconfdir/pam.d/kde
%config(noreplace) %_sysconfdir/pam.d/kde-fingerprint
%config(noreplace) %_sysconfdir/pam.d/kde-smartcard
%if_enabled kcheckpass
%attr(2711,root,chkpwd) %_K6libexecdir/kcheckpass
%_K6libexecdir/kscreenlocker_greet
%else
%attr(2711,root,chkpwd) %_K6libexecdir/kscreenlocker_greet
%endif
%_K6plug/plasma/kcms/systemsettings/*screenlocker*.so
%_K6data/ksmserver/screenlocker/
%_K6notif/*.notifyrc
%_K6xdgapp/*screenlocker*.desktop

%files devel
%_K6inc/KScreenLocker/
%_K6link/lib*.so
%_K6lib/cmake/KScreenLocker/
%_K6lib/cmake/ScreenSaverDBusInterface/
%_K6dbus_iface/*creen?aver*.xml

%files -n %libkscreenlocker
%_K6lib/libKScreenLocker.so.*
%_K6lib/libKScreenLocker.so.%sover



%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Mon Jul 21 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt2
- fix russian translation

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Thu Feb 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Thu Feb 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt2
- update pam_pkcs11 options

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Fri Sep 13 2024 Oleg Solovyov <mcpain@altlinux.org> 6.1.5-alt2
- enable non-interactive authenticators
- use system-auth-multi for interactive prompts
- use own fprintd and pkcs11 configs

* Tue Sep 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Wed Sep 11 2024 Oleg Solovyov <mcpain@altlinux.org> 6.1.4-alt7
- revert: use system-auth-local instead of system-auth
- disable non-interactive authenticators

* Wed Sep 11 2024 Oleg Solovyov <mcpain@altlinux.org> 6.1.4-alt6
- use system-auth-local instead of system-auth

* Thu Sep 05 2024 Oleg Solovyov <mcpain@altlinux.org> 6.1.4-alt5
- do not respond if authenticators are in Idle state

* Fri Aug 30 2024 Oleg Solovyov <mcpain@altlinux.org> 6.1.4-alt4
- kcheckpass fixes:
  + fix handling abort requests
  + cancel non-interactive authenticators after interactive prompts
  + abort PAM conversations completely

* Wed Aug 21 2024 Oleg Solovyov <mcpain@altlinux.org> 6.1.4-alt3
- port kcheckpass to KF6

* Tue Aug 20 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt2
- fix find pkcs11 pam-file

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

