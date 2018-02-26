%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname mayavi
Name:           Mayavi
Version:        4.1.1
Release:        alt2.git20120411
Summary:        Scientific data 3-dimensional visualizer

Group:          Graphics
License:        BSD and EPL and LGPLv2+ and LGPLv3+
URL:            http://code.enthought.com/projects/mayavi/
# https://github.com/enthought/mayavi.git
Source:         %name-%version.tar.gz
Source1:        Mayavi.desktop
Source2:        tvtk_doc.desktop
# Removes already generated tvtk class zip file
# https://svn.enthought.com/enthought/ticket/1817
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-module-setuptools python-module-setupdocs
BuildRequires: python-module-sphinx-devel libnumpy-devel
BuildRequires: python-module-vtk /proc strace
BuildPreReq: desktop-file-utils
BuildPreReq: python-module-sip-devel libpympi-devel
BuildPreReq: python-module-PyQt4-devel /usr/bin/ssh python-module-pyMPI
BuildPreReq: libGL-devel libGLU-devel xvfb-run

Provides: %oname = %version-%release
%py_requires %oname tvtk wx
#Requires: python-module-%oname.tests = %version-%release
Requires:       python-module-apptools
#Requires:       python-module-EnthoughtBase
Requires:       python-module-EnvisageCore
Requires:       python-module-EnvisagePlugins
Requires:       python-module-traits
Requires:       python-module-wx
#Requires:       python-module-TraitsGUI
#Requires:       python-module-TraitsBackendQt

%add_python_req_skip test tvtk_classes

%description
The Mayavi project includes two related packages for 3-dimensional
visualization:

 * Mayavi2: A tool for easy and interactive visualization of data.
 * TVTK: A Traits-based wrapper for the Visualization Toolkit, a
popular open-source visualization library.
These operate at different levels of abstraction. TVTK manipulates
visualization objects, while Mayavi2 lets you operate on your data,
and then see the results. Most users either use the Mayavi user
interface or program to its scripting interface; you probably don't
need to interact with TVTK unless you want to create a new Mayavi
module.

%package -n python-module-%oname
Summary: Python files for Mayavi, scientific data 3-dimensional visualizer
Group: Development/Python
Conflicts: %name < %version-%release

%description -n python-module-%oname
This package contains Python files for Mayavi, scientific data
3-dimensional visualizer.

%package -n python-module-%oname.tests
Summary: Tests for Mayavi, scientific data 3-dimensional visualizer
Group: Development/Python
Requires: python-module-%oname = %version-%release

%description -n python-module-%oname.tests
This package contains tests for Mayavi, scientific data
3-dimensional visualizer.

%package -n python-module-tvtk
Summary: TVTK: A Traits-based wrapper for the Visualization Toolkit
Group: Development/Python
Conflicts: %name < %version-%release

%description -n python-module-tvtk
TVTK: A Traits-based wrapper for the Visualization Toolkit, a
popular open-source visualization library.
These operate at different levels of abstraction. TVTK manipulates
visualization objects, while Mayavi2 lets you operate on your data,
and then see the results. Most users either use the Mayavi user
interface or program to its scripting interface; you probably don't
need to interact with TVTK unless you want to create a new Mayavi
module.

%package -n python-module-tvtk.tests
Summary: Tests for TVTK
Group: Development/Python
Requires: python-module-tvtk = %version-%release

%description -n python-module-tvtk.tests
TVTK: A Traits-based wrapper for the Visualization Toolkit, a
popular open-source visualization library.
These operate at different levels of abstraction. TVTK manipulates
visualization objects, while Mayavi2 lets you operate on your data,
and then see the results. Most users either use the Mayavi user
interface or program to its scripting interface; you probably don't
need to interact with TVTK unless you want to create a new Mayavi
module.

This package contains tests for TVTK.

%package doc
Summary: Documentation for Mayavi, scientific data 3-dimensional visualizer
Group: Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description doc
This package contains documentation for Mayavi, scientific data
3-dimensional visualizer.

%prep
%setup

%build
source %mpidir/bin/mpivars.sh

export PYTHONPATH=$PWD:$PWD/docs/source/mayavi/sphinxext
xvfb-run --server-args="-screen 0 1024x768x24" \
	python setup.py build

%install
source %mpidir/bin/mpivars.sh

export PYTHONPATH=$PWD:$PWD/docs/source/mayavi/sphinxext
xvfb-run --server-args="-screen 0 1024x768x24" \
	python setup.py install --skip-build --root=%buildroot

install -d %buildroot%_man1dir
install -p -m644 docs/mayavi2.man %buildroot%_man1dir/mayavi2.1

install -d %buildroot%_desktopdir
install -p -m644 %SOURCE1 %SOURCE2 %buildroot%_desktopdir

install -d %buildroot%_liconsdir
install -d %buildroot%_miconsdir
install -d %buildroot%_niconsdir

install -p -m644 docs/source/mayavi/images/mayavi2-48x48.png \
	%buildroot%_liconsdir/mayavi2.png
ln -s %_liconsdir/mayavi2.png %buildroot%_miconsdir/
ln -s %_liconsdir/mayavi2.png %buildroot%_niconsdir/

%files
%doc *.txt
%_bindir/mayavi2
%_bindir/tvtk_doc
%python_sitelibdir/*
%exclude %python_sitelibdir/mayavi*
%exclude %python_sitelibdir/tvtk
#exclude %python_sitelibdir/examples
%_man1dir/*
%_desktopdir/*
%_liconsdir/*
%_miconsdir/*
%_niconsdir/*

%files -n python-module-%oname
%python_sitelibdir/mayavi*
%exclude %python_sitelibdir/mayavi/tests

%files -n python-module-%oname.tests
%python_sitelibdir/mayavi/tests

%files -n python-module-tvtk
%python_sitelibdir/tvtk
%exclude %python_sitelibdir/tvtk/tests

%files -n python-module-tvtk.tests
%python_sitelibdir/tvtk/tests

%files doc
%doc docs/*.txt docs/pdf examples docs/build/tvtk docs/build/mayavi

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2.git20120411
- New snapshot

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt2.git20111221.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Feb 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2.git20111221
- Built without OSMesa

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20111221
- Version 4.1.1

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt3.git20111111
- Added explicit requirement on python-module-wx

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2.git20111111
- Moved examples into doc package

* Mon Nov 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111111
- Version 4.0.1

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt1.svn20110127
- Version 3.4.2

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20101112.2
- Rebuilt with NumPy 2.0.0-alt2.git20110405.4

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20101112.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20101112
- Version 3.4.1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20100725
- Version 3.3.3
- Requires python-module-wx2.9 instead of python-module-wx

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt1.svn200225
- Version 3.3.2

* Mon Jan 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20090919.5
- Rebuilt with new NumPy

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20090919.4
- Add requirement on python-module-mayavi.tests

* Mon Dec 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20090919.3
- Moved tests into separate package

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20090919.2
- Rebuilt with python 2.6

* Mon Oct 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20090919.1
- Extracted documentation into separate package

* Sat Oct 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20090919
- Version 3.3.1

* Fri Oct 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2
- Fixed versions of requirements

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus (thnx Valery Pipin)

* Fri Jun 26 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-6
- Fixed BR, and removed .template & .static directories from docs/source
- Included missing icon from .desktop

* Fri Jun 26 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-5
- Using mayavi2-48x48.png has icons for both .desktop files
- Added Categories to .desktop files

* Thu Jun 25 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-4
- Removed wrong scriplets and corrected 'commets' in
-  tvtk_doc.desktop file.

* Wed Jun 24 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-3
- Fixed license issue and group tag
- Added a .desktop file

* Mon Jun 15 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-3
- included man page, adjusted description, removed useless BR's,
- fixed owned directory issue, cleaned up spec

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-2
- Saving timestamp, and fixed indentation

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-1
- Updated

* Wed Jun 10 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-3
- Changed name to Mayavi

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-2
- Fixed description.

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-1
- Initial package
