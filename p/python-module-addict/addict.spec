%define oname addict

%def_with python3

Name: python-module-%oname
Version: 0.2.7
Release: alt1.git20141219.1.1
Summary: The Python Dict that's better than heroin
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/addict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mewwts/addict.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
A Python Dict whos keys can be set both using attribute and item syntax.

%package -n python3-module-%oname
Summary: The Python Dict that's better than heroin
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A Python Dict whos keys can be set both using attribute and item syntax.


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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.7-alt1.git20141219.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.7-alt1.git20141219.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt1.git20141219
- Initial build for Sisyphus

