%define _unpackaged_files_terminate_build 1
%define oname minipg

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.6
Release: alt1
Summary: Yet another PostgreSQL database driver
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/minipg/
Packager: Python Development Team <python@packages.altlinux.org>

# https://github.com/nakagami/minipg.git
Source0: https://pypi.python.org/packages/08/5b/672bb919188d537ac67e3a201b9218208db2ebe156b31cd8b61407706739/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-Cython
#BuildPreReq: python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-Cython
#BuildPreReq: python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-json python-modules-xml python3 python3-base python3-dev python3-module-zope
#BuildRequires: python-module-Cython python3-module-Cython rpm-build-python3

%description
Yet another Python PostgreSQL database driver.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Yet another Python PostgreSQL database driver.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Yet another PostgreSQL database driver
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Yet another Python PostgreSQL database driver.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Yet another Python PostgreSQL database driver.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
rm -rf ../python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
exit 1

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1
- automated PyPI update

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.3-alt1.git20150208.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sat Mar 26 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.3-alt1.git20150208.2
- NMU: Fixed BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1.git20150208.1
- NMU: Use buildreq for BR.

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.git20150208
- Initial build for Sisyphus

