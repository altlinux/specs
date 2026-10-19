%define pypi_name django_postgres_extra

Name: python3-module-django-postgres-extra
Version: 3.0.1
Release: alt1

Summary: Bringing all of PostgreSQL's awesomeness to Django

License: MIT
Group: Development/Python3
URL: https://github.com/SectorLabs/django-postgres-extra
# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar
# https://github.com/SectorLabs/django-postgres-extra/pull/275
Patch1: django-postgres-extra-3.0.1-django6.patch
Patch2: django-postgres-extra-3.0.1-django61-on-delete-db.patch
Patch3: django-postgres-extra-3.0.1-exclude-docs-package.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
%if_disabled check
%else
BuildRequires: python3-module-django python3-module-psycopg python3-module-dateutil
%endif

%description
django-postgres-extra makes PostgreSQL features available through the Django
ORM: HStore field with unique and required constraints, upserts (ON CONFLICT),
partitioned tables, views and materialized views, table locking, schema
management and more.

%prep
%setup -n %pypi_name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# the upstream test suite needs a running PostgreSQL server
%__python3 -c '
import django
from django.conf import settings
settings.configure(INSTALLED_APPS=["psqlextra"], DATABASES={"default": {"ENGINE": "psqlextra.backend"}})
django.setup()
import psqlextra.models, psqlextra.query, psqlextra.manager, psqlextra.backend.schema, psqlextra.partitioning
'

%files
%doc README.md
%python3_sitelibdir/psqlextra/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- initial build for Sisyphus
- add Django 6.0/6.1 support (upstream PR #275 and on_delete_db fix)
