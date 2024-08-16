%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname polkit-kde-agent-1

Name: polkit-kde-agent
Version: 6.1.4
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 PolicyKit authentication agent
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: polkit
Provides: plasma5-polkit-kde-agent = 1:%version-%release
Obsoletes: plasma5-polkit-kde-agent < 1:%version-%release

Source: %rname-%version.tar
Patch1: alt-stay-on-top.patch
Patch2: alt-show-only-one-user-too.patch

BuildRequires(pre): rpm-build-kf6 extra-cmake-modules
BuildRequires: libvulkan-devel
BuildRequires: qt6-declarative-devel
BuildRequires: pkgconfig(polkit-qt6-1)
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kitemviews-devel
BuildRequires: kf6-knotifications-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kcrash-devel

%description
Provides Policy Kit Authentication Agent that nicely fits to KDE.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K6build \
    #

%install
%K6install
%find_lang %name --all-name

%files -f %name.lang
%_K6libexecdir/polkit-kde-authentication-agent-1
%_K6start/*polkit-kde-authentication-agent*.desktop
%_K6xdgapp/*polkit-kde-authentication-agent*.desktop
%_K6notif/policykit1-kde.notifyrc
%_userunitdir/*.service

%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

