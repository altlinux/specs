%define oname afl

Name: python3-module-%oname
Version: 0.7.3
Release: alt1.1

Summary: American Fuzzy Lop fork server and instrumentation for pure-Python code

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/python-afl
VCS: https://github.com/jwilk/python-afl

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

# See BAO #42228
%add_python3_req_skip nose

%description
This is experimental module that enables American Fuzzy Lop fork server and
instrumentation for pure-Python code.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE doc/*
%_bindir/py-%oname-*
%python3_sitelibdir/%oname.*.so
%python3_sitelibdir/python_afl-%version.dist-info

%changelog
* Fri Nov 15 2024 Grigory Ustinov <grenka@altlinux.org> 0.7.3-alt1.1
- Moved on pyproject macros.

* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.7.3-alt1
- Automatically updated to 0.7.3.

* Tue May 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.2-alt1
- Initial build.
