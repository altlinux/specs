%def_without bootstrap
%def_without check

%define  oname pydantic

Name:    python3-module-%oname
Version: 1.10.4
Release: alt1

Summary: Data parsing and validation using Python type hints

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pydantic

# https://github.com/pydantic/pydantic
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-mypy
BuildRequires: python3-module-hypothesis
# These three deps are optional for extra tests
BuildRequires: python3-module-email_validator
BuildRequires: python3-module-dotenv
BuildRequires: python3-module-devtools
%endif

%if_with bootstrap
BuildArch: noarch
%else
BuildRequires: python3-module-Cython
%endif

%description
Data validation and settings management using Python type hints.

Fast and extensible, pydantic plays nicely with your linters/IDE/brain.
Define how data should be in pure, canonical Python 3.7+; validate it
with pydantic.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Wed Jan 11 2023 Grigory Ustinov <grenka@altlinux.org> 1.10.4-alt1
- Automatically updated to 1.10.4 (Closes: #44879).
- Build without check.

* Sun Sep 18 2022 Grigory Ustinov <grenka@altlinux.org> 1.10.2-alt4
- Build with Cython.
- Update description.
- Use modern %%pyproject macros.
- Add extra BuildRequires for tests.
- Great thanks for ancieg@.

* Sun Sep 18 2022 Anton Zhukharev <ancieg@altlinux.org> 1.10.2-alt3
- rollback to 1.10.2-alt1 state

* Sun Sep 18 2022 Anton Zhukharev <ancieg@altlinux.org> 1.10.2-alt2
- build with Cython
- update description
- use modern %%pyproject macros
- reformat and clean up spec

* Tue Sep 13 2022 Grigory Ustinov <grenka@altlinux.org> 1.10.2-alt1
- Initial build for Sisyphus.
