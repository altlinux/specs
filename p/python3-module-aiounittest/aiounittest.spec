%define pypi_name aiounittest

%def_with check

Name:    python3-module-%pypi_name
Version: 1.4.2
Release: alt1

Summary: Test python asyncio-based code with ease

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/aiounittest
VCS:     https://github.com/kwarunek/aiounittest

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-wrapt
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
The aiounittest is a helper library to ease of your pain (and boilerplate), when
writing a test of the asynchronous code (asyncio). You can test:
  synchronous code (same as the unittest.TestCase)
  asynchronous code, it supports syntax with async/await (Python 3.5+) and
    asyncio.coroutine/yield from (Python 3.4)
In the Python 3.8 (release note) and newer consider to use the
unittest.IsolatedAsyncioTestCase. Builtin unittest module is now asyncio-featured.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Dec 28 2023 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus.
