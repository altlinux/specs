%define oname pymetis
Name: python-module-%oname
Version: 2011.1.1
Release: alt2.git20111128
Summary: Python wrapper for the Metis graph partititioning software
License: MIT
Group: Development/Python
Url: http://mathema.tician.de/software/pymetis
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://git.tiker.net/trees/pymetis.git
Source: %oname-%version.tar

BuildPreReq: python-module-setuptools gcc-c++ boost-python-devel

%description
PyMetis is a Python wrapper for the Metis graph partititioning software
by George Karypis, Vipin Kumar and others. It includes version 5.0pre2
of Metis and wraps it using the Boost Python wrapper generator library.
So far, it only wraps the most basic graph partitioning functionality,
but extending it in case you need more should be quite straightforward.
Using PyMetis to partition your meshes is really easy--essentially all
you need to pass into PyMetis is an adjacency list for the graph and the
number of parts you would like.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc LICENSE
%python_sitelibdir/*

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1.1-alt2.git20111128
- Rebuilt with Boost 1.49.0

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1.1-alt1.git20111128
- Version 2011.1.1

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20110314
- Rebuilt with Boost 1.48.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2011.1-alt1.git20110314.1.1
- Rebuild with Python-2.7

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110314.1
- Rebuilt with Boost 1.47.0

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110314
- Version 2011.1

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.1-alt1.git20091015.1
- Rebuilt for debuginfo

* Tue Dec 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.1-alt1.git20091015
- Initial build for Sisyphus

