%define _unpackaged_files_terminate_build 1
%define oname ratelim

%def_with python3

Name: python-module-%oname
Version: 0.1.6
Release: alt2
Summary: Makes it easy to respect rate limits
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/ratelim/

# https://github.com/themiurgo/ratelim.git
Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-decorator
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-decorator
%endif

%py_provides %oname
%py_requires decorator

%description
Ratelim is a simple Python library that limits the number of times a
function can be called in during a time interval. It is particularly
useful when using online APIs, which commonly enforce rate limits.

%if_with python3
%package -n python3-module-%oname
Summary: Makes it easy to respect rate limits
Group: Development/Python3
%py3_provides %oname
%py3_requires decorator

%description -n python3-module-%oname
Ratelim is a simple Python library that limits the number of times a
function can be called in during a time interval. It is particularly
useful when using online APIs, which commonly enforce rate limits.
%endif

%prep
%setup -q -n %{oname}-%{version}

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt2
- Updated build dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150113.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.git20150113.1
- NMU: Use buildreq for BR.

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150113
- Initial build for Sisyphus

