
%define opencv_ver %{get_version libopencv-devel}

%add_findreq_skiplist %_K6data/digikam/utils/*

# Debian abandon libjasper
%def_disable jasper
%def_disable baloo
%def_enable mysql
%ifver_lt %opencv_ver 3
%def_disable opencv3
%else
%def_enable opencv3
%endif

%define rname digikam
%define label digiKam
Name: %rname
%define ver_major 8
%define ver_minor 3
%define ver_bugfix 0
Version: 8.4.0
Release: alt1
%K6init no_altplace

%define sover %version
%define libdigikamdatabase libdigikamdatabase%sover
%define libdigikamcore libdigikamcore%sover
%define libdigikamgui libdigikamgui%sover

Summary: digiKam is an advanced digital photo management application for linux
License: GPL-2.0-or-later
Group: Graphics
Url: http://www.digikam.org/

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-digikam = %EVR
Obsoletes: kde5-digikam < %EVR

Requires: qt6-sql-sqlite
Requires: %name-data = %version-%release
%if_enabled mysql
Requires: qt6-sql-mysql
%endif
# libs/dimg/filters/icc
Requires: icc-profiles
Requires: /usr/bin/exiftool

Source0: %rname-%version.tar
Source1: po.tar
Source2: doc.tar
Source3: doc-translated.tar
#
Source6: CMakeLists.txt
#
Source10: mysql_install_db
# ALT
Patch100: alt-libraw-aarch64.patch
Patch101: alt-own-mysql-install-db.patch
Patch102: fix-segfault-on-action-search.patch
Patch103: alt-find-sane.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-ifver rpm-macros-qt6-webengine libopencv-devel
BuildRequires: doxygen eigen3 extra-cmake-modules flex graphviz
BuildRequires: qt6-multimedia-devel qt6-networkauth-devel qt6-scxml-devel
BuildRequires: qt6-webengine-devel
BuildRequires: libx265-devel libheif-devel
BuildRequires: libXres-devel libexiv2-devel libexpat-devel libgomp-devel libgphoto2-devel libjpeg-devel libpng-devel
%{?_enable_jasper:BuildRequires: libjasper-devel}
BuildRequires: libavcodec-devel libavfilter-devel libavformat-devel libavdevice-devel libavutil-devel
BuildRequires: libswscale-devel libpostproc-devel libswresample-devel
BuildRequires: liblcms2-devel liblensfun-devel liblqr-devel libtiff-devel libusb-devel libtbb-devel libxml2-devel libxslt-devel
BuildRequires: libEGL-devel libGL-devel libGLU-devel
BuildRequires: libraw-devel
BuildRequires: libImageMagick-devel
BuildRequires: sqlite3 zlib-devel
#BuildRequires: marble-devel
BuildRequires: akonadi-devel akonadi-mime-devel kf6-kcalendarcore-devel kf6-kcontacts-devel kmime-devel kcalcore-devel
BuildRequires: kde6-libksane-devel akonadi-contacts-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-knotifications-devel
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-knotifyconfig-devel kf6-sonnet-devel kf6-threadweaver-devel
%if_enabled mysql
BuildRequires: libmysqlclient-devel
%endif
%if_enabled baloo
BuildRequires: kf6-kfilemetadata-devel kf6-baloo-devel
%endif
%if_enabled opencv3
BuildRequires: libopencv-devel-static
%endif

%description
DigiKam is an advanced digital photo management application for KDE.
Photos can be collected into albums which can be sorted chronologically,
by directory layout or by custom collections.
DigiKam also provides tagging functionality. Images can be tagged despite of
their position and digiKam provides fast and intuitive ways to browse them.
User comments and customized meta-information added to images, are stored
into a database and retrieved to make them available into the user interface.
As soon as the camera is plugged in digikam allows you to preview, download,
upload and delete images.
DigiKam also includes tools like Image Editor, to modify photos using plugins
such as red eye correction or Gamma correction, exif management,...
Light Table to make artistic photos and an external image editor such
as Showfoto.
DigiKam also uses KIPI plugins (KDE Image Plugin Interface) to increase
its functionalities.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-digikam-common = %EVR
Obsoletes: kde5-digikam-common < %EVR
%description common
%name common package

%package -n %libdigikamdatabase
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libdigikamdatabase8.3.0 < %EVR
%description -n %libdigikamdatabase
%name library

%package -n %libdigikamcore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libdigikamcore8.3.0 < %EVR
%description -n %libdigikamcore
%name library

%package -n %libdigikamgui
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libdigikamgui8.3.0 < %EVR
%description -n %libdigikamgui
%name library

%package data
Group: Graphics
Summary: A Photo Management Application for KDE
Requires: %name-common
BuildArch: noarch
Provides: kde5-digikam-data = %EVR
Obsoletes: kde5-digikam-data < %EVR
%description data
%label is an advanced digital photo management application for KDE.
Photos can be collected into albums which can be sorted chronologically,
by directory layout or by custom collections.
DigiKam also provides tagging functionality. Images can be tagged despite of
their position and digiKam provides fast and intuitive ways to browse them.
User comments and customized meta-information added to images, are stored
into a database and retrieved to make them available into the user interface.
As soon as the camera is plugged in digikam allows you to preview, download,
upload and delete images.
DigiKam also includes tools like Image Editor, to modify photos using plugins
such as red eye correction or Gamma correction, exif management,...
Light Table to make artistic photos and an external image editor such
as Showfoto.
%label also uses KIPI plugins (KDE Image Plugin Interface) to increase
its functionalities.

%package devel
Group: Development/KDE and QT
Summary: Development files for %label
Requires: %name-common
%description devel
Development files for %label.

%prep
%setup -n %rname-%version -c -a1 -a2 -a3
mv %rname-%version core
pushd core
%patch100 -p1
%patch101 -p1
%patch102 -p2
%patch103 -p1
popd
install -m 0644 %SOURCE6 ./
sed -i '/DIGIKAM_MAJOR_VERSION/s|@VERMAJOR@|%ver_major|' CMakeLists.txt
sed -i '/DIGIKAM_MINOR_VERSION/s|@VERMINOR@|%ver_minor|' CMakeLists.txt
sed -i '/DIGIKAM_PATCH_VERSION/s|@VERPATCH@|%ver_bugfix|' CMakeLists.txt
cat >>CMakeLists.txt <<__EOF__
    find_package(KF6 ${KF6_MIN_VERSION} REQUIRED COMPONENTS DocTools)
    ECM_OPTIONAL_ADD_SUBDIRECTORY(doc)
    ECM_OPTIONAL_ADD_SUBDIRECTORY(doc-translated)
__EOF__
# change double to qreal for casting on arm
#find -type f -name \*.cpp | \
#while read f ; do
#    sed -i 's|<double>|<qreal>|g' $f
#done
#find -type f -name \*.h | \
#while read f ; do
#    sed -i 's|<double>|<qreal>|g' $f
#done

#sed -i 's|add_subdirectory|ECM_OPTIONAL_ADD_SUBDIRECTORY|' doc-translated/CMakeLists.txt
#rm -rf doc-translated/showfoto
rm -rf doc-translated/sv/
sed -i '/add_subdirectory.*sv.*/d' doc-translated/CMakeLists.txt

%ifarch armh
sed -i '/set(HAVE_OPENGL TRUE)/ s,TRUE,FALSE,' core/CMakeLists.txt
%endif

%build
%K6build \
    -DBUILD_WITH_QT6=ON \
%ifarch ppc64le
    -DENABLE_FACESENGINE_DNN=OFF \
%endif
    -DENABLE_INTERNALMYSQL=%{?_enable_mysql:ON}%{!?_enable_mysql:OFF} \
    -DENABLE_MYSQLSUPPORT=%{?_enable_mysql:ON}%{!?_enable_mysql:OFF} \
    -DENABLE_KFILEMETADATASUPPORT=%{?_enable_baloo:ON}%{!?_enable_baloo:OFF} \
    -DENABLE_APPSTYLES=ON \
    -DBUILD_TESTING=OFF \
    -DENABLE_OPENCV3=%{?_enable_opencv3:ON}%{!?_enable_opencv3:OFF} \
    #

%install
%K6install
%K6install_move data kconf_update solid
install -m 0755 %SOURCE10 %buildroot/%_K6bin/digikam_mysql_install_db
%find_lang --with-kde %rname
%find_lang --with-kde --append --output=%rname.lang showfoto

mv %buildroot/%_datadir/kxmlgui{5,6}

%files common
%dir %_K6data/%rname/*
%dir %_K6data/showfoto/*

%files
%_K6bin/%rname
%_K6bin/digikam_mysql_install_db
%_K6bin/showfoto
%_K6bin/cleanup_digikamdb
%_K6bin/digitaglinktree
%_K6plug/digikam/
%_K6xdgapp/*.desktop
%_K6xmlgui/%rname/
%_K6xmlgui/showfoto/
%_K6notif/%rname.notifyrc
%_K6data/solid/actions/%rname-*.desktop
%_datadir/metainfo/*.xml

%files data -f %rname.lang
#%doc AUTHORS ChangeLog HACKING NEWS README* TODO
%_K6data/%rname/*
%_K6data/showfoto/*
%_K6icon/hicolor/*/apps/avplayer.*
%_K6icon/hicolor/*/apps/%rname.*
%_K6icon/hicolor/*/apps/dk-*.*
%_K6icon/hicolor/*/apps/showfoto.*
%_K6icon/hicolor/*/apps/panorama.*
%_K6icon/hicolor/*/apps/expoblending.*
%_K6icon/hicolor/*/actions/tag-*.*
%_K6icon/hicolor/*/actions/albumfolder-*.*
%_K6icon/hicolor/*/actions/tag.*
%_K6icon/hicolor/*/actions/overexposure.*
%_K6icon/hicolor/*/actions/underexposure.*

%files devel
%_K6link/*.so
%_includedir/digikam/
%_libdir/cmake/Digikam*/

%files -n %libdigikamdatabase
%_K6lib/libdigikamdatabase.so.%sover
%_K6lib/libdigikamdatabase.so.*
%files -n %libdigikamcore
%_K6lib/libdigikamcore.so.%sover
%_K6lib/libdigikamcore.so.*
%files -n %libdigikamgui
%_K6lib/libdigikamgui.so.%sover
%_K6lib/libdigikamgui.so.*


%changelog
* Wed Oct 09 2024 Sergey V Turchin <zerg@altlinux.org> 8.4.0-alt1
- initial build
