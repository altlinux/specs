%define _dkf5_bin %_prefix/lib/dkf5/bin

%def_disable zeitgeist
%def_disable settings

Name: dqt5-phonon
Version: 4.11.1
Release: alt1.dde.1
%K5init no_altplace

Group: Graphical desktop/KDE
Summary: KDE5 Multimedia Framework
Url: http://phonon.kde.org/
License: LGPLv2+

#Source: ftp://ftp.kde.org/pub/kde/stable/%name/%version/%name-%version.tar.bz2
Source: phonon-%version.tar

BuildRequires(pre): dqt5-base-devel rpm-build-kf5
BuildRequires: dqt5-tools-devel dqt5-declarative-devel
BuildRequires: libEGL-devel libGL-devel
BuildRequires: cmake extra-cmake-modules
BuildRequires: libalsa-devel libpulseaudio-devel
%if_enabled zeitgeist
BuildRequires: libqzeitgeist-devel
%endif

# find libraries
%add_findprov_lib_path %_dqt5_libdir

%description
Phonon is the KDE5 Multimedia Framework

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package

%package -n libphonon4dqt5experimental
Group: System/Libraries
Summary: Phonon library
Requires: %name-common
%description -n libphonon4dqt5experimental
Phonon library.

%package -n libphonon4dqt5
Group: System/Libraries
Summary: Phonon library
Requires: %name-common
%description -n libphonon4dqt5
Phonon library.

%package devel
Group: Development/KDE and QT
Summary: Header files and documentation for compiling Phonon applications
Requires: %name-common
%description devel
This package includes the header files you will need to compile applications
with Phonon.


%prep
%setup -n phonon-%version


%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
%add_optflags %optflags_shared -UPIE -U__PIE__
#%add_optflags %optflags_shared
%K5cmake \
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
    -DLIB_INSTALL_DIR:PATH=%_dqt5_libdir \
    -DSHARE_INSTALL_PREFIX:PATH=%_dqt5_prefix \
    -DPHONON_PLUGIN_PATH:PATH=%_dqt5_plugindir \
    -DPLUGIN_INSTALL_DIR:PATH=%_dqt5_plugindir \
    -DQT_PLUGIN_INSTALL_DIR:PATH=%_dqt5_plugindir \
    -DINCLUDE_INSTALL_DIR:PATH=%_dqt5_headerdir \
    -DPLUGIN_INSTALL_DIR:PATH=%_dqt5_archdatadir \
    -DECM_MKSPECS_INSTALL_DIR:PATH=%_dqt5_archdatadir/mkspecs/modules \
    -DLOCALE_INSTALL_DIR:PATH=%_K5i18n \
    -DPHONON_INSTALL_QT_COMPAT_HEADERS:BOOL=ON \
    -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT:BOOL=ON \
    -DPHONON_BUILD_EXPERIMENTAL:BOOL=ON \
    -DPHONON_BUILD_DEMOS:BOOL=OFF \
    -DPHONON_BUILD_DESIGNER_PLUGIN:BOOL=ON \
    -DPHONON_BUILD_SETTINGS:BOOL=ON \
    -DPHONON_NO_CAPTURE:BOOL=OFF \
    #
#    -DINCLUDE_INSTALL_DIR:PATH=%_dqt5_headerdir/phonon4qt5 \

%K5make

%install
%K5install

# ls -1 %%buildroot/%%_K5link/lib*.so 2>/dev/null |
# while read p
# do
#     [ -L "$p" ] || continue
#     f=`basename $(readlink "$p")`
#     l=`basename "$p"`
#     ln -sf "$f" "%%buildroot/%%_dqt5_libdir/$l"
#     rm -f "$p"
# done

mkdir -p %buildroot%_dqt5_plugindir/phonon4qt5_backend

mkdir -p %buildroot%_dkf5_bin
mv %buildroot%_bindir/phononsettings{,-dqt5}
ln -s `relative %_bindir/phononsettings-dqt5 %_dkf5_bin/phononsettings` %buildroot%_dkf5_bin/phononsettings

%K5find_qtlang libphonon_qt

%if_enabled settings
%files
%_bindir/phononsettings-dqt5
%_dkf5_bin/phononsettings
%endif

%files common -f libphonon_qt.lang

%files -n libphonon4dqt5experimental
%_dqt5_libdir/libphonon4qt5experimental.so.*

%files -n libphonon4dqt5
%dir %_dqt5_plugindir/phonon4qt5_backend/
%_dqt5_libdir/libphonon4qt5.so.*

%files devel
%_dqt5_headerdir/phonon4qt5
#%_dqt5_headerdir/KDE
%_dqt5_libdir/libphonon4qt5.so
%_dqt5_libdir/libphonon4qt5experimental.so
%dir %_dqt5_prefix/phonon4qt5/
%_dqt5_prefix/phonon4qt5/buildsystem/
%_dqt5_libdir/cmake/phonon4qt5/
%_dqt5_plugindir/designer/phononwidgets.so
%_dqt5_archdatadir/mkspecs/modules/qt_phonon4qt5.pri
%_dqt5_libdir/pkgconfig/phonon4qt5.pc

%changelog
* Thu May 30 2024 Leontiy Volodin <lvol@altlinux.org> 4.11.1-alt1.dde.1
- fork qt5 for separate deepin buildings (ALT #48138)

* Tue Jan 21 2020 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt2
- don't package settings tool

* Fri Jan 17 2020 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt2
- fix build requires

* Mon Jul 22 2019 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Mon Jun 17 2019 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Fri Apr 27 2018 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Wed Apr 05 2017 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt0.M80P.1
- build for M80P

* Mon Nov 14 2016 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt1
- new version

* Mon Apr 18 2016 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt4
- fix conflict with phonon debuginfo (ALT#31977)

* Mon Apr 04 2016 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt3
- fix to build with new Qt

* Thu Jul 02 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2
- rebuild with gcc5

* Fri Dec 19 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Tue Dec 02 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Tue Oct 21 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt3
- fix cmake configs

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix install paths

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Aug 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.80-alt0.M70P.1
- build for M70P

* Mon Aug 25 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.80-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- initial build
