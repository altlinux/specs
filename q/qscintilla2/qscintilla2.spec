%def_with python
%def_without python-qt3
%def_without qt3
%def_with qt4
%def_with python3
%def_with python3qt5

Summary: QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class
%define oname qscintilla2
%define suff 13
Name: %oname
Version: 2.10.1
Release: alt5%ubt
License: GPL
Group: Development/KDE and QT

Source: qscintilla-gpl-%version.tar.gz
Patch1: %name-%version-alt-build.patch

Url: http://www.riverbankcomputing.co.uk/software/qscintilla/

%define libname lib%{oname}-%{suff}

BuildRequires(pre): rpm-build-ubt python-module-sip-devel
%define sipver2 %(rpm -q --qf '%%{VERSION}' python-module-sip)
BuildRequires: gcc-c++
%if_with qt3
BuildRequires: libqt3-devel python-module-qt-devel
%endif
%if_with qt4
Buildrequires: libqt4-devel
%endif
%if_with python
%if_with qt4
BuildRequires: python-module-PyQt4-devel
%endif
BuildRequires: python-module-PyQt5-devel
BuildRequires: python-module-sip-devel
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3 python3-module-sip-devel
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
BuildRequires: python3-devel python3-module-sip-devel
%if_with qt4
BuildPreReq: python3-module-PyQt4-devel
%endif
%endif
BuildRequires: chrpath qt5-base-devel
%if_with python3qt5
BuildRequires: python3-module-PyQt5-devel
%endif

%description
Qscintilla is a free source code editing component. It comes with complete
source code and a license that permits use in any free project or commercial
product. As well as features found in standard text editing components,
Scintilla includes features especially useful when editing and debugging
source code. These include support for syntax styling, error indicators, code
completion and call tips. The selection margin can contain markers like those
used in debuggers to indicate breakpoints and the current line. Styling
choices are more open than with many editors, allowing the use of proportional
fonts, bold and italics, multiple foreground and background colours and
multiple fonts.

%if_with qt3
%package -n %libname-qt3
Summary: QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class.
Group: Development/KDE and QT
Conflicts: libqscintilla
Provides: lib%oname-qt3 = %version-%release
Obsoletes: lib%oname-qt3
Obsoletes: lib%oname-5-qt3
Obsoletes: lib%oname-qt3-compat

%description -n %libname-qt3
Qscintilla is a free source code editing component. It comes with complete
source code and a license that permits use in any free project or commercial
product. As well as features found in standard text editing components,
Scintilla includes features especially useful when editing and debugging
source code. These include support for syntax styling, error indicators, code
completion and call tips. The selection margin can contain markers like those
used in debuggers to indicate breakpoints and the current line. Styling
choices are more open than with many editors, allowing the use of proportional
fonts, bold and italics, multiple foreground and background colours and
multiple fonts.
%endif

%if_with qt4
%package -n %libname-qt4
Summary: QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class.
Group: Development/KDE and QT
Provides: lib%oname-qt4 = %version-%release
Obsoletes: lib%oname-qt4
Obsoletes: lib%oname-5-qt4
Obsoletes: lib%oname-qt4-compat
Conflicts: lib%oname-11-qt4
Obsoletes: lib%oname-11-qt4
Conflicts: lib%oname-12-qt4
Obsoletes: lib%oname-12-qt4

%description -n %libname-qt4
Qscintilla is a free source code editing component. It comes with complete
source code and a license that permits use in any free project or commercial
product. As well as features found in standard text editing components,
Scintilla includes features especially useful when editing and debugging
source code. These include support for syntax styling, error indicators, code
completion and call tips. The selection margin can contain markers like those
used in debuggers to indicate breakpoints and the current line. Styling
choices are more open than with many editors, allowing the use of proportional
fonts, bold and italics, multiple foreground and background colours and
multiple fonts.
%endif

%package -n %libname-qt5
Summary: QScintilla is a port to Qt5 of Neil Hodgson's Scintilla C++ editor class.
Group: Development/KDE and QT
Provides: lib%oname-qt5 = %version-%release
Conflicts: lib%oname-11-qt5
Obsoletes: lib%oname-11-qt5
Conflicts: lib%oname-12-qt5
Obsoletes: lib%oname-12-qt5

%description -n %libname-qt5
Qscintilla is a free source code editing component. It comes with complete
source code and a license that permits use in any free project or commercial
product. As well as features found in standard text editing components,
Scintilla includes features especially useful when editing and debugging
source code. These include support for syntax styling, error indicators, code
completion and call tips. The selection margin can contain markers like those
used in debuggers to indicate breakpoints and the current line. Styling
choices are more open than with many editors, allowing the use of proportional
fonts, bold and italics, multiple foreground and background colours and
multiple fonts.

%if_with qt3
%package -n lib%oname-qt3-devel
Requires: %libname-qt3 = %version-%release
Requires: libqt3-devel
Summary: Header files for %oname
Group: Development/KDE and QT

%description -n lib%oname-qt3-devel
Header files for %oname
%endif

%if_with qt4
%package -n lib%oname-qt4-devel
Requires: %libname-qt4 = %version-%release
Requires: libqt4-devel
Summary: Header files for %oname
Group: Development/KDE and QT

%description -n lib%oname-qt4-devel
Header files for %oname
%endif

%package -n lib%oname-qt5-devel
Requires: %libname-qt5 = %version-%release
Requires: qt5-base-devel
Summary: Header files for %oname-qt5
Group: Development/KDE and QT

%description -n lib%oname-qt5-devel
Header files for %oname-qt5

%if_with qt3
%package -n lib%oname-qt3-designer
Requires: %libname-qt3 = %version-%release
Summary: QScintilla designer plugin
Group: Development/KDE and QT

%description -n lib%oname-qt3-designer
QScintillla designer plugin.
%endif

%if_with qt4
%package -n lib%oname-qt4-designer
Requires: %libname-qt4 = %version-%release
Summary: QScintilla designer plugin
Group: Development/KDE and QT

%description -n lib%oname-qt4-designer
QScintillla designer plugin.
%endif

%if_with python
%if_with qt4
%package -n python-module-%oname-qt4
Requires: %libname-qt4 = %version-%release
Summary: Python bindings for %oname
Group: Development/KDE and QT
Provides: lib%oname-qt4-python = %version-%release
Obsoletes: lib%oname-qt4-python
Requires: python-module-sip = %sipver2
%py_provides PyQt4.Qsci

%description -n python-module-%oname-qt4
Python bindings for %oname

%package -n python-module-%oname-qt4-devel
Requires: python-module-%oname-qt4 = %version-%release
Summary: Python bindings for %oname
Group: Development/KDE and QT
BuildArch: noarch
Provides: lib%oname-qt4-python-devel = %version-%release
Obsoletes: lib%oname-qt4-python-devel

%description -n python-module-%oname-qt4-devel
Devel files for Python bindings for %oname
%endif

%package -n python-module-%oname-qt5
Requires: %libname-qt5 = %version-%release
Summary: Python bindings for %oname-qt5
Group: Development/KDE and QT
Provides: lib%oname-qt5-python = %version-%release
Requires: python-module-sip = %sipver2
%py_provides PyQt5.Qsci

%description -n python-module-%oname-qt5
Python bindings for %oname-qt5

%package -n python-module-%oname-qt5-devel
Requires: python-module-%oname-qt5 = %version-%release
Summary: Python bindings for %oname-qt5
Group: Development/KDE and QT
BuildArch: noarch
Provides: lib%oname-qt5-python-devel = %version-%release

%description -n python-module-%oname-qt5-devel
Devel files for Python bindings for %oname

%if_with python3
%if_with qt4
%package -n python3-module-%oname-qt4
Requires: %libname-qt4 = %version-%release
Summary: Python 3 bindings for %oname
Group: Development/KDE and QT
Requires: python3-module-sip = %sipver3
%py3_provides PyQt4.Qsci

%description -n python3-module-%oname-qt4
Python bindings for %oname

%package -n python3-module-%oname-qt4-devel
Requires: python3-module-%oname-qt4 = %version-%release
Summary: Python 3 bindings for %oname
Group: Development/KDE and QT
BuildArch: noarch

%description -n python3-module-%oname-qt4-devel
Devel files for Python bindings for %oname
%endif

%if_with python3qt5
%package -n python3-module-%oname-qt5
Requires: %libname-qt5 = %version-%release
Summary: Python 3 bindings for %oname (Qt5)
Group: Development/KDE and QT
Requires: python3-module-sip = %sipver3
%py3_provides PyQt5.Qsci

%description -n python3-module-%oname-qt5
Python bindings for %oname

%package -n python3-module-%oname-qt5-devel
Requires: python3-module-%oname-qt5 = %version-%release
Summary: Python 3 bindings for %oname (Qt5)
Group: Development/KDE and QT
BuildArch: noarch

%description -n python3-module-%oname-qt5-devel
Devel files for Python bindings for %oname
%endif
%endif

%if_with python-qt3
%package -n python-module-%oname-qt3
Requires: %libname-qt3 = %version-%release
Summary: Python bindings for %oname
Group: Development/KDE and QT
Provides: lib%oname-qt3-python = %version-%release
Obsoletes: lib%oname-qt3-python

%description -n python-module-%oname-qt3
Python bindings for %oname

%package -n python-module-%oname-qt3-devel
Requires: python-module-%oname-qt3 = %version-%release
Summary: Python bindings for %oname
Group: Development/KDE and QT
BuildArch: noarch
Provides: lib%oname-qt3-python-devel = %version-%release
Obsoletes: lib%oname-qt3-python-devel

%description -n python-module-%oname-qt3-devel
Devel files for Python bindings for %oname
%endif
%endif

%package -n %libname-doc
Summary: Documentation for %oname
Group: Development/KDE and QT
BuildArch: noarch

%description -n %libname-doc
Documentation for %oname

%prep
%setup -n QScintilla-gpl-%version
%patch1 -p2
%if_with qt4
ln -s Qt4Qt5 Qt4
%endif
cp -fR Qt4Qt5 Qt5
%if_with qt4
cp -a Python Python-qt4
sed -i \
	-e "s|@Q5CFLAGS@||g" \
	-e "s|-lQt5PrintSupport -lQt5Widgets||g" \
	-e "s|@QSCINTILLALIB@|qscintilla2_qt4|g" \
	Python-qt4/configure.py
%endif
cp -a Python Python-qt5
Q5CFLAGS="$(pkg-config --cflags Qt5Widgets)"
Q5CFLAGS="$Q5CFLAGS $(pkg-config --cflags Qt5PrintSupport)"
sed -i \
	-e "s|@Q5CFLAGS@|$Q5CFLAGS|g" \
	-e "s|@QSCINTILLALIB@|qscintilla2_qt5|g" \
	Python-qt5/configure.py
%if_with python3
%if_with qt4
cp -fR Python-qt4 ../python3
%endif
%endif
%if_with python3qt5
cp -fR Python-qt5 ../python3qt5
%endif
%if_with python-qt3
mv Python Python-qt3
%endif

%build

forDebug() {
	# around of bug in /usr/lib/rpm/debugedit
	sed -i 's|\(QTDIR)\)/|\1|g' Makefile
}

# Qt3
%if_with qt3
pushd Qt3
qmake-qt3 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" qscintilla.pro
forDebug
%make_build
popd

# Designer for Qt3
pushd designer-Qt3
qmake-qt3 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" designer.pro
forDebug
%make_build
popd
%endif

# Qt4
%if_with qt4
pushd Qt4Qt5
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" qscintilla.pro
forDebug
%make_build
popd
%endif

# Qt5
pushd Qt5
qmake-qt5 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" qscintilla.pro
forDebug
%make_build
popd

# Designer for Qt4
%if_with qt4
pushd designer-Qt4Qt5
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" designer.pro
forDebug
%make_build
popd
%endif

%if_with python
# Python bindings
%if_with python-qt3
pushd Python-qt3
python configure.py -p 3 -n ../Qt3 -o ../Qt3
STR=`cat Makefile | grep "LFLAGS ="`
# add rpath for use qt3 %oname lib
sed -i "s:$STR:$STR,-rpath,%_qt3dir/lib:g" Makefile
%make
popd
%endif

cp -fR Qt4Qt5 ../
cp -fR Qt5 ../Qt5

# Python bindings for PyQt4
%if_with qt4
pushd Python-qt4
python configure.py --debug -n ../Qt4Qt5 -o ../Qt4Qt5 \
	--qmake=%_qt4dir/bin/qmake
%make_build
popd
%endif

# Python bindings for PyQt5
pushd Python-qt5
python configure.py --debug -n ../Qt5 -o ../Qt5 \
	--qmake=%_qt5_bindir/qmake \
	--pyqt=PyQt5
%make_build
popd

%if_with python3
%if_with qt4
OLDPATH=$PATH
export PATH=$PATH:%_qt4dir/bin
pushd ../python3
python3 configure.py \
	--apidir=%_datadir/qt4/qsci3 \
	--sip=%_bindir/sip3 \
	--pyqt-sipdir=%_datadir/sip3/PyQt4 \
	--debug -n ../Qt4Qt5 -o ../Qt4Qt5
sed -i \
	's|-lpython%_python3_version|-lpython%{_python3_version}m|g' \
	Makefile
%make_build
popd
export PATH=$OLDPATH
%endif
%endif

%if_with python3qt5
OLDPATH=$PATH
export PATH=$PATH:%_qt5_bindir
pushd ../python3qt5
python3 configure.py --debug -n ../Qt5 -o ../Qt5 \
	--apidir=%_datadir/qt5/qsci3 \
	--qmake=%_qt5_bindir/qmake \
	--sip=%_bindir/sip3 \
	--pyqt-sipdir=%_datadir/sip3/PyQt5 \
	--pyqt=PyQt5
sed -i \
	's|-lpython%_python3_version|-lpython%{_python3_version}m|g' \
	Makefile
%make_build
popd
export PATH=$OLDPATH
%endif

%endif

%install
%if_with python
# Python bindings
%if_with python-qt3
pushd Python-qt3
%makeinstall_std
mv %buildroot%python_sitelibdir/PyQt4/qsci.so %buildroot%python_sitelibdir
popd
%endif

# Python bindings for PyQt4
%if_with qt4
%if_with python3
pushd ../python3
mkdir -p %buildroot%python3_sitelibdir/PyQt4
%makeinstall_std INSTALL_ROOT=%buildroot
popd
%endif
pushd Python-qt4
%makeinstall_std INSTALL_ROOT=%buildroot
popd
%endif
# Python bindings for PyQt5
pushd Python-qt5
%makeinstall_std INSTALL_ROOT=%buildroot
popd
%if_with python3qt5
pushd ../python3qt5
mkdir -p %buildroot%python3_sitelibdir/PyQt5
%makeinstall_std INSTALL_ROOT=%buildroot
popd
%endif
%endif

%if_with qt4
mkdir -p %buildroot%python_sitelibdir/PyQt4
mkdir -p %buildroot%python3_sitelibdir/PyQt4
mkdir -p %buildroot%_includedir/qt4/Qsci
mkdir -p %buildroot%_libdir/qt4/{lib,translations,plugins/designer}
mkdir -p %buildroot%_datadir/qt4/qsci3/api/python
mkdir -p %buildroot%_datadir/qt4/qsci/api/python
%endif
mkdir -p %buildroot%python_sitelibdir/PyQt5
mkdir -p %buildroot%python3_sitelibdir/PyQt5
mkdir -p %buildroot%_includedir/qt5/Qsci
mkdir -p %buildroot%_libdir/qt5/{lib,translations,plugins/designer}
mkdir -p %buildroot%_qt5_libdatadir
mkdir -p %buildroot%_qt5_translationdir
mkdir -p %buildroot%_datadir/sip/qsci
mkdir -p %buildroot%_datadir/qt5/qsci/api/python
%if_with qt3
mkdir -p %buildroot%_qt3dir/include/Qsci
mkdir -p %buildroot%_libdir/qt3/{lib,translations,plugins/designer}
mkdir -p %buildroot%_datadir/qt3/qsci/api/python
mkdir -p %buildroot%_datadir/qt3/qsci3/api/python
%endif

# Qt3 library
%if_with qt3
install Qt3/lib%oname.so.*.*.* %buildroot%_qt3dir/lib
install Qt3/*.qm %buildroot%_qt3dir/translations
pushd %buildroot%_qt3dir/lib
ln -s lib%oname.so.*.*.* `ls lib%oname.so.*.*.* | sed s/\.[0-9]$//`
ln -s lib%oname.so.*.*.* `ls lib%oname.so.*.*.* | sed s/\.[0-9]\.[0-9]$//`
ln -s lib%oname.so.*.*.* `ls lib%oname.so.*.*.* | sed s/\.[0-9]\.[0-9]\.[0-9]$//`
popd
%endif

# Qt4 library
%if_with qt4
install Qt4Qt5/lib%{oname}_qt4.so.*.*.* %buildroot%_libdir
install Qt4Qt5/*.qm %buildroot%_qt4dir/translations
pushd %buildroot%_libdir
ln -s lib%{oname}_qt4.so.*.*.* `ls lib%{oname}_qt4.so.*.*.* | sed s/\.[0-9]*$//`
ln -s lib%{oname}_qt4.so.*.*.* `ls lib%{oname}_qt4.so.*.*.* | sed s/\.[0-9]*\.[0-9]*$//`
ln -s lib%{oname}_qt4.so.*.*.* `ls lib%{oname}_qt4.so.*.*.* | sed s/\.[0-9]*\.[0-9]*\.[0-9]*$//`
# NOTE: add a symlink for compatibility with older branches
ln -s lib%{oname}_qt4.so.*.*.* lib%{oname}.so
popd
pushd %buildroot%_qt4dir/lib
for libname in ../../lib%{oname}_qt4.*; do
ln -s $libname ./
done
popd
%endif

# Qt5 library
install Qt5/lib%{oname}_qt5.so.*.*.* %buildroot%_libdir
install Qt5/*.qm %buildroot%_qt5_translationdir
pushd %buildroot%_libdir
ln -s lib%{oname}_qt5.so.*.*.* `ls lib%{oname}_qt5.so.*.*.* | sed s/\.[0-9]*$//`
ln -s lib%{oname}_qt5.so.*.*.* `ls lib%{oname}_qt5.so.*.*.* | sed s/\.[0-9]*\.[0-9]*$//`
ln -s lib%{oname}_qt5.so.*.*.* `ls lib%{oname}_qt5.so.*.*.* | sed s/\.[0-9]*\.[0-9]*\.[0-9]*$//`
popd
pushd %buildroot%_qt5_libdatadir
for libname in ../../../%_lib/lib%{oname}_qt5.*; do
ln -s $libname ./
done
popd

# Qt3 designer
%if_with qt3
install designer-Qt3/libqscintillaplugin.so %buildroot%_qt3dir/plugins/designer
%endif

# Qt4 designer
%if_with qt4
install designer-Qt4Qt5/libqscintillaplugin.so %buildroot%_qt4dir/plugins/designer
%endif

# Qt3 headers
%if_with qt3
install -m644 Qt3/*.h %buildroot%_qt3dir/include
install -m644 Qt3/Qsci/*.h %buildroot%_qt3dir/include/Qsci
%endif

# Qt4 headers
%if_with qt4
install -m644 Qt4Qt5/*.h %buildroot%_includedir/qt4
install -m644 Qt4Qt5/Qsci/*.h %buildroot%_includedir/qt4/Qsci
%endif

# Qt5 headers
install -m644 Qt5/*.h %buildroot%_qt5_headerdir/
install -m644 Qt5/Qsci/*.h %buildroot%_qt5_headerdir/Qsci/

# docs
mkdir -p %buildroot%_docdir/%libname-%version
cp -a doc/Scintilla %buildroot%_docdir/%libname-%version
#cp -a doc/html-Qt3 %buildroot%_docdir/%libname-%version
cp -a doc/html-Qt4Qt5 %buildroot%_docdir/%libname-%version
cp ChangeLog NEWS README %buildroot%_docdir/%libname-%version

# Quick fix RPATH
%if_with qt4
chrpath -d %buildroot%python_sitelibdir/PyQt4/Qsci.so 
%endif

%if_with qt3
%files -n %libname-qt3
%_qt3dir/lib/*.so.*
%_qt3dir/translations/*
%endif

%if_with qt4
%files -n %libname-qt4
%_qt4dir/lib/*.so.*
%_libdir/*_qt4.so.*
%_qt4dir/translations/*
%endif

%files -n %libname-qt5
%_qt5_libdatadir/*.so.*
%_libdir/*_qt5.so.*
%_qt5_translationdir/*

%if_with qt3
%files -n lib%oname-qt3-devel
%_qt3dir/include/*.h
%_qt3dir/include/Qsci
%_qt3dir/lib/*.so
%endif

%if_with qt4
%files -n lib%oname-qt4-devel
%_includedir/qt4/*.h
%_includedir/qt4/Qsci
%_qt4dir/lib/*.so
%_libdir/*_qt4.so
%_libdir/lib%{oname}.so
%endif

%files -n lib%oname-qt5-devel
%_includedir/qt5/*.h
%_includedir/qt5/Qsci
%_qt5_libdatadir/*.so
%_libdir/*_qt5.so

%if_with qt3
%files -n lib%oname-qt3-designer
%_qt3dir/plugins/designer/*.so
%endif

%if_with qt4
%files -n lib%oname-qt4-designer
%_qt4dir/plugins/designer/*.so
%endif

%if_with python
%if_with python-qt3
%files -n python-module-%oname-qt3
%python_sitelibdir/qsci.so
%_qt3dir/qsci

%files -n python-module-%oname-qt3-devel
%_datadir/sip/qsci
%endif

%if_with qt4
%files -n python-module-%oname-qt4
%python_sitelibdir/PyQt4/Qsci.so
%python_sitelibdir/PyQt4/Qsci.pyi
%_datadir/qt4/qsci/api/python/*.api

%files -n python-module-%oname-qt4-devel
%_datadir/sip/PyQt4/Qsci
%endif

%files -n python-module-%oname-qt5
%python_sitelibdir/PyQt5/Qsci.so
%python_sitelibdir/PyQt5/Qsci.pyi
%_datadir/qt5/qsci/api/python/*.api

%files -n python-module-%oname-qt5-devel
%_datadir/sip/PyQt5/Qsci

%if_with python3
%if_with qt4
%files -n python3-module-%oname-qt4
%python3_sitelibdir/PyQt4/Qsci.so
%python3_sitelibdir/PyQt4/Qsci.pyi
%_datadir/qt4/qsci3/api/python/*.api

%files -n python3-module-%oname-qt4-devel
%_datadir/sip3/PyQt4/Qsci
%endif

%if_with python3qt5
%files -n python3-module-%oname-qt5
%python3_sitelibdir/PyQt5/Qsci.so
%python3_sitelibdir/PyQt5/Qsci.pyi
%_datadir/qt5/qsci3/api/python/*.api

%files -n python3-module-%oname-qt5-devel
%_datadir/sip3/PyQt5/Qsci
%endif
%endif

%endif

%files -n %libname-doc
%_docdir/%libname-%version

%changelog
* Thu Jan 25 2018 Andrew Savchenko <bircoph@altlinux.org> 2.10.1-alt5%ubt
- Make qt4 support optional (needed on e2k arch)

* Mon Nov 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.1-alt4%ubt
- Fix provides.

* Sun Nov 12 2017 Anton Midyukov <antohami@altlinux.org> 2.10.1-alt3%ubt
- Added missing files
- Fix missing provides (Closes: 34171)

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.1-alt2%ubt
- Added devel symlink for compatibility.
- Pinned dependency on sip because rebuild of sip requires rebuild of this package.

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.1-alt1%ubt
- Updated to upstream version 2.10.1.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.9-alt4.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Jul 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt4
- Rebuilt with new SIP

* Mon Jun 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt3
- Rebuilt with new SIP

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt2
- Added conflicts+obsoletes: libqscintilla2-11*

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1
- Version 2.9

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.4-alt2
- Rebuilt with new SIP

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.4-alt1
- Version 2.8.4

* Thu Aug 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3-alt4
- Avoid linking python-module-qscintilla2-qt4 with qt5 (ALT #30257)

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3-alt3
- Added module for Python 3 for Qt5

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3-alt2
- Added module for Python 3 for Qt4

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3-alt1
- Version 2.8.3

* Fri Jun 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.2-alt3
- Rebuilt with new SIP

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.2-alt2
- Added python module for Qt5

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.2-alt1
- Version 2.8.2
- Added library for Qt5

* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.1-alt1
- Version 2.8.1

* Sat Nov 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt1
- Version 2.8

* Tue Apr 16 2013 Andrey Cherepanov <cas@altlinux.org> 2.7-alt3.1
- Remove standard library path from RPATH

* Fri Mar 01 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7-alt3
- rebuilt without python3

* Thu Dec 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt2
- Rebuilt with updates python-module-sip

* Thu Dec 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1
- Version 2.7

* Mon Sep 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt1
- Version 2.6.2

* Tue May 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt2
- Added module for Python 3

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1
- Version 2.6.1

* Tue Jan 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6
- Disabled build for Qt3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.1-alt2.1
- Rebuild with Python-2.7

* Mon Sep 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2
- Added obsoletes on libqscintilla2-5-qt3 (ALT #26323)

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Version 2.5.1

* Sun Mar 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.6-alt1.2
- Rebuilt for debuginfo (thnx iv@)

* Mon Feb 07 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.6-alt1.1
- rebuilt

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.6-alt1
- Version 2.4.6

* Mon Dec 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt2
- Rebuilt with python-module-sip 4.11.2

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1.1
- Rebuilt for soname set-versions

* Sat Feb 06 2010 Boris Savelev <boris@altlinux.org> 2.4.2-alt1
- new version (2.4.2)

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt5.1
- Rebuilt with python 2.6

* Tue Sep 01 2009 Boris Savelev <boris@altlinux.org> 2.4-alt5
- add obsoletes for compat

* Mon Aug 31 2009 Boris Savelev <boris@altlinux.org> 2.4-alt4
- add obsoletes for python modules

* Sun Aug 30 2009 Boris Savelev <boris@altlinux.org> 2.4-alt3
- add obsoletes for libs (closes: #21302)

* Mon Aug 10 2009 Boris Savelev <boris@altlinux.org> 2.4-alt2
- remove python-module-%name-qt3

* Thu Aug 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.2
- Fixed linking with libqt3

* Mon Jul 20 2009 Boris Savelev <boris@altlinux.org> 2.4-alt1
- new version
- rename libs
- rename python modules

* Thu Feb 05 2009 Boris Savelev <boris@altlinux.org> 2.3.2-alt1
- new version (2.3.2)
- build python packages

* Tue Dec 16 2008 Boris Savelev <boris@altlinux.org> 2.3-alt5
- move %libname-qt3-devel headers to %_qt3dir/include
- add requires libqt3-devel for lib%name-qt3-devel and libqt4-devel for lib%name-qt4-devel

* Fri Dec 12 2008 Boris Savelev <boris@altlinux.org> 2.3-alt4
- remove python packages until fix problem with python-sip module

* Wed Oct 15 2008 Boris Savelev <boris@altlinux.org> 2.3-alt3
- add rpath to %libname-qt3-python (fix #17560)
- %libname-qt?-python-devel become noarch
- remove post and postun for lib%name-qt3
- clean spec

* Tue Oct 14 2008 Boris Savelev <boris@altlinux.org> 2.3-alt2
- doc become noarch

* Sat Oct 11 2008 Boris Savelev <boris@altlinux.org> 2.3-alt1
- new version

* Fri May 02 2008 Gennady Kovalev <gik@altlinux.ru> 2.2-alt2
- Version 2.2

* Fri Jan 04 2008 Gennady Kovalev <gik@altlinux.ru> 2-alt1.20080103
- Version 2, 20080103 snapshot
 + fixed python dependency
 + fixed RPATH bug during build

* Wed Jan 02 2008 Gennady Kovalev <gik@altlinux.ru> 2-alt2.20071223
- Fixed symlinks in lib

* Mon Dec 31 2007 Gennady Kovalev <gik@altlinux.ru> 2-alt1.20071223
- Version 2, 20071223 snapshot

* Wed Jan 11 2006 Ivan Fedorov <ns@altlinux.ru> 1.6-alt1
- 1.6

* Sat Mar 12 2005 Ivan Fedorov <ns@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Mon Feb 21 2005 Ivan Fedorov <ns@altlinux.ru> 1.5-alt1
- 1.5

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.4-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Sep 21 2004 Eugene V. Horohorin <genix@altlinux.org> 1.4-alt1
- new release
- spec clean up
- Rex Dieter's patch for qt-designer plugin: don't require an already installed
  qscintilla-devel

* Tue May 18 2004 Serge V. Sergeev <ssv@altlinux.ru> 1.3-alt1
- new release
- appropriate spec changes

* Thu Dec 11 2003 Serge V. Sergeev <ssv@altlinux.ru> 1.2-alt1
- new release

* Tue Jul 08 2003 Serge Sergeev <ssv@altlinux.ru> 1.1-alt1
- new release
- add define subver
- some minor changes

* Thu Apr 10 2003 Serge Sergeev <ssv@altlinux.ru> 0.4-alt0.1
- New release from snapshot

* Mon Dec 23 2002 Serge Sergeev <ssv@altlinux.ru> 0.3-alt1.2
- fixed install section

* Fri Dec 20 2002 Serge Sergeev <ssv@altlinux.ru> 0.3-alt1.1
- build from snapshot (corrects encodings)

* Tue Dec 17 2002 Serge Sergeev <ssv@altlinux.ru> 0.3-alt1
- Initial release

