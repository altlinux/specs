%define pypi_name django-prometheus

%def_with check

Name:    python3-module-%pypi_name
Version: 2.3.1
Release: alt1

Summary: Export Django monitoring metrics for Prometheus.io
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/korfuri/django-prometheus

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
Requires: python3-module-django

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-prometheus_client
BuildRequires: python3-module-pytest-django
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install
rm -fr %buildroot%python3_sitelibdir/django_prometheus/tests

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/django_prometheus/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 02 2023 Alexander Burmatov <thatman@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus.
