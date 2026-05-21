%define pypi_name pyfuse3

%def_enable check

Name: python3-module-%pypi_name
Version: 3.5.0
Release: alt1

Summary: Python 3 bindings for libfuse 3 with async I/O support
Group: Development/Python3
License: LGPL-2.1-or-later
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/libfuse/pyfuse3.git

#Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz
Source: https://github.com/libfuse/pyfuse3/releases/download/v%version/%pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: pkgconfig(fuse3)
BuildRequires: python3(cython) python3(wheel)
BuildRequires: python3(setuptools) python3(setuptools_scm)
%{?_enable_check:BuildRequires: /proc python3(pytest)
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
%pyproject_run_pytest

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README* Changes.*

%changelog
* Thu May 21 2026 Yuri N. Sedunov <aris@altlinux.org> 3.5.0-alt1
- 3.5.0

* Wed Jan 07 2026 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Dec 23 2025 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1
- enabled %%check

* Thu Aug 29 2024 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue May 21 2024 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- first build for Sisyphus


