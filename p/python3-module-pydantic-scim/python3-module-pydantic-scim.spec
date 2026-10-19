%define pypi_name pydantic-scim

Name: python3-module-pydantic-scim
Version: 0.0.8
Release: alt1

Summary: Pydantic types for SCIM

License: Apache-2.0
Group: Development/Python3
URL: https://chalk.ai

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar
Patch: pydantic-scim-0.0.8-alt-pydantic2-ref-field.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-setuptools_scm
# pydantic[email] extra: EmailStr needs email-validator at import time
BuildRequires: python3-module-email-validator python3-module-pydantic
Requires: python3-module-email-validator

%description
Pydantic models for the SCIM (System for Cross-domain Identity Management)
resources: users, groups, enterprise user extension, resource types,
service provider configuration and list responses.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
for m in group user enterprise_user resource_type responses service_provider; do
    python3 -c "import pydanticscim.$m"
done
python3 -c "
from pydanticscim.user import User
from pydanticscim.group import Group
from pydanticscim.responses import ListResponse
u = User(userName='a', emails=[{'value': 'a@example.com'}])
assert u.dict()['userName'] == 'a'
Group(displayName='g')
"

%files
%doc README.md
%python3_sitelibdir/pydanticscim/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 0.0.8-alt1
- initial build for Sisyphus

