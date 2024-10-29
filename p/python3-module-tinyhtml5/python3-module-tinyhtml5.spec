%define pypi_name tinyhtml5

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: A tiny HTML5 parser
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tinyhtml5
Vcs: https://github.com/CourtBouillon/tinyhtml5

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-webencodings
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 30 2024 Anton Vyatkin <toni@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
