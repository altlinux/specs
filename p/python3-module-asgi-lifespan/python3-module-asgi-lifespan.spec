%define _unpackaged_files_terminate_build 1
%define pypi_name asgi-lifespan
%define mod_name asgi_lifespan

# TODO: fix tests
%def_without check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1.1.gff5d3d0

Summary: Programmatic startup/shutdown of ASGI apps
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/asgi-lifespan/
Vcs: https://github.com/florimondmanca/asgi-lifespan

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_check
%endif

%description
Programmatically send startup/shutdown lifespan events into ASGI applications.
When used in combination with an ASGI-capable HTTP client such as HTTPX,
this allows mocking or testing ASGI applications without having to spin up
an ASGI server.

Features:
* Send lifespan events to an ASGI app using LifespanManager.
* Support for asyncio and trio.
* Fully type-annotated.
* 100%% test coverage.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# remove setup.cfg to development and testing options
rm setup.cfg
%pyproject_run_pytest -vvvra --asyncio-mode=strict

%files
%doc CHANGELOG.md LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 24 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.0-alt1.1.gff5d3d0
- Built for ALT Sisyphus.

