%define _unpackaged_files_terminate_build 1

%def_with check
%global pypi_name fast-depends

Name: python3-module-%pypi_name
Version: 3.0.8
Release: alt1

Summary: Extracted FastAPI Dependency Injection System
License: MIT
Group: Development/Python3
BuildArch: noarch

VCS: https://github.com/Lancetnik/FastDepends
Url: https://lancetnik.github.io/FastDepends/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-uv-build

%if_with check
BuildRequires: python3-module-anyio
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-dirty-equals
%endif

%description
FastDepends -  FastAPI Dependency  Injection system  extracted from  FastAPI and
cleared of all HTTP  logic. This is a small library which  provides you with the
ability to use lovely FastAPI interfaces in your own projects or tools.

Thanks  to fastapi  and pydantic  projects  for this  great functionality.  This
package is  just a small  change of the original  FastAPI sources to  provide DI
functionality in a pure-Python way.

Async and sync modes are both supported.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.md
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir_noarch/%{pep427_name %pypi_name}

%changelog
* Fri Mar 20 2026 Egor Ignatov <egori@altlinux.org> 3.0.8-alt1
- New version 3.0.8.

* Sun Dec 07 2025 Egor Ignatov <egori@altlinux.org> 3.0.5-alt1
- New version 3.0.5.

* Thu Nov 06 2025 Egor Ignatov <egori@altlinux.org> 3.0.3-alt1
- New version 3.0.3.

* Tue Mar 18 2025 Egor Ignatov <egori@altlinux.org> 2.4.12-alt2
- Fix FTBFS: Add python3-module-pytest BR.

* Thu Nov 28 2024 Egor Ignatov <egori@altlinux.org> 2.4.12-alt1
- First build for ALT.
