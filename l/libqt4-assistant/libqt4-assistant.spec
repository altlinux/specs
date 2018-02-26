%define Qtname Qt4

Name: libqt4-assistant
Version: 4.6.3
Release: alt10.2

Group: System/Libraries
Summary: %Qtname old help system support library
Url: http://qt.nokia.com/
License: GPLv3 / LGPLv2.1

Source: %name-%version.tar
Packager: Sergey V Turchin <zerg@altlinux.org>

BuildRequires(pre): libqt4-devel
BuildRequires: gcc-c++

%description
%Qtname old help system support library

%package devel
Summary: %name development files
Group: Development/KDE and QT
Requires: %name = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on old %Qtname help system


%prep
%setup -q
find -type f -name \*.pro | \
while read f; do
    echo "QMAKE_CXXFLAGS += \$\$(RPM_OPT_FLAGS)" >> $f
    pushd `dirname $f`
    qmake-qt4 `basename $f`
    popd
done


%build
find -type f -name Makefile | \
while read f; do
%make_build -C `dirname $f`
done


%install
find -type f -name Makefile | \
while read f; do
%make install -C `dirname $f` INSTALL_ROOT=%buildroot
done
mkdir -p %buildroot/%_pkgconfigdir/
mv %buildroot/%_libdir/QtAssistantClient.pc %buildroot/%_pkgconfigdir/
sed -i "s|^prefix=.*|prefix=%_prefix|" %buildroot/%_pkgconfigdir/QtAssistantClient.pc
sed -i "s|^libdir=.*|libdir=%_libdir|" %buildroot/%_pkgconfigdir/QtAssistantClient.pc


%files
%_qt4dir/bin/assistant_adp
%_libdir/libQtAssistantClient.so.*

%files devel
%_libdir/libQtAssistantClient.so
%_includedir/qt4/QtAssistant
%_pkgconfigdir/QtAssistantClient.pc

%changelog
* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.3-alt10.2
- Rebuilt for debuginfo

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.3-alt10.1
- Rebuilt for soname set-versions

* Thu Jul 22 2010 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt10
- initial specfile
