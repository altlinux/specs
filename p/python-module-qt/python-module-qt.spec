Name: python-module-qt
Version: 3.18.2
Release: alt1.29855a84d8b6.2.1.1
%setup_python_module qt
Summary: Python bindings for Qt
License: GPLv2
Group: Development/Python
Url: http://www.riverbankcomputing.co.uk/software/pyqt/
Packager: Python Development Team <python@packages.altlinux.org>

# http://www.riverbankcomputing.co.uk/static/Downloads/PyQt3/PyQt-x11-gpl-%version.tar.gz
Source: PyQt-x11-gpl-%version.tar

#Requires: libqscintilla >= 1.4
%py_package_requires sip >= 4.4

Provides: PyQt
Obsoletes: PyQt
Provides: python-module-PyQt = %version-%release
Obsoletes: python-module-PyQt

BuildPreReq: %py_package_dependencies sip-devel >= 4.8

# Manually edited by morozov@
BuildRequires: gcc-c++ libGL-devel libXmu-devel libqt3-devel

%description
Python bindings for the Qt C++ class library.  Also includes a PyQt backend
code generator for Qt Designer.

%package devel
Requires: %name = %version-%release
Summary:  Sip files for %name
Group: Development/Python
BuildArch: noarch
Obsoletes: PyQt-devel
Obsoletes: python-module-PyQt-devel
Provides: PyQt-devel
Provides: python-module-PyQt-devel
%py_package_provides %modulename-devel = %version-%release

%description devel
Sip files for PyQt to build extension

%package examples
Summary: PyQt examples
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release
%py_package_provides %modulename-examples = %version-%release

%description examples
This package contains PyQt examples 


%prep
%setup -n PyQt-x11-gpl-%version

%build
export QTDIR=%_qt3dir
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
echo 'yes' | python configure.py -u -w -y qt-mt \
	-o %_libdir -d %python_sitelibdir
%make_build

%install
export QTDIR=%_qt3dir
%makeinstall_std

%files
%_bindir/pyuic
%_bindir/pylupdate
%python_sitelibdir/*
%doc NEWS README THANKS LICENSE doc/*.html

%files devel
%_datadir/sip

%files examples
%doc examples3

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.18.2-alt1.29855a84d8b6.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.18.2-alt1.29855a84d8b6.2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.18.2-alt1.29855a84d8b6.2
- Rebuilt for debuginfo

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.18.2-alt1.29855a84d8b6.1
- Set devel and examples packages as noarch

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.18.2-alt1.29855a84d8b6
- Version 3.18.2 (dev) (ALT #23446)

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.18.1-alt1.1
- Rebuilt with python 2.6

* Tue Jul 21 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.18.1-alt1
- Updated to 3.18.1

* Mon Dec 22 2008 Dmitry V. Levin <ldv@altlinux.org> 3.17.6-alt1
- Updated to 3.17.6.

* Sat Oct 11 2008 Vitaly Lipatov <lav@altlinux.ru> 3.17.4-alt2
- build with libqscintilla2
- cleanup spec, update Url
- enable SMP build

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 3.17.4-alt1
- 3.17.4

* Mon Sep 03 2007 Ivan Fedorov <ns@altlinux.org> 3.17.3-alt1
- 3.17.3

* Thu Nov 09 2006 Ivan Fedorov <ns@altlinux.ru> 3.17-alt1
- 3.17

* Sat Sep 09 2006 Ivan Fedorov <ns@altlinux.ru> 3.16-alt2
- fix x86_64 building

* Sun Apr 09 2006 Ivan Fedorov <ns@altlinux.ru> 3.16-alt1
- 3.16

* Mon Mar 06 2006 Alexey Morozov <almorozov@altlinux.org> 3.15.1-alt1.2
- NMU: removed unneeded xorg-x11-libs from BuildRequires
  and cleared other BuildDependencies
- cleared dependencies list a bit using rpm-build-python macros
- added path to libqscintilla.so

* Wed Dec 07 2005 Ivan Fedorov <ns@altlinux.ru> 3.15.1-alt1
- 3.15.1

* Thu Jun 16 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.14.1-alt1.1.1.1.1
- Rebuilt with libqt3.

* Thu Jun 02 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.14.1-alt1.1.1.1
- Rebuild with new libgnutls.so.11 .

* Tue Apr 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.14.1-alt1.1.1
- Rebuilt with libqt3

* Fri Mar 25 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.14.1-alt1.1
- Rebuilt with libqt3

* Sat Mar 12 2005 Ivan Fedorov <ns@altlinux.ru> 3.14.1-alt1
- 3.14.1
- rebuild with python 2.4

* Sat Mar 05 2005 Ivan Fedorov <ns@altlinux.ru> 3.14-alt2
- small fix spec

* Mon Feb 21 2005 Ivan Fedorov <ns@altlinux.ru> 3.14-alt1
- 3.14

* Fri Feb 04 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.13-alt4.1.1
- Rebuilt with qt3-3.3.4

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.13-alt4.1
- Rebuilt with libstdc++.so.6.

* Mon Dec 27 2004 Ivan Fedorov <ns@altlinux.ru> 3.13-alt4
- fixing requires (libqt3)

* Sun Dec 12 2004 Ivan Fedorov <ns@altlinux.ru> 3.13-alt3
- fix spec to be compatible with python policy

* Wed Oct 27 2004 Eugene V. Horohorin <genix@altlinux.ru> 3.13-alt2
- fix sip>=4.1 requires bug (#5323)

* Fri Sep 24 2004 Eugene V. Horohorin <genix@altlinux.org> 3.13-alt1
- new release

* Tue Sep 21 2004 Eugene V. Horohorin <genix@altlinux.ru> 3.12-alt2
- new buildrequires

* Thu Sep 02 2004 Eugene V. Horohorin <genix@altlinux.ru> 3.12-alt1
- new release
- removed macros (_findprov_lib_path)
- spec cleanup

* Fri Aug 01 2003 Serge Sergeev <ssv@altlinux.ru> 3.7-alt2
- added _findprov_lib_path macro to temporary solve problem with dependencies

* Tue Jul 08 2003 Serge Sergeev <ssv@altlinux.ru> 3.7-alt1
- new release

* Mon Apr 28 2003 Serge Sergeev <ssv@altlinux.ru> 3.6-alt1
- new release

* Thu Apr 10 2003 Serge Sergeev <ssv@altlinux.ru> 3.6-alt0.1
- New build from snapshot

* Fri Dec 20 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt2
- comment patch added ( this comment line needs for eric )
- add devel package ( need to build some extension of qt )

* Tue Dec 17 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt1
- build with qscintilla
- new release

* Mon Dec 16 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt0.1.20021205
- correct version

* Sat Dec 07 2002 Serge Sergeev <ssv@altlinux.ru> 20021205-alt1
- build from snapshot
- add documentation

* Tue Nov 05 2002 Serge Sergeev <ssv@altlinux.ru> 3.4-alt1
- new release

* Wed Sep 04 2002 Serge Sergeev <ssv@altlinux.ru> 3.3.2-alt1
- new release

* Thu Jul 25  2002 <sergeyssv@mail.ru>
- Initial release

