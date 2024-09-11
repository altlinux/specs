%define rname kscreenlocker

%def_disable seccomp
%def_enable kcheckpass

%define sover 6
%define libkscreenlocker libkscreenlocker%sover

Name: %rname
Version: 6.1.5
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
BuildRequires: libXi-devel libxcb-devel libxcbutil-keysyms-devel
%if_enabled seccomp
BuildRequires: libseccomp-devel
%endif
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel
BuildRequires: kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdeclarative-devel
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
%patch3 -p1
%patch4 -p1
%patch5 -p1

%if_enabled kcheckpass
tar xf %SOURCE2 kcheckpass/
mv kcheckpass/authenticator.* greeter/
mv kcheckpass/config-unix.h.cmake ./
%endif

mkdir bin_fake
ln -s /bin/true bin_fake/loginctl

%build
export PATH=$PWD/bin_fake:$PATH
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -DKSCREENLOCKER_PAM_SERVICE="kde6-screenlocker" \
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
install -m 0644 %SOURCE10 %buildroot/%_sysconfdir/pam.d/kde6-screenlocker

%files common -f %name.lang
%doc COPYING
%_datadir/qlogging-categories6/*.*categories

%files
%config(noreplace) %_sysconfdir/pam.d/kde6-screenlocker
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

