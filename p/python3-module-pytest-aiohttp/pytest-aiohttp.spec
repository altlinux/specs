%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-aiohttp
%define mod_name pytest_aiohttp

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.4
Release: alt1
Summary: pytest plugin for aiohttp support
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pytest-aiohttp/
VCS: https://github.com/aio-libs/pytest-aiohttp
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

# well-known PyPI name
%py3_provides %pypi_name

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# dependencies
BuildRequires: python3(aiohttp)
BuildRequires: python3(aiohttp.test_utils)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-asyncio)
%endif

%description
pytest plugin for aiohttp support

%prep
%setup
%autopatch -p1
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Feb 09 2023 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1
- 0.3.0 -> 1.0.4.

* Sat May 22 2021 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- new version (0.3.0) with rpmgs script
- cleanup spec

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt2
- Updated build dependencies.

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.1.3-alt1
- Initial build for ALT Linux Sisyphus.
