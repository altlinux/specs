%define rname ghostwriter

Name: ghostwriter
Version: 26.04.2
Release: alt1
%K6init

Group: Editors
Summary: Cross-platform, aesthetic, distraction-free Markdown editor
License: GPL-3.0-or-later and CC-BY-SA-4.0 and BSD-2-Clause and BSD-3-Clause and LGPL-2.0-or-later and MIT and Apache-2.0
Url: https://invent.kde.org/office/ghostwriter

ExcludeArch: %not_qt6_qtwebengine_arches

# Requires one of pandoc or multimarkdown or cmark
#Requires: pandoc

# Source-url: https://github.com/KDE/ghostwriter/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Patch1: alt-crash.patch

BuildRequires(pre): rpm-macros-qt6 rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: qt6-declarative-devel qt6-5compat-devel qt6-tools-devel
BuildRequires: qt6-webengine-devel qt6-webchannel-devel qt6-svg-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kcoreaddons-devel kf6-kxmlgui-devel kf6-kconfigwidgets-devel kf6-kwidgetsaddons-devel kf6-sonnet-devel kf6-kcolorscheme-devel
BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib-devel
BuildRequires: libhunspell-devel

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
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%find_lang %name --with-kde --all-name
%K6find_qtlang %name --all-name

%files -f %name.lang
%doc COPYING LICENSES/* CHANGELOG.md CONTRIBUTING.md README.md
%_K6bin/%rname
%_K6xdgapp/*%{rname}*.desktop
%_K6icon/hicolor/*/apps/%rname.*
%_datadir/metainfo/*%{rname}*.xml


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

