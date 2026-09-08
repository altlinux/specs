%define pypi_name django-extensions

%def_with check

Name: python3-module-%pypi_name
Version: 4.1
Release: alt1

Summary: Extensions for Django
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/django-extensions
VCS: https://github.com/django-extensions/django-extensions

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch: django-6.0-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-shortuuid
BuildRequires: python3-module-pip
BuildRequires: python3-module-factory_boy
BuildRequires: python3-module-vobject
BuildRequires: python3-module-Pygments
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-requests
BuildRequires: python3-module-pygraphviz
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-pydot
BuildRequires: python3-module-werkzeug
%endif

%description
This is a repository for collecting global custom management extensions
for the Django Framework.

%prep
%setup -n %pypi_name-%version
%autopatch -p1

# mail_debug depends on asyncore and smtpd, which have been removed from Python 3.12
# https://github.com/django-extensions/django-extensions/issues/1831
rm django_extensions/management/commands/mail_debug.py
rm tests/management/commands/test_mail_debug.py

%build
%pyproject_build

%install
%pyproject_install

%check
export DJANGO_SETTINGS_MODULE=tests.testapp.settings

# not compatible with Django 6.0
%pyproject_run_pytest -k "\
not PipCheckerTests \
and not DumpScriptTests \
and not test_with_length_args \
and not test_should_print_all_signals \
and not test_field_class \
and not testRandomCharTestModelDuplicate"

%files
%doc README.*
%python3_sitelibdir/django_extensions
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Sep 08 2026 Aleksandr Dovydenkov <asd@altlinux.org> 4.1-alt1
- New version 4.1.

* Fri Mar 28 2025 Anton Vyatkin <toni@altlinux.org> 3.2.3-alt4
- Fixed FTBFS.

* Wed Jan 22 2025 Anton Vyatkin <toni@altlinux.org> 3.2.3-alt3
- Fixed FTBFS.

* Wed Jul 31 2024 Anton Vyatkin <toni@altlinux.org> 3.2.3-alt2
- Fixed FTBFS.

* Sun Jul 21 2024 Anton Vyatkin <toni@altlinux.org> 3.2.3-alt1
- Initial build for Sisyphus.
