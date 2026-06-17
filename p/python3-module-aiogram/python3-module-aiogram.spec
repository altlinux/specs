%define _unpackaged_files_terminate_build 1
%define pypi_name aiogram
%define module_name aiogram

%def_with check

Name: python3-module-%pypi_name
Version: 3.23.0
Release: alt2
Summary: Modern and fully asynchronous framework for Telegram Bot API
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/aiogram/
Vcs: https://github.com/aiogram/aiogram.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra mongo
%pyproject_builddeps_metadata_extra redis
%pyproject_builddeps_metadata_extra i18n
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra proxy
%pyproject_builddeps_check
%endif

%description
aiogram is a modern and fully asynchronous framework for Telegram Bot API
written in Python 3.8+ using asyncio and aiohttp. It provides a simple and
powerful way to create Telegram bots with features like updates router,
finite state machine, magic filters, middlewares, and integrated I18n/L10n
support.

%prep
%setup

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -W'default::DeprecationWarning'

%files
%doc README.rst LICENSE
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 09 2026 Stanislav Levin <slev@altlinux.org> 3.23.0-alt2
- NMU: fixed FTBFS (aiohttp 3.14.0).

* Tue Dec 09 2025 Aleksandr A. Voyt <sobue@altlinux.org> 3.23.0-alt1
- 3.22.0 -> 3.23.0

* Fri Nov 07 2025 Aleksandr A. Voyt <sobue@altlinux.org> 3.22.0-alt1
- Initial build.

