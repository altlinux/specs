%define pypi_name django-rq

Name:    python3-module-%pypi_name
Version: 2.8.1
Release: alt1

Summary: A simple app that provides django integration for RQ (Redis Queue)
License: MIT
Group:   Development/Python3
URL:     https://github.com/rq/django-rq

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Django integration with RQ, a Redis based Python queuing library. Django-RQ
is a simple app that allows you to configure your queues in django's
settings.py and easily use them in your project.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%python3_sitelibdir/django_rq/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 04 2023 Alexander Burmatov <thatman@altlinux.org> 2.8.1-alt1
- Initial build for Sisyphus.
