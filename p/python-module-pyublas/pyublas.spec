%define oname pyublas

%def_with python3

Name: python-module-%oname
Version: 2013.1
Release: alt1.git20140620.1.1.1
Summary: Seamless Numpy-UBlas interoperability
License: BSD
Group: Development/Python
Url: http://mathema.tician.de/software/pyublas
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://git.tiker.net/trees/pyublas.git
Source: %oname-%version.tar

BuildPreReq: boost-python-devel libnumpy-devel python-module-sphinx-devel
BuildPreReq: gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel python3-module-setuptools
%endif

%description
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

%package -n python3-module-%oname
Summary: Seamless Numpy-UBlas interoperability
Group: Development/Python3

%description -n python3-module-%oname
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

%package -n python3-module-%oname-devel
Summary: Development files of PyUblas
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-devel
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

This package contains development files of PyUblas.

%package devel
Summary: Development files of PyUblas
Group: Development/Python
Requires: %name = %version-%release

%description devel
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

This package contains development files of PyUblas.

%package docs
Summary: Documentation for PyUblas
Group: Development/Documentation
BuildArch: noarch

%description docs
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

This package contains documentation for PyUblas.

%package pickles
Summary: Pickles for PyUblas
Group: Development/Python

%description pickles
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

This package contains pickles for PyUblas.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make -C doc html

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
install -d %buildroot%_includedir
ln -s %python3_sitelibdir/pyublas/include/pyublas \
	%buildroot%_includedir/%oname-py3
popd
%endif

install -d %buildroot%_includedir
ln -s %python_sitelibdir/pyublas/include/pyublas %buildroot%_includedir/

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%pre devel
rm -fR %_includedir/pyublas

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/pyublas/include
%exclude %python_sitelibdir/pyublas/testhelp_ext.so

%files devel
%doc test/*
%_includedir/%oname
%python_sitelibdir/pyublas/include

%files docs
%doc doc/.build/html

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/pyublas/include
%exclude %python3_sitelibdir/pyublas/testhelp_ext.*.so

%files -n python3-module-%oname-devel
%doc test/*
%_includedir/%oname-py3
%python3_sitelibdir/pyublas/include
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2013.1-alt1.git20140620.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2013.1-alt1.git20140620.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2013.1-alt1.git20140620.1
- rebuild with boost 1.57.0

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt1.git20140620
- New snapshot
- Added module for Python 3

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt1.git20130718
- New snapshot

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt1.git20130314
- Version 2013.1

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt6.git20120417
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt5.git20120417
- Rebuilt with Boost 1.52.0

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt4.git20120417
- Rebuilt with Boost 1.51.0

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt3.git20120417
- New snapshot

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt3.git20111202
- Rebuilt with Boost 1.49.0

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20111202
- New snapshot

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20110405
- Rebuilt with Boost 1.48.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2011.1-alt1.git20110405.1.1
- Rebuild with Python-2.7

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110405.1
- Rebuilt with Boost 1.47.0

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110405
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110318
- Version 2011.1
- Enabled using Boost iterators

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.1-alt1.git20101020.2
- Rebuilt with python-module-sphinx-devel

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.1-alt1.git20101020.1
- Rebuilt with debuginfo

* Tue Dec 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.1-alt1.git20101020
- Initial build for Sisyphus

