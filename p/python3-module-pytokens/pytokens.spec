%define _unpackaged_files_terminate_build 1
%define pypi_name pytokens
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.1
Release: alt1.1
Summary: Fast, spec compliant Python 3.13+ tokenizer
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytokens
Vcs: https://github.com/tusharsadhwani/pytokens
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-mypy

%if_with check
BuildRequires: python3-module-black
BuildRequires: python3-module-build
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-tox
BuildRequires: python3-module-twine
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
# disable mypycifying because it's alpha sw
export PYTOKENS_USE_MYPYC=0

%build
# disable mypycifying because it's alpha sw
export PYTOKENS_USE_MYPYC=0
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=''

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1.1
- Demodernized packaging.

* Tue Mar 10 2026 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.3.0 -> 0.4.1.

* Thu Nov 27 2025 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- 0.2.0 -> 0.3.0.

* Wed Oct 15 2025 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1
- initial build for sisyphus (0.2.0).
