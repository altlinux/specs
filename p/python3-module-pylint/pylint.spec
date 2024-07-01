%define _unpackaged_files_terminate_build 1
%define pypi_name pylint
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.2.5
Release: alt1
Summary: Python code static checker
License: GPLv2+
Group: Development/Python3
Url: https://pypi.org/project/pylint/
Vcs: https://github.com/pylint-dev/pylint
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
Provides: pylint-py3 = %EVR
Obsoletes: pylint-py3 < %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%set_pyproject_deps_check_filter towncrier
%pyproject_builddeps_metadata_extra testutils
%pyproject_builddeps_metadata_extra spelling
%pyproject_builddeps_check
# PyEnchant's spelling dictionary
BuildRequires: hunspell-en_US
%endif

%description
Pylint is a static code analyser for Python 2 or 3. The latest version supports
Python 3.7.2 and above.

Pylint analyses your code without actually running it. It checks for errors,
enforces a coding standard, looks for code smells, and can make suggestions
about how the code could be refactored.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements_test_min.txt
%endif

%build
%pyproject_build

%install
%pyproject_install
# do not pack tests
rm -r %buildroot%python3_sitelibdir/pylint/test*

pushd %buildroot%_bindir
for i in $(ls); do
       mv $i $i.py3
done

%check
%pyproject_run_pytest -ra --benchmark-disable tests

%files
%doc README.rst
%_bindir/pylint.py3
%_bindir/pyreverse.py3
%_bindir/symilar.py3
%_bindir/pylint-config.py3
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 01 2024 Stanislav Levin <slev@altlinux.org> 3.2.5-alt1
- 3.2.4 -> 3.2.5.

* Wed Jun 26 2024 Stanislav Levin <slev@altlinux.org> 3.2.4-alt1
- 3.2.3 -> 3.2.4.

* Fri Jun 07 2024 Stanislav Levin <slev@altlinux.org> 3.2.3-alt1
- 3.2.2 -> 3.2.3.

* Mon May 20 2024 Stanislav Levin <slev@altlinux.org> 3.2.2-alt1
- 3.2.0 -> 3.2.2.

* Wed May 15 2024 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1
- 3.1.1 -> 3.2.0.

* Tue May 14 2024 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1
- 3.1.0 -> 3.1.1.

* Wed May 08 2024 Stanislav Levin <slev@altlinux.org> 3.1.0-alt2
- Fixed FTBFS (astroid 3.2.0).

* Mon Feb 26 2024 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 2.17.5 -> 3.1.0.

* Thu Jul 27 2023 Stanislav Levin <slev@altlinux.org> 2.17.5-alt1
- 2.17.4 -> 2.17.5.

* Tue May 16 2023 Stanislav Levin <slev@altlinux.org> 2.17.4-alt1
- 2.12.2 -> 2.17.4.

* Wed Apr 06 2022 Stanislav Levin <slev@altlinux.org> 2.12.2-alt2
- Fixed FTBFS (mccabe 0.7).

* Thu Jan 27 2022 Stanislav Levin <slev@altlinux.org> 2.12.2-alt1
- 2.8.2 -> 2.12.2.

* Wed May 26 2021 Grigory Ustinov <grenka@altlinux.org> 2.8.2-alt2
- Fixed FTBFS (cherry-picked 6f246a03346ea4f592c4d70002382eab1e89d219).

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 2.8.2-alt1
- 2.7.4 -> 2.8.2.

* Tue Mar 30 2021 Stanislav Levin <slev@altlinux.org> 2.7.4-alt1
- 2.7.2 -> 2.7.4.

* Wed Mar 24 2021 Stanislav Levin <slev@altlinux.org> 2.7.2-alt1
- 2.6.0 -> 2.7.2.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1
- 2.5.3 -> 2.6.0.

* Mon Aug 03 2020 Stanislav Levin <slev@altlinux.org> 2.5.3-alt1
- 2.4.4 -> 2.5.3.

* Sat Nov 16 2019 Stanislav Levin <slev@altlinux.org> 2.4.4-alt1
- 2.4.3 -> 2.4.4.

* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 2.4.3-alt1
- 2.4.2 -> 2.4.3.

* Wed Oct 16 2019 Stanislav Levin <slev@altlinux.org> 2.4.2-alt1
- 2.3.1 -> 2.4.2.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 2.3.1-alt1
- 2.2.2 -> 2.3.1.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 2.2.2-alt1
- 2.1.1 -> 2.2.2.

* Mon Sep 03 2018 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- 1.9.1 -> 2.1.1.
- Move Python3 module to a separated src package.

* Fri May 25 2018 Stanislav Levin <slev@altlinux.org> 1.9.1-alt1
- 1.7.4 -> 1.9.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.4-alt2
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.4-alt2
- Updated runtime dependencies.

* Wed Nov 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.4-alt1
- Updated to upstream version 1.7.4.

* Mon Sep 25 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.1-alt1
- Rebuild with universal build tag (aka ubt macros)

* Thu Jun 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.1-alt1
- Updated to upstream release 1.5.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1
- Version 1.4.4

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.1
- Added module for Python 3

* Wed Mar 19 2014 Timur Aitov <timonbl4@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.21.3-alt1.1
- Rebuild with Python-2.7

* Wed Sep 29 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.21.3-alt1
- 0.21.3
- run tests

* Mon Jun 14 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.21.1-alt1
- 0.21.1

* Fri May 14 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.21.0-alt1
- 0.21.0
- disable findreq for gui.py

* Fri Mar 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Fri Dec 18 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.0-alt1
- 0.19.0

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18.1-alt1.1
- Rebuilt with python 2.6

* Fri Sep 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.18.1-alt1
- 0.18.1

* Thu Mar 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Sun Mar 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Sun Feb 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.16.0-alt2
- use %%python_{build,install}

* Fri Jan 30 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Wed Oct 15 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Sun Oct 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.15.1-alt1
- 0.15.1
- spec cleanup
- don't package tests

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.12.2-alt3.1
- Rebuilt with python-2.5.

* Sat Dec 9 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 0.12.2-alt3
- Fixed requires/provides calculation

* Fri Dec 8 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 0.12.2-alt2
- Fixed dependencies

* Wed Dec 6 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 0.12.2-alt1
- Initial build for ALT Linux
