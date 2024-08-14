%define rname ksshaskpass
%define openssh_askpass_dir %_libexecdir/openssh

Name: %rname
Version: 6.1.2
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
#%_K6xdgapp/org.kde.ksshaskpass.desktop


%changelog
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

