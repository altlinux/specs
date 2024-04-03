%define rname ghostwriter
%def_enable qt5
%def_disable qt6

Name: ghostwriter
Version: 24.02.1
Release: alt1
%if_enabled qt5
%K5init
%endif
%if_enabled qt6
%K6init
%endif

Group: Editors
Summary: Cross-platform, aesthetic, distraction-free Markdown editor
License: GPL-3.0-or-later and CC-BY-SA-4.0 and BSD-2-Clause and BSD-3-Clause and LGPL-2.0-or-later and MIT and Apache-2.0
Url: https://invent.kde.org/office/ghostwriter

# Requires one of pandoc or multimarkdown or cmark
#Requires: pandoc

# Requires QtWebEngine. Can be built either with Qt5 or Qt6.
%if_enabled qt5
ExcludeArch: %not_qt5_qtwebengine_arches
%endif
%if_enabled qt6
ExcludeArch: %not_qt6_qtwebengine_arches
%endif

# Source-url: https://github.com/KDE/ghostwriter/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Patch1: alt-crash.patch

%if_enabled qt5
BuildRequires(pre): rpm-macros-qt5 rpm-macros-qt5-webengine
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel
BuildRequires: qt5-webengine-devel qt5-svg-devel qt5-tools-devel
BuildRequires: kf5-kdoctools kf5-kcoreaddons-devel kf5-kxmlgui-devel kf5-kconfigwidgets-devel kf5-kwidgetsaddons-devel kf5-sonnet-devel
%endif
%if_enabled qt6
BuildRequires(pre): rpm-macros-qt6 rpm-macros-qt6-webengine
#BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-base-devel qt6-5compat-devel qt6-tools-devel
BuildRequires: qt6-webengine-devel qt6-webchannel-devel qt6-svg-devel
BuildRequires: kf6-kdoctools kf6-kcoreaddons-devel kf6-kxmlgui-devel kf6-kconfigwidgets-devel kf6-kwidgetsaddons-devel kf6-sonnet-devel
%endif
BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib-devel
BuildRequires: libhunspell-devel
BuildRequires: gcc-c++

%description
Ghostwriter is a text editor for Markdown, which is a plain text markup
format created by John Gruber. For more information about Markdown, please
visit John Gruber's website at http://www.daringfireball.net.

Ghostwriter provides a relaxing, distraction-free writing environment,
whether your masterpiece be that next blog post, your school paper,
or your novel.

%prep
%setup
%patch1 -p1

%build
%if_enabled qt5
%K5build -DQT_MAJOR_VERSION=5
%endif
%if_enabled qt6
%K6build -DQT_MAJOR_VERSION=6
%endif

%install
%if_enabled qt5
%K5install
%endif
%if_enabled qt6
%K6install
%endif
%find_lang %name --with-kde --all-name
%if_enabled qt5
%K5find_qtlang %name --all-name
%endif
%if_enabled qt6
%K6find_qtlang %name --all-name
%endif

%files -f %name.lang
%doc COPYING LICENSES/* CHANGELOG.md CONTRIBUTING.md README.md
%if_enabled qt5
%_K5bin/%rname
%_K5xdgapp/*%{rname}*.desktop
%_K5icon/hicolor/*/apps/%rname.*
%endif
%if_enabled qt6
%_K6bin/%rname
%_K6xdgapp/*%{rname}*.desktop
%_K6icon/hicolor/*/apps/%rname.*
%endif
%_datadir/metainfo/*%{rname}*.xml

%changelog
* Wed Apr 03 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.1-alt1
- new version

* Wed Apr 03 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Mon Mar 11 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.1.6-alt2
- NMU: build for LoongArch (use Qt6 here)

* Mon Dec 19 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version
- update URL and Source URL

* Sat Sep 10 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- new version 2.1.4 (with rpmrb script)

* Fri Feb 18 2022 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt2
- using not_qt5_qtwebengine_arches macro

* Mon Jan 24 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script)

* Sat Sep 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt2
- fix build with Qt 5.15+

* Sun Mar 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- initial build for ALT Sisyphus
