%define pypi_name aioitertools

%def_with check

Name: python3-module-%pypi_name
Version: 0.12.0
Release: alt1

Summary: itertools and builtins for AsyncIO and mixed iterables
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/aioitertools
VCS: https://github.com/omnilib/aioitertools

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 10 2024 Anton Vyatkin <toni@altlinux.org> 0.12.0-alt1
- New version 0.12.0.

* Thu Oct 10 2024 Anton Vyatkin <toni@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus
