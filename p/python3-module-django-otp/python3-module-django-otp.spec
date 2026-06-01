%define pypi_name django-otp
%define mod_name django_otp

Name:    python3-module-%pypi_name
Version: 1.7.0
Release: alt1

Summary: A pluggable framework for adding two-factor authentication to Django using one-time passwords
License: Unlicense
Group:   Development/Python3
URL:     https://github.com/django-otp/django-otp

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatchling

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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 01 2026 Alexander Burmatov <thatman@altlinux.org> 1.7.0-alt1
- New 1.7.0 version.

* Fri Dec 12 2025 Alexander Burmatov <thatman@altlinux.org> 1.6.3-alt1
- New 1.6.3 version.

* Fri Nov 10 2023 Alexander Burmatov <thatman@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus.
