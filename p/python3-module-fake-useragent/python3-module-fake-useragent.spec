%define pypi_name fake_useragent

Name: python3-module-fake-useragent
Version: 2.2.0
Release: alt1
Summary: User agent strings from a local browser database

License: Apache-2.0
Group: Development/Python3
URL: https://github.com/fake-useragent/fake-useragent
# Source-url: https://github.com/fake-useragent/fake-useragent/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3 python3-module-setuptools python3-module-wheel

%description
User agent strings from a local browser database.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
PYTHONPATH=src python3 - <<'CHECK'
from fake_useragent import UserAgent
agent = UserAgent(browsers=["Chrome"], platforms=["desktop"])
assert "Chrome/" in agent.random
assert agent.getBrowser("Chrome")["browser"] == "Chrome"
CHECK

%files
%python3_sitelibdir/fake_useragent/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README.md LICENSE

%changelog
* Thu Nov 05 2026 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- initial build for ALT Sisyphus

