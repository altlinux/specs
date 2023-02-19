%define oname ironic-lib
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.4.0
Release: alt1.1

Summary: OpenStack Ironic common library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/ironic-lib

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.34.0
BuildRequires: python3-module-zeroconf >= 0.24.0
BuildRequires: python3-module-bcrypt >= 3.1.3
BuildRequires: python3-module-webob
BuildRequires: python3-module-tenacity >= 6.2.0

%if_with check
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-keystonemiddleware >= 4.17.0
BuildRequires: python3-module-keystoneauth1
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
A common library to be used exclusively by projects under the Ironic governance.

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

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/%oname/rootwrap.d
mv %buildroot/usr/etc/ironic/rootwrap.d/*.filters %buildroot%_sysconfdir/%oname/rootwrap.d

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%dir %_sysconfdir/%oname
%dir %_sysconfdir/%oname/rootwrap.d
%config(noreplace) %_sysconfdir/%oname/rootwrap.d/*
%python3_sitelibdir/ironic_lib
%python3_sitelibdir/ironic_lib-%version.dist-info
%exclude %python3_sitelibdir/ironic_lib/tests

%files tests
%python3_sitelibdir/ironic_lib/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 5.4.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.4.0-alt1
- Automatically updated to 5.4.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 5.3.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 5.3.0-alt1
- Automatically updated to 5.3.0.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 5.2.0-alt1
- Automatically updated to 5.2.0.
- Unified (thx for felixz@).

* Tue Jun 16 2020 Grigory Ustinov <grenka@altlinux.org> 4.2.1-alt1
- Automatically updated to 4.2.1.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Automatically updated to 4.2.0.
- Build with docs.

* Thu Oct 31 2019 Grigory Ustinov <grenka@altlinux.org> 2.21.0-alt1
- Initial build for Sisyphus.
