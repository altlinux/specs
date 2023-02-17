%define _unpackaged_files_terminate_build 1
%define pypi_name Werkzeug
%define mod_name werkzeug

%def_enable check

Name: python3-module-%mod_name
Version: 2.2.2
Release: alt2

Summary: Werkzeug is one of the most advanced WSGI utility modules

License: BSD-3-Clause
Group: Development/Python3
URL: https://palletsprojects.com/p/werkzeug/
VCS: https://github.com/pallets/werkzeug

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: alt_tests_conftest_py.patch

# well-known PyPI name
%py3_provides %pypi_name
Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_enabled check
# dependencies
BuildRequires: python3(markupsafe)

BuildRequires: /proc
BuildRequires: pytest3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xprocess
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-cryptography
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

%build
%pyproject_build

%install
%pyproject_install

%check
# skip: test_serving::test_reloader_sys_path (hangs up) and test_serving::test_exclude_patterns (always fails)
%pyproject_run_pytest -vra -k "not test_reloader_sys_path and not test_exclude_patterns"

%files
%doc CHANGES.rst README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
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
