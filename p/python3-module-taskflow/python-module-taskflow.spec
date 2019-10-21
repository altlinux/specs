%define oname taskflow

Name: python3-module-%oname
Version: 3.2.0
Release: alt3
Epoch: 1
Summary: Taskflow structured state management library

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Requires: python3-module-networkx-drawing

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

%description
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.

%package tests
Summary: Tests for %oname
Group: Development/Python3
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

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %{oname}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python3_build

#python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo

%install
%python3_install

%files
%doc README.rst LICENSE ChangeLog
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/test*

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/test*

%changelog
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

