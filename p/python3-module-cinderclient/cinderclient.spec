%define oname cinderclient
%def_with check
%def_with docs

Name: python3-module-%oname
Epoch: 1
Version: 9.6.0
Release: alt1

Summary: OpenStack Block Storage API Client Library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-cinderclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 5.5.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-keystoneauth1 >= 5.0.0
BuildRequires: python3-module-oslo.i18n >= 5.0.1
BuildRequires: python3-module-oslo.utils >= 4.8.0
BuildRequires: python3-module-requests >= 2.25.1
BuildRequires: python3-module-stevedore >= 3.3.0

%if_with check
BuildRequires: python3-module-docutils >= 0.16
BuildRequires: python3-module-coverage >= 5.5
BuildRequires: python3-module-ddt >= 1.4.1
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-testtools >= 2.4.0
BuildRequires: python3-module-stestr >= 3.1.0
BuildRequires: python3-module-oslo.serialization >= 4.1.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-hacking >= 4.0.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-doc8 >= 0.8.1
%endif

%description
There's a Python API (the cinderclient module), and a command-line script (cinder).
Each implements 100%% of the OpenStack Cinder API.

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

# reno is not used, after openstack moved on openstackdocstheme
find . -name "conf.py" | xargs sed -i '/reno/d'

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
install -pDm 644 man/cinder.1 %buildroot%_man1dir/%oname.1
%endif

# install bash completion
install -pDm 644 tools/cinder.bash_completion \
  %buildroot%_sysconfdir/bash_completion.d/cinder.bash_completion

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/cinder
%python3_sitelibdir/%oname
%python3_sitelibdir/python_cinderclient-%version.dist-info
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/cinder.bash_completion
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Thu Oct 03 2024 Grigory Ustinov <grenka@altlinux.org> 1:9.6.0-alt1
- Automatically updated to 9.6.0.

* Tue May 28 2024 Grigory Ustinov <grenka@altlinux.org> 1:9.5.0-alt1
- Automatically updated to 9.5.0.

* Mon Oct 16 2023 Grigory Ustinov <grenka@altlinux.org> 1:9.3.0-alt1.2
- Dropped build dependency on python3-module-reno.

* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 1:9.3.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 1:9.3.0-alt1
- Automatically updated to 9.3.0.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 1:9.1.0-alt2
- Fixed unowned dir.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 1:9.1.0-alt1
- Automatically updated to 9.1.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 1:7.0.0-alt2
- Unify documentation building.
- Added docs subpackage.
- Spec refactoring.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 1:7.0.0-alt1
- Automatically updated to 7.0.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 1:5.0.0-alt1
- Automatically updated to 5.0.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1:4.2.1-alt1
- Automatically updated to 4.2.1

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1:4.0.1-alt1
- 4.0.1

* Tue Aug 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:3.5.0-alt2
- Rebuild with openstackdocstheme

* Wed Mar 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:3.5.0-alt1
- Updated to version 3.5.0
  Fixed sphinx_doc errors

* Mon Mar 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.11.0-alt2
- Updated build dependencies.

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1:1.11.0-alt1
- 1.11.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1:1.9.0-alt1
- 1.9.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1:1.6.0-alt1
- 1.6.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:1.4.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.1.2-alt1
- 1.1.2
- fixed version

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.11.1-alt1
- 1.11.1
- add python3 package

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.9-alt1
- New version (based on Fedora 1.0.9-1.fc21.src)

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2.26-alt1
- Initial release for Sisyphus (based on Fedora)
