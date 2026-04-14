%define pypi_name django-rq
%define mod_name django_rq

%def_without check

Name:    python3-module-%pypi_name
Version: 4.1.0
Release: alt1

Summary: A simple app that provides django integration for RQ (Redis Queue)
License: MIT
Group:   Development/Python3
URL:     https://github.com/rq/django-rq

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-rq
BuildRequires: python3-module-django
BuildRequires: python3-module-django-redis
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Django integration with RQ, a Redis based Python queuing library. Django-RQ
is a simple app that allows you to configure your queues in django's
settings.py and easily use them in your project.

%prep
%setup -n %pypi_name-%version
find . -name '*.py' -o -name 'cxxtestgen' | xargs sed -i \
    -e '1 s:#!%_bindir/env python$:#!%_bindir/python3:' \
    -e '1 s:#! %_bindir/env python$:#! %_bindir/python3:' \
    %nil
sed -i "s/import urlunsplit import urlunsplit/import urlunsplit/" integration_test/_tests.py

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
export DJANGO_SETTINGS_MODULE=django_rq.tests.settings
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Apr 14 2026 Alexander Burmatov <thatman@altlinux.org> 4.1.0-alt1
- Update version to 4.1.0.

* Mon Jan 12 2026 Alexander Burmatov <thatman@altlinux.org> 3.2.2-alt1
- Update version to 3.2.2.

* Wed Nov 26 2025 Alexander Burmatov <thatman@altlinux.org> 3.2.1-alt1
- Update version to 3.2.1.

* Wed Aug 13 2025 Alexander Burmatov <thatman@altlinux.org> 3.1-alt1
- Update version to 3.1.

* Mon May 12 2025 Alexander Burmatov <thatman@altlinux.org> 3.0.1-alt1
- Update version to 3.0.1.

* Wed Dec 18 2024 Alexander Burmatov <thatman@altlinux.org> 3.0-alt1
- Update version to 3.0.

* Thu Dec 14 2023 Alexander Burmatov <thatman@altlinux.org> 2.9.0-alt1
- Update version to 2.9.0.

* Wed Oct 04 2023 Alexander Burmatov <thatman@altlinux.org> 2.8.1-alt1
- Initial build for Sisyphus.
