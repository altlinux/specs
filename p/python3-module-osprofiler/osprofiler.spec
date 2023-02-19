%define oname osprofiler
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.4.3
Release: alt2.1

Summary: OpenStack Profiler Library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/osprofiler

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-webob >= 1.6.0

%if_with check
BuildRequires: python3-module-oslo.messaging >= 5.2.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-hacking >= 3.1.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-ddt >= 1.0.1
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-docutils >= 0.14
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-pymongo >= 3.0.2
BuildRequires: python3-module-elasticsearch >= 2.0.0
BuildRequires: python3-module-pre-commit >= 2.6.0
BuildRequires: python3-module-redis-py
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
OSProfiler provides a tiny but powerful library that is used by most
(soon to be all) OpenStack projects and their python clients. It provides
functionality to be able to generate 1 trace per request, that goes through all
involved services. This trace can then be extracted and used to build a tree
of calls which can be quite handy for a variety of reasons (for example in
isolating cross-project performance issues).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%pyproject_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
# jaeger-client is deprecated
%__python3 -m stestr run --exclude-regex '(^osprofiler.tests.unit.drivers.test_jaeger.JaegerTestCase.*$)'

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.4.3-alt2.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.4.3-alt2
- Fixed build with check.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 3.4.3-alt1
- Automatically updated to 3.4.3.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Automatically updated to 2.9.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.8.2-alt1
- Automatically updated to 2.8.2.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.6.0-alt1
- Automatically updated to 2.6.0

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 2.3.0-alt1
- Updated to 2.3.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- Initial release
