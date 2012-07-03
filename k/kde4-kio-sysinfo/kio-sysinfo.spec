%define __kde4_alternate_placement 1

%define rname kio-sysinfo
%ifdef __kde4_alternate_placement
Name: kde4-%rname
%else
Name: %rname
%endif
%define major 2
%define minor 0
%define bugfix %nil

%if "%bugfix" == "%nil"
Version: %major.%minor
%else
Version: %major.%minor.%bugfix
%endif
Release: alt4.1

Group: Graphical desktop/KDE
Summary: KIO-Slave to show system information
Url: http://www.kde.org/
License: GPL

Requires: kde4libs >= %{get_version kde4libs}

%ifdef __kde4_alternate_placement
%else
Provides: kde4-kio-sysinfo = %version-%release
Obsoletes: kde4-kio-sysinfo < %version-%release
%endif


Source: sysinfo-%version.tar.gz
Patch1: sysinfo-2.0-altlinux.patch

# Automatically added by buildreq on Mon Mar 30 2009 (-bi)
#BuildRequires: gcc-c++ kde4base-workspace-core kde4libs-devel libGL-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libhwinfo-devel libqt3-devel libxkbfile-devel rpm-build-ruby xorg-xf86vidmodeproto-devel
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ kde4base-workspace-devel libhwinfo-devel

%description
KIO-Slave to show system information


%prep
%setup -q -n sysinfo-%version
%patch1 -p0

if ! grep -qe '^add_subdirectory([[:space:]]*po[[:space:]]*)' CMakeLists.txt
then
cat >> CMakeLists.txt <<__EOF__
find_package(Msgfmt REQUIRED)
find_package(Gettext REQUIRED)
add_subdirectory( po )
__EOF__
fi

pushd po
for f in *.po
do
    NAME=$(echo "$f"| sed -e 's|\..*||')
    echo "add_subdirectory( $NAME )" >> CMakeLists.txt
    mkdir $NAME
    mv $f $NAME/kio_sysinfo.po
    echo "GETTEXT_PROCESS_PO_FILES( $NAME ALL INSTALL_DESTINATION \${LOCALE_INSTALL_DIR} kio_sysinfo.po )" >$NAME/CMakeLists.txt
done
popd


%build
%K4cmake -DSYSINFO_DISTRO:STRING=altlinux
%K4make


%install
%K4install
%K4find_lang --with-kde kio_sysinfo


%files -f kio_sysinfo.lang
%_K4lib/libksysinfopart.so
%_K4lib/kio_sysinfo.so
%_K4apps/sysinfo/
%__kde4_xdg_apps/kfmclient_sysinfo.desktop
%_K4xdg_mime/x-sysinfo.xml
%_K4srv/sysinfo.protocol
%_K4srv/ksysinfopart.desktop


%changelog
* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt4.1
- Rebuilt with hwinfo 18.5

* Mon Sep 21 2009 Sergey V Turchin <zerg@altlinux.org> 2.0-alt4
- update to svn r1026324

* Thu Aug 06 2009 Sergey V Turchin <zerg@altlinux.org> 2.0-alt3
- fix paths to startup khelpcenter and systemsettings

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 2.0-alt2
- fix compile

* Tue Mar 31 2009 Sergey V Turchin <zerg@altlinux.org> 2.0-alt0.M50.1
- built for M50

* Mon Mar 30 2009 Sergey V Turchin <zerg at altlinux dot org> 2.0-alt1
- initial specfile
