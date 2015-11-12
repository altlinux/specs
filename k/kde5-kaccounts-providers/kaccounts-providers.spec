%define rname kaccounts-providers

Name: kde5-%rname
Version: 15.08.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Accounts Providers
Url: http://www.kde.org
License: GPLv2+

BuildArch: noarch
#Requires: signon-ui

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Aug 21 2015 (-bi)
# optimized out: cmake cmake-modules libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-widgets libstdc++-devel perl-Encode perl-XML-Parser pkg-config python-base python3 python3-base qt5-base-devel
#BuildRequires: accounts-qt5-devel extra-cmake-modules gcc-c++ intltool kde5-kaccounts-integration-devel kf5-kcoreaddons-devel rpm-build-python3 ruby ruby-stdlibs signon-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: accounts-qt5-devel signon-devel intltool
BuildRequires: kde5-kaccounts-integration-devel kf5-kcoreaddons-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kf5-filesystem
%description common
%name common package


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
#%find_lang %name --with-kde --all-name

%files
%config(noreplace) /etc/signon-ui/webkit-options.d/*.conf
%_datadir/accounts/providers/*.provider


%changelog
* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Tue Aug 04 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt1
- initial build
