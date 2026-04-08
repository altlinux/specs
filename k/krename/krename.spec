%define rname krename

Name: %rname
Version: 5.0.60
Release: alt0.1
%K6init

Summary: A powerful batch renamer for KDE5
Group: File tools
License: GPL-2.0
Url: https://invent.kde.org/utilities/krename

Provides: kde5-krename = %EVR
Obsoletes: kde5-krename < %EVR

Source: %rname-%version.tar
Source10: po-ru.po
#
Patch10: alt-startupinfo-labels-color.patch
Patch11: alt-cmake.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-5compat-devel
BuildRequires: kf6-kcompletion-devel kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-kio-devel kf6-kservice-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: libexiv2-devel
BuildRequires: fontconfig-devel libfreetype-devel libpodofo-devel
BuildRequires: taglib-devel
BuildRequires: qt5-base-devel

%description
Krename is a very powerful batch file renamer for KDE5 which can rename a list
of files based on a set of expressions. It can copy/move the files to another
directory or simply rename the input files. Krename supports many conversion
operations, including conversion of a filename to lowercase or to uppercase,
conversion of the first letter of every word to uppercase, adding numbers to
filenames, finding and replacing parts of the filename, and many more.
It can also change access and modification dates, permissions, and file ownership.

%prep
%setup -n %rname-%version
#
%patch10 -p1
%patch11 -p1
#cat %SOURCE10 >po/ru/krename.po

%build
%K6build

%install
%K6install
#K6install_move data locale
%find_lang --with-kde %rname

%files -f %rname.lang
%_K6bin/%rname
%_K6xdgapp/*.desktop
%_K6icon/*/*/apps/*.*
%_K6data/kio/servicemenus/*.desktop
%_datadir/metainfo/*.xml

%changelog
* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 5.0.60-alt0.1
- switch to KF6 beta

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 5.0.2-alt4
- build with new taglib

* Tue Apr 29 2025 Sergey V Turchin <zerg@altlinux.org> 5.0.2-alt3
- move service menus to standard place

* Mon Mar 04 2024 Sergey V Turchin <zerg@altlinux.org> 5.0.2-alt2
- add upstream fixes for new podofo and exiv2

* Wed Nov 08 2023 Sergey V Turchin <zerg@altlinux.org> 5.0.2-alt1
- new version
- build without exiv2

* Wed Apr 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt1
- new version

* Thu Aug 27 2020 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt7
- fix compile with new environment

* Fri Jun 14 2019 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt6
- dont use ubt macro

* Tue Sep 04 2018 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt5
- NMU: rebuild with podofo 0.9.6

* Wed Apr 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt4
- fix conflict with kde4-krename

* Tue Apr 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt3
- add fix against KDEBUG-391291
- fix startup info page labels color

* Wed Apr 18 2018 Oleg Solovyov <mcpain@altlinux.org> 5.0.0-alt2
- add %%ubt tag for backporting

* Mon Apr 16 2018 Oleg Solovyov <mcpain@altlinux.org> 5.0.0-alt1
- initial build for ALT

