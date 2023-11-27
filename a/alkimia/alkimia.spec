%define lib_name libalkimia5

%ifarch %qt5_qtwebengine_arches
%def_enable qtwebengine
%else
%def_disable qtwebengine
%endif

Name:    alkimia
Version: 8.1.2
Release: alt3.1

Summary: Alkimia is the infrastructure for common storage and business logic that will be used by all financial applications in KDE
License: LGPLv2+
Group:	 Office
URL:     http://community.kde.org/Alkimia/libalkimia
# Download from https://download.kde.org/stable/alkimia/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: extra-cmake-modules qt5-tools-devel-static
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%endif
BuildRequires: libgmp_cxx-devel
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-plasma-framework-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: mpir-devel
BuildRequires: doxygen

Requires: lib%name = %version-%release

%description
Alkimia is the infrastructure for common storage and business logic that
will be used by all financial applications in KDE. The target is to
share financial related information over application bounderies.

%package -n lib%name
Summary: A library with common classes and functionality used by finance applications for the KDE SC
Group:   System/Libraries

%description -n lib%name
libalkimia is a library with common classes and functionality used by
finance applications for the KDE SC. Currently it supports a common
class to represent monetary values with arbitrary precision.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: lib%name = %version-%release
Requires: mpir-devel

%description -n lib%name-devel
Headers and other files for develop with %name.

%prep
%setup -q

%build
%K5init no_altplace
%K5build -DCMAKE_SKIP_RPATH=1 \
         -DBUILD_WITH_WEBKIT=OFF \
%if_enabled qtwebengine
         -DBUILD_WITH_WEBENGINE=ON \
%else
         -DBUILD_WITH_WEBENGINE=OFF \
%endif
         -DAPPDATA_INSTALL_DIR=%_datadir

%install
%K5install
%K5install_move data knsrcfiles
%find_lang alkimia --all

%files -f alkimia.lang
%doc README.md
%_K5bin/onlinequoteseditor*
%_K5qml/org/kde/alkimia
%_K5xdgapp/*.desktop
%_K5icon/hicolor/*/apps/onlinequoteseditor*
%_datadir/metainfo/*.appdata.xml
%_datadir/kf5/plasma/plasmoids/org.wincak.foreigncurrencies2
%_K5data/knsrcfiles/*.knsrc
%_K5srv/*.desktop

%files -n lib%name
%_libdir/%lib_name.so.*

%files -n lib%name-devel
%dir %_includedir/alkimia
%_includedir/alkimia/*
%_K5link/%lib_name.so
%_pkgconfigdir/%lib_name.pc
%_libdir/cmake/LibAlkimia*

%changelog
* Mon Nov 27 2023 Ivan A. Melnikov <iv@altlinux.org> 8.1.2-alt3.1
- NMU: Use rpm-macros-qt5-webengine (fixes build on loongarch64).

* Fri Oct 27 2023 Andrey Cherepanov <cas@altlinux.org> 8.1.2-alt3
- Fixed build (ALT #48214) (thanks zerg@).

* Thu Oct 26 2023 Andrey Cherepanov <cas@altlinux.org> 8.1.2-alt2
- FTBFS: fixed desktop and plasmoid location.

* Thu Sep 21 2023 Andrey Cherepanov <cas@altlinux.org> 8.1.2-alt1
- New version.

* Sun Jul 10 2022 Andrey Cherepanov <cas@altlinux.org> 8.1.1-alt1
- New version.

* Thu Jan 27 2022 Sergey V Turchin <zerg@altlinux.org> 8.1.0-alt3
- build without qtwebengine on ppc64le and e2k

* Fri Jul 16 2021 Andrey Cherepanov <cas@altlinux.org> 8.1.0-alt2
- FTBFS: do not package service file.

* Tue Jul 06 2021 Andrey Cherepanov <cas@altlinux.org> 8.1.0-alt1
- New version.

* Fri Jul 02 2021 Andrey Cherepanov <cas@altlinux.org> 8.0.4-alt2
- Build with qt5-webengine (thanks zerg@).

* Wed Dec 23 2020 Andrey Cherepanov <cas@altlinux.org> 8.0.4-alt1
- New version.
- Rename source package to upstream name alkimia.

* Wed Jan 29 2020 Andrey Cherepanov <cas@altlinux.org> 8.0.3-alt1
- New version.

* Thu Oct 10 2019 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 8.0.1-alt1
- New version.

* Mon Apr 16 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt1
- New version.

* Mon Mar 19 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.1-alt1
- New version.

* Fri Feb 16 2018 Andrey Cherepanov <cas@altlinux.org> 7.0-alt1
- New version.

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1.1
- Rebuilt with gmp 5.0.5

* Thu Feb 09 2012 Andrey Cherepanov <cas@altlinux.org> 4.3.2-alt1
- New version 4.3.2

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- Initial build in Sisyphus

