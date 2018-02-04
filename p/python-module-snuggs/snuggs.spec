%define _unpackaged_files_terminate_build 1
%define oname snuggs

%def_with python3

Name: python-module-%oname
Version: 1.4.1
Release: alt3.1
Summary: Snuggs are s-expressions for Numpy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/snuggs

# https://github.com/mapbox/snuggs.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-numpy-testing python-module-pyparsing python-module-setuptools
BuildRequires: python2.7(click)
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-numpy-testing python3-module-pyparsing python3-module-setuptools
BuildRequires: python3(click)
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
%py_requires click numpy pyparsing

%description
Snuggs are s-expressions for Numpy.

%if_with python3
%package -n python3-module-%oname
Summary: Snuggs are s-expressions for Numpy
Group: Development/Python3
%py3_provides %oname
%py3_requires click numpy pyparsing

%description -n python3-module-%oname
Snuggs are s-expressions for Numpy.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
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
python setup.py test -v
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test3 -vv
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.1-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt3
- Updated build dependencies.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.git20150403.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1.git20150403.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20150403
- Initial build for Sisyphus

