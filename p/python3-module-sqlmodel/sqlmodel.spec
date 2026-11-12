%define _unpackaged_files_terminate_build 1
%define pypi_name sqlmodel
%define mod_name %pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 0.0.49
Release: alt1

Summary: SQL databases in Python, designed for simplicity, compatibility, and robustness
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sqlmodel/
Vcs: https://github.com/fastapi/sqlmodel
BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
# No +extra subpackages of these exist in Sisyphus: the plain packages are
# required instead (greenlet is what the asyncio extra of sqlalchemy adds).
%pyproject_configure_with_check_filter 'sqlalchemy$' 'psycopg$' 'pymysql$'
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-psycopg
BuildRequires: python3-module-pymysql
BuildRequires: python3-module-black
BuildRequires: python3-module-greenlet
BuildRequires: python3-module-pytest-timeout
%endif
%pyproject_configure_pypi_package

%description
SQLModel is a library for interacting with SQL databases from Python code,
with Python objects. It is designed to be intuitive, easy to use, highly
compatible, and robust.

SQLModel is based on Python type annotations, and powered by Pydantic and
SQLAlchemy.

The key features are:

* Intuitive to write: Great editor support. Completion everywhere. Less time
  debugging. Designed to be easy to use and learn. Less time reading docs.
* Easy to use: It has sensible defaults and does a lot of work underneath to
  simplify the code you write.
* Compatible: It is designed to be compatible with FastAPI, Pydantic, and
  SQLAlchemy.
* Extensible: You have all the power of SQLAlchemy and Pydantic underneath.
* Short: Minimize code duplication. A single type annotation does a lot of
  work. No need to duplicate models in SQLAlchemy and Pydantic.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH="$PYTHONPATH:$(realpath ./)"
%pyproject_run_pytest --session-timeout=600 -q -Wignore tests

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.49-alt1
- Updated to 0.0.49.

* Sun Oct 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.48-alt1
- Updated to 0.0.48.

* Thu Sep 24 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.47-alt1
- Updated to 0.0.47.

* Wed Sep 23 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.45-alt1
- Updated to 0.0.45.

* Fri Sep 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.42-alt1
- Updated to 0.0.42.

* Fri Jul 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.39-alt1
- Updated to 0.0.39.

* Tue Apr 07 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.38-alt1
- Updated to 0.0.38.

* Tue Mar 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.37-alt1
- Updated to 0.0.37.

* Thu Feb 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.33-alt1
- Updated to 0.0.33.

* Tue Feb 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.32-alt1
- Updated to 0.0.32.

* Mon Dec 29 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.31-alt1
- Updated to 0.0.31.

* Thu Oct 16 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.27-alt1
- Updated to 0.0.27.

* Tue Sep 23 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.25-alt1
- Updated to 0.0.25.

* Mon Mar 10 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.24-alt1
- Updated to 0.0.24.

* Tue Oct 15 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.22-alt1
- Initial build for ALT Sisyphus.

