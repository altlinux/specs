%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: kaichat
Version: 0.7.0
Release: alt2

Summary: Chat interface for AI models such as ollama
License: CC0-1.0 AND LGPL-2.0-or-later AND MIT AND GPL-2.0-or-later AND BSD-3-Clause
Group: Graphical desktop/KDE
Url: https://invent.kde.org/utilities/kaichat

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6TextToSpeech)

BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-sonnet-devel
BuildRequires: kf6-kstatusnotifieritem-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-purpose-devel
BuildRequires: kf6-ktextaddons-devel >= 1.9.0

Requires: plasma6-breeze
Requires: icon-theme-breeze
Requires: kf6-ktextaddons
Requires: libkaichatlibs = %EVR

%description
KAIChat allows to chat with AI (local ollama, network service).

KAIChat supports the following features:

* Export chat as Json/Text/Markdown
* Increase/Decrease global font by using CTRL++/CTRL+- shortcut

The functionality much extended by installing kaichat-addons package.

%package -n libkaichatlibs
Group: System/Libraries
Summary: libraries for %name

%description -n libkaichatlibs
This package contains libraries for %name.

%prep
%setup
sed -i "s|Categories=.*|Categories=Qt;KDE;Science;ArtificialIntelligence;|" src/data/org.kde.kaichat.desktop

%build
%K6build

%install
%K6install

%find_lang %name --with-kde

%files -f %name.lang
%doc README.md
%_K6bin/kaichat
%_K6xdgapp/org.kde.kaichat.desktop
%_K6icon/hicolor/16x16/apps/kaichat.png
%_K6icon/hicolor/22x22/apps/kaichat.png
%_K6icon/hicolor/24x24/apps/kaichat.png
%_K6icon/hicolor/32x32/apps/kaichat.png
%_K6icon/hicolor/48x48/apps/kaichat.png
%_K6icon/hicolor/scalable/apps/kaichat.svg
%_K6data/knotifications6/kaichat.notifyrc
%_K6data/metainfo/org.kde.kaichat.appdata.xml
%_K6data/qlogging-categories6/kaichat.categories

%files -n libkaichatlibs
%_K6lib/libkaichatcore.so.0*
%_K6lib/libkaichatwidgets.so.0*
%_K6lib/qt6/plugins/autogeneratetext/textplugins/kaichat_sharetextplugin.so
%_K6lib/qt6/plugins/autogeneratetext/textplugins/kaichat_webshortcuttextplugin.so
%_K6lib/qt6/plugins/autogeneratetext/toolplugins/textautogeneratetext_currentdatetimeplugin.so

%changelog
* Thu Jun 11 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.0-alt2
- Moved libraries to libkaichatlibs package (closes: #59500).

* Thu May 21 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.0-alt1
- New version 0.7.0.
- Enable build on riscv64 and loongarch64.

* Wed Feb 04 2026 Nikolay Strelkov <snk@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus
