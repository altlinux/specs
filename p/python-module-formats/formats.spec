%define oname formats

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt2.git20150211.1
Summary: Support multiple formats with ease
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/formats/

# https://github.com/redodo/formats.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-modules-json
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
%py_requires json

%description
Formats will provide you with a consistent API to parse and compose
data.

You could of course use the register method to register your own parser,
but decorators are much more fun!

%if_with python3
%package -n python3-module-%oname
Summary: Support multiple formats with ease
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Formats will provide you with a consistent API to parse and compose
data.

You could of course use the register method to register your own parser,
but decorators are much more fun!
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
python setup.py test
py.test -vv

%if_with python3
pushd ../python3
python3 setup.py test
py.test3 -vv
popd
%endif

%files
%doc *.md *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt2.git20150211.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2.git20150211
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20150211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20150211
- Initial build for Sisyphus

