%def_disable zeitgeist
%def_enable settings
%define _K5link %_libdir

Name: qt6-phonon
Version: 4.12.0
Release: alt1
%K5init no_altplace

Group: Graphical desktop/KDE
Summary: KDE5 Multimedia Framework
Url: http://phonon.kde.org/
License: LGPL-2.0-or-later

Conflicts: qt5-phonon-settings

#Source: ftp://ftp.kde.org/pub/kde/stable/%name/%version/%name-%version.tar.bz2
Source: phonon-%version.tar

BuildRequires(pre): qt6-base-devel rpm-build-kf5
BuildRequires: qt6-tools-devel qt6-declarative-devel qt6-5compat-devel
BuildRequires: libEGL-devel libGL-devel
BuildRequires: cmake extra-cmake-modules
BuildRequires: glib2-devel libpulseaudio-devel
%if_enabled zeitgeist
BuildRequires: libqzeitgeist-devel
%endif

%description
Phonon is the KDE5 Multimedia Framework

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt6-base-common
%description common
%name common package

%package -n libphonon4qt6experimental
Group: System/Libraries
Summary: Phonon library
Requires: %name-common
%description -n libphonon4qt6experimental
Phonon library.

%package -n libphonon4qt6
Group: System/Libraries
Summary: Phonon library
Requires: %name-common
%description -n libphonon4qt6
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
%add_optflags %optflags_shared
# -UPIE -U__PIE__
%K5cmake \
    -DSHARE_INSTALL_PREFIX:PATH=%_datadir \
    -DLOCALE_INSTALL_DIR:PATH=%_K5i18n \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt6_archdatadir \
    -DPHONON_INSTALL_QT_COMPAT_HEADERS:BOOL=ON \
    -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT:BOOL=ON \
    -DPHONON_BUILD_EXPERIMENTAL:BOOL=ON \
    -DPHONON_BUILD_QT5:BOOL=OFF \
    -DPHONON_BUILD_QT6:BOOL=ON \
    -DPHONON_BUILD_DESIGNER_PLUGIN:BOOL=ON \
    -DPHONON_BUILD_SETTINGS:BOOL=ON \
    -DPHONON_NO_CAPTURE:BOOL=OFF \
    #
%K5make

%install
%K5install
mkdir -p %buildroot/%_qt6_plugindir/phonon4qt6_backend

%K5find_qtlang --all-name libphonon_qt

%if_enabled settings
%files
%_bindir/phononsettings
%endif

%files common -f libphonon_qt.lang

%files -n libphonon4qt6experimental
%_libdir/libphonon4qt6experimental.so.*

%files -n libphonon4qt6
%dir %_qt6_plugindir/phonon4qt6_backend/
%_libdir/libphonon4qt6.so.*

%files devel
%_includedir/phonon4qt6
%_libdir/libphonon4qt6.so
%_libdir/libphonon4qt6experimental.so
%_libdir/cmake/phonon4qt6/
%_qt6_plugindir/designer/phonon4qt6widgets.so
%_pkgconfigdir/phonon4qt6.pc

%changelog
* Thu May 02 2024 Sergey V Turchin <zerg@altlinux.org> 4.12.0-alt1
- initial build
