%define pypi_name django-memcached-consul

%def_with check

Name:    python3-module-%pypi_name
Version: 0.2.0
Release: alt1

Summary: Used consul discovered memcached servers
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/criteo/django-memcached-consul

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-consul
BuildRequires: python3-module-memcached
BuildRequires: python3-module-httmock
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch1: remove-broken-tests.patch

%description
%summary.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %version-%release
Requires: python3(httmock)

%description tests
This package contains tests for %name.

%prep
%setup -n %pypi_name-%version
sed -i 's|memcached.MemcachedCache|memcached.PyMemcacheCache|' \
    $(find . -name 'memcached.py')
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc *.md
%python3_sitelibdir/django_memcached_consul/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files tests
%python3_sitelibdir/tests/

%changelog
* Mon Oct 02 2023 Alexander Burmatov <thatman@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
