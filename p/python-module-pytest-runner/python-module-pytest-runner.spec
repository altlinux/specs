%def_with python3

%define oname pytest-runner

Name: python-module-%oname
Version: 2.9
Release: alt1.1

Summary: Setup scripts can use pytest-runner to add setup.py test support for pytest runner
License: ISC
Group: Development/Python

Url: https://pypi.python.org/pypi/%oname/
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.python.org/packages/11/d4/c335ddf94463e451109e3494e909765c3e5205787b772e3b25ee8601b86a/%oname-%version.tar.gz

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-setuptools_scm
BuildRequires: python3-module-pytest
%endif
BuildPreReq: python-devel python-module-setuptools python-module-setuptools_scm
BuildRequires: python-module-pytest

%py_provides ptr

%description
Setup scripts can use pytest-runner to add setup.py test support for pytest
runner.

%if_with python3
%package -n python3-module-%oname
Summary: Setup scripts can use pytest-runner to add setup.py test support for pytest runner
Group: Development/Python3
%py3_provides ptr

%description -n python3-module-%oname
Setup scripts can use pytest-runner to add setup.py test support for pytest
runner.
%endif

%prep
%setup -n %oname-%version
%if_with python3
rm -fR ../python3-module-%oname-%version
cp -fR . ../python3-module-%oname-%version
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3-module-%oname-%version
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3-module-%oname-%version
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
python3 setup.py test
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.9-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 2.9-alt1
- New version 2.9
- srpm build

* Sun Mar 13 2016 Ivan Zakharyaschev <imz at altlinux.org> 2.6.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt at altlinux.ru> 2.6.1-alt2
- remove hgtools from buildreq

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1
- Version 2.6.1

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus

