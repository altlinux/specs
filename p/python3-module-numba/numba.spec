%define  oname numba

# check runs more then half of a day
%def_without check

Name:    python3-module-%oname
Version: 0.56.4
Release: alt1

Summary: A Just-In-Time Compiler for Numerical Functions in Python

License: BSD
Group:   Development/Python3
URL:     https://pypi.org/project/numba

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libgomp-devel libnumpy-py3-devel

Source:  %name-%version.tar

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
sed -i 's|"version": "0+unknown"|"version": "%version"|' versioneer.py

%ifarch %e2k
# error: misspelling pragma string
sed -i "/omp parallel/s/),/)/" numba/np/ufunc/omppool.cpp
%endif

%build
%python3_build

%install
%python3_install

mv %buildroot%_bindir/numba %buildroot%_bindir/numba3
mv %buildroot%_bindir/pycc %buildroot%_bindir/pycc3

%check
mkdir emtpytestdir
pushd emtpytestdir
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m numba.runtests -v
popd

%files
%doc CHANGE_LOG *.rst
%_bindir/numba3
%_bindir/pycc3
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
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
