%define _unpackaged_files_terminate_build 1
%define oname robotframework-selenium2screenshots

%def_with python3

Name: python-module-%oname
Version: 0.7.2
Release: alt2.1
Summary: Robot Framework keyword library for capturing annotated screenshots with Selenium2Library
License: GPL
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/robotframework-selenium2screenshots/

# https://github.com/datakurre/robotframework-selenium2screenshots.git
Source: %{oname}-%{version}.tar.gz
Patch1: %oname-%version-alt-build.patch

BuildRequires: python-module-setuptools python-module-robotframework
BuildRequires: python-module-robotframework-selenium2library
BuildRequires: python-module-docutils python-module-cffi
BuildRequires: python-module-html5lib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-robotframework
BuildRequires: python3-module-robotframework-selenium2library
BuildRequires: python3-module-docutils python3-module-cffi
BuildRequires: python3-module-html5lib
%endif

%py_requires PIL robot Selenium2Library

%description
Robot Framework keyword library for capturing annotated screenshots with
Selenium2Library.

%if_with python3
%package -n python3-module-%oname
Summary: Robot Framework keyword library for capturing annotated screenshots with Selenium2Library
Group: Development/Python3
%py3_requires PIL robot Selenium2Library

%description -n python3-module-%oname
Robot Framework keyword library for capturing annotated screenshots with
Selenium2Library.
%endif

%prep
%setup -q -n %{oname}-%{version}
%patch1 -p2

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
%doc *.txt *.rst docs
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.2-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt2.git20140720.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt2.git20140720.1
- NMU: Use buildreq for BR.

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.git20140720
- Added module for Python 3

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20140720
- Initial build for Sisyphus

