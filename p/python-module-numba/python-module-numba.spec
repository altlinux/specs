%define  oname numba

Name:    python-module-%oname
Version: 0.46.0
Release: alt1

Summary: A Just-In-Time Compiler for Numerical Functions in Python

License: BSD
Group:   Development/Python
URL:     https://pypi.org/project/numba

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools
BuildRequires: gcc-c++ libgomp9-devel libnumpy-devel libnumpy-py3-devel
BuildRequires: python-module-six

Source:  %oname-%version.tar

%description
Numba is an open source, NumPy-aware optimizing compiler for Python sponsored by
Anaconda, Inc. It uses the LLVM compiler project to generate machine code from
Python syntax.

Numba can compile a large subset of numerically-focused Python, including many
NumPy functions. Additionally, Numba has support for automatic parallelization
of loops, generation of GPU-accelerated code, and creation of ufuncs and
C callbacks.

%prep
%setup -n %oname-%version
# Use system six instead of bundled
find -type f -name '*.py*' -exec sed -i 's|numba.six.moves|six.moves|'  -- '{}' +

%build
%python_build

%install
%python_install

%if ""=="3"
mv %buildroot%_bindir/numba %buildroot%_bindir/numba
mv %buildroot%_bindir/pycc %buildroot%_bindir/pycc
%endif

%if ""==""
rm -rf %buildroot/%python_sitelibdir/numba/tests
%endif

%files
%_bindir/numba
%_bindir/pycc
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info
%doc CHANGE_LOG *.rst

%changelog
* Wed Dec 18 2019 Grigory Ustinov <grenka@altlinux.org> 0.46.0-alt1
- Build new version.

* Thu Sep 05 2019 Grigory Ustinov <grenka@altlinux.org> 0.45.1-alt1
- Initial build for Sisyphus (Closes: #35680).
