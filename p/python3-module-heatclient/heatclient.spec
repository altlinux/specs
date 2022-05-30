%define oname heatclient

Name: python3-module-%oname
Version: 2.5.1
Release: alt1

Summary: Python API and CLI for OpenStack Heat

Group: Development/Python3
License: Apache-2.0
Url: http://docs.openstack.org/developer/python-heatclient

Source: python-%oname-%version.tar.gz
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-osc-lib >= 1.14.0
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.8.0
BuildRequires: python3-module-swiftclient >= 3.2.0
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-babel
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-tempest >= 17.1.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0

%description
This is a client for the OpenStack Heat API. There's a Python API
(the heatclient module), and a command-line script (heat).
Each implements 100 percent of the OpenStack Heat API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for OpenStack Heat API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Heat API. There's a Python API
(the heatclient module), and a command-line script (heat).
Each implements 100 percent of the OpenStack Heat API.

This package contains documentation for %oname.
%endif

%prep
%setup -n python-%oname-%version

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config.
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%python3_build

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
%python3_install
echo "%version" > %buildroot%python3_sitelibdir/heatclient/versioninfo

%if_with docs
# install man page
install -p -D -m 644 man/heat.1 %buildroot%_man1dir/heat.1
%endif

# install bash completion
install -p -D -m 644 tools/heat.bash_completion \
    %buildroot%_sysconfdir/bash_completion.d/heat.bash_completion

%files
%doc *.rst LICENSE
%_bindir/heat
#_man1dir/heat*
%python3_sitelibdir/*
%_sysconfdir/bash_completion.d/heat*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with docs
%files doc
%doc LICENSE html
%endif

%changelog
* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.1-alt1
- Automatically updated to 2.5.1.
- Build without docs.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.18.0-alt1
- Automatically updated to 1.18.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.17.0-alt1
- Automatically updated to 1.17.0

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.16.1-alt1
- 1.16.1

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.14.0-alt1
- new version 1.14.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- 0.3.0
- add python package

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.9-alt1
- First build for ALT (based on Fedora 0.2.9-1.fc21.src)

