%define pypi_name django-extensions

%def_with check

Name: python3-module-%pypi_name
Version: 3.2.3
Release: alt1

Summary: Extensions for Django
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/django-extensions
VCS: https://github.com/django-extensions/django-extensions

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch: remove-distutils-version.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-pytest-django
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
%patch -p1

# mail_debug depends on asyncore and smtpd, which have been removed from Python 3.12
# https://github.com/django-extensions/django-extensions/issues/1831
rm django_extensions/management/commands/mail_debug.py
rm tests/management/commands/test_mail_debug.py

%build
%pyproject_build

%install
%pyproject_install

%check
rm setup.cfg

export DJANGO_SETTINGS_MODULE=tests.testapp.settings

# PipCheckerTests use network
sed -i 's/djangorestframework==[0-9.]*/djangorestframework/g;s/pip==[0-9.]*/pip/g' tests/management/commands/test_pipchecker.py

%pyproject_run_pytest -k "\
not PipCheckerTests \
and not DumpScriptTests \
and not test_migration_is_last_applied \
and not test_installed_apps_no_resolve_conflicts_function \
and not test_validate_templates \
and not test_pipchecker_when_requirements_file_does_not_exist"

%files
%doc README.*
%python3_sitelibdir/django_extensions
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Jul 21 2024 Anton Vyatkin <toni@altlinux.org> 3.2.3-alt1
- Initial build for Sisyphus.
