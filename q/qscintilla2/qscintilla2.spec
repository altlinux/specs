%define _unpackaged_files_terminate_build 1

%define oname qscintilla2

Name: qscintilla2
Version: 2.13.1
Release: alt1.1

Summary: QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class

License: GPLv3
Group: Development/KDE and QT
Url: https://riverbankcomputing.com/software/qscintilla

# Source-url: https://www.riverbankcomputing.com/static/Downloads/QScintilla/%version/QScintilla_src-%version.zip
Source: QScintilla-%version.tar
#Patch1: %name-%version-alt-build.patch

%define libname lib%{oname}

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires(pre): rpm-macros-qt5
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: python3-module-PyQt5-devel
BuildRequires: python3-module-sip6 python3-module-PyQt-builder

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

%package -n %libname-qt5
Summary: QScintilla is a port to Qt5 of Neil Hodgson's Scintilla C++ editor class.
Group: Development/KDE and QT
Conflicts: lib%oname-11-qt5
Obsoletes: lib%oname-11-qt5
Conflicts: lib%oname-12-qt5
Obsoletes: lib%oname-12-qt5
Conflicts: lib%oname-13-qt5
Obsoletes: lib%oname-13-qt5
Conflicts: lib%oname-15-qt5
Obsoletes: lib%oname-15-qt5

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

%package -n lib%oname-qt5-devel
Requires: %libname-qt5 = %EVR
Requires: qt5-base-devel
Summary: Header files for %oname-qt5
Group: Development/KDE and QT

%description -n lib%oname-qt5-devel
Header files for %oname-qt5

%package -n lib%oname-qt5-designer
Requires: %libname-qt5 = %EVR
Summary: QScintilla designer plugin
Group: Development/KDE and QT

%description -n lib%oname-qt5-designer
QScintillla designer plugin.


%package -n python3-module-%oname-qt5
Requires: %libname-qt5 = %EVR
Summary: Python 3 bindings for %oname (Qt5)
Group: Development/KDE and QT
%py3_provides PyQt5.Qsci

%description -n python3-module-%oname-qt5
Python bindings for %oname

%package -n python3-module-%oname-qt5-devel
Requires: python3-module-%oname-qt5 = %EVR
Summary: Python 3 bindings for %oname (Qt5)
Group: Development/KDE and QT

%description -n python3-module-%oname-qt5-devel
Devel files for Python bindings for %oname


%package -n %libname-doc
Summary: Documentation for %oname
Group: Development/KDE and QT
BuildArch: noarch

%description -n %libname-doc
Documentation for %oname


%prep
%setup -n QScintilla-%version
#patch1 -p2
Q5CFLAGS="$(pkg-config --cflags Qt5Widgets)"
#Q5CFLAGS="$Q5CFLAGS $(pkg-config --cflags Qt5PrintSupport)"
#sed -i \
#	-e "s|@Q5CFLAGS@|$Q5CFLAGS|g" \
#	-e "s|@QSCINTILLALIB@|qscintilla2_qt5|g" \
#	Python/configure.py

%build

forDebug() {
	# around of bug in /usr/lib/rpm/debugedit
	sed -i 's|\(QTDIR)\)/|\1|g' Makefile
}

%ifarch %e2k
# bits/c++0x_warning.h
%add_optflags -std=gnu++11
%endif

pushd src
qmake-qt5 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" qscintilla.pro
forDebug
%make_build
popd

pushd designer
qmake-qt5 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags -I../src" designer.pro
forDebug
%make_build
popd

%ifarch %e2k
# Qsci: error while loading shared libraries: libqscintilla2_qt5.so.15
export LD_LIBRARY_PATH=$(pwd)/src
%endif
pushd Python
cp -v pyproject-qt5.toml pyproject.toml
sip-build \
    --no-make \
    --qmake=%_qt5_bindir/qmake \
    --qsci-features-dir ../src/features \
    --qsci-include-dir ../src \
    --qsci-library-dir ../src \
    --api-dir %_datadir/qt5/qsci3/api/python \

#sed -i \
#	's|-lpython%_python3_version|-lpython%{_python3_version}m|g' \
#	Makefile
%make_build -C build
popd

%install

# Python bindings for PyQt5
pushd Python/build
mkdir -p %buildroot%python3_sitelibdir/PyQt5
%makeinstall_std INSTALL_ROOT=%buildroot
popd

mkdir -p %buildroot%python3_sitelibdir/PyQt5
mkdir -p %buildroot%_includedir/qt5/Qsci
mkdir -p %buildroot%_qt5_libdatadir
mkdir -p %buildroot%_qt5_translationdir
mkdir -p %buildroot%_qt5_plugindir/designer
mkdir -p %buildroot%_datadir/sip/qsci
mkdir -p %buildroot%_datadir/qt5/qsci/api/python

# Qt5 library
install src/lib%{oname}_qt5.so.*.*.* %buildroot%_libdir
install src/*.qm %buildroot%_qt5_translationdir
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

# Qt5 designer
install -D designer/libqscintillaplugin.so %buildroot%_qt5_plugindir/designer

# Qt5 headers
install -m644 src/*.h %buildroot%_qt5_headerdir/
install -m644 src/Qsci/*.h %buildroot%_qt5_headerdir/Qsci/

# docs
mkdir -p %buildroot%_docdir/%libname-%version
cp -a doc/Scintilla %buildroot%_docdir/%libname-%version
cp -a doc/html %buildroot%_docdir/%libname-%version
cp ChangeLog NEWS LICENSE %buildroot%_docdir/%libname-%version

rm -rf %buildroot/%python3_sitelibdir/QScintilla-%version.dist-info

%files -n %libname-qt5
%_qt5_libdatadir/*.so.*
%_libdir/*_qt5.so.*
%_qt5_translationdir/*

%files -n lib%oname-qt5-devel
%_includedir/qt5/*.h
%_includedir/qt5/Qsci
%_qt5_libdatadir/*.so
%_libdir/*_qt5.so

%files -n lib%oname-qt5-designer
%_qt5_plugindir/designer/*.so

%files -n python3-module-%oname-qt5
%python3_sitelibdir/PyQt5/Qsci.so
#python3_sitelibdir/PyQt5/Qsci.pyi
%_datadir/qt5/qsci3/api/python/*.api

%files -n python3-module-%oname-qt5-devel
%dir %python3_sitelibdir/PyQt5/bindings/
%dir %python3_sitelibdir/PyQt5/bindings/Qsci/
%python3_sitelibdir/PyQt5/bindings/Qsci/*


%files -n %libname-doc
%_docdir/%libname-%version

%changelog
* Fri Jan 21 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.13.1-alt1.1
- fixed build for Elbrus

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 2.13.1-alt1
- new version 2.13.1 (with rpmrb script)
- build with sip6

* Sun Aug 01 2021 Vitaly Lipatov <lav@altlinux.ru> 2.11.5-alt4
- drop suffix from the library package name
- drop python2 and Qt4 support
- drop pinning to sip version

* Wed Jul 14 2021 Vitaly Lipatov <lav@altlinux.ru> 2.11.5-alt3
- use sip5 for python3 module, still use sip4 for python2 module

* Mon Jun 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.11.5-alt2
- Rebuilt without qt4.

* Mon Sep 07 2020 Vitaly Lipatov <lav@altlinux.ru> 2.11.5-alt1
- new version 2.11.5 (with rpmrb script)
- fix order of fields

* Fri Feb 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.11.4-alt1
- Updated to upstream version 2.11.4.

* Fri Jul 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.11.2-alt1
- Updated to upstream version 2.11.2.
- Removed disabled qt3 support.

* Thu Apr 25 2019 Michael Shigorin <mike@altlinux.org> 2.10.8-alt4
- fix build on %%e2k

* Thu Jan 17 2019 Michael Shigorin <mike@altlinux.org> 2.10.8-alt3
- Re-enabled qt4 knob by default: at least qgis version update results in FTBFS
  (full list: hgview juffed openscad qgis smokeqt sqliteman universalindentgui)

* Mon Jan 14 2019 Michael Shigorin <mike@altlinux.org> 2.10.8-alt2
- Disabled qt4 knob by default
- Fixed qt3 knob (and unescaped macro use in %%changelog)

* Sat Dec 01 2018 Alexander Makeenkov <amakeenk@altlinux.org> 2.10.8-alt1
- Updated to upstream version 2.10.8.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.1-alt5.S1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Feb 14 2018 Vitaly Lipatov <lav@altlinux.ru> 2.10.1-alt5.S1.1
- NMU: autorebuild with python-module-sip 4.9.7

* Thu Jan 25 2018 Andrew Savchenko <bircoph@altlinux.org> 2.10.1-alt5
- Make qt4 support optional (needed on e2k arch)

* Mon Nov 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.1-alt4
- Fix provides.

* Sun Nov 12 2017 Anton Midyukov <antohami@altlinux.org> 2.10.1-alt3
- Added missing files
- Fix missing provides (Closes: 34171)

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.1-alt2
- Added devel symlink for compatibility.
- Pinned dependency on sip because rebuild of sip requires rebuild of this package.

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.1-alt1
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
- move %libname-qt3-devel headers to %%_qt3dir/include
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

