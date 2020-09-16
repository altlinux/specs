%define _unpackaged_files_terminate_build 1

%define oname pyublas

%def_without docs

Name: python3-module-%oname
Version: 2017.1
Release: alt2

Summary: Seamless Numpy-UBlas interoperability
License: BSD
Group: Development/Python3
Url: http://mathema.tician.de/software/pyublas

# http://git.tiker.net/trees/pyublas.git
Source: %name-%version.tar

Patch1: %oname-%version-alt-armh-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ boost-python3-devel libnumpy-py3-devel
%if_with docs
BuildRequires: python3-module-sphinx
%endif

%description
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

%package devel
Summary: Development files of PyUblas
Group: Development/Python3
Requires: %name = %version-%release

%description devel
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

This package contains development files of PyUblas.

%if_with docs
%package docs
Summary: Documentation for PyUblas
Group: Development/Documentation
BuildArch: noarch

%description docs
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

This package contains documentation for PyUblas.
%endif

%package pickles
Summary: Pickles for PyUblas
Group: Development/Python3

%description pickles
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

This package contains pickles for PyUblas.

%prep
%setup
%patch1 -p1

sed -i 's|#!.*python|&3|' configure.py
sed -i 's|sphinx-build|&-3|' doc/Makefile

%build
./configure.py \
    --boost-python-libname=boost_python%{python_version_nodots python3}
%python3_build_debug

%if_with docs
%make -C doc html
%endif

%install
%python3_install

install -d %buildroot%_includedir
ln -s %python3_sitelibdir/pyublas/include/pyublas %buildroot%_includedir/

%if_with docs
cp -fR doc/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%pre devel
rm -fR %_includedir/pyublas

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/pyublas/include
%if_with docs
%exclude %python3_sitelibdir/%oname/pickle

%files docs
%doc doc/.build/html

%files pickles
%python3_sitelibdir/%oname/pickle
%endif

%files devel
%doc test/*
%_includedir/%oname
%python3_sitelibdir/pyublas/include

%changelog
* Wed Sep 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.1-alt2
- Fixed build for armh.

* Thu Mar 19 2020 Andrey Bychkov <mrdrew@altlinux.org> 2017.1-alt1
- Version updated to 2017.1
- build for python2 disabled.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2013.1-alt1.git20140620.1.1.2
- NMU: rebuilt with boost-1.67.0

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

