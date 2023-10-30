%define pypi_name django-redis
%define mod_name  django_redis

Name: python3-module-%pypi_name
Version: 5.3.0
Release: alt1

Summary: Full featured redis cache backend for Django
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/niwibe/django-redis
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 05 2023 Alexander Burmatov <thatman@altlinux.org> 5.3.0-alt1
- New 5.3.0 version.

* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.6.0-alt2
- build for python2 disabled

* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 4.6.0-alt1
- Initial build for ALT Linux
