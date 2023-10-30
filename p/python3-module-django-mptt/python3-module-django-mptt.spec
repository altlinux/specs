%define pypi_name django-mptt

%def_with check

Name:    python3-module-%pypi_name
Version: 0.15
Release: alt1

Summary: Utilities for implementing a modified pre-order traversal tree in django
License: MIT
Group:   Development/Python3
URL:     https://github.com/django-mptt/django-mptt

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: python3(hatchling)

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
%find_lang %name

%files -f %name.lang
%doc *.rst
%python3_sitelibdir/mptt/
%python3_sitelibdir/django_mptt-%version.0.dist-info/

%changelog
* Mon Oct 02 2023 Alexander Burmatov <thatman@altlinux.org> 0.15-alt1
- Initial build for Sisyphus.
