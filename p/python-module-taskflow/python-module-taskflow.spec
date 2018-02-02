%define oname taskflow
%def_with python3

Name: python-module-%oname
Version: 2.9.0
Release: alt1.1
Epoch: 1
Summary: Taskflow structured state management library

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-SQLAlchemy-Utils
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-enum34
BuildRequires: python-module-futurist >= 0.11.0
BuildRequires: python-module-fasteners >= 0.7
BuildRequires: python-module-networkx >= 1.10 python-module-networkx-tests
BuildRequires: python-module-contextlib2 >= 0.4.0
BuildRequires: python-module-stevedore >= 1.17.1
BuildRequires: python-module-futures >= 3.0
BuildRequires: python-module-jsonschema >= 2.0.0
BuildRequires: python-module-automaton >= 0.5.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-tenacity >= 3.2.1
BuildRequires: python-module-cachetools >= 1.1.0
BuildRequires: python-module-debtcollector >= 1.2.0


# for build doc and tests
BuildRequires: python-module-hacking >= 0.10.0
BuildRequires: python-module-oslotest >= 1.10.0
BuildRequires: python-module-mock >= 1.2
BuildRequires: python-module-testtools >= 1.4.0
BuildRequires: python-module-testscenarios >= 0.4
BuildRequires: python-module-kombu >= 3.0.25
#BuildRequires: python-module-doc8
BuildRequires: python-module-kazoo >= 2.2
BuildRequires: python-module-redis-py >= 2.10.0
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-alembic >= 0.8.0
BuildRequires: python-module-psycopg2 >= 2.5
BuildRequires: python-module-pymysql >= 0.6.2
BuildRequires: python-module-eventlet >= 0.18.2


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
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-futurist >= 0.1.2
BuildRequires: python3-module-fasteners >= 0.7
BuildRequires: python3-module-networkx >= 1.10
BuildRequires: python3-module-contextlib2 >= 0.4.0
BuildRequires: python3-module-stevedore >= 1.17.1
BuildRequires: python3-module-jsonschema >= 2.0.0
BuildRequires: python3-module-automaton >= 0.5.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-tenacity >= 3.2.1
BuildRequires: python3-module-cachetools >= 1.1.0
BuildRequires: python3-module-debtcollector >= 1.2.0
%endif

%description
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.


%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Taskflow
Group: Development/Documentation

%description doc
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.
This package contains the associated documentation.

%package -n python3-module-%oname
Summary: Taskflow structured state management library
Group: Development/Python3

%description -n python3-module-%oname
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %{oname}.egg-info

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

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst LICENSE ChangeLog
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/test.*

%files doc
%doc doc/build/html

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/test*
%endif

%changelog
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

