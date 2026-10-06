%define rname kio

%def_enable streebog
%define sover 0
%define libkuriikwsfiltereng_private libdkuriikwsfiltereng_private%sover

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 network transparent access to files and data
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: dkf6-kded

Source: %name-%version.tar
Source10: add-ru.po
Patch1: alt-def-trash.patch
Patch2: alt-kio-help-fallback.patch
Patch3: alt-copy-first.patch
Patch4: alt-soname.patch
Patch5: alt-crash.patch
Patch10: alt-streebog-support.patch

# prevent hasher-privd limits
BuildRequires(pre): rpm-build-dkf6
BuildRequires: dqt6-tools-devel dqt6-declarative-devel dqt6-5compat-devel
BuildRequires: libdqt6-concurrent vulkan-headers
BuildRequires: docbook-style-xsl deepin-extra-cmake-modules
BuildRequires: libxslt-devel xsltproc zlib-devel
BuildRequires: libacl-devel libattr-devel libkrb5-devel
BuildRequires: libmount-devel libblkid-devel
BuildRequires: dkf6-karchive-devel dkf6-kauth-devel dkf6-kbookmarks-devel dkf6-kcodecs-devel
BuildRequires: dkf6-kcompletion-devel dkf6-kconfig-devel dkf6-kconfigwidgets-devel dkf6-kcoreaddons-devel
# BuildRequires: dkf6-kglobalaccel-devel
BuildRequires: dkf6-kdoctools dkf6-kdoctools-devel
BuildRequires: dkf6-kdbusaddons-devel
BuildRequires: dkf6-kguiaddons-devel dkf6-ki18n-devel dkf6-kiconthemes-devel dkf6-kitemviews-devel
BuildRequires: dkf6-kservice-devel dkf6-kjobwidgets-devel
# BuildRequires: dkf6-knotifications-devel dkf6-ktextwidgets-devel
BuildRequires: dkf6-kwallet-devel dkf6-kwidgetsaddons-devel dkf6-kwindowsystem-devel dkf6-kxmlgui-devel
BuildRequires: dkf6-solid-devel dkf6-sonnet-devel dkf6-attica-devel dkf6-kcrash-devel dkf6-kcolorscheme-devel
BuildRequires: dkf6-kded-devel

# find libraries
%add_findprov_lib_path %_DK6lib

%description
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file management.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
# Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
# Requires: dqt6-base-devel
# Requires: dkf6-kbookmarks-devel dkf6-kcompletion-devel dkf6-kconfig-devel dkf6-kcoreaddons-devel
# Requires: dkf6-kitemviews-devel dkf6-kjobwidgets-devel dkf6-kservice-devel dkf6-kxmlgui-devel dkf6-solid-devel
# Requires: dkf6-kwindowsystem-devel dkf6-kcrash-devel dkf6-kdbusaddons-devel dkf6-kcolorscheme-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkuriikwsfiltereng_private
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libkuriikwsfiltereng_private
KF6 library

%package -n libdkf6kiocore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6kiocore
KF6 library

%package -n libdkf6kiogui
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
#Requires: switcheroo-control
%description -n libdkf6kiogui
KF6 library

%package -n libdkf6kiowidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6kiowidgets
KF6 library

%package -n libdkf6kiofilewidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6kiofilewidgets
KF6 library

%package -n libdkf6kiontlm
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6kiontlm
KF6 library

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1
%if_enabled streebog
%patch10 -p2 -b .streebog
%endif

msgcat --use-first %SOURCE10 po/ru/kio6.po > po/ru/kio6.po.tmp
cat po/ru/kio6.po.tmp >po/ru/kio6.po
rm -f po/ru/kio6.po.tmp

sed -i 's|libexec/kf6|libexec/dkf6|' \
  src/core/worker.cpp

%build
%DK6build \
%if_enabled streebog
	-DEXTRA_CRYPTO:BOOL=ON \
%endif
	#

%install
%DK6install
%DK6install_move data doc kconf_update kdevappwizard kdevfiletemplates
%find_lang %name --with-kde --all-name
%DK6find_qtlang %name --all-name
mkdir -p %buildroot/%_DK6data/kio/servicemenus/

%files common -f %name.lang
%doc LICENSES/* README.md
%dir %_DK6data/kio/
%dir %_DK6data/kio/servicemenus/
%dir %_DK6data/searchproviders/
%_DK6data/qlogging-categories6/*.*categories

%files
#%config(noreplace) %_DK6xdgconf/*
%exclude %_bindir/*6
%_DK6bin/*6
%_DK6exec/*
%_DK6plug/kf6/*
%_DK6xdgapp/*.desktop
%_DK6data/searchproviders/*.desktop
%_DK6dbus_srv/*.service

%files devel
%_DK6plug/designer/*.so
%_DK6inc/KIO*/
%_DK6link/lib*.so
%_DK6lib/cmake/KF6KIO
%_DK6data/kdevappwizard/templates/*io*

%files -n %libkuriikwsfiltereng_private
%_DK6lib/libkuriikwsfiltereng_private.so.*
%_DK6lib/libkuriikwsfiltereng_private.so.%sover
%files -n libdkf6kiocore
%_DK6lib/libKF6KIOCore.so.*
%files -n libdkf6kiogui
%_DK6lib/libKF6KIOGui.so.*
%files -n libdkf6kiowidgets
%_DK6lib/libKF6KIOWidgets.so.*
%files -n libdkf6kiofilewidgets
%_DK6lib/libKF6KIOFileWidgets.so.*


%changelog
* Tue Oct 06 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
- fork for independent deepin build

* Tue Jul 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.28.0-alt1
- new version

* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Mon Feb 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.0-alt1
- new version

* Thu Jan 22 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.1-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.21.0-alt1
- new version

* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Mon Oct 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.1-alt1
- new version

* Fri Oct 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.0-alt1
- new version

* Mon Sep 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Thu Sep 11 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 6.17.0-alt2
- reintroduce the streebog suppor

* Mon Aug 25 2025 Sergey V Turchin <zerg@altlinux.org> 6.17.0-alt1
- new version
- temporary disable streebog support

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.15.0-alt1
- new version

* Tue May 27 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt3
- fix crash (closes: 54392)

* Tue May 27 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt2
- fix crash (closes: 54392)

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Thu Mar 06 2025 Daniil-Viktor Ratkin <krf10@altlinux.org> 6.11.0-alt3
- fix streebog patch

* Thu Feb 27 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt2
- fix russian translation

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Mon Dec 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.9.0-alt1
- new version

* Tue Dec 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt2
- fix requires

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

