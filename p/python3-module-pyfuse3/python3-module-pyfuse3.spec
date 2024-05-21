%define pypi_name pyfuse3

# RuntimeError: Multi-threaded test running is not supported ?
%def_disable check

Name: python3-module-%pypi_name
Version: 3.3.0
Release: alt1

Summary: Python 3 bindings for libfuse 3 with async I/O support
Group: Development/Python3
License: LGPL-2.0-or-later
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/libfuse/pyfuse3.git

Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: pkgconfig(fuse3)
BuildRequires: python3(cython) python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(trio) python3(pytest_trio)}

%description
pyfuse3 is a set of Python 3 bindings for libfuse 3. It provides an
asynchronous API compatible with Trio and asyncio, and enables you to
easily write a full-featured Linux filesystem in Python.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -v -rs test/

%files
%python3_sitelibdir/%{pypi_name}_asyncio.py
%python3_sitelibdir/%{pypi_name}*.so
%python3_sitelibdir/_%{pypi_name}.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir/__pycache__/*
%doc README* Changes.*

%changelog
* Tue May 21 2024 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- first build for Sisyphus


