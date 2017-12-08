%define oname collect-exceptions

%def_with python3

Name: python-module-%oname
Version: 0.0.5
Release: alt2.git20150209
Summary: Python exception collector
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/collect-exceptions/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Yemsheng/collect-exceptions.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python-tools-2to3
%endif

%py_provides collect_exceptions

%description
'collect-exceptions' is a python exception collector. It can collect
django and celery exception.

%if_with python3
%package -n python3-module-%oname
Summary: Python exception collector
Group: Development/Python3
%py3_provides collect_exceptions

%description -n python3-module-%oname
'collect-exceptions' is a python exception collector. It can collect
django and celery exception.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Dec 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.5-alt2.git20150209
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.5-alt1.git20150209.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20150209
- Initial build for Sisyphus

