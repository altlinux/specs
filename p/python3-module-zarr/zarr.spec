%define pypi_name zarr

%def_without check

Name:    python3-module-%pypi_name
Version: 3.1.3
Release: alt1

Summary: An implementation of chunked, compressed, N-dimensional arrays for Python

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/zarr
VCS:     https://github.com/zarr-developers/zarr-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-typing-extensions
BuildRequires: python3-module-numpy
BuildRequires: python3-module-donfig
BuildRequires: python3-module-numcodecs
BuildRequires: python3-module-numpydoc
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-tomlkit
BuildRequires: python3-module-crc32c
BuildRequires: python3-module-hypothesis
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --ignore=tests/test_examples.py

%files
%doc LICENSE.txt *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 17 2026 Grigory Ustinov <grenka@altlinux.org> 3.1.3-alt1
- Initial build for Sisyphus.
