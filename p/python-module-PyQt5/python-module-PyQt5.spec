%define oname PyQt5

%def_with python3

Name: python-module-%oname
Version: 5.5
Release: alt1.1
Summary: Python bindings for Qt.
License: GPL
Group: Development/Python

%setup_python_module %oname

Source0: PyQt-gpl.tar
URL: http://www.riverbankcomputing.co.uk/software/pyqt

#BuildPreReq: %py_package_dependencies sip-devel >= 4.8.1
#BuildPreReq: %py_package_dependencies dbus-devel

# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: elfutils gcc-c++ libGL-devel libdbus-devel libgpg-error libgst-plugins1.0 libjson-c libqt5-bluetooth libqt5-clucene libqt5-core libqt5-dbus libqt5-designer libqt5-gui libqt5-help libqt5-location libqt5-multimedia libqt5-network libqt5-nfc libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-sensors libqt5-serialport libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-websockets libqt5-widgets libqt5-x11extras libqt5-xml libqt5-xmlpatterns libstdc++-devel pkg-config python-base python-devel python-module-dbus python-module-sip python-modules python-modules-compiler python-modules-logging python-modules-xml python3 python3-base python3-dev python3-module-sip qt5-base-devel qt5-declarative-devel rpm-build-gir
BuildRequires: python-module-dbus-devel python-module-sip-devel python3-module-dbus python3-module-sip-devel qt5-connectivity-devel qt5-location-devel qt5-multimedia-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel rpm-build-python3

#BuildRequires: gcc-c++ qt5-base-devel lout
#BuildPreReq: python-module-qscintilla2-qt5-devel libqscintilla2-qt5-devel
#BuildPreReq: libqscintilla2-qt5-devel
#BuildRequires: python-module-sip-devel python-devel
#BuildPreReq: python-module-dbus-devel libqt5-help qt5-multimedia-devel
#BuildPreReq: qt5-declarative-devel qt5-svg-devel qt5-webkit-devel
#BuildPreReq: qt5-xmlpatterns-devel qt5-tools-devel qt5-sensors-devel
#BuildPreReq: qt5-serialport-devel qt5-x11extras-devel qt5-location-devel
#BuildPreReq: qt5-connectivity-devel qt5-websockets-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-module-sip-devel python3-devel
#BuildPreReq: python3-module-dbus
%endif

%description
Python bindings for the Qt C++ class library.  Also includes a PyQt5 backend
code generator for Qt Designer.

%package -n python3-module-%oname
Summary: Python bindings for Qt.
Group: Development/Python3

%description -n python3-module-%oname
Python bindings for the Qt C++ class library.  Also includes a PyQt5 backend
code generator for Qt Designer.

%package -n python3-module-%oname-devel
Summary:  Sip files for python3-module-%oname
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-devel
Python bindings for the Qt C++ class library.  Also includes a PyQt5 backend
code generator for Qt Designer.

%package devel
Requires: %name = %version-%release
Summary:  Sip files for %name
BuildArch: noarch
Group: Development/Python
%py_package_provides %modulename-devel = %version-%release

%description devel
Sip files for PyQt to build extension

%package examples
Summary: PyQt5 examples
Group: Development/Python
BuildArch: noarch
Requires: %name
%py_package_provides %modulename-examples = %version-%release

%description examples
This package contains PyQt5 examples

%package doc
Summary: PyQt5 docs
Group: Development/Python
BuildArch: noarch
Requires: %name
%py_package_provides %modulename-examples = %version-%release

%description doc
This package contains PyQt5 docs

%prep
%setup -n PyQt-gpl
subst 's|/lib/libpython|/%_lib/libpython|g' configure.py
subst 's|/lib" |/%_lib" |g' configure.py
subst 's|#include <QTextStream>|#include <QTextStream>\n#define QT_SHARED\n|g' \
	configure.py
sed -i 's|@LIBDIR@|%_libdir|g' configure.py
find . -type f -name \*.pro -o -name '*.pro-in' |while read f; do
cat >> $f << 'E_O_F'
QMAKE_CFLAGS += %optflags %optflags_shared
QMAKE_CXXFLAGS += %optflags %optflags_shared
E_O_F
done

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -I$PWD/qpy/QtGui -I%_includedir/qt5/QtPrintSupport
export PATH=$PATH:%_qt5_bindir

echo 'yes' | python configure.py \
	--debug \
	--verbose \
	--assume-shared \
	-q %_qt5_bindir/qmake \
	-d %python_sitelibdir \
	-a --confirm-license \
	--qsci-api \
	CFLAGS+="%optflags" CXXFLAGS+="%optflags"
for i in $(find ./ -name Makefile); do
	sed -i 's|-Wl,-rpath,|-I|g' $i
done
%make_build

%if_with python3
pushd ../python3
echo 'yes' | python3 configure.py \
	--debug \
	--verbose \
	--assume-shared \
	-q %_qt5_bindir/qmake \
	-d %python3_sitelibdir \
	-a --confirm-license \
	--qsci-api \
	--sip=%_bindir/sip3 \
	--sip-incdir=%python3_includedir%_python3_abiflags \
	--sipdir=%_datadir/sip3/PyQt5 \
	--qsci-api-destdir=%_qt5_datadir/qsci3 \
	CFLAGS+="%optflags" CXXFLAGS+="%optflags"
for i in $(find ./ -name Makefile); do
	sed -i 's|-Wl,-rpath,|-I|g' $i
done
%make_build
popd
%endif

%install
%if_with python3
pushd ../python3
%makeinstall_std INSTALL_ROOT=%buildroot
rm -rf %buildroot%python3_sitelibdir/%oname/uic/port_v2
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%makeinstall_std INSTALL_ROOT=%buildroot
rm -rf %buildroot%python_sitelibdir/%oname/uic/port_v3

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

##wait ##
#install -d %buildroot/usr/share/sip/PyQt5/Qsci \
#	PyQt-x11-gpl/sip/QtGui

%files
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%_qt5_plugindir/*

%files devel
%dir %_datadir/sip
%_datadir/sip/*
%dir %_qt5_datadir
%_qt5_datadir/qsci

%files doc
%doc doc/*
%doc NEWS README

%files examples
%doc examples

%if_with python3
%files -n python3-module-%oname
%_bindir/*.py3
%python3_sitelibdir/*

%files -n python3-module-%oname-devel
%_datadir/sip3
%dir %_qt5_datadir
%_qt5_datadir/qsci3
%endif

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 5.5-alt1.1
- NMU: Use buildreq for BR.

* Mon Jul 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5-alt1
- Version 5.5

* Mon Jun 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.2-alt1
- Version 5.4.2

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.1-alt2
- Applied repocop's python-module-PyQt5-5.4.1-alt1.diff

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.1-alt1
- Version 5.4.1

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4-alt1
- Version 5.4

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.2-alt1
- Version 5.3.2

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.1-alt2
- Added module for Python 3

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.1-alt1
- Version 5.3.1

* Fri Jun 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt3
- Rebuilt with new SIP

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt2
- Built with qt5-websockets

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1
- Initial build for Sisyphus

