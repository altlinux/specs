%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname kwallet-pam

Name: %rname
Version: 6.1.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma PAM KWallet integration
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar
# ALT
Patch10: alt-allow-empty-password.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake gcc-c++ glibc-devel extra-cmake-modules qt6-base-devel libgcrypt-devel libpam-devel
BuildRequires: kf6-kwallet-devel
# find kwalletd6
BuildRequires: kf6-kwallet

%description
%summary.

%package -n pam0_kwallet5
Summary: KDE6 PAM KWallet integration
Group: System/Base
Requires: socat
%description -n pam0_kwallet5
KDE6 PAM KWallet integration.

%prep
%setup -n %rname-%version
%patch10 -p1

%build
KWALLETD_PATH=%_K6bin/kwalletd6
for f in \
    /usr/share/dbus-1/services/org.kde.kwalletd6.service \
    #
do
    [ -e $f ] || continue
    KWALLETD_PATH_NEW=`grep '^Exec=' $f | sed 's|^Exec=||'`
    [ -z "$KWALLETD_PATH_NEW" ] || KWALLETD_PATH=$KWALLETD_PATH_NEW
done
%K6build \
    -DKWALLETD_BIN_PATH=$KWALLETD_PATH \
    -DCMAKE_INSTALL_LIBDIR:PATH=%_libdir \
    #

%install
%K6install

%files -n pam0_kwallet5
%doc LICENSES/*
%_libdir/security/pam_kwallet5.so
%_K6libexecdir/pam_kwallet_init
%_K6start/pam_kwallet_init.desktop
%_userunitdir/*.service



%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

