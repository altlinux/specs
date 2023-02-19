%define oname taskflow
%def_without check
%def_with docs

Name: python3-module-%oname
Version: 5.0.0
Release: alt1.1
Epoch: 1

Summary: Taskflow structured state management library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/taskflow

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Requires: python3-module-networkx-drawing

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-futurist >= 1.2.0
BuildRequires: python3-module-fasteners >= 0.17.3
BuildRequires: python3-module-networkx >= 2.1.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-jsonschema >= 3.2.0
BuildRequires: python3-module-automaton >= 1.9.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-tenacity >= 6.0.0
BuildRequires: python3-module-cachetools >= 2.0.0
BuildRequires: python3-module-pydot >= 1.2.4

%if_with check
BuildRequires: python3-module-kazoo >= 2.6.0
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-kombu >= 4.3.0
BuildRequires: python3-module-alembic >= 0.8.10
BuildRequires: python3-module-SQLAlchemy-Utils
BuildRequires: python3-module-zake >= 0.1.6
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-pymysql
BuildRequires: python3-module-psycopg2 >= 2.8.0
BuildRequires: python3-module-pydotplus >= 2.0.2
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
%endif

%description
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.

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
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/test.py
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/test.py
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 1:5.0.0-alt1.1
- Moved on modern pyproject macros.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 1:5.0.0-alt1
- Automatically updated to 5.0.0.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 1:4.1.0-alt1
- Automatically updated to 4.1.0.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1:3.8.0-alt1
- Automatically updated to 3.8.0.
- Added watch file.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1:3.7.1-alt1
- Automatically updated to 3.7.1.
- Build with docs.

* Tue Oct 29 2019 Grigory Ustinov <grenka@altlinux.org> 1:3.2.0-alt3
- Build without python2.

* Thu Mar 14 2019 Lenar Shakirov <snejok@altlinux.ru> 1:3.2.0-alt2
- Requires: s/networkx-core/networkx-drawing/
- needed by taskflow/types/graph.py

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1:3.2.0-alt1
- 3.2.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:2.9.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1:2.9.0-alt1
- 2.9.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1:2.6.0-alt1
- 2.6.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1:1.30.0-alt1
- 1.30.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.21.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.21.0-alt1
- 1.21.0
- add python3 package

* Mon Oct 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1:0.7.1-alt1
- downgrade to 0.7.1

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 0.1.2-alt1
- First build for ALT (based on Fedora 0.1.2-7.fc21.src)

