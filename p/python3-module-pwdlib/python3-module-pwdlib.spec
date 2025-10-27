%define pypi_name pwdlib

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Modern password hashing for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pwdlib
Vcs: https://github.com/frankie567/pwdlib

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-bcrypt
BuildRequires: python3-module-argon2-cffi
%endif

%description
%summary

%prep
%setup -n %pypi_name-%version

# do not use hatch-regex-commit
sed -i 's/^dynamic = \["version"\]$/version = "%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest  -o=addopts='' -v

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 27 2025 Anton Vyatkin <toni@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Tue Apr 29 2025 Anton Vyatkin <toni@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus.
