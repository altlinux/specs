%define oname etcd3gw
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 2.1.0
Release: alt1.1

Summary: A python client for etcd3 grpc-gateway v3 API

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/etcd3gw

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0
BuildRequires: python3-module-requests >= 2.20.0
BuildRequires: python3-module-futurist >= 0.16.0

%if_with check
BuildRequires: python3-module-mock
BuildRequires: python3-module-stestr
BuildRequires: python3-module-testtools >= 1.4.0
BuildRequires: python3-module-oslotest >= 1.10.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-pifpaf >= 0.10.0
BuildRequires: python3-module-hacking >= 3.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-urllib3 >= 1.15.1
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.5.1
BuildRequires: python3-module-openstackdocstheme
%endif

%description
%summary.

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
install -pDm 644 man/etcd3-gateway.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr --test-path etcd3gw/tests run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1.1
- Moved on modern pyproject macros.

* Fri Oct 21 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 0.2.6-alt1
- Build new version.

* Thu May 21 2020 Grigory Ustinov <grenka@altlinux.org> 0.2.5-alt1
- Build new version.
- Enable check.
- Fix license.
- Fix url.

* Tue Oct 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.4-alt2
- Build without python2.

* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 0.2.4-alt1
- Initial build
