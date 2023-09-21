%define _unpackaged_files_terminate_build 1

%define oname pyproj

%def_with check

Name: python3-module-%oname
Version: 3.6.1
Release: alt1
Summary: Python interface to PROJ
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyproj/
VCS: https://github.com/pyproj4/pyproj

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython
BuildRequires: proj
BuildRequires: proj-devel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-certifi
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-pandas
BuildRequires: python3-module-xarray
BuildRequires: python3-module-shapely
%endif

%description
Python interface to PROJ (cartographic projections and coordinate
transformations library)

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
export PROJ_DIR="%_usr/"
export PROJ_LIBDIR="%_libdir"
export PROJ_INCDIR="%_includedir"
%pyproject_build

%install
%pyproject_install

%check
cd ..
mkdir -p pyproj-test-folder
cd pyproj-test-folder
cp -r ../%name-%version/test .
cp -r ../%name-%version/pytest.ini .

PATH="%buildroot%_bindir:$PATH" \
PYTHONPATH=%buildroot%python3_sitelibdir \
py.test-3 -m "not network"

%files
%doc LICENSE* *.md docs
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}


%changelog
* Thu Sep 21 2023 Anton Vyatkin <toni@altlinux.org> 3.6.1-alt1
- New version 3.6.1.

* Thu Jun 15 2023 Anton Vyatkin <toni@altlinux.org> 3.6.0-alt1
- New version 3.6.0.

* Sun Jun 11 2023 Anton Vyatkin <toni@altlinux.org> 3.5.0-alt1
- New version 3.5.0.

* Tue Feb 28 2023 Anton Vyatkin <toni@altlinux.org> 3.4.1-alt1
- new version 3.4.1

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.9.6-alt2
- Drop python2 support.

* Fri Apr 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.6-alt1
- Build new version for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.4-alt3.git20141229.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.4-alt3.git20141229.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.4-alt3.git20141229.1
- NMU: Use buildreq for BR.

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt3.git20141229
- New snapshot

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt2.svn20131105
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt1.svn20131105
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt1.svn20130619
- Version 1.9.4

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.3-alt1.svn20130125
- Version 1.9.3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.0-alt1.svn20111223.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.svn20111223
- Version 1.9.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.9-alt1.svn20110504.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.9-alt1.svn20110504
- Version 1.8.9

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt1.svn20100914.1
- Rebuilt for debuginfo

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt1.svn20100914
- Version 1.8.8

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.7-alt1.svn20100715
- Version 1.8.7

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1.20091103
- Version 1.8.6
- Extracted tests into separate package

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5-alt1.20090914.1
- Rebuilt with python 2.6

* Fri Sep 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5-alt1.20090914
- Initial build for Sisyphus

