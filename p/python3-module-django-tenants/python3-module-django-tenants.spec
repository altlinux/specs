%define pypi_name django_tenants

Name: python3-module-django-tenants
Version: 3.14.0
Release: alt1

Summary: Tenant support for Django using PostgreSQL schemas

License: MIT
Group: Development/Python3
URL: https://github.com/django-tenants/django-tenants
# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
%if_disabled check
%else
BuildRequires: python3-module-django python3-module-psycopg
%endif

# optional mypy plugin, used only for type checking
%add_python3_req_skip mypy.plugin mypy.plugins.common mypy.types

%description
django-tenants allows Django powered websites to have multiple tenants
via PostgreSQL schemas: each tenant gets its own schema, shared data
lives in the public schema, and requests are routed by domain.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install
# the tests need the upstream test project (dts_test_app...), not installed
rm -rv %buildroot%python3_sitelibdir/django_tenants/tests

%check
# the upstream test project needs a running PostgreSQL server
cd %buildroot%python3_sitelibdir
%__python3 -c '
import django
from django.conf import settings
settings.configure(
    INSTALLED_APPS=["django_tenants", "django.contrib.contenttypes"],
    DATABASES={"default": {"ENGINE": "django_tenants.postgresql_backend"}},
    DATABASE_ROUTERS=["django_tenants.routers.TenantSyncRouter"],
    TENANT_MODEL="customers.Client",
    TENANT_DOMAIN_MODEL="customers.Domain",
    SHARED_APPS=["django_tenants", "django.contrib.contenttypes"],
    TENANT_APPS=["django.contrib.contenttypes"],
)
django.setup()
import django_tenants.models, django_tenants.utils, django_tenants.middleware
import django_tenants.postgresql_backend.base, django_tenants.postgresql_backend.introspection
'

%files
%doc README.rst
%python3_sitelibdir/django_tenants/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 3.14.0-alt1
- initial build for Sisyphus
