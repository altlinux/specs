%define rname kwallet-pam

Name: kf5-%rname
Version: 5.5.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 PAM KWallet integration
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-defaults.patch

# Automatically added by buildreq on Thu Aug 27 2015 (-bi)
# optimized out: cmake-modules elfutils libgpg-error libgpg-error-devel libstdc++-devel python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: cmake gcc-c++ glibc-devel-static libgcrypt-devel libpam-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake gcc-c++ glibc-devel libgcrypt-devel libpam-devel

%package -n pam0_kwallet
Summary: KDE4 PAM KWallet integration
Group: System/Base
%description -n pam0_kwallet
KDE4 PAM KWallet integration

%package -n pam0_kwallet5
Summary: KDE5 PAM KWallet integration
Group: System/Base
%description -n pam0_kwallet5
KDE5 PAM KWallet integration



%description
%summary.

%prep
%setup -n %rname-%version
%patch1 -p1

mkdir kde4
mv c* C* p* kde4
cp -ar kde4 kde5

%build
pushd kde4
%K5build -DKWALLET4=1 -DCMAKE_INSTALL_LIBDIR=/%_lib
popd
pushd kde5
%K5build -DKWALLET5=1 -DCMAKE_INSTALL_LIBDIR=/%_lib
popd

%install
for d in kde4 kde5; do
pushd $d
%K5install
popd
done

%files -n pam0_kwallet
%doc kde4/COPYING.LIB
%_pam_modules_dir/pam_kwallet.so

%files -n pam0_kwallet5
%doc kde5/COPYING.LIB
%_pam_modules_dir/pam_kwallet5.so

%changelog
* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt2
- fix path to KDE4 kwalletd

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- initial build
