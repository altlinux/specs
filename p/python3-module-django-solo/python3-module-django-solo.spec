%define pypi_name django-solo

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.0
Release: alt1

Summary: Django Solo helps working with singletons
License: CC-BY-3.0
Group: Development/Python3
URL: https://pypi.org/project/django-solo
VCS: https://github.com/lazybird/django-solo

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
Helps working with singletons - things like global settings that you want
to edit from the admin site.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.*
%python3_sitelibdir/solo
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 24 2024 Anton Vyatkin <toni@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus.
