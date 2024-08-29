%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi

%def_with check

Name: python3-module-%pypi_name
Version: 0.112.2
Release: alt1

Summary: FastAPI framework, high performance, easy to learn, fast to code, ready for production
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi
Vcs: https://github.com/tiangolo/fastapi

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: clean_coverage_usage.py
Patch0: fastapi-0.95.1-alt-fix-databases-tests-connections.patch

# Some packages require fastapi-slim, but it's fastapi with the no installed
# certain requirements.
Provides: %name-slim = %EVR
# Filter fastapi-cli, because it's needed for managing fastapi project.
%add_pyproject_deps_runtime_filter fastapi-cli
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata -- --extra all
%pyproject_builddeps_check
%endif

%description
FastAPI is a modern, fast (high-performance), web framework for
building APIs with Python 3.8+ based on standard Python type hints.

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
%if_with check
cat requirements-docs-tests.txt requirements-tests.txt > alt-requirements-tests.txt
%pyproject_deps_resync_check_pipreqfile alt-requirements-tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Clean of the using coverage module, because we don't needs to it.
%SOURCE2 tests/
# test_async_sql_databases/test_tutorial001.py::test_create_read:
# Due to too new sqlalchemy databases' sqlite backend is broken.
# Temporary skip this test.
%pyproject_run_pytest -q -Wignore \
    --deselect='tests/test_tutorial/test_async_sql_databases/test_tutorial001.py::test_create_read' \
    tests

%files
%doc README.*
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 29 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.112.2-alt1
- Updated to 0.112.2.

* Mon Aug 05 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.112.0-alt1
- Updated to 0.112.0.

* Sun May 19 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.111.0-alt1
- 0.110.3 -> 0.111.0.

* Thu May 02 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.110.3-alt1
- 0.110.2 -> 0.110.3.

* Sun Apr 21 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.110.2-alt1
- 0.110.1 -> 0.110.2.

* Thu Apr 04 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.110.1-alt1
- 0.110.0 -> 0.110.1.

* Mon Mar 04 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.110.0-alt1
- 0.109.2 -> 0.110.0

* Fri Feb 09 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.109.2-alt1
- 0.109.0 -> 0.109.2 (Fixed: CVE-2024-24762)

* Fri Jan 19 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.109.0-alt1
- 0.108.0 -> 0.109.0

* Sun Dec 31 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.108.0-alt1
- 0.106.0 -> 0.108.0

* Tue Dec 26 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.106.0-alt1
- 0.105.0 -> 0.106.0

* Wed Dec 13 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.105.0-alt1
- 0.104.1 -> 0.105.0

* Fri Nov 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.104.1-alt2
- Fix failed tests when build with pydantic >= 2.5.0

* Mon Oct 30 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.104.1-alt1
- 0.104.0 -> 0.104.1

* Sun Oct 22 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.104.0-alt1
- 0.103.2 -> 0.104.0

* Fri Sep 29 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.103.2-alt1
- 0.103.1 -> 0.103.2

* Sun Sep 03 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.103.1-alt1
- 0.103.0 -> 0.103.1

* Sat Aug 26 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.103.0-alt1
- 0.102.0 -> 0.103.0

* Fri Aug 25 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.102.0-alt1
- 0.101.1 -> 0.102.0

* Tue Aug 15 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.101.1-alt1
- 0.99.1 -> 0.101.1

* Thu Jul 27 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.99.1-alt2
- Skipped a dependency_gets_exception test to fix FTBFS
- Stopped packaging of useless files

* Mon Jul 03 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.99.1-alt1
- 0.99.0 -> 0.99.1

* Sat Jul 01 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.99.0-alt1
- 0.98.0 -> 0.99.0

* Thu Jun 29 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.98.0-alt1
- 0.97.0 -> 0.98.0

* Mon Jun 12 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.97.0-alt1
- 0.96.1 -> 0.97.0

* Sun Jun 11 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.96.1-alt1
- 0.96.0 -> 0.96.1

* Sat Jun 03 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.96.0-alt1
- 0.95.2 -> 0.96.0

* Tue May 16 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.95.2-alt1
- 0.95.1 -> 0.95.2

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

