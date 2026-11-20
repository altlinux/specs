%define pypi_name telegrinder

Name: python3-module-telegrinder
Version: 0.5.1
Release: alt1

Summary: Modern visionary telegram bot framework

License: MIT
Group: Development/Python3
URL: https://github.com/timoniq/telegrinder
# Source-url: https://files.pythonhosted.org/packages/1b/68/9066a40c1b6b5aee9289dce4b7bc2a5a41c10b316351a304fbb48d453a82/telegrinder-0.5.1.tar.gz
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch1: telegrinder-python314-event-loop.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-python3 rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-aiodns python3-module-aiohttp
BuildRequires: python3-module-certifi python3-module-colorama
BuildRequires: python3-module-choicelib python3-module-envparse
BuildRequires: python3-module-funtypes = 0.2.1
BuildRequires: python3-module-msgspec python3-module-typing_extensions
BuildRequires: python3-module-vbml
BuildRequires: python3-module-pytest python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-mock

# Conditional and dynamically loaded dependencies come from wheel metadata.
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata

%description
Modern visionary telegram bot framework.

%prep
%setup
%patch1 -p1
# Validate compatibility with current Sisyphus libraries in %%check.
sed -i -e 's/aiodns (>=3.5.0,<4.0.0)/aiodns (>=3.5.0)/' \
    -e 's/certifi (>=2025.7.9,<2026.0.0)/certifi (>=2025.7.9)/' \
    -e 's/msgspec (>=0.19.0,<0.20.0)/msgspec (>=0.19.0)/' pyproject.toml
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
python3 -c "import telegrinder"
%pyproject_run_pytest tests

%files
%doc LICENSE readme.md
%python3_sitelibdir/telegrinder/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 19 2026 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for Sisyphus.

