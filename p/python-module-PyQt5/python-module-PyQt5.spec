%define oname PyQt5

Name: python-module-%oname
Version: 5.3.1
Release: alt1
Summary: Python bindings for Qt.
License: GPL
Group: Development/Python

%setup_python_module %oname

Source0: PyQt-gpl.tar
URL: http://www.riverbankcomputing.co.uk/software/pyqt

BuildPreReq: %py_package_dependencies sip-devel >= 4.8.1
BuildPreReq: %py_package_dependencies dbus-devel

BuildRequires: gcc-c++ qt5-base-devel lout
#BuildPreReq: python-module-qscintilla2-qt5-devel libqscintilla2-qt5-devel
BuildPreReq: libqscintilla2-qt5-devel
BuildRequires: python-module-sip-devel python-devel
BuildPreReq: python-module-dbus-devel libqt5-help qt5-multimedia-devel
BuildPreReq: qt5-declarative-devel qt5-svg-devel qt5-webkit-devel
BuildPreReq: qt5-xmlpatterns-devel qt5-tools-devel qt5-sensors-devel
BuildPreReq: qt5-serialport-devel qt5-x11extras-devel qt5-location-devel
BuildPreReq: qt5-connectivity-devel qt5-websockets-devel

%description
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
find . -type f -name \*.pro -o -name '*.pro-in' |while read f; do
cat >> $f << 'E_O_F'
QMAKE_CFLAGS += %optflags %optflags_shared
QMAKE_CXXFLAGS += %optflags %optflags_shared
E_O_F
done

%build
#export QT4DIR=%_qt5dir
%add_optflags -I$PWD/qpy/QtGui
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

%install
%makeinstall_std INSTALL_ROOT=%buildroot
rm -rf %buildroot%python_sitelibdir/%oname/uic/port_v3

##wait ##
#install -d %buildroot/usr/share/sip/PyQt5/Qsci \
#	PyQt-x11-gpl/sip/QtGui

%files
%_bindir/*
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

%changelog
* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.1-alt1
- Version 5.3.1

* Fri Jun 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt3
- Rebuilt with new SIP

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt2
- Built with qt5-websockets

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1
- Initial build for Sisyphus

