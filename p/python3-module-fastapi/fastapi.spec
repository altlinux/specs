%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi
%define module_name %pypi_name
%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 0.138.2
Release: alt1

Summary: FastAPI framework, high performance, easy to learn, fast to code, ready for production
License: MIT
Group: Development/Python3
Url: https://fastapi.tiangolo.com/
Vcs: https://github.com/fastapi/fastapi
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: clean_coverage_usage.py
Patch: %name-%version-alt.patch

# Manually manage extra dependencies with metadata.
AutoReq: yes, nopython3
# Some packages require fastapi-slim, but it's fastapi with the no installed
# certain requirements.
Provides: %name-slim = %EVR
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# Upstream says that Argon2 has superiority over bcrypt
# See https://github.com/fastapi/fastapi/pull/13917
BuildRequires: python3-module-argon2-cffi
BuildRequires: python3-module-pytest-timeout
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra all
%pyproject_builddeps_check
%endif

%description
FastAPI is a modern, fast (high-performance), web framework for
building APIs with Python based on standard Python type hints.

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

%add_python_extra standard
%add_python_extra standard-no-fastapi-cloud-cli
%add_python_extra all

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup tests
%endif

# Clean of the using coverage module, because we don't needs to it.
%SOURCE2 tests/

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- bash -s <<-'ENDTESTS'
# Create symbolic link to python_multipart in order to make 'multipart' import
# name for passing tests since it was deleted in the python3-module-multipart
# 0.0.20-alt2.
ln -s %python3_sitelibdir/python_multipart \
	.run_venv/lib/python3/site-packages/multipart
python3 -m pytest -vvv -Wignore --timeout=300 tests
ENDTESTS

%files
%doc README.md LICENSE docs
%_bindir/%pypi_name
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 01 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.138.2-alt1
- Updated to 0.138.2.

* Tue Jun 16 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.137.1-alt1
- Updated to 0.137.1.

* Fri Jun 05 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.136.3-alt1
- Updated to 0.136.3.

* Mon Apr 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.136.1-alt1
- Updated to 0.136.1.

* Sun Apr 19 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.136.0-alt1
- Updated to 0.136.0.

* Thu Apr 02 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.135.3-alt1
- Updated to 0.135.3.

* Tue Mar 24 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.135.2-alt1
- Updated to 0.135.2.

* Thu Mar 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.135.1-alt2
- Introduced subpackages needed to install FastAPI with its optional
  dependencies.

* Tue Mar 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.135.1-alt1
- Updated to 0.135.1.

* Tue Feb 24 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.133.0-alt1
- Updated to 0.133.0.

* Tue Feb 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.128.7-alt1
- Updated to 0.128.7.

* Mon Dec 29 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.128.0-alt1
- Updated to 0.128.0.

* Mon Dec 22 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.127.0-alt1
- Updated to 0.127.0.

* Fri Dec 19 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.125.0-alt1
- Updated to 0.125.0.

* Fri Dec 12 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.124.4-alt1
- Updated to 0.124.4.

* Sat Dec 06 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.124.0-alt1
- Updated to 0.124.0.

* Fri Dec 05 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.123.9-alt1
- Updated to 0.123.9.

* Thu Dec 04 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.123.7-alt1
- Updated to 0.123.7.

* Wed Dec 03 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.123.5-alt1
- Updated to 0.123.5.

* Tue Dec 02 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.123.4-alt1
- Updated to 0.123.4.

* Tue Oct 14 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.119.0-alt1
- Updated to 0.119.0.

* Tue Sep 30 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.118.0-alt1
- Updated to 0.118.0.

* Tue Sep 23 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.117.1-alt1
- Updated to 0.117.1.

* Thu Sep 18 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.116.2-alt1
- Updated to 0.116.2.

* Tue Sep 16 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.116.1-alt4
- Fixed FTBFS by skipping the failing test.

* Mon Jul 21 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.116.1-alt3
- Built with python3-module-python-multipart 0.0.20-alt2.

* Mon Jul 14 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.116.1-alt2
- Built with httpx 0.28.0 compatibility.

* Mon Jul 14 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.116.1-alt1
- Updated to 0.116.1.

* Tue Jul 08 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.116.0-alt1
- Updated to 0.116.0.

* Fri Jun 27 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.14-alt1
- Updated to 0.115.14.

* Thu Jun 19 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.13-alt1
- Updated to 0.115.13.

* Fri Apr 04 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.12-alt1
- Updated to 0.115.12.

* Mon Mar 03 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.11-alt1
- Updated to 0.115.11.

* Fri Feb 28 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.10-alt1
- Updated to 0.115.10.

* Thu Jan 30 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.8-alt1
- Updated to 0.115.8.

* Thu Jan 23 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.7-alt1
- Updated to 0.115.7.

* Tue Jan 14 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.6-alt2
- Fixed FTBFS: updated test_fastapi_cli test to pass with fastapi-cli==0.0.7.

* Sat Dec 14 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.6-alt1
- Updated to 0.115.6.

* Tue Oct 29 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.4-alt1
- Updated to 0.115.4.

* Fri Oct 25 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.3-alt2
- Built with python-multipart >= 0.0.13.

* Wed Oct 23 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.3-alt1
- Updated to 0.115.3.

* Tue Oct 15 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.2-alt1
- Updated to 0.115.2.

* Wed Sep 18 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.115.0-alt1
- Updated to 0.115.0.

* Mon Sep 16 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.114.2-alt1
- Updated to 0.114.2.

* Wed Sep 11 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.114.1-alt1
- Updated to 0.114.1.

* Mon Sep 09 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.114.0-alt1
- Updated to 0.114.0.

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
- 0.109.2 -> 0.110.0.

* Fri Feb 09 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.109.2-alt1
- 0.109.0 -> 0.109.2 (Fixed: CVE-2024-24762).

* Fri Jan 19 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.109.0-alt1
- 0.108.0 -> 0.109.0.

* Sun Dec 31 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.108.0-alt1
- 0.106.0 -> 0.108.0.

* Tue Dec 26 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.106.0-alt1
- 0.105.0 -> 0.106.0.

* Wed Dec 13 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.105.0-alt1
- 0.104.1 -> 0.105.0.

* Fri Nov 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.104.1-alt2
- Fix failed tests when build with pydantic >= 2.5.0.

* Mon Oct 30 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.104.1-alt1
- 0.104.0 -> 0.104.1.

* Sun Oct 22 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.104.0-alt1
- 0.103.2 -> 0.104.0.

* Fri Sep 29 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.103.2-alt1
- 0.103.1 -> 0.103.2.

* Sun Sep 03 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.103.1-alt1
- 0.103.0 -> 0.103.1.

* Sat Aug 26 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.103.0-alt1
- 0.102.0 -> 0.103.0.

* Fri Aug 25 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.102.0-alt1
- 0.101.1 -> 0.102.0.

* Tue Aug 15 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.101.1-alt1
- 0.99.1 -> 0.101.1.

* Thu Jul 27 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.99.1-alt2
- Skipped a dependency_gets_exception test to fix FTBFS.
- Stopped packaging of useless files.

* Mon Jul 03 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.99.1-alt1
- 0.99.0 -> 0.99.1.

* Sat Jul 01 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.99.0-alt1
- 0.98.0 -> 0.99.0.

* Thu Jun 29 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.98.0-alt1
- 0.97.0 -> 0.98.0.

* Mon Jun 12 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.97.0-alt1
- 0.96.1 -> 0.97.0.

* Sun Jun 11 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.96.1-alt1
- 0.96.0 -> 0.96.1.

* Sat Jun 03 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.96.0-alt1
- 0.95.2 -> 0.96.0.

* Tue May 16 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.95.2-alt1
- 0.95.1 -> 0.95.2.

* Wed May 10 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.95.1-alt1
- 0.90.1 -> 0.95.1.

* Fri Feb 10 2023 Anton Zhukharev <ancieg@altlinux.org> 0.90.1-alt1
- 0.87.0 -> 0.90.1.

* Tue Nov 15 2022 Anton Zhukharev <ancieg@altlinux.org> 0.87.0-alt1
- 0.85.0 -> 0.87.0.

* Sun Sep 18 2022 Anton Zhukharev <ancieg@altlinux.org> 0.85.0-alt1
- Initial build for sisyphus (thanks Alexandr Shashkin <dutyrok@altlinux.org>).

