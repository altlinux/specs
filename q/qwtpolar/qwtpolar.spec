Name: qwtpolar
Version: 1.0.0
Release: alt1
Summary: A Qwt/Qt Polar Plot Library
License: QWT
Group: Development/KDE and QT
Url: http://qwtpolar.sourceforge.net/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://downloads.sourceforge.net/projects/qwtpolar/files/qwtpolar/%version/%name-%version.tar.bz2

# Automatically added by buildreq on Fri Jan 13 2012
# optimized out: libqt4-core libqt4-designer libqt4-gui libqt4-script libqt4-svg libqt4-xml libstdc++-devel phonon-devel
BuildRequires: gcc-c++ libqt4-devel libqwt6-devel >= 6.0.1-alt2

%description
The QwtPolar library contains classes for displaying values on a polar coordinate system.
It is an addon package for to the Qwt Library.

%package -n lib%name
Summary: A Qwt/Qt Polar Plot Library
Group: Development/KDE and QT

%description -n lib%name
Contains %name shared library

%package -n lib%name-devel
Summary: Header files for %name
Group: Development/KDE and QT
Requires: lib%name = %version-%release
Requires: libqwt6-devel >= 6.0.1-alt2

%description -n lib%name-devel
Header files for %name

%package -n lib%name-qt4-designer
Requires: lib%name = %version-%release
Summary: %name qt4 designer plugin
Group: Development/KDE and QT

%description -n lib%name-qt4-designer
%name designer plugin.

%prep
%setup -q
# install to buildroot
sed -i 's|/usr/local/%name-$$QWT_POLAR_VERSION|%prefix|g' qwtpolarconfig.pri
# install headers to libqwt-devel directory
sed -i 's|$${QWT_POLAR_INSTALL_PREFIX}/include|$${QWT_POLAR_INSTALL_PREFIX}/include/qwt|g' qwtpolarconfig.pri
# install doc
sed -i 's|$${QWT_POLAR_INSTALL_PREFIX}/doc|%_datadir/%name|g' qwtpolarconfig.pri
# install lib
sed -i 's|$${QWT_POLAR_INSTALL_PREFIX}/lib$|$${QWT_POLAR_INSTALL_PREFIX}/%_lib|g' qwtpolarconfig.pri
#install features
sed -i 's|$${QWT_POLAR_INSTALL_PREFIX}/features|$${QWT_POLAR_INSTALL_PREFIX}/include/qwt|g' qwtpolarconfig.pri
# install plugins
sed -i 's|$$\[QWT_POLAR_INSTALL_PLUGINS\]/designer$|%_qt4dir/plugins/designer|g' designer/designer.pro

%build
qmake-qt4 -set QMAKEFEATURES %_includedir/qwt
qmake-qt4
%make_build

cd designer
qmake-qt4
%make_build

%install
INSTALL_ROOT=%buildroot %makeinstall_std
#install -d %buildroot%_qt4dir/plugins/designer
#install -m644 designer/plugins/designer/*.so %buildroot%_qt4dir/plugins/designer

%files -n lib%name
%doc CHANGES COPYING
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/qwt/*.h
%_includedir/qwt/%name.prf
%_includedir/qwt/qwtpolarconfig.pri
%_libdir/*.so
%_datadir/%name


%files -n lib%name-qt4-designer
%_qt4dir/plugins/designer/*.so

%changelog
* Thu Jan 12 2012 Anatoly Lyutin <vostok@altlinux.org> 1.0.0-alt1
- new version

* Sat Sep 05 2009 Boris Savelev <boris@altlinux.org> 0.1.0-alt1
- new version (0.1.0) 

* Sun Nov 16 2008 Boris Savelev <boris@altlinux.org> 0.0.3-alt1
- initial build for Sisyphus

