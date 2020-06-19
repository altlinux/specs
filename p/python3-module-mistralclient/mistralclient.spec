%define oname mistralclient

Name:       python3-module-%oname
Version:    4.0.1
Release:    alt2

Summary:    Client Library for OpenStack Mistral Workflow Service API

Group:      Development/Python3
License:    Apache-2.0
Url:        http://docs.openstack.org/developer/python-%oname

Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-stevedore >= 1.20.0

BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-tempest

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc

%description
This is a Python library for accessing the API (mistralclient module),
and a command-line script (mistral).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Mistral Workflow Service API
Group: Development/Documentation

%description doc
This is a Python library for accessing the API (mistralclient module),
and a command-line script (mistral).

This package contains documentation for %oname.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf *.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

# install man page
install -p -D -m 644 man/mistral_client.1 %buildroot%_man1dir/mistralclient.1

# install bash completion
install -p -D -m 644 tools/mistral.bash_completion \
    %buildroot%_sysconfdir/bash_completion.d/mistral.bash_completion

%files
%doc *.rst LICENSE
%_bindir/mistral
%_man1dir/mistralclient*
%python3_sitelibdir/*
%_sysconfdir/bash_completion.d/mistral*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Automatically updated to 4.0.1.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.10.0-alt1
- Automatically updated to 3.10.0.
- Build without python2.

* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 3.7.0-alt1
- 3.7.0

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- new version 3.3.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- 3.0.0
- add test packages

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- Initial release for Sisyphus
