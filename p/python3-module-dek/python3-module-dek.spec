%define pypi_name dek

%def_with check

Name:    python3-module-%pypi_name
Version: 1.4.2
Release: alt1

Summary: The decorator-decorator
License: MIT
Group:   Development/Python3
URL:     https://github.com/rec/dek

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-xmod
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Dek decorates your decorators to diminish defects and drudgery.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus.
