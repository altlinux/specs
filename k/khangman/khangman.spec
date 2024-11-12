%define rname khangman

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Games/Educational
Summary: Classical hangman game
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kdeedu-data
Provides:  kde5-khangman = %EVR
Obsoletes: kde5-khangman < %EVR

Source: %rname-%version.tar
Source10: ru.txt
Patch1: alt-ru-keys.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-svg-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdeclarative-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-ki18n-devel kf6-kio-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel
BuildRequires: kf6-kpackage-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kde6-libkeduvocdocument-devel

%description
KHangman is the classical hangman game. The child should guess a word
letter by letter. At each miss, the picture of a hangman appears. After
10 tries, if the word is not guessed, the game is over and the answer
is displayed.

%prep
%setup -n %rname-%version
%patch1 -p1
mkdir -p languages/ru/
cat <<__EOF__ >languages/ru/CMakeLists.txt
install( FILES ru.txt  DESTINATION \${DATA_INSTALL_DIR}/khangman )
__EOF__
install -m 0644 %SOURCE10 languages/ru/
echo 'add_subdirectory(ru)' >> languages/CMakeLists.txt

%build
%K6build

%install
%K6install
%K6install_move data khangman
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6bin/khangman
%_K6data/khangman/
%_K6cfg/khangman.kcfg
%_K6xdgapp/org.kde.khangman.desktop
%_K6icon/*/*/apps/khangman*.*
%_datadir/metainfo/*.xml
%_K6data/knsrcfiles/khangman.knsrc


%changelog
* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

