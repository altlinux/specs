%define oname senlinclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.0.0
Release: alt1

Summary: OpenStack Clustering API Client Library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-senlinclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-prettytable
BuildRequires: python3-module-keystoneauth1 >= 3.11.0
BuildRequires: python3-module-openstacksdk >= 0.24.0
BuildRequires: python3-module-osc-lib >= 1.11.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-heatclient
BuildRequires: python3-module-yaml
BuildRequires: python3-module-requests >= 2.14.2

%if_with check
BuildRequires: python3-module-pip
BuildRequires: python3-module-mock
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-tox
BuildRequires: python3-module-bandit >= 1.1.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-tempest >= 17.1.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-osc-lib-tests
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-setuptools >= 21.0.0
BuildRequires: python3-module-testscenarios >= 0.4
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
%endif

%description
This is a client library for Senlin built on the Senlin clustering API.
It provides a plugin for the openstackclient command-line tool.

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

%if_with docs
# install man page
install -pDm 644 man/senlin.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/python_senlinclient-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt2
- Build with check.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1
- Automatically updated to 2.5.0.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 2.4.0-alt1
- Automatically updated to 2.4.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt2
- Add docs subpackage.
- Add tests subpackage.
- Massive spec refactoring.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Automatically updated to 2.0.1.

* Thu Oct 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.11.0-alt1
- new version 1.11.0
- Build without python2.

* Fri Nov 11 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.0-alt1
- First build for ALT (bsed on ClearLinux)
