%define pypi_name pyinstrument

# don't work in upstream
%def_without check

Name:    python3-module-%pypi_name
Version: 4.6.2
Release: alt1

Summary: Call stack profiler for Python
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/joerick/pyinstrument

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-ipython
%endif

Source: %pypi_name-%version.tar

%description
Pyinstrument is a Python profiler. A profiler is a tool to help you optimize
your code - make it faster. To get the biggest speed increase you should focus
on the slowest part of your program. Pyinstrument helps you find it!

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jul 19 2024 Alexander Burmatov <thatman@altlinux.org> 4.6.2-alt1
- Initial build for Sisyphus.
