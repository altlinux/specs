%define sover 8
%define libk3blib libk3blib%sover
%define libk3bdevice libk3bdevice%sover

%define req_permhelper /usr/sbin/usermod

%define req_std_burning /usr/bin/cdrecord /usr/bin/mkisofs /usr/bin/readcd cdrdao dvd+rw-tools cdrskin
%define req_std_common kde-runtime %req_permhelper
#define req_multimedia sox-play libsox-fmt-pulseaudio transcode vcdimager normalize lame flac mpc
%define req_multimedia sox-play libsox-fmt-pulseaudio normalize lame flac mpc
%define req_mini %req_std_burning %req_std_common
%define req_all %req_mini %req_multimedia

%def_disable musicbrainz

%define rname k3b
Name: %rname
Version: 24.08.1
Release: alt1
%K6init no_altplace

Group: Archiving/Cd burning
Summary: The CD Kreator (Complete set)
Summary(ru_RU.UTF-8): Программа записи CD (Полный набор)
URL: http://www.k3b.org/
License: GPL-2.0-or-later

Provides: k3b = %version-%release
Requires: %req_all
Provides: kde5-k3b = %EVR
Obsoletes: kde5-k3b < %EVR

Source0: %rname-%version.tar
Patch1: alt-permissions.patch
Patch2: alt-return-wodim.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-multimedia-devel qt6-declarative-devel
BuildRequires: libavdevice-devel libavformat-devel libpostproc-devel libswscale-devel
BuildRequires: libdvdread-devel libflac++-devel liblame-devel libmad-devel libmpcdec-devel
%if_enabled musicbrainz
BuildRequires: libmusicbrainz-devel
%endif
BuildRequires: libsamplerate-devel libsndfile-devel libtag-devel libvorbis-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel  kf6-kdoctools-devel
BuildRequires: kf6-kfilemetadata-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kde6-libkcddb-devel

%description
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording. 
This package contains all requiremnts and libraries necessary for full 
program functionality.
%description -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков. 
Этот пакет cодержит зависимости и библиотеки, необходимые для 
полнофункциональной работы программы.

%package mini
Summary: The CD Creator
Summary(ru_RU.UTF-8): Программа записи CD
Group: Archiving/Cd burning
Requires: %req_mini
Provides: kde5-k3b-mini = %EVR
Obsoletes: kde5-k3b-mini < %EVR
%description mini
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording.
Install 'k3b' package to get all of the program's features.
%description mini -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков.
Для полнофункцмональной работы Вы можете установить пакет 'k3b'.

%package devel
Summary: The CD Kreator (Development package.)
Summary(ru_RU.UTF-8): Программа записи CD (Пакет разработчика.)
Group: Development/KDE and QT
%description devel
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording. 
This package contains k3b development files and libraries.
%description devel -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков. 
Этот пакет содержит файлы и библиотеки, необходимые разработчику 
модулей k3b.

%package -n %libk3blib
Summary: %name library
Group: System/Libraries
Requires: kde-common
%description -n %libk3blib
%name library.

%package -n %libk3bdevice
Summary: %name library
Group: System/Libraries
Requires: kde-common
%description -n %libk3bdevice
%name library.

%prep
%setup -q -n %rname-%version
%patch1 -p1
#%patch2 -p1

%build
%K6build \
    -DK3B_ENABLE_MUSICBRAINZ:BOOL=%{?_enable_musicbrainz:ON}%{!?_enable_musicbrainz:OFF} \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data k3b solid konqsidebartng knsrcfiles

%find_lang --with-kde --all-name %name


%files -f %name.lang
%doc LICENSES/* README.txt FAQ.txt PERMISSIONS.txt
%_datadir/qlogging-categories6/*.*categories
%_K6bin/%rname
%_K6plug/k3b_plugins/
%_K6xdgapp/org.kde.%rname.desktop
%_K6data/solid/actions/%{rname}_*.desktop
%_K6data/%rname/
%_K6data/kio/servicemenus/*%{rname}*.desktop
%_K6data/knsrcfiles/*k3b*.knsrc
%_K6xdgmime/*%{rname}*.xml
%_K6notif/%rname.notifyrc
%_K6icon/hicolor/*/apps/%rname.*
%_K6icon/hicolor/*/mimetypes/application-x-%rname.*
%_datadir/metainfo/*k3b*.xml
#
%_K6plug/kf6/kio/videodvd.so
%_K6data/konqsidebartng/virtual_folders/services/videodvd.desktop
# permhelper
#%_K6dbus_sys_srv/org.kde.k3b.service
#%_K6libexecdir/kauth/k3bhelper
#%_K6dbus/system.d/org.kde.k3b.conf
#%_datadir/polkit-1/actions/org.kde.k3b.policy

%files -n %libk3blib
%_K6lib/libk3blib.so.%sover
%_K6lib/libk3blib.so.%sover.*

%files -n %libk3bdevice
%_K6lib/libk3bdevice.so.%sover
%_K6lib/libk3bdevice.so.%sover.*

%files devel
%_K6link/*.so
%_K6inc/k3b*.h


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

