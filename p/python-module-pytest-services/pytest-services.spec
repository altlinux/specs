%define oname pytest-services
Name: python-module-%oname
Version: 2.0.1
Release: alt1
Summary: Services plugin for pytest testing framework
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pytest-services/
# https://github.com/pytest-dev/pytest-services.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-mysqlclient python3-module-pbr python3-module-pylibmc
BuildRequires: python3-module-pytest-cov python3-module-tox python3-module-unittest2
BuildRequires: python3-tools-pep8

%py_provides pytest_services
%py_requires requests psutil subprocess32
# we have several versions of Django
# so, we cannot rely on auto-requires
%filter_from_requires /^python2\.7(django\(\..*\)\?)/d
%filter_from_requires /^python3(django\(\..*\)\?)/d


%description
The plugin provides a set of fixtures and utility functions to start
service processes for your tests with pytest.

%package -n python3-module-%oname
Summary: Services plugin for pytest testing framework
Group: Development/Python
%py3_provides pytest_services
%py3_requires requests psutil

%description -n python3-module-%oname
The plugin provides a set of fixtures and utility functions to start
service processes for your tests with pytest.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
py.test3 -vv --fixtures tests

%files -n python3-module-%oname
%doc *.rst docs/*.rst docs/api
%python3_sitelibdir/*

%changelog
* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Fri Sep 06 2019 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- 1.2.1 -> 1.3.1
- removed subpackage for python-2
- added filter for django autorequires

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.1-alt1
- Updated to upstream version 1.2.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt1.git20150725.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt1.git20150725.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20150725
- Version 1.1.3

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.git20150120
- Version 1.0.4

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20150120
- Initial build for Sisyphus

