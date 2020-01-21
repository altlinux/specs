%def_disable zeitgeist

Name: qt5-phonon-settings
Version: 4.11.1
Release: alt1
%K5init no_altplace

Group: Graphical desktop/KDE
Summary: Phonon settings tool
Url: http://phonon.kde.org/
License: LGPLv2+

#Source: ftp://ftp.kde.org/pub/kde/stable/%name/%version/%name-%version.tar.bz2
Source: phonon-settings-%version.tar

BuildRequires(pre): qt5-base-devel rpm-build-kf5
BuildRequires: qt5-tools-devel qt5-declarative-devel
BuildRequires: qt5-phonon-devel
BuildRequires: libEGL-devel libGL-devel
BuildRequires: cmake extra-cmake-modules
BuildRequires: libalsa-devel libpulseaudio-devel
%if_enabled zeitgeist
BuildRequires: libqzeitgeist-devel
%endif

%description
%{summary}.

%prep
%setup -n phonon-settings-%version


%build
%add_optflags %optflags_shared -UPIE -U__PIE__
#%add_optflags %optflags_shared
%K5cmake \
    -DSHARE_INSTALL_PREFIX:PATH=%_datadir \
    -DLOCALE_INSTALL_DIR:PATH=%_K5i18n \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt5_archdatadir \
    -DPHONON_INSTALL_QT_COMPAT_HEADERS:BOOL=ON \
    -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT:BOOL=ON \
    -DPHONON_BUILD_EXPERIMENTAL:BOOL=ON \
    -DPHONON_BUILD_DEMOS:BOOL=OFF \
    -DPHONON_BUILD_DESIGNER_PLUGIN:BOOL=ON \
    -DPHONON_BUILD_SETTINGS:BOOL=ON \
    -DPHONON_NO_CAPTURE:BOOL=OFF \
    #
#    -DINCLUDE_INSTALL_DIR:PATH=%_includedir/phonon4qt5 \

%K5make

%install
%K5install

rm -rf %buildroot/{%_includedir,%_datadir,%_K5link}
rm -rf %buildroot/%_libdir/{c,l,p,q}*

mkdir -p %buildroot/%_kf5_bin
mv %buildroot/%_bindir/phononsettings{,-5}
ln -s `relative %_bindir/phononsettings-5 %_kf5_bin/phononsettings` %buildroot/%_kf5_bin/phononsettings

%files
%_bindir/phononsettings-5
%_kf5_bin/phononsettings


%changelog
* Tue Jan 21 2020 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- initial build
