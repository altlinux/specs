%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi

%def_with check

Name: python3-module-%pypi_name
Version: 0.95.1
Release: alt1

Summary: FastAPI framework, high performance, easy to learn, fast to code, ready for production
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi
Vcs: https://github.com/tiangolo/fastapi

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: fastapi-0.95.1-alt-email_tests.patch
Patch1: fastapi-0.95.1-alt-fix-databases-tests-connections.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter ruff types-
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check

# BuildRequires: python3(multipart)
# FastAPI based on Starlette, which requires 'python-multipart' exactly.
# See https://bugzilla.altlinux.org/43483 for more information.
BuildRequires: python3(python-multipart)
%endif

%description
FastAPI is a modern, fast (high-performance), web framework for
building APIs with Python 3.7+ based on standard Python type hints.

The key features are:
- Fast: Very high performance, on par with NodeJS and Go (thanks to
  Starlette and Pydantic). One of the fastest Python frameworks
  available.
- Fast to code: Increase the speed to develop features by about 200%%
  to 300%%.
- Fewer bugs: Reduce about 40%% of human (developer) induced errors.
- Intuitive: Great editor support. Completion everywhere. Less time
  debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each
  parameter declaration. Fewer bugs.
- Robust: Get production-ready code. With automatic interactive
  documentation.
- Standards-based: Based on (and fully compatible with) the open
  standards for APIs: OpenAPI (previously known as Swagger) and JSON
  Schema.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# Due to too new sqlalchemy databases' sqlite backend is broken.
# Temporary skip this test.
sed -i "1iimport pytest" \
	tests/test_tutorial/test_async_sql_databases/test_tutorial001.py
sed -i "/def test_create_read()/i@pytest.mark.skip(reason='workaround')" \
	tests/test_tutorial/test_async_sql_databases/test_tutorial001.py
# Ignore SQLAlchemy deprecation warnings until the package been updated.
%pyproject_run_pytest -vra -W ignore::sqlalchemy.exc.MovedIn20Warning

%files
%doc README.* CONTRIBUTING.md SECURITY.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 10 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.95.1-alt1
- 0.90.1 -> 0.95.1
- reformat description
- add Vcs tag
- do not ship MIT license file
- temporary ignore problematic tests

* Fri Feb 10 2023 Anton Zhukharev <ancieg@altlinux.org> 0.90.1-alt1
- 0.87.0 -> 0.90.1

* Tue Nov 15 2022 Anton Zhukharev <ancieg@altlinux.org> 0.87.0-alt1
- 0.85.0 -> 0.87.0

* Sat Sep 18 2022 Anton Zhukharev <ancieg@altlinux.org> 0.85.0-alt1
- Initial build for sisyphus (thanks Alexandr Shashkin <dutyrok@altlinux.org>)

