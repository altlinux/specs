%define oname afl

Name: python3-module-%oname
Version: 0.7.3
Release: alt1

Summary: American Fuzzy Lop fork server and instrumentation for pure-Python code

License: MIT
Group: Development/Python3
Url: https://github.com/jwilk/python-%oname

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython

# See BAO #42228
%add_python3_req_skip nose

%description
This is experimental module that enables American Fuzzy Lop fork server and
instrumentation for pure-Python code.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE doc/*
%_bindir/py-%oname-*
%python3_sitelibdir/%oname.*.so
%python3_sitelibdir/python_afl-%version-py%_python3_version.egg-info

%changelog
* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.7.3-alt1
- Automatically updated to 0.7.3.

* Tue May 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.2-alt1
- Initial build.
