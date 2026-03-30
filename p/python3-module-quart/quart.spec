%define _unpackaged_files_terminate_build 1
%define pypi_name Quart
%define pypi_nname quart
%define mod_name %pypi_nname

%def_with check

Name: python3-module-%pypi_nname
Version: 0.20.0
Release: alt2.1
Summary: A Python ASGI web microframework with the same API as Flask
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/quart
Vcs: https://github.com/pallets/quart/
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-sugar
BuildRequires: python3-module-python-dotenv

BuildRequires: python3-module-aiofiles
BuildRequires: python3-module-blinker
BuildRequires: python3-module-click
BuildRequires: python3-module-flask
BuildRequires: python3-module-hypercorn
BuildRequires: python3-module-itsdangerous
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-markupsafe
BuildRequires: python3-module-werkzeug
%endif

%description
Quart is an async Python web microframework. Using Quart you can,
- render and serve HTML templates,
- write (RESTful) JSON APIs,
- serve WebSockets,
- stream request and response data,
- do pretty much anything over the HTTP or WebSocket protocols.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc README.*
%_bindir/quart
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Mar 28 2026 Grigory Ustinov <grenka@altlinux.org> 0.20.0-alt2.1
- Demodernized packaging.

* Thu Mar 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.20.0-alt2
- NMU: Fixed FTBFS (werkzeug==3.1.7).

* Tue Dec 24 2024 Stanislav Levin <slev@altlinux.org> 0.20.0-alt1
- 0.19.9 -> 0.20.0.

* Fri Nov 15 2024 Stanislav Levin <slev@altlinux.org> 0.19.9-alt1
- 0.19.8 -> 0.19.9.

* Mon Oct 28 2024 Stanislav Levin <slev@altlinux.org> 0.19.8-alt1
- 0.19.6 -> 0.19.8.

* Mon May 20 2024 Stanislav Levin <slev@altlinux.org> 0.19.6-alt1
- 0.19.5 -> 0.19.6.

* Wed Apr 03 2024 Stanislav Levin <slev@altlinux.org> 0.19.5-alt1
- 0.19.4 -> 0.19.5.

* Mon Feb 05 2024 Stanislav Levin <slev@altlinux.org> 0.19.4-alt1
- Initial build for Sisyphus.
