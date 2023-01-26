%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_disable bootstrap
%def_disable docs

%define oname mayavi

Name:           Mayavi
Version:        4.8.1
Release:        alt1
Summary:        Scientific data 3-dimensional visualizer

Group:          Graphics
License:        BSD and BSD-3-Clause and BSD-style and EPL-1.0 and LGPL and LGPLv2+ and LGPLv3+
URL:            http://code.enthought.com/projects/mayavi/

VCS:            https://github.com/enthought/mayavi.git
Source:         %name-%version.tar
Source1:        Mayavi.desktop
Source2:        tvtk_doc.desktop

Patch1: %name-alt-test-dependencies.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-vtk /proc
BuildRequires: desktop-file-utils
BuildRequires: vtk-python3
BuildRequires: libGL-devel libGLU-devel
%if_enabled docs
BuildRequires: python3-module-setupdocs
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: xvfb-run
%endif
%if_disabled bootstrap
BuildRequires: python3-module-traits python3(traits.api)
%endif

Provides: %oname = %EVR
Requires: python3-module-%oname = %EVR

%add_python3_req_skip test tvtk_classes

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

%package -n python3-module-%oname
Summary: Python files for Mayavi, scientific data 3-dimensional visualizer
Group: Development/Python3
Conflicts: %name < %EVR
%add_python3_req_skip wx wxversion
%add_python3_req_skip ipywidgets ipyevents
Requires: python3-module-tvtk = %EVR

%description -n python3-module-%oname
This package contains Python files for Mayavi, scientific data
3-dimensional visualizer.

%package -n python3-module-%oname-tests
Summary: Tests for Mayavi, scientific data 3-dimensional visualizer
Group: Development/Python3
Obsoletes: python3-module-%oname.tests < %EVR
Requires: python3-module-%oname = %EVR
%add_python3_req_skip vtk.numpy_interface

%description -n python3-module-%oname-tests
This package contains tests for Mayavi, scientific data
3-dimensional visualizer.

%package -n python3-module-tvtk
Summary: TVTK: A Traits-based wrapper for the Visualization Toolkit
Group: Development/Python
Conflicts: %name < %EVR
%add_python3_req_skip tvtk.tvtk_classes tvtk.tvtk_classes.vtk_version
%add_python3_req_skip vtk.util vtk.wx.wxVTKRenderWindowInteractor

%description -n python3-module-tvtk
TVTK: A Traits-based wrapper for the Visualization Toolkit, a
popular open-source visualization library.
These operate at different levels of abstraction. TVTK manipulates
visualization objects, while Mayavi2 lets you operate on your data,
and then see the results. Most users either use the Mayavi user
interface or program to its scripting interface; you probably don't
need to interact with TVTK unless you want to create a new Mayavi
module.

%package -n python3-module-tvtk-tests
Summary: Tests for TVTK
Group: Development/Python3
Obsoletes: python3-module-tvtk.tests < %EVR
Requires: python3-module-tvtk = %EVR

%description -n python3-module-tvtk-tests
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
Conflicts: %name < %EVR

%description doc
This package contains documentation for Mayavi, scientific data
3-dimensional visualizer.

%prep
%setup
%patch1 -p1

%build
%if_enabled docs
export PYTHONPATH=$PWD
xvfb-run \
%endif
%pyproject_build

%install
%if_enabled docs
export PYTHONPATH=$PWD
xvfb-run \
%endif
%pyproject_install

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

# remove shebangs from files
find %buildroot%python3_sitelibdir -type f -name '*py' -exec \
	sed -i -e '1!b' -e '/^\#\!\/usr\/bin\/env python$/d' '{}' +

%files
%doc image_LICENSE*.txt LICENSE_COLORBREWER.txt LICENSE.txt LICENSE_YORICK.txt
%doc DEVELOPING.rst README.rst README-tvtk.txt
%_bindir/mayavi2
%_bindir/tvtk_doc
%_man1dir/*
%_desktopdir/*
%_liconsdir/*
%_miconsdir/*
%_niconsdir/*

%files -n python3-module-%oname
%python3_sitelibdir/mayavi*
%exclude %python3_sitelibdir/mayavi/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/mayavi/tests

%files -n python3-module-tvtk
%python3_sitelibdir/tvtk
%exclude %python3_sitelibdir/tvtk/tests

%files -n python3-module-tvtk-tests
%python3_sitelibdir/tvtk/tests

%files doc
%doc docs/*.txt docs/pdf examples
%if_enabled docs
%doc docs/build/mayavi
%if_disabled bootstrap
%doc docs/build/tvtk
%endif
%endif

%changelog
* Mon Jan 23 2023 Anton Vyatkin <toni@altlinux.org> 4.8.1-alt1
- new version 4.8.1

* Tue Dec 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.4-alt1
- Updated to upstream version 4.7.4.

* Wed Jun 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.3-alt2
- Renamed tests packages.
- Updated package dependencies.

* Thu May 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.3-alt1
- Updated to upstream version 4.7.3.

* Mon Sep 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.2-alt1
- Updated to upstream version 4.7.2.

* Mon Aug 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.1-alt2
- Spec cleanup.
- Disabled documentation build.

* Thu Jun 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.1-alt1
- Updated to upstream version 4.7.1.

* Tue Jul 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.0-alt1
- Updated to upstream version 4.7.0.
- Rebuilt with python-3.

* Mon Jun 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.2-alt3
- Updated build dependencies.

* Mon May 20 2019 Slava Aseev <ptrnine@altlinux.org> 4.6.2-alt2
- Rebuild with vtk8.2

* Mon Sep 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.2-alt1
- Updated to upstream version 4.6.2.

* Mon May 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.git20150422
- Version 4.4.0

* Sat Apr 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt3.git20140924
- Rebuilt with vtk6.2

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt2.git20140924
- New snapshot

* Tue May 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt2.git20140421
- Rebuilt with vtk6.1

* Thu May 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1.git20140421
- Version 4.3.2

* Mon Oct 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt3.git20130807
- Added necessary requirement

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130807
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130406
- Rebuilt with updated NumPy

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130406
- Version 4.3.0

* Fri Apr 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt3.git20121228
- Fixed build

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt2.git20121228
- New snapshot

* Tue Jan 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt2.git20120930
- Rebuilt with new qscintilla2

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20120930
- Version 4.2.1

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt3.git20120411
- Rebuilt with OpenMPI 1.6

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
