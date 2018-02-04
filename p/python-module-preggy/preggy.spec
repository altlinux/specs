%define oname preggy

%def_with python3

Name: python-module-%oname
Version: 1.1.3
Release: alt3.git20141002.1
Summary: preggy is an assertion library for Python. (What were you ``expect()``ing?)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/preggy/

# https://github.com/heynemann/preggy.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-coverage python-module-nose python-module-setuptools python-module-six python-module-tox python-module-unidecode 
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-module-coverage python3-module-nose python3-module-setuptools python3-module-six python3-module-tox python3-module-unidecode
%endif

%py_provides %oname

%description
preggy is a collection of expectations for python applications,
extracted from the pyVows project.

%package -n python3-module-%oname
Summary: preggy is an assertion library for Python. (What were you ``expect()``ing?)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
preggy is a collection of expectations for python applications,
extracted from the pyVows project.

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
py.test
%if_with python3
pushd ../python3
py.test3
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.3-alt3.git20141002.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.3-alt3.git20141002
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt2.git20141002.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 1.1.3-alt2.git20141002
- cleanup buildreq

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20141002
- Initial build for Sisyphus

