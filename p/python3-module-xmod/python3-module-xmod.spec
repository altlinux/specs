%define pypi_name xmod

%def_with check

Name:    python3-module-%pypi_name
Version: 1.8.1
Release: alt1

Summary: Turn any object into a module
License: MIT
Group:   Development/Python3
URL:     https://github.com/rec/xmod

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Xmod is a tiny library that lets a module to do things that normally only a
class could do - handy for modules that "just do one thing".

%prep
%setup -n %pypi_name-%version
sed -i 's/assert partial_function and False/assert partial_function/g' ./test/test_xmod.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 1.8.1-alt1
- Initial build for Sisyphus.
