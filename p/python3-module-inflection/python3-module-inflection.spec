%define pypi_name inflection

%def_with check

Name:    python3-module-%pypi_name
Version: 0.5.1
Release: alt1

Summary: A port of Ruby on Rails' inflector to Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/jpvanhal/inflection

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Inflection is a string transformation library. It singularizes and
pluralizes English words, and transforms strings from CamelCase to
underscored string. Inflection is a port of Ruby on Rails' inflector to Python.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 04 2023 Alexander Burmatov <thatman@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus.
