%define  oname numba

# check runs 3 hours on x86_64
# FAIL: test_nonsense_gdb_binary (numba.tests.test_cli.TestGDBCLIInfoBrokenGdbs.test_nonsense_gdb_binary)
# FAIL: tests_numba_types (numba.tests.test_moved_modules.TestMovedModule.tests_numba_types)
# FAIL: test_record_arg_transform (numba.tests.test_record_dtype.TestRecordDtype.test_record_arg_transform)
# FAIL: test_record_arg_transform (numba.tests.test_record_dtype.TestRecordDtypeWithDispatcher.test_record_arg_transform)
# FAIL: test_record_arg_transform (numba.tests.test_record_dtype.TestRecordDtypeWithStructArrays.test_record_arg_transform)
# FAIL: test_record_arg_transform (numba.tests.test_record_dtype.TestRecordDtypeWithStructArraysAndDispatcher.test_record_arg_transform)
# FAIL: test_has_no_error (numba.tests.test_sysinfo.TestSysInfo.test_has_no_error)
# Ran 10356 tests in 11587.148s
# FAILED (failures=7, skipped=643, expected failures=20)
%def_without check

Name:    python3-module-%oname
Version: 0.59.1
Release: alt1

Summary: A Just-In-Time Compiler for Numerical Functions in Python

License: BSD
Group:   Development/Python3
URL:     https://pypi.org/project/numba

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libgomp-devel libnumpy-py3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-llvmlite
BuildRequires: python3-module-numpy-testing
%endif

Source:  %name-%version.tar

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/tests/pycc_distutils_usecase/

%add_python3_req_skip numba_rvsdg.core.datastructures
%add_python3_req_skip numba_rvsdg.core.datastructures.basic_block
%add_python3_req_skip numba_rvsdg.core.datastructures.byte_flow
%add_python3_req_skip numba_rvsdg.core.datastructures.scfg
%add_python3_req_skip numba_rvsdg.rendering.rendering

%description
Numba is an open source, NumPy-aware optimizing compiler for Python sponsored by
Anaconda, Inc. It uses the LLVM compiler project to generate machine code from
Python syntax.

Numba can compile a large subset of numerically-focused Python, including many
NumPy functions. Additionally, Numba has support for automatic parallelization
of loops, generation of GPU-accelerated code, and creation of ufuncs and
C callbacks.

%prep
%setup
sed -i 's/@VERSION@/%version/' setup.py
sed -i 's|"version": "0+unknown"|"version": "%version"|' versioneer.py

%ifarch %e2k
# error: misspelling pragma string
sed -i "/omp parallel/s/),/)/" numba/np/ufunc/omppool.cpp
%endif

%build
%pyproject_build

%install
%pyproject_install

mv %buildroot%_bindir/numba %buildroot%_bindir/numba3

%check
mkdir emtpytestdir
pushd emtpytestdir
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m numba.runtests -v
popd

%files
%doc CHANGE_LOG *.rst
%_bindir/numba3
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri Jul 19 2024 Grigory Ustinov <grenka@altlinux.org> 0.59.1-alt1
- Build new version.

* Fri Dec 22 2023 Grigory Ustinov <grenka@altlinux.org> 0.59.0-alt0.rc1
- Build new version.

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 0.57.1-alt2
- Fixed build with numpy 1.25.

* Mon Jul 17 2023 Grigory Ustinov <grenka@altlinux.org> 0.57.1-alt1
- Automatically updated to 0.57.1.

* Wed May 03 2023 Grigory Ustinov <grenka@altlinux.org> 0.57.0-alt1
- Automatically updated to 0.57.0.

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.56.4-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Fri Nov 04 2022 Grigory Ustinov <grenka@altlinux.org> 0.56.4-alt1
- Automatically updated to 0.56.4.

* Fri Oct 14 2022 Grigory Ustinov <grenka@altlinux.org> 0.56.3-alt1
- Automatically updated to 0.56.3.

* Mon Sep 12 2022 Grigory Ustinov <grenka@altlinux.org> 0.56.2-alt1
- Automatically updated to 0.56.2.

* Fri Aug 05 2022 Grigory Ustinov <grenka@altlinux.org> 0.56.0-alt1.1
- Fix tags filter.

* Mon Aug 01 2022 Grigory Ustinov <grenka@altlinux.org> 0.56.0-alt1
- Build new version.
- Fix building on %%e2k (thx to ilyakurdyukov@).

* Tue Feb 08 2022 Grigory Ustinov <grenka@altlinux.org> 0.55.1-alt1
- Build new version.

* Tue Jan 11 2022 Grigory Ustinov <grenka@altlinux.org> 0.54.1-alt1
- Build new version.

* Sat Apr 10 2021 Grigory Ustinov <grenka@altlinux.org> 0.53.1-alt1
- Build new version.

* Mon Mar 15 2021 Grigory Ustinov <grenka@altlinux.org> 0.53.0-alt1
- Build new version. (Closes: #39744).

* Sun Feb 14 2021 Grigory Ustinov <grenka@altlinux.org> 0.52.0-alt2
- Fixed build with python3.9.

* Wed Dec 02 2020 Grigory Ustinov <grenka@altlinux.org> 0.52.0-alt1
- Build new version.

* Sun Oct 04 2020 Grigory Ustinov <grenka@altlinux.org> 0.51.2-alt1
- Build new version.

* Sat Jun 27 2020 Grigory Ustinov <grenka@altlinux.org> 0.50.1-alt1
- Build new version.

* Wed Dec 18 2019 Grigory Ustinov <grenka@altlinux.org> 0.46.0-alt1
- Build new version.

* Thu Sep 05 2019 Grigory Ustinov <grenka@altlinux.org> 0.45.1-alt1
- Initial build for Sisyphus (Closes: #35680).
