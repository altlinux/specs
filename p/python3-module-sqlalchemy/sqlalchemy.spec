%define _unpackaged_files_terminate_build 1
%define pypi_name sqlalchemy
%define mod_name %pypi_name

# %%python3_set_limited_api not supported yet

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.51
Release: alt1

Summary: Python SQL toolkit and Object Relational Mapper
License: MIT
Group: Development/Python
Url: https://pypi.org/project/sqlalchemy
Vcs: https://github.com/sqlalchemy/sqlalchemy
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%py3_provides SQLAlchemy
Provides: python3-module-SQLAlchemy = %EVR
Obsoletes: python3-module-SQLAlchemy
# merged into main
Provides: python3-module-sqlalchemy-tests = %EVR
Obsoletes: python3-module-sqlalchemy-tests <= %EVR
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# Make sure that at least the Python built-in sqlite driver
# is present (and can be used by SQLAlchemy--among other things--
# in various tests, like in the tests for sphinx).
Requires: python3-modules-sqlite3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra asyncio
%pyproject_builddeps_check
%endif

%description
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns,
designed for efficient and high-performing database access, adapted into a
simple and Pythonic domain language.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
# https://setuptools.pypa.io/en/latest/deprecated/commands.html#release-tagging-options
%pyproject_build --backend-config-settings='{"--build-option": ["egg_info", "--tag-build=''", "--no-date"]}'

%install
%pyproject_install

%check
%pyproject_run_pytest -m "not memory_intensive and not mypy and not timing_intensive" test -n4

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 16 2026 Stanislav Levin <slev@altlinux.org> 2.0.51-alt1
- 2.0.50 -> 2.0.51

* Mon May 25 2026 Stanislav Levin <slev@altlinux.org> 2.0.50-alt1
- 2.0.49 -> 2.0.50.

* Mon Apr 06 2026 Stanislav Levin <slev@altlinux.org> 2.0.49-alt1
- 2.0.48 -> 2.0.49.

* Tue Mar 31 2026 Stanislav Levin <slev@altlinux.org> 2.0.48-alt3
- Undone Python vandalism.

* Tue Mar 03 2026 Stanislav Levin <slev@altlinux.org> 2.0.48-alt1
- 2.0.47 -> 2.0.48.

* Fri Feb 27 2026 Stanislav Levin <slev@altlinux.org> 2.0.47-alt1
- 2.0.46 -> 2.0.47.

* Fri Feb 06 2026 Stanislav Levin <slev@altlinux.org> 2.0.46-alt1
- 2.0.45 -> 2.0.46.

* Wed Dec 10 2025 Stanislav Levin <slev@altlinux.org> 2.0.45-alt1
- 2.0.44 -> 2.0.45.

* Fri Oct 31 2025 Stanislav Levin <slev@altlinux.org> 2.0.44-alt2
- NMU: added missing conditional runtime dependency on greenlet.

* Thu Oct 30 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.44-alt1
- 2.0.44 released

* Wed Sep 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.43-alt1
- 2.0.43 released

* Thu Jul 31 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.42-alt1
- 2.0.42 released

* Fri May 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.41-alt1
- 2.0.41 released

* Wed Apr 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.40-alt1
- 2.0.40 released

* Wed Mar 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.39-alt1
- 2.0.39 released

* Thu Jan 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.37-alt1
- 2.0.37 released

* Wed Nov 13 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.36-alt1
- 2.0.36 released

* Fri Sep 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.34-alt1
- 2.0.34 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.31-alt1
- 2.0.31 released

* Fri Apr 26 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.29-alt1
- 2.0.29 released

* Mon Mar 18 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.28-alt1
- 2.0.28 released

* Thu Feb 15 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.27-alt1
- 2.0.27 released

* Mon Dec 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.23-alt1
- 2.0.23 released

* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.22-alt1
- 2.0.22 released
- revert unwarranted subpackage merge made in previous release

* Wed Jul 12 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 2.0.18-alt1.1
- NMU: Merged subpackage with test back into main package to avoid dependency
  from main package on subpackage with tests

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.18-alt1
- 2.0.18 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.12-alt1
- 2.0.12 released

* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.4-alt1
- 2.0.4 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.44-alt1
- 1.4.44 released

* Mon Nov  7 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.43-alt1
- 1.4.43 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.40-alt1
- 1.4.40 released

* Fri Jul 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.39-alt1
- 1.4.39

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.36-alt1
- 1.4.36

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.31-alt1
- 1.4.31

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.25-alt1
- 1.4.25

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.22-alt1
- 1.4.22 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.13-alt1
- 1.4.13

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.23-alt1
- 1.3.23

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.20-alt2
- build python3 package separately

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.20-alt1
- 1.3.20

* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.19-alt1
- 1.3.19

* Tue Jul 07 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.18-alt1
- 1.3.18

* Mon Sep 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.8-alt1
- Version updated to 1.3.8

* Thu Jan 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.15-alt1
- 1.2.15

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.12-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Fri Apr 15 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt2
- Make sure that at least the Python built-in sqlite driver is present
  (and can be used by SQLAlchemy whenever SQLAlchemy is installed;
  among other things, it's useful for tests, like in sphinx).

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt1.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1
- Version 1.0.8

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Version 1.0.2

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.b3
- Version 1.0.0b3

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.b1
- Version 1.0.0b1

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1
- Version 0.9.8

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1
- Version 0.9.7

* Thu Dec 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt2
- Extracted tests into separated packages

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1
- Version 0.8.3

* Thu Mar 21 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7.10-alt1.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.10-alt1
- Version 0.7.10

* Sat Sep 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.8-alt1
- Version 0.7.8

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt3
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2
- Added provides of SQLAlchemy

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2 (ALT #23768)
- Moved tests into separate package

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.1
- Rebuilt with python 2.6

* Mon Feb 23 2009 Gennady Kovalev <gik@altlinux.ru> 0.5.2-alt1
- 0.5.2 release

* Sun Jan 11 2009 Gennady Kovalev <gik@altlinux.ru> 0.5.0-alt1
- 0.5.0 release

* Mon Jan 05 2009 Gennady Kovalev <gik@altlinux.ru> 0.5.0rc4-alt1
- 0.5.0rc4

* Sun Oct 12 2008 Gennady Kovalev <gik@altlinux.ru> 0.5.0rc1-alt1
- 0.5.0rc1

* Fri Aug 01 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.7p1-alt1
- 0.4.7p1 release

* Sun May 04 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.5-alt1
- 0.4.5 release

* Wed Jan 09 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.2b-alt1
- 0.4.2b release

* Mon Jan 07 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.2a-alt1
- 0.4.2a release

* Wed Jan 02 2008 Gennady Kovalev <gik@altlinux.ru> 0.4.2-alt1
- 0.4.2 release

* Thu Nov 15 2007 Gennady Kovalev <gik@altlinux.ru> 0.4.0-alt1
- 0.4 release

* Sun Jun 18 2006 Alex V. Myltsev <avm@altlinux.ru> 0.2.3-alt1
- Initial build for Sisyphus.

