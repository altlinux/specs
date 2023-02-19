%define oname mistralclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.0.0
Release: alt1

Summary: OpenStack Mistral Client Library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-mistralclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-stevedore >= 1.20.0

%if_with check
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-tempest >= 17.1.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-docutils >= 0.11
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
This is a Python library for accessing the API (mistralclient module),
and a command-line script (mistral).

Mistral is a workflow service. Most business processes consist of multiple
distinct interconnected steps that need to be executed in a particular order in
a distributed environment. A user can describe such a process as a set of tasks
and their transitions. After that, it is possible to upload such a description
to Mistral, which will take care of state management, correct execution order,
parallelism, synchronization and high availability.

Mistral also provides flexible task scheduling so that it can run a process
according to a specified schedule (for example, every Sunday at 4.00pm) instead
of running it immediately. In Mistral terminology such a set of tasks and
relations between them is called a workflow.

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
install -pDm 644 man/mistral_client.1 %buildroot%_man1dir/%oname.1
%endif

# install bash completion
install -pDm 644 tools/mistral.bash_completion \
  %buildroot%_sysconfdir/bash_completion.d/mistral.bash_completion

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/mistral
%python3_sitelibdir/%oname
%python3_sitelibdir/python_mistralclient-%version-py%_python3_version.egg-info
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/mistral.bash_completion
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt2
- Fixed unowned dir.

* Thu Oct 20 2022 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1
- Automatically updated to 4.5.0.

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
