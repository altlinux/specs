%define modulename zigpy

%def_without check

Name: python3-module-zigpy
Version: 2.1.0
Release: alt1

Summary: Library implementing a Zigbee stack
License: GPL-3.0-or-later
Group: Development/Python3
URL: https://github.com/zigpy/zigpy
VCS: https://github.com/zigpy/zigpy

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: python3-module-attrs
Requires: python3-module-aiohttp
Requires: python3-module-aiosqlite >= 0.20.0
Requires: python3-module-crccheck
Requires: python3-module-cryptography
Requires: python3-module-voluptuous
Requires: python3-module-jsonschema
Requires: python3-module-serialx >= 1.4.0
Requires: python3-module-typing_extensions
Requires: python3-module-frozendict

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
%endif

%description
zigpy is a hardware-independent Zigbee protocol stack integration
library for Python 3, implementing ZCL (Zigbee Cluster Library) and
ZDO (Zigbee Device Object) application state management shared by
radio libraries such as bellows, zigpy-deconz, zigpy-xbee, zigpy-znp
and zigpy-zigate. It is used by Home Assistant's ZHA integration.

%prep
%setup
sed -i 's/dynamic = \["version"\]/version = "%version"/' pyproject.toml
sed -i '/\[tool.setuptools-git-versioning\]/,+1d' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE COPYING
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Wed Aug 05 2026 Dina Tagantseva <dinchik@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus.

