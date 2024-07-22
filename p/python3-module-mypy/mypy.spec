%define _unpackaged_files_terminate_build 1
%define pypi_name mypy
%def_with check

# mypyc doesn't work on 32bit arches
# https://github.com/mypyc/mypyc/issues/760
%ifarch %ix86 armh
%def_without mypyc
%else
%def_with mypyc
%endif

Name: python3-module-%pypi_name
Version: 1.11.0
Release: alt1
Summary: Optional static typing for Python 3 and 2 (PEP 484)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mypy/
VCS: https://github.com/python/mypy
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_build_filter types-
%pyproject_builddeps_build
%if_with check
BuildRequires: /proc
BuildRequires: gcc-c++
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# required for mypy/test/testpep561.py
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-editables
%endif
# Needed to generate the man pages
BuildRequires: help2man

%description
Mypy is an optional static type checker for Python.  You can add type
hints to your Python programs using the upcoming standard for type
annotations introduced in Python 3.5 beta 1 (PEP 484), and use mypy to
type check them statically. Find bugs in your programs without even
running them!

%if_with mypyc
%package -n python3-module-mypyc
Summary: Mypy to Python C Extension Compiler
Group: Development/Python3
Requires: python3-module-%pypi_name = %EVR
Requires: python3-dev

%description -n python3-module-mypyc
Mypyc is a compiler that compiles mypy-annotated, statically typed Python
modules into CPython C extensions. Currently our primary focus is on making
mypy faster through compilation -- the default mypy wheels are compiled with
mypyc. Compiled mypy is about 4x faster than without compilation.
%endif

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.in
%endif

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
    mkdir -p %buildroot%python3_sitelibdir
    mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

mv %buildroot%python3_sitelibdir/mypy/{typeshed,mypy_typeshed}
ln -sr %buildroot%python3_sitelibdir/mypy/{mypy_typeshed,typeshed}

# Generate man pages
mkdir -p %buildroot%_man1dir

PYTHONPATH=%buildroot%python3_sitelibdir \
    help2man --no-info --version-string 'mypy %version-dev' \
        --no-discard-stderr -o %buildroot%_man1dir/mypy.1 \
        %buildroot%_bindir/mypy

PYTHONPATH=%buildroot%python3_sitelibdir \
    help2man --no-info --version-string 'mypy stubgen %version-dev' \
        --no-discard-stderr -o %buildroot%_man1dir/stubgen.1 \
        %buildroot%_bindir/stubgen

# don't package tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/test/
rm -r %buildroot%python3_sitelibdir/mypyc/external/googletest/
rm -r %buildroot%python3_sitelibdir/mypyc/test/
rm -r %buildroot%python3_sitelibdir/mypyc/test-data/

%if_without mypyc
rm %buildroot%_bindir/mypyc
rm -r %buildroot%python3_sitelibdir/mypyc/
%endif

%check
# https://github.com/mypyc/mypyc/issues/760
%ifarch %ix86 armh
%define pytest_args --ignore mypyc/test
%endif
%pyproject_run_pytest -ra %{?pytest_args}

%files
%doc README.md
%python3_sitelibdir/mypy/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_bindir/mypy
%_bindir/dmypy
%_bindir/stubgen
%_bindir/stubtest
%_man1dir/mypy.1*
%_man1dir/stubgen.1*

%if_with mypyc
%files -n python3-module-mypyc
%python3_sitelibdir/mypyc/
%_bindir/mypyc
# Build script for mypyc C runtime library unit tests
%exclude %python3_sitelibdir/mypyc/lib-rt/setup.py
%exclude %python3_sitelibdir/mypyc/lib-rt/__pycache__/setup.*
%endif

%changelog
* Mon Jul 22 2024 Stanislav Levin <slev@altlinux.org> 1.11.0-alt1
- 1.10.1 -> 1.11.0.

* Tue Jun 25 2024 Stanislav Levin <slev@altlinux.org> 1.10.1-alt1
- 1.10.0 -> 1.10.1.

* Thu Apr 25 2024 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1
- 1.9.0 -> 1.10.0.

* Mon Mar 18 2024 Stanislav Levin <slev@altlinux.org> 1.9.0-alt2
- Fixed FTBFS (hatchling 1.22.0).

* Mon Mar 11 2024 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.8.0 -> 1.9.0.

* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 1.8.0-alt3
- Fixed FTBFS (typing_extensions 4.10.0).

* Tue Feb 20 2024 Stanislav Levin <slev@altlinux.org> 1.8.0-alt2
- Fixed FTBFS (hatchling 1.21.0).

* Fri Dec 22 2023 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1
- 1.7.1 -> 1.8.0.

* Fri Dec 08 2023 Stanislav Levin <slev@altlinux.org> 1.7.1-alt1
- 1.7.0 -> 1.7.1.

* Tue Nov 14 2023 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.6.1 -> 1.7.0.

* Fri Oct 27 2023 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1
- 1.5.1 -> 1.6.1.

* Thu Aug 17 2023 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1
- 1.5.0 -> 1.5.1.

* Fri Aug 11 2023 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.4.1 -> 1.5.0.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 1.3.0 -> 1.4.1.

* Thu Jun 15 2023 Stanislav Levin <slev@altlinux.org> 1.3.0-alt2
- Fixed FTBFS (typing-extensions 4.6.3).

* Thu May 11 2023 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.1 -> 1.2.0.

* Tue Mar 07 2023 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.1 -> 1.1.1.

* Tue Feb 21 2023 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- 0.991 -> 1.0.1.

* Tue Nov 15 2022 Stanislav Levin <slev@altlinux.org> 0.991-alt1
- 0.990 -> 0.991.

* Wed Nov 09 2022 Stanislav Levin <slev@altlinux.org> 0.990-alt1
- 0.982 -> 0.990.

* Tue Oct 04 2022 Stanislav Levin <slev@altlinux.org> 0.982-alt1
- 0.981 -> 0.982.

* Tue Sep 27 2022 Stanislav Levin <slev@altlinux.org> 0.981-alt1
- 0.971 -> 0.981.

* Fri Sep 23 2022 Stanislav Levin <slev@altlinux.org> 0.971-alt2
- Removed build dependency on nonexistent typeshed.

* Thu Aug 18 2022 Stanislav Levin <slev@altlinux.org> 0.971-alt1
- 0.942 -> 0.971.

* Fri Mar 25 2022 Stanislav Levin <slev@altlinux.org> 0.942-alt1
- 0.931 -> 0.942.

* Thu Mar 03 2022 Stanislav Levin <slev@altlinux.org> 0.931-alt2
- Fixed FTBFS (pytest-xdist 2.5.0).

* Wed Jan 26 2022 Stanislav Levin <slev@altlinux.org> 0.931-alt1
- 0.910 -> 0.931.

* Wed Oct 20 2021 Stanislav Levin <slev@altlinux.org> 0.910-alt2
- Fixed FTBFS (pip 21.3).

* Wed Jun 23 2021 Stanislav Levin <slev@altlinux.org> 0.910-alt1
- 0.812 -> 0.910.

* Thu May 20 2021 Fr. Br. George <george@altlinux.ru> 0.812-alt2
- Fix tempfile.TemporaryDirectory() naming in tests

* Tue Mar 23 2021 Stanislav Levin <slev@altlinux.org> 0.812-alt1
- 0.790 -> 0.812.

* Wed Oct 28 2020 Stanislav Levin <slev@altlinux.org> 0.790-alt2
- Fixed FTBFS(virtualenv 20.1.0).

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 0.790-alt1
- 0.782 -> 0.790.

* Tue Sep 15 2020 Stanislav Levin <slev@altlinux.org> 0.782-alt1
- 0.701 -> 0.782.

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.701-alt1
- Initial build for Sisyphus
