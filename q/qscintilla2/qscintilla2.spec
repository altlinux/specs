%def_with python
%def_without python-qt3
%def_without qt3
%def_with python3

Summary: QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class
Name: qscintilla2
Version: 2.6.1
Release: alt2
License: GPL
Group: Development/KDE and QT
Source: qscintilla-gpl-%version.tar.gz
Patch: qscintilla-2.4-alt-allinone.patch

Url: http://www.riverbankcomputing.co.uk/software/qscintilla/

%define suff 8
%define libname lib%{name}-%{suff}

# Automatically added by buildreq on Sun Oct 12 2008
BuildRequires: gcc-c++ libqt4-devel
%if_with qt3
BuildRequires: libqt3-devel
%endif
BuildRequires: python-module-PyQt4-devel python-module-qt-devel
BuildRequires: python-module-sip-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-sip-devel
BuildPreReq: python3-module-PyQt4-devel
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

%package -n %libname-qt3
Summary: QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class.
Group: Development/KDE and QT
Conflicts: libqscintilla
Provides: lib%name-qt3 = %version-%release
Obsoletes: lib%name-qt3
Obsoletes: lib%name-5-qt3
Obsoletes: lib%name-qt3-compat

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

%package -n %libname-qt4
Summary: QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class.
Group: Development/KDE and QT
Provides: lib%name-qt4 = %version-%release
Obsoletes: lib%name-qt4
Obsoletes: lib%name-5-qt4
Obsoletes: lib%name-qt4-compat

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

%package -n lib%name-qt3-devel
Requires: %libname-qt3 = %version-%release
Requires: libqt3-devel
Summary: Header files for %name
Group: Development/KDE and QT

%description -n lib%name-qt3-devel
Header files for %name

%package -n lib%name-qt4-devel
Requires: %libname-qt4 = %version-%release
Requires: libqt4-devel
Summary: Header files for %name
Group: Development/KDE and QT

%description -n lib%name-qt4-devel
Header files for %name

%package -n lib%name-qt3-designer
Requires: %libname-qt3 = %version-%release
Summary: QScintilla designer plugin
Group: Development/KDE and QT

%description -n lib%name-qt3-designer
QScintillla designer plugin.

%package -n lib%name-qt4-designer
Requires: %libname-qt4 = %version-%release
Summary: QScintilla designer plugin
Group: Development/KDE and QT

%description -n lib%name-qt4-designer
QScintillla designer plugin.

%if_with python
%package -n python-module-%name-qt4
Requires: %libname-qt4 = %version-%release
Summary: Python bindings for %name
Group: Development/KDE and QT
Provides: lib%name-qt4-python = %version-%release
Obsoletes: lib%name-qt4-python

%description -n python-module-%name-qt4
Python bindings for %name

%package -n python-module-%name-qt4-devel
Requires: python-module-%name-qt4 = %version-%release
Summary: Python bindings for %name
Group: Development/KDE and QT
BuildArch: noarch
Provides: lib%name-qt4-python-devel = %version-%release
Obsoletes: lib%name-qt4-python-devel

%description -n python-module-%name-qt4-devel
Devel files for Python bindings for %name

%if_with python3
%package -n python3-module-%name-qt4
Requires: %libname-qt4 = %version-%release
Summary: Python 3 bindings for %name
Group: Development/KDE and QT

%description -n python3-module-%name-qt4
Python bindings for %name

%package -n python3-module-%name-qt4-devel
Requires: python3-module-%name-qt4 = %version-%release
Summary: Python 3 bindings for %name
Group: Development/KDE and QT
BuildArch: noarch

%description -n python3-module-%name-qt4-devel
Devel files for Python bindings for %name
%endif

%if_with python-qt3
%package -n python-module-%name-qt3
Requires: %libname-qt3 = %version-%release
Summary: Python bindings for %name
Group: Development/KDE and QT
Provides: lib%name-qt3-python = %version-%release
Obsoletes: lib%name-qt3-python

%description -n python-module-%name-qt3
Python bindings for %name

%package -n python-module-%name-qt3-devel
Requires: python-module-%name-qt3 = %version-%release
Summary: Python bindings for %name
Group: Development/KDE and QT
BuildArch: noarch
Provides: lib%name-qt3-python-devel = %version-%release
Obsoletes: lib%name-qt3-python-devel

%description -n python-module-%name-qt3-devel
Devel files for Python bindings for %name
%endif
%endif

%package -n %libname-doc
Summary: Documentation for %name
Group: Development/KDE and QT
BuildArch: noarch

%description -n %libname-doc
Documentation for %name

%prep
%setup -n QScintilla-gpl-%version
%patch0 -p2
cp -a Python Python-qt4
%if_with python3
cp -fR Python-qt4 ../python3
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
pushd Qt4
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" qscintilla.pro
forDebug
%make_build
popd

# Designer for Qt4
pushd designer-Qt4
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" designer.pro
forDebug
%make_build
popd

%if_with python
# Python bindings
%if_with python-qt3
pushd Python-qt3
python configure.py -p 3 -n ../Qt3 -o ../Qt3
STR=`cat Makefile | grep "LFLAGS ="`
# add rpath for use qt3 %name lib
sed -i "s:$STR:$STR,-rpath,%_qt3dir/lib:g" Makefile
%make
popd
%endif

cp -fR Qt4 ../

# Python bindings for PyQt4
pushd Python-qt4
python configure.py --debug -p 4 -n ../Qt4 -o ../Qt4
%make_build
popd

%if_with python3
pushd ../python3
python3 configure.py \
	--apidir=%_datadir/qt4/qsci3 \
	--sipdir=%_datadir/sip3/PyQt4 \
	--debug -p 4 -n ../Qt4 -o ../Qt4
sed -i \
	's|-lpython%_python3_version|-lpython%{_python3_version}mu|g' \
	Makefile
%make_build
popd
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
%if_with python3
pushd ../python3
mkdir -p %buildroot%python3_sitelibdir/PyQt4
%makeinstall_std
popd
%endif
pushd Python-qt4
%makeinstall_std
popd
%endif

mkdir -p %buildroot%python_sitelibdir/PyQt4
mkdir -p %buildroot%python3_sitelibdir/PyQt4
mkdir -p %buildroot%_includedir/qt4/Qsci
mkdir -p %buildroot%_qt3dir/include/Qsci
mkdir -p %buildroot%_libdir/{qt3,qt4}/{lib,translations,plugins/designer}
mkdir -p %buildroot%_datadir/sip/qsci
mkdir -p %buildroot%_datadir/{qt3,qt4}/qsci/api/python
mkdir -p %buildroot%_datadir/{qt3,qt4}/qsci3/api/python

# Qt3 library
%if_with qt3
install Qt3/lib%name.so.*.*.* %buildroot%_qt3dir/lib
install Qt3/*.qm %buildroot%_qt3dir/translations
pushd %buildroot%_qt3dir/lib
ln -s lib%name.so.*.*.* `ls lib%name.so.*.*.* | sed s/\.[0-9]$//`
ln -s lib%name.so.*.*.* `ls lib%name.so.*.*.* | sed s/\.[0-9]\.[0-9]$//`
ln -s lib%name.so.*.*.* `ls lib%name.so.*.*.* | sed s/\.[0-9]\.[0-9]\.[0-9]$//`
popd
%endif

# Qt4 library
install Qt4/lib%name.so.*.*.* %buildroot%_libdir
install Qt4/*.qm %buildroot%_qt4dir/translations
pushd %buildroot%_libdir
ln -s lib%name.so.*.*.* `ls lib%name.so.*.*.* | sed s/\.[0-9]$//`
ln -s lib%name.so.*.*.* `ls lib%name.so.*.*.* | sed s/\.[0-9]\.[0-9]$//`
ln -s lib%name.so.*.*.* `ls lib%name.so.*.*.* | sed s/\.[0-9]\.[0-9]\.[0-9]$//`
popd
pushd %buildroot%_qt4dir/lib
for libname in ../../lib%name.*; do
ln -s $libname ./
done
popd

# Qt3 designer
%if_with qt3
install designer-Qt3/libqscintillaplugin.so %buildroot%_qt3dir/plugins/designer
%endif

# Qt4 designer
install designer-Qt4/libqscintillaplugin.so %buildroot%_qt4dir/plugins/designer

# Qt3 headers
%if_with qt3
install -m644 Qt3/*.h %buildroot%_qt3dir/include
install -m644 Qt3/Qsci/*.h %buildroot%_qt3dir/include/Qsci
%endif

# Qt4 headers
install -m644 Qt4/*.h %buildroot%_includedir/qt4
install -m644 Qt4/Qsci/*.h %buildroot%_includedir/qt4/Qsci

# docs
mkdir -p %buildroot%_docdir/%libname-%version
cp -a doc/Scintilla %buildroot%_docdir/%libname-%version
cp -a doc/html-Qt3 %buildroot%_docdir/%libname-%version
cp -a doc/html-Qt4 %buildroot%_docdir/%libname-%version

%if_with qt3
%files -n %libname-qt3
%_qt3dir/lib/*.so.*
%_qt3dir/translations/*
%endif

%files -n %libname-qt4
%_qt4dir/lib/*.so.*
%_libdir/*.so.*
%_qt4dir/translations/*

%if_with qt3
%files -n lib%name-qt3-devel
%_qt3dir/include/*.h
%_qt3dir/include/Qsci
%_qt3dir/lib/*.so
%endif

%files -n lib%name-qt4-devel
%_includedir/qt4/*.h
%_includedir/qt4/Qsci
%_qt4dir/lib/*.so
%_libdir/*.so

%if_with qt3
%files -n lib%name-qt3-designer
%_qt3dir/plugins/designer/*.so
%endif

%files -n lib%name-qt4-designer
%_qt4dir/plugins/designer/*.so

%if_with python
%if_with python-qt3
%files -n python-module-%name-qt3
%python_sitelibdir/qsci.so
%_qt3dir/qsci

%files -n python-module-%name-qt3-devel
%_datadir/sip/qsci
%endif

%files -n python-module-%name-qt4
%python_sitelibdir/PyQt4/Qsci.so
%_datadir/qt4/qsci/api/python/*.api

%files -n python-module-%name-qt4-devel
%_datadir/sip/PyQt4/Qsci

%if_with python3
%files -n python3-module-%name-qt4
%python3_sitelibdir/PyQt4/Qsci.so
%_datadir/qt4/qsci3/api/python/*.api

%files -n python3-module-%name-qt4-devel
%_datadir/sip3/PyQt4/Qsci
%endif

%endif

%files -n %libname-doc
%_docdir/%libname-%version

%changelog
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

