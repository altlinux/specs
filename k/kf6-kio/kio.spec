%define rname kio

%def_disable streebog
%define sover 0
%define libkuriikwsfiltereng_private libkuriikwsfiltereng_private%sover

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init no_altplace

Group: System/Libraries
Summary: KDE Frameworks 6 network transparent access to files and data
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: kf5-kded

Source: %rname-%version.tar
Source10: add-ru.po
Patch1: alt-def-trash.patch
Patch2: alt-kio-help-fallback.patch
Patch3: alt-copy-first.patch
Patch4: alt-soname.patch
Patch10: alt-streebog-support.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-tools-devel qt6-declarative-devel qt6-5compat-devel
BuildRequires: docbook-style-xsl extra-cmake-modules
BuildRequires: libxslt-devel xsltproc zlib-devel
BuildRequires: libacl-devel libattr-devel libkrb5-devel
BuildRequires: libmount-devel libblkid-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel
BuildRequires: kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdoctools kf6-kdoctools-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-attica-devel kf6-kcrash-devel kf6-kcolorscheme-devel
BuildRequires: kf6-kded-devel

%description
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file management.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: qt6-base-devel
Requires: kf6-kbookmarks-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kcoreaddons-devel
Requires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-kxmlgui-devel kf6-solid-devel
Requires: kf6-kwindowsystem-devel kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kcolorscheme-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkuriikwsfiltereng_private
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libkuriikwsfiltereng_private
KF6 library

%package -n libkf6kiocore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6kiocore
KF6 library

%package -n libkf6kiogui
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
#Requires: switcheroo-control
%description -n libkf6kiogui
KF6 library

%package -n libkf6kiowidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6kiowidgets
KF6 library

%package -n libkf6kiofilewidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6kiofilewidgets
KF6 library

%package -n libkf6kiontlm
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6kiontlm
KF6 library

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%if_enabled streebog
%patch10 -p2 -b .streebog
%endif

msgcat --use-first %SOURCE10 po/ru/kio6.po > po/ru/kio6.po.tmp
cat po/ru/kio6.po.tmp >po/ru/kio6.po
rm -f po/ru/kio6.po.tmp


%build
%K6build \
%if_enabled streebog
	-DEXTRA_CRYPTO:BOOL=ON \
%endif
	#

%install
%K6install
%K6install_move data doc kconf_update kdevappwizard kdevfiletemplates
%find_lang %name --with-kde --all-name
%K6find_qtlang %name --all-name
mkdir -p %buildroot/%_K6data/kio/servicemenus/

%files common -f %name.lang
%doc LICENSES/* README.md
%dir %_K6data/kio/
%dir %_K6data/kio/servicemenus/
%dir %_K6data/kf6/searchproviders/
%_datadir/qlogging-categories6/*.*categories

%files
#%config(noreplace) %_K6xdgconf/*
%_bindir/*6
%_K6bin/*6
%_K6exec/*
%_K6plug/kf6/*
%_K6xdgapp/*.desktop
%_K6data/kf6/searchproviders/*.desktop
%_K6dbus_srv/*.service

%files devel
%_K6plug/designer/*.so
%_K6inc/KIO*/
%_K6link/lib*.so
%_K6lib/cmake/KF6KIO
%_K6data/kdevappwizard/templates/*io*

%files -n %libkuriikwsfiltereng_private
%_K6lib/libkuriikwsfiltereng_private.so.*
%_K6lib/libkuriikwsfiltereng_private.so.%sover
%files -n libkf6kiocore
%_K6lib/libKF6KIOCore.so.*
%files -n libkf6kiogui
%_K6lib/libKF6KIOGui.so.*
%files -n libkf6kiowidgets
%_K6lib/libKF6KIOWidgets.so.*
%files -n libkf6kiofilewidgets
%_K6lib/libKF6KIOFileWidgets.so.*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

