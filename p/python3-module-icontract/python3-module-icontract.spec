%define _unpackaged_files_terminate_build 1
%define pypi_name icontract
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.7.1
Release: alt1.1
Summary: Design-by-contract in Python3 with informative violation messages and inheritance
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/icontract/
Vcs: https://github.com/Parquery/icontract.git
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-astor
BuildRequires: python3-module-asttokens
BuildRequires: python3-module-asyncstdlib
BuildRequires: python3-module-black
BuildRequires: python3-module-coverage
BuildRequires: python3-module-docutils
BuildRequires: python3-module-mypy
BuildRequires: python3-module-numpy
BuildRequires: python3-module-py-cpuinfo
BuildRequires: python3-module-pydocstyle
BuildRequires: python3-module-pygments
BuildRequires: python3-module-pylint
BuildRequires: python3-module-tabulate
BuildRequires: python3-module-tox
BuildRequires: python3-module-typeguard
BuildRequires: python3-module-typing-extensions
%endif

%description
Icontract provides design-by-contract to Python3 with informative
violation messages and inheritance.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# see for details: precommit.py
export ICONTRACT_SLOW=true
%pyproject_run_unittest discover -v

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.7.1-alt1.1
- Demodernized packaging.

* Fri Feb 07 2025 Stanislav Levin <slev@altlinux.org> 2.7.1-alt1
- 2.6.6 -> 2.7.1.

* Wed Jun 19 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 2.6.6-alt1
- Initial build for ALT Linux
