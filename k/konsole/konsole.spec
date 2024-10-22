%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%define rname konsole

%define sover 6
%define libkonsoleprivate libkonsoleprivate%sover
%define libkonsoleapp libkonsoleapp%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init no_altplace

Group: Terminals
Summary: Terminal emulator for KDE
Url: http://www.kde.org
License: LGPL-2.0-only

Requires(post,preun): alternatives >= 0.2
Provides: x-terminal-emulator xvt %_x11bindir/xvt
#Requires: fonts-bitmap-misc
Provides: kde5-konsole = %EVR
Obsoletes: kde5-konsole < %EVR

Source: %rname-%version.tar
Source10: profiles.tar
Patch11: alt-sover.patch
Patch12: alt-def-font.patch
Patch13: alt-def-colors.patch
Patch14: alt-fix-empty-profile.patch
Patch15: alt-disable-colorfilter.patch
Patch16: alt-new-tab-button.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: rpm-build-xdg
BuildRequires: libalternatives-devel
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-multimedia-devel qt6-5compat-devel
BuildRequires: libdb4-devel zlib-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel
BuildRequires: kf6-knotifyconfig-devel kf6-kparts-devel kf6-kpty-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-sonnet-devel kf6-knewstuff-devel kf6-kglobalaccel-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel
BuildRequires: libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libxkbfile-devel

%description
As well as being a standalone program, it is also used by other KDE programs
such as the Kate editor and KDevelop development environment to provide easy
access to a terminal window. Konsole's features and usage are explained and
illustrated in the Konsole handbook, which can be accessed by browsing to
"help:/konsole" in Konqueror.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-konsole-common = %EVR
Obsoletes: kde5-konsole-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkonsoleprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
Obsoletes: libkonsoleprivate1 < %EVR
%description -n %libkonsoleprivate
%name library

%package -n %libkonsoleapp
Group: System/Libraries
Summary: %name library
Requires: %name-common
Obsoletes: libkonsoleapp1 < %EVR
%description -n %libkonsoleapp
%name library

%prep
%setup -q -n %rname-%version -a10
%patch11 -p1
#patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
%K6build \
    -DCONFIG_INSTALL_DIR:PATH=%_xdgconfigdir \
    -DDATA_INSTALL_DIR=%_datadir \
    #

%install
%K6install
%K6install_move data kglobalaccel kio knsrcfiles kconf_update

# install profiles
KONSOLE_DATA_DIR=%buildroot/%_datadir/konsole/
mkdir -p "$KONSOLE_DATA_DIR"
for f in profiles/*.profile ; do
    install -m 0644 $f $KONSOLE_DATA_DIR
done

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/konsole <<__EOF__
%_x11bindir/xvt %_K6bin/konsole        57
%_x11bindir/x-terminal-emulator %_K6bin/konsole        57
__EOF__

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%config %_sysconfdir/alternatives/packages.d/konsole
# konsole may problems for some reasons because sgid
#%attr(2711,root,utempter) %_K6bin/konsole
%_K6bin/konsole
%_K6bin/konsoleprofile
%_K6conf_bin/konsole_globalaccel
%_K6plug/kf6/parts/*konsole*.so
%_K6plug/konsoleplugins/
%_K6xdgapp/org.kde.konsole.desktop
%_datadir/konsole/
%_K6conf_bin/*konsole*
%_K6conf_up/*konsole*
%_K6data/kio/servicemenus/konsolerun.desktop
#
%_K6notif/*
%_K6data/kglobalaccel/*konsole*
%_datadir/metainfo/*konsole*
%_datadir//zsh/site-functions/*konsole*

%files -n %libkonsoleprivate
%_K6lib/libkonsoleprivate.so.*
%_K6lib/libkonsoleprivate.so.%sover

%files -n %libkonsoleapp
%_K6lib/libkonsoleapp.so.*
%_K6lib/libkonsoleapp.so.%sover


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

