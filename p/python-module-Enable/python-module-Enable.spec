%define _unpackaged_files_terminate_build 1

%def_with python3
%def_enable bootstrap

%define oname Enable
Name: python-module-%oname
Version: 4.8.0
Release: alt2
Summary: Drawing and interaction packages

Group: Development/Python
License: BSD and GPLv2
URL: https://github.com/enthought/enable/

# https://github.com/enthought/enable.git
Source: enable-%version.tar

Patch: use_system_freetype.patch

BuildRequires: gcc-c++ swig
BuildRequires: libX11-devel libGL-devel libGLU-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: libnumpy-devel libfreetype-devel
BuildRequires: python-module-Cython
%if_disabled bootstrap
BuildRequires: python-module-Pyrex
BuildRequires: python-module-sphinx-devel python-module-Pygments
BuildRequires: python-module-traits fonts-ttf-PT
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-Cython
%endif

%add_python_req_skip macport mac_context hypothesis
%add_python_req_skip tvtk

%description
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

%package tests
Summary: Tests for Enable project
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip hypothesis

%description tests
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

This package contains tests for Enable project.

%if_with python3
%package -n python3-module-%oname
Summary: Drawing and interaction packages
Group: Development/Python3
%add_python3_req_skip macport mac_context hypothesis
%add_python3_req_skip wx.aui wx.glcanvas wx.grid wx.py.shell

%description -n python3-module-%oname
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

%package -n python3-module-%oname-tests
Summary: Tests for Enable project
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip hypothesis
%add_python3_req_skip etsdevtools.debug.memusage

%description -n python3-module-%oname-tests
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

This package contains tests for Enable project.
%endif

%if_disabled bootstrap
%package pickles
Summary: Pickles for Enable project
Group: Development/Python

%description pickles
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

This package contains pickles for Enable project.

%package doc
Summary: Documentation for Enable project
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %EVR

%description doc
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

This package contains development documentation for Enable project.
%endif

%prep
%setup -n enable-%version
%patch -p1

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

# remove python3-only backend
rm -rf enable/enable/vtk_backend

%if_disabled bootstrap
%prepare_sphinx .
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%if_disabled bootstrap
%generate_pickles docs/source docs/source %oname
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

rm -fR %buildroot%python_sitelibdir/enthought/kiva/mac
rm -f $(find %buildroot%python_sitelibdir -name '*mac*.py*')

# remove shebangs from files
find %buildroot%python_sitelibdir -type f -name '*.py' -exec \
	sed -i -e '1!b' -e '/^\#\!\/usr\/bin\/env python$/d' '{}' +

%if_with python3
rm -fR %buildroot%python3_sitelibdir/enthought/kiva/mac
rm -f $(find %buildroot%python3_sitelibdir -name '*mac*.py*')

# remove shebangs from files
find %buildroot%python3_sitelibdir -type f -name '*.py' -exec \
	sed -i -e '1!b' -e '/^\#\!\/usr\/bin\/env python$/d' '{}' +
%endif

%if_disabled bootstrap
install -d %buildroot%python_sitelibdir/enable
cp -fR pickle %buildroot%python_sitelibdir/enable/
%endif

%files
%doc image_LICENSE*.txt LICENSE.txt
%doc *.rst CHANGES.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/example*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%if_disabled bootstrap
%exclude %python_sitelibdir/enable/pickle
%endif

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/example*
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_disabled bootstrap
%files pickles
%dir %python_sitelibdir/enable
%python_sitelibdir/enable/pickle

%files doc
%doc docs examples
%endif

%if_with python3
%files -n python3-module-%oname
%doc image_LICENSE*.txt LICENSE.txt
%doc *.rst CHANGES.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/example*
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/example*
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 4.8.0-alt2
- Build with system freetype (Closes: #36385).

* Fri Jul 19 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.0-alt1
- Updated to upstream version 4.8.0.
- Built modules for python-3.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.6.1-alt1
- automated PyPI update

* Tue Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 4.6.0-alt3.git20151207
- skip hypothesys requirement for -tests subpackage

* Mon Dec 07 2015 Sergey Alembekov <rt@altlinux.ru> 4.6.0-alt2.git20151207
- update to current upstream branch

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20150423
- Version 4.6.0

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20141003
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140501
- Version 4.5.0

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20131017
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130328
- Rebuilt with updated NumPy

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130328
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130108
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20120920
- Version 4.2.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120504
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt1.git20120117.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120117
- Version 4.1.1

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111114
- Version 4.0.1

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt1.svn20110127.2
- Rebuild with Python-2.7

* Mon Oct 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20110127.1
- Rebuilt with updated NumPy

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20110127
- Version 3.4.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101113.2
- Rebuilt with python-module-sphinx-devel

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101113.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101113
- Version 3.3.3

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt1.svn20100722
- Version 3.3.2

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20100225
- Version 3.3.1
- Extracted tests into separate package
- Added pickles package

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.5
- Extracted tests into separated package
- Rebuilt with reformed NumPy

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.4
- Rebuilt with reformed NumPy

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.3
- Rebuilt without python-module-Numeric

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.2
- Rebuilt with python 2.6

* Mon Oct 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.1
- Extracted documentation into separate package

* Wed Oct 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901
- Initial build for Sisyphus

