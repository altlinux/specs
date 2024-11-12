%define rname kanagram

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Games/Educational
Summary: Word learning program
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kdeedu-data
Provides:  kde5-kanagram = %EVR
Obsoletes: kde5-kanagram < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-speech-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdeclarative-devel  kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-kpackage-devel
BuildRequires: kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kde6-libkeduvocdocument-devel

%description
Kanagram mixes up the letters of a word (creating an anagram),
and you have to guess what the mixed up word is. Kanagram features several
built-in word lists, hints, and a cheat feature which reveals the original
word. Kanagram also has a vocabulary editor, so you can make your own
vocabularies, and distribute them through Kanagram's KNewStuff download service.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kanagram knsrcfiles
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6bin/kanagram
%_K6xdgapp/org.kde.kanagram.desktop
%_K6data/kanagram/
%_K6data/knsrcfiles/*.knsrc
%_K6cfg/kanagram.kcfg
%_K6icon/*/*/apps/kanagram*.*
%_datadir/metainfo/*.xml


%changelog
* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

