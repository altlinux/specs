%define _unpackaged_files_terminate_build 1
%define pypi_name Werkzeug
%define mod_name werkzeug

%def_with check

Name: python3-module-%mod_name
Version: 3.0.3
Release: alt1

Summary: Werkzeug is one of the most advanced WSGI utility modules
License: BSD-3-Clause
Group: Development/Python3
Url: https://palletsprojects.com/p/werkzeug/
Vcs: https://github.com/pallets/werkzeug

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# well-known PyPI name
Provides: python3-module-%pypi_name = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: /proc
%endif

%description
Werkzeug is a comprehensive WSGI web application library.
It began as a simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility libraries.

Flask wraps Werkzeug, using it to handle the details of WSGI while providing
more structure and patterns for defining powerful applications.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# skip: test_serving::test_reloader_sys_path (hangs up) and test_serving::test_exclude_patterns (always fails)
%pyproject_run_pytest -vra -k "not test_reloader_sys_path and not test_exclude_patterns"

%files
%doc LICENSE.txt CHANGES.rst README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 13 2024 Anton Zhukharev <ancieg@altlinux.org> 3.0.3-alt1
- Updated to 3.0.3.

* Thu Apr 11 2024 Anton Zhukharev <ancieg@altlinux.org> 3.0.2-alt2
- Fixed FTBFS (pytest-xprocess 1.0.1).

* Mon Mar 25 2024 Anton Zhukharev <ancieg@altlinux.org> 3.0.2-alt1
- Updated to 3.0.2.

* Wed Feb 07 2024 Anton Zhukharev <ancieg@altlinux.org> 3.0.1-alt2
- Fixed FTBFS.

* Wed Dec 06 2023 Anton Zhukharev <ancieg@altlinux.org> 3.0.1-alt1
- Updated to 3.0.1 (fixed CVE-2023-23934, CVE-2023-25577, CVE-2023-46136).

* Wed Feb 08 2023 Stanislav Levin <slev@altlinux.org> 2.2.2-alt2
- Fixed FTBFS (packaging 22).

* Fri Sep 16 2022 Danil Shein <dshein@altlinux.org> 2.2.2-alt1
- new version 2.2.2
  + migrate to pyproject macroses
  + reduce excluded tests list

* Thu Mar 03 2022 Danil Shein <dshein@altlinux.org> 2.0.3-alt1
- new version 0.16.1 -> 2.0.3
  + enable tests

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.16.1-alt2
- build only python3 package

* Tue Mar 24 2020 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1
- New version.
- Fix License tag according SPDX.
- Build from upstream tag.

* Fri Aug 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.15.5-alt1
- Version updated to 0.15.5

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.1-alt1
- Updated to upstream version 0.14.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.10.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Version 0.10.1

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1
- Version 0.9.6
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.1
- Fixed build

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.8.3-alt1
- 0.8.3 (ALT #28297);
- minor packaging improvements.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Sergey Alembekov <rt@altlinux.ru> 0.6.2-alt1
- Initial release for ALTLinux
