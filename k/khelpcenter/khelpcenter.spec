%define rname khelpcenter

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 help center
Url: http://www.kde.org
License: GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-khelpcenter = %EVR
Obsoletes: kde5-khelpcenter < %EVR

Requires: kf6-kdoctools
Requires(post,preun): alternatives >= 0.2

Source: %rname-%version.tar

Patch1: khelpcenter-alt-hide-links-on-contents-screen.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-webengine-devel
BuildRequires: libxapian-devel libxml2-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-ktexttemplate-devel
BuildRequires: kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
KDE help center.

%prep
%setup -n %rname-%version
%patch1 -p2

%build
%K6build

%install
%K6install
%K6install_move data khelpcenter

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
> %buildroot/%_sysconfdir/alternatives/packages.d/%name
if [ "%_bindir" != "%_K6bin" ] ; then
    echo "%_bindir/khelpcenter       %_K6bin/khelpcenter      %version" \
	> %buildroot/%_sysconfdir/alternatives/packages.d/%name
fi

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%config /%_sysconfdir/alternatives/packages.d/%name
%_K6bin/khelpcenter*
%_K6libexecdir/khc*
%_K6xdgapp/*khelpcenter*
%_K6cfg/*
%_K6data/khelpcenter/
%_datadir/qlogging-categories6/*.*categories
%_K6dbus_srv/*.service
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

