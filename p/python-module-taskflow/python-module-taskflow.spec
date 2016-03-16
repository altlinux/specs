%define pypi_name taskflow
%def_with python3

Name: python-module-%pypi_name
Version: 1.21.0
Release: alt1.1
Epoch: 1
Summary: Taskflow structured state management library

Group: Development/Python
License: ASL 2.0
URL: https://launchpad.net/taskflow
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-enum34
BuildRequires: python-module-futurist >= 0.1.2
BuildRequires: python-module-fasteners >= 0.7
BuildRequires: python-module-networkx >= 1.10 python-module-networkx-tests
BuildRequires: python-module-contextlib2 >= 0.4.0
BuildRequires: python-module-stevedore >= 1.5.0
BuildRequires: python-module-futures >= 3.0
BuildRequires: python-module-monotonic >= 0.3
BuildRequires: python-module-jsonschema >= 2.0.0
BuildRequires: python-module-automaton >= 0.5.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-cachetools >= 1.0.0
BuildRequires: python-module-debtcollector >= 0.3.0

# for build doc and tests
BuildRequires: python-module-hacking >= 0.10.0
BuildRequires: python-module-oslotest >= 1.10.0
BuildRequires: python-module-mock >= 1.2
BuildRequires: python-module-testtools >= 1.4.0
BuildRequires: python-module-testscenarios >= 0.4
BuildRequires: python-module-kombu >= 3.0.7
#BuildRequires: python-module-doc8
BuildRequires: python-module-kazoo >= 2.2
BuildRequires: python-module-redis-py >= 2.10.0
BuildRequires: python-module-SQLAlchemy >= 0.9.9
BuildRequires: python-module-alembic >= 0.8.0
BuildRequires: python-module-psycopg2 >= 2.5
BuildRequires: python-module-pymysql >= 0.6.2
BuildRequires: python-module-eventlet >= 0.17.4


Requires: python-module-six
Requires: python-module-jsonschema
Requires: python-module-networkx-core
Requires: python-module-stevedore
Requires: python-module-futures
Requires: python-module-oslo.serialization
Requires: python-module-oslo.utils

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-futurist >= 0.1.2
BuildRequires: python3-module-fasteners >= 0.7
BuildRequires: python3-module-networkx >= 1.10
BuildRequires: python3-module-contextlib2 >= 0.4.0
BuildRequires: python3-module-stevedore >= 1.5.0
BuildRequires: python3-module-monotonic >= 0.3
BuildRequires: python3-module-jsonschema >= 2.0.0
BuildRequires: python3-module-automaton >= 0.5.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-cachetools >= 1.0.0
BuildRequires: python3-module-debtcollector >= 0.3.0
%endif

%description
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.

%package doc
Summary:          Documentation for Taskflow
Group:            Development/Documentation

%description doc
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.
This package contains the associated documentation.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Taskflow structured state management library
Group: Development/Python3

%description -n python3-module-%pypi_name
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.
%endif

%prep
%setup

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python_sitelibdir/*/test*
rm -fr %buildroot%python_sitelibdir/*/examples
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/examples

%files
%doc README.rst LICENSE ChangeLog
%python_sitelibdir/*

%files doc
%doc html

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%changelog
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

