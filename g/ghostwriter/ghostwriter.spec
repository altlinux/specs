Name: ghostwriter
Version: 2.1.6
Release: alt2

Summary: Cross-platform, aesthetic, distraction-free Markdown editor

License: GPLv3+ and CC-BY and CC-BY-SA and MPLv1.1 and BSD and LGPLv3 and MIT and ISC
Group: Graphics
Url: https://github.com/KDE/ghostwriter

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/KDE/ghostwriter/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Patch: ghostwriter-qt5.15-fix.patch

BuildRequires(pre): rpm-macros-qt5 rpm-macros-qt6

BuildRequires(pre): rpm-macros-qt5-webengine rpm-macros-qt6-webengine

# Requires QtWebEngine. Can be built either with Qt5 or Qt6.
ExclusiveArch: %qt5_qtwebengine_arches %qt6_qtwebengine_arches
%ifarch %qt5_qtwebengine_arches
# Use Qt5 on architectures where qt5-webengine is available.
%def_with qt5
%def_without qt6
%else
%ifarch %qt6_qtwebengine_arches
# Otherwise use Qt6 if qt6-webengine is available.
%def_with qt6
%def_without qt5
%endif
%endif

%if_with qt5
BuildRequires: qt5-base-devel libqt5-core libqt5-network libqt5-gui libqt5-dbus
BuildRequires: qt5-webengine-devel qt5-svg-devel qt5-tools
%endif
%if_with qt6
BuildRequires: qt6-base-devel qt6-5compat-devel qt6-tools-devel
BuildRequires: qt6-webengine-devel qt6-webchannel-devel qt6-svg-devel
%endif

#BuildRequires: cmake(Qt5LinguistTools)
#BuildRequires: cmake(Qt5XmlPatterns)
#BuildRequires: cmake(Qt5WebEngine)
#BuildRequires: cmake(Qt5X11Extras)
#BuildRequires: cmake(Qt5Network)
#BuildRequires: cmake(Qt5Core)
#BuildRequires: cmake(Qt5DBus)
#BuildRequires: cmake(Qt5Help)
#BuildRequires: cmake(Qt5Gui)
#BuildRequires: cmake(Qt5Svg)
#BuildRequires: cmake(Qt5Xml)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib-devel
BuildRequires: libhunspell-devel
BuildRequires: gcc-c++

#Requires: hicolor-icon-theme


%description
Ghostwriter is a text editor for Markdown, which is a plain text markup
format created by John Gruber. For more information about Markdown, please
visit John Gruber's website at http://www.daringfireball.net.

Ghostwriter provides a relaxing, distraction-free writing environment,
whether your masterpiece be that next blog post, your school paper,
or your novel.

%prep
%setup
#patch -p2
sed -i 's@appdata/@metainfo/@g' %name.pro

%build
%if_with qt5
%qmake_qt5 PREFIX=%prefix .
%else
%if_with qt6
%qmake_qt6 PREFIX=%prefix .
%endif
%endif
%make_build

%install
%make_install install INSTALL_ROOT=%buildroot
#find_lang %name --with-qt

%files
# -f %name.lang
%doc CHANGELOG.md CONTRIBUTING.md CREDITS.md README.md COPYING
%_bindir/%name
%_man1dir/%name.1*
 %_datadir/ghostwriter
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/metainfo/%name.appdata.xml

%changelog
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
