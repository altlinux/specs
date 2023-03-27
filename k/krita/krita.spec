
%define optflags_lto %nil
%def_disable python_bindings

%define sover 18
%define libkritacommand libkritacommand%sover
%define libkritaimpex libkritaimpex%sover
%define libkritalibkis libkritalibkis%sover
%define libkritalibkra libkritalibkra%sover
%define libkritaqml libkritaqml%sover
%define libkritawidgetutils libkritawidgetutils%sover
%define libkritametadata libkritametadata%sover
%define libkritaglobal libkritaglobal%sover
%define libkritaversion libkritaversion%sover
%define libkritabasicflakes libkritabasicflakes%sover
%define libkritastore libkritastore%sover
%define libkritaimage libkritaimage%sover
%define libkritalibbrush libkritalibbrush%sover
%define libkritawidgets libkritawidgets%sover
%define libkritaflake libkritaflake%sover
%define libkritaundo2 libkritaundo2%sover
%define libkritatextlayout libkritatextlayout%sover
%define libkritaui libkritaui%sover
%define libkritaplugin libkritaplugin%sover
%define libkritapsd libkritapsd%sover
%define libkritaodf libkritaodf%sover
%define libkritalibpaintop libkritalibpaintop%sover
%define libkritapigment libkritapigment%sover
%define libkritacolor libkritacolor%sover
%define libkritacolord libkritacolord%sover
%define libkritatext libkritatext%sover
%define libkritaqmicinterface libkritaqmicinterface%sover
%define libkritaresources libkritaresources%sover
%define libkritaresourcewidgets libkritaresourcewidgets%sover
%define libkritapsdutils libkritapsdutils%sover
%define libkritatiffpsd libkritatiffpsd%sover
%define libkritaexifcommon libkritaexifcommon%sover

Name: krita
Version: 5.1.5
Release: alt1
%K5init no_altplace

Group: Graphics
Summary: A creative sketching and painting application
Url: http://krita.org/
License: GPLv3

AutoReq: yes, nopython
AutoProv: yes, nopython nopython3
%add_python3_path %_libdir/krita-python-libs
%add_python3_path %_datadir/krita/pykrita
%add_python3_req_skip PyKrita pykrita
#Requires: kde5-kross-python
Requires: create-resources

Provides: calligra-krita = %EVR
Obsoletes: calligra-krita < %EVR

Source: krita-%version.tar
Patch1: alt-find-pyqt.patch
Patch2: alt-py3-syntax-error.patch
Patch3: alt-soname.patch

# Automatically added by buildreq on Thu Nov 16 2017 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules elfutils fontconfig gcc-c++ glibc-devel-static glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache ilmbase-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libgpg-error liblcms2-devel libpoppler-devel libpoppler1-qt5 libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel perl pkg-config python-base python-modules python3 python3-base python3-module-yieldfrom qt5-base-common qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: appstream boost-devel eigen3 extra-cmake-modules git-core kf5-karchive-devel kf5-kcrash-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kwindowsystem-devel libXres-devel libexiv2-devel libfftw3-devel libgomp-devel libgsl-devel libjpeg-devel libpng-devel libpoppler-qt5-devel libquadmath-devel libraw-devel libssl-devel libtiff-devel libxcbutil-devel openexr-devel python-module-google python3-dev python3-module-zope qt5-multimedia-devel qt5-svg-devel qt5-wayland-devel qt5-x11extras-devel rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-python3 rpm-build-kf5
BuildRequires: zlib-devel libssl-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-multimedia-devel qt5-svg-devel qt5-wayland-devel qt5-x11extras-devel
BuildRequires: python3-devel
%if_enabled python_bindings
BuildRequires: python3-module-PyQt5-devel python3-module-sip5
%endif
BuildRequires: eigen3 libfftw3-devel libgomp-devel libgsl-devel
BuildRequires: boost-devel boost-geometry-devel
#BuildRequires: libgif-devel
BuildRequires: quazip-qt5-devel
#BuildRequires: libquadmath-devel
BuildRequires: libopencolorio2.0-devel
BuildRequires: libXres-devel libxcbutil-devel
BuildRequires: libjpeg-devel libpng-devel libpoppler-qt5-devel libraw-devel libtiff-devel libwebp-devel
BuildRequires: libturbojpeg-devel pkgconfig(libopenjp2)
#BuildRequires: libheif-devel openexr-devel
BuildRequires: libexiv2-devel liblcms2-devel
#BuildRequires: libmypaint-devel
BuildRequires: kf5-karchive-devel kf5-kcrash-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kwindowsystem-devel

%description
Krita is a free and open source digital painting application.
It is for artists who want to create professional work from start to end.
Krita is used by comic book artists, illustrators, concept artists, matte
and texture painters and in the digital VFX industry.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Header files and libraries needed for %name development
%description devel
Header files and libraries needed for %name development

%package -n %libkritatext
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritatext17
%description -n %libkritatext
%name library.

%package -n %libkritacolord
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritacolord17
%description -n %libkritacolord
%name library.

%package -n %libkritacolor
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritacolor17
%description -n %libkritacolor
%name library.

%package -n %libkritapigment
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritapigment17
%description -n %libkritapigment
%name library.

%package -n %libkritalibpaintop
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritalibpaintop17
%description -n %libkritalibpaintop
%name library.

%package -n %libkritaodf
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaodf17
%description -n %libkritaodf
%name library.

%package -n %libkritapsd
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritapsd17
%description -n %libkritapsd
%name library.

%package -n %libkritaplugin
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaplugin17
%description -n %libkritaplugin
%name library.

%package -n %libkritaui
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaui17
%description -n %libkritaui
%name library.

%package -n %libkritatextlayout
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritatextlayout17
%description -n %libkritatextlayout
%name library.

%package -n %libkritaundo2
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaundo217
%description -n %libkritaundo2
%name library.

%package -n %libkritaflake
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaflake17
%description -n %libkritaflake
%name library.

%package -n %libkritawidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritawidgets17
%description -n %libkritawidgets
%name library.

%package -n %libkritalibbrush
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritalibbrush17
%description -n %libkritalibbrush
%name library

%package -n %libkritaimage
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaimage17
%description -n %libkritaimage
%name library

%package -n %libkritastore
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritastore17
%description -n %libkritastore
%name library

%package -n %libkritabasicflakes
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritabasicflakes17
%description -n %libkritabasicflakes
%name library

%package -n %libkritaversion
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaversion17
%description -n %libkritaversion
%name library

%package -n %libkritaglobal
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaglobal17
%description -n %libkritaglobal
%name library

%package -n %libkritawidgetutils
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritawidgetutils17
%description -n %libkritawidgetutils
%name library

%package -n %libkritacommand
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritacommand17
%description -n %libkritacommand
%name library

%package -n %libkritaimpex
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaimpex17
%description -n %libkritaimpex
%name library

%package -n %libkritalibkis
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritalibkis17
%description -n %libkritalibkis
%name library

%package -n %libkritalibkra
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritalibkra17
%description -n %libkritalibkra
%name library

%package -n %libkritaqml
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaqml17
%description -n %libkritaqml
%name library

%package -n %libkritametadata
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritametadata17
%description -n %libkritametadata
%name library

%package -n %libkritaresourcewidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaresourcewidgets17
%description -n %libkritaresourcewidgets
%name library

%package -n %libkritaresources
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaresources17
%description -n %libkritaresources
%name library

%package -n %libkritaqmicinterface
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritaqmicinterface17
%description -n %libkritaqmicinterface
%name library

%package -n %libkritapsdutils
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritapsdutils17
%description -n %libkritapsdutils
%name library

%package -n %libkritatiffpsd
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libkritatiffpsd17
%description -n %libkritatiffpsd
%name library

%package -n %libkritaexifcommon
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkritaexifcommon
%name library

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i 's|sipbuild|sipbuild5|' cmake/modules/FindSIP.py
sed -i 's|sipbuild|sipbuild5|' cmake/modules/sip-generate.py
%ifarch %arm
sed -i 's,HAVE_OCIO,0,' plugins/dockers/CMakeLists.txt
%endif

%build
%ifarch %arm
%add_optflags -DHAS_ONLY_OPENGL_ES=1
%endif
%ifarch ppc64 ppc64le
%add_optflags -DEIGEN_ALTIVEC_DISABLE_MMA
%endif
%K5build \
    -DRELEASE_BUILD=ON \
    -DFOUNDATION_BUILD=OFF \
    #

%install
%K5install
%K5install_move data color-schemes

# remove InitialPreference
for f in %buildroot/%_K5xdgapp/*.desktop ; do
    sed -i '/^InitialPreference=/d' $f
done

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc AUTHORS README*
%_K5icon/*/*/mimetypes/application-x-krita.*

%files
%config(noreplace) %_K5xdgconf/kritarc
%_K5bin/krita*
%_libdir/kritaplugins/
%if_enabled python_bindings
%_libdir/krita-python-libs/
%endif
%_K5qml/org/krita/
%_datadir/krita/
%_datadir/kritaplugins/
%_datadir/color/icc/krita/
#%_K5plug/krita/
%_K5xdgapp/*krita*.desktop
%_K5icon/*/*/apps/krita.*
%_K5data/color-schemes/*
%_datadir/metainfo/*krita*.xml

%files devel
%_K5link/lib*.so
#%_K5inc/krita/
#%_K5inc/*.h
%_includedir/*.h

%files -n %libkritaqmicinterface
%_libdir/libkritaqmicinterface.so.%sover
%_libdir/libkritaqmicinterface.so.*
%files -n %libkritaresources
%_libdir/libkritaresources.so.%sover
%_libdir/libkritaresources.so.*
%files -n %libkritaresourcewidgets
%_libdir/libkritaresourcewidgets.so.%sover
%_libdir/libkritaresourcewidgets.so.*
%files -n %libkritacommand
%_libdir/libkritacommand.so.%sover
%_libdir/libkritacommand.so.*
%files -n %libkritaimpex
%_libdir/libkritaimpex.so.%sover
%_libdir/libkritaimpex.so.*
%files -n %libkritalibkis
%_libdir/libkritalibkis.so.%sover
%_libdir/libkritalibkis.so.*
%files -n %libkritalibkra
%_libdir/libkritalibkra.so.%sover
%_libdir/libkritalibkra.so.*
%files -n %libkritaqml
%_libdir/libkritaqml.so.%sover
%_libdir/libkritaqml.so.*
%files -n %libkritacolord
%_libdir/libkritacolord.so.%sover
%_libdir/libkritacolord.so.*
%files -n %libkritacolor
%_libdir/libkritacolor.so.%sover
%_libdir/libkritacolor.so.*
%files -n %libkritapigment
%_libdir/libkritapigment.so.%sover
%_libdir/libkritapigment.so.*
%files -n %libkritalibpaintop
%_libdir/libkritalibpaintop.so.%sover
%_libdir/libkritalibpaintop.so.*
%files -n %libkritapsd
%_libdir/libkritapsd.so.%sover
%_libdir/libkritapsd.so.*
%files -n %libkritaplugin
%_libdir/libkritaplugin.so.%sover
%_libdir/libkritaplugin.so.*
%files -n %libkritaui
%_libdir/libkritaui.so.%sover
%_libdir/libkritaui.so.*
%files -n %libkritaflake
%_libdir/libkritaflake.so.%sover
%_libdir/libkritaflake.so.*
%files -n %libkritawidgets
%_libdir/libkritawidgets.so.%sover
%_libdir/libkritawidgets.so.*
%files -n %libkritalibbrush
%_libdir/libkritalibbrush.so.%sover
%_libdir/libkritalibbrush.so.*
%files -n %libkritaimage
%_libdir/libkritaimage.so.%sover
%_libdir/libkritaimage.so.*
%files -n %libkritastore
%_libdir/libkritastore.so.%sover
%_libdir/libkritastore.so.*
%files -n %libkritabasicflakes
%_libdir/libkritabasicflakes.so.%sover
%_libdir/libkritabasicflakes.so.*
%files -n %libkritaversion
%_libdir/libkritaversion.so.%sover
%_libdir/libkritaversion.so.*
%files -n %libkritaglobal
%_libdir/libkritaglobal.so.%sover
%_libdir/libkritaglobal.so.*
%files -n %libkritawidgetutils
%_libdir/libkritawidgetutils.so.%sover
%_libdir/libkritawidgetutils.so.*
%files -n %libkritametadata
%_libdir/libkritametadata.so.%sover
%_libdir/libkritametadata.so.*
%files -n %libkritapsdutils
%_libdir/libkritapsdutils.so.%sover
%_libdir/libkritapsdutils.so.*
%files -n %libkritatiffpsd
%_libdir/libkritatiffpsd.so.%sover
%_libdir/libkritatiffpsd.so.*
%files -n %libkritaexifcommon
%_libdir/libkritaexifcommon.so.%sover
%_libdir/libkritaexifcommon.so.*

%changelog
* Mon Mar 27 2023 Sergey V Turchin <zerg@altlinux.org> 5.1.5-alt1
- new version

* Mon Nov 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.1.3-alt1
- new version

* Mon Oct 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt4
- fix upgrade from previous version

* Fri Sep 02 2022 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt3
- update requires

* Mon Aug 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt2
- fix library packaging

* Tue Aug 23 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 5.1.0-alt1
- NMU:
      + new version
      + libkritapsdutils libkritatiffpsd added

* Thu Jul 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.0.8-alt1
- new version

* Tue Jul 05 2022 Sergey V Turchin <zerg@altlinux.org> 5.0.6-alt2
- update build options

* Tue May 24 2022 Sergey V Turchin <zerg@altlinux.org> 5.0.6-alt1
- new version

* Fri Jan 21 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.2-alt2
- Rebuilt with opencolorio 2.0

* Fri Jan 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.0.2-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 4.4.8-alt1
- new version

* Fri Jul 16 2021 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version (closes: 40461)

* Thu Jul 15 2021 Vitaly Lipatov <lav@altlinux.ru> 4.4.2-alt2
- NMU: fix build with SIP5

* Tue Feb 02 2021 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Nov 03 2020 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Mon Aug 31 2020 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- new version

* Fri Dec 27 2019 Sergey V Turchin <zerg@altlinux.org> 4.2.8.2-alt1
- new version

* Tue Oct 08 2019 Sergey V Turchin <zerg@altlinux.org> 4.2.7.1-alt1
- new version

* Mon Aug 12 2019 Sergey V Turchin <zerg@altlinux.org> 4.2.5-alt1
- new version

* Mon Jul 01 2019 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Fri Jun 21 2019 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt1
- new version (ALT#36818)

* Tue Mar 26 2019 Sergey V Turchin <zerg@altlinux.org> 4.1.8-alt1
- new version (ALT#36336)

* Thu Sep 13 2018 Sergey V Turchin <zerg@altlinux.org> 4.1.1-alt2
- fix to build witn new libraw

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 4.1.1-alt1
- new version

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.2-alt2
- NMU: rebuilt with boost-1.67.0

* Wed Nov 15 2017 Sergey V Turchin <zerg@altlinux.org> 3.3.2-alt1
- initial build
