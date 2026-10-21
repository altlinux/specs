%define pypi_name sanic-ext
%define mod_name sanic_ext

%def_with check

Name:    python3-module-%pypi_name
Version: 23.3.0
Release: alt1

Summary: Extended Sanic functionality
License: MIT
Group:   Development/Python3
URL:     https://sanic.dev/en/
VCS:     https://github.com/sanic-org/sanic-ext

# backport pydantic 2 openAPI support, drop with sanic-ext >= 25.12.0
Patch0: sanic-ext-23.3.0-pydantic2.patch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildREquires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-sanic
BuildRequires: python3-module-sanic-testing
BuildRequires: python3-module-aiofiles
BuildRequires: python3-module-yaml
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-attrs
BuildRequires: python3-module-jinja2
%endif

BuildArch: noarch

%description
Sanic Extensions is an officially supported Sanic plugin to provide application
developers with additional tools and features.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# Upstream includes tests in the wheel, exclude them
rm -r %buildroot%python3_sitelibdir/tests

%check
%pyproject_run_pytest -v

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Oct 06 2026 Evgeniy Serov <scala@altlinux.org> 23.3.0-alt1
- Initial build for Sisyphus.
