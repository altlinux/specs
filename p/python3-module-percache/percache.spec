%define pypi_name percache

%def_with check

Name:    python3-module-%pypi_name
Version: 0.4.4
Release: alt1

Summary: Persistently cache results of callables

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/percache

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
percache is a Python module to persistently cache results of functions
(or callables in general) using decorators.

It is somehow similar to the Memoize Example from the Python Decorator Library
but with the advantage that results are stored persistently in a cache.
percache provides memoization across multiple invocations of the Python
interpreter.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 tests.py

%files
%doc *.md
%python3_sitelibdir/percache.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Jul 06 2025 Grigory Ustinov <grenka@altlinux.org> 0.4.4-alt1
- Initial build for Sisyphus.
