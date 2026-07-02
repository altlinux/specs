%define rname ksshaskpass
%define openssh_askpass_dir %_libexecdir/openssh

Name: %rname
Version: 6.7.2
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma front-end for ssh-add
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires(pre,postun): alternatives >= 0:0.4, %openssh_askpass_dir
Requires: ssh-provider-openssh-askpass-common
Provides: openssh-askpass-kf6 = %version-%release

Provides: plasma5-ksshaskpass = 1:%version-%release
Obsoletes: plasma5-ksshaskpass < 1:%version-%release

Source: %rname-%version.tar
Source1: ksshaskpass-autostart
Source2: ksshaskpass.desktop

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: libvulkan-devel libqtkeychain-qt6-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel

%description
Ksshaskpass is a front-end for ssh-add which stores the password of the ssh key in KWallet.


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install

mkdir -p %buildroot/%openssh_askpass_dir/
mv %buildroot/%_K6bin/%rname \
    %buildroot/%openssh_askpass_dir/%name
mkdir -p %buildroot/%_K6bin/
install -m 0755 %SOURCE1 %buildroot/%_K6bin/
mkdir -p %buildroot/%_K6start/
install -m 0644 %SOURCE2 %buildroot/%_K6start/

# setup alternative
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name<<EOF
%openssh_askpass_dir/ssh-askpass        %openssh_askpass_dir/%name        41
EOF

%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_altdir/%name
%openssh_askpass_dir/%name
%_K6bin/ksshaskpass-autostart
%_K6start/ksshaskpass.desktop
%_K6xdgapp/*ksshaskpass*.desktop

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

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

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

