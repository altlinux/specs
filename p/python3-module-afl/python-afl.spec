%define oname afl

Name: python3-module-%oname
Version: 0.7.2
Release: alt1

Summary: American Fuzzy Lop fork server and instrumentation for pure-Python code
License: MIT
Group: Development/Python3
Url: https://github.com/jwilk/python-%oname

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython

%description
This is experimental module that enables American Fuzzy Lop fork server and
instrumentation for pure-Python code.

%package tests
Summary: Tests for %name
Group: Development/Python3
Requires: %name = %EVR

%description tests
Contains the tests for %name.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

install -d %buildroot%python3_sitelibdir/py_%oname
mv tests/ %buildroot%python3_sitelibdir/py_%oname

%files
%doc LICENSE doc/*
%_bindir/py-%oname-*
%python3_sitelibdir/%{oname}.*.so
%python3_sitelibdir/*.egg-info

%files tests
%python3_sitelibdir/py_%oname/tests/


%changelog
* Tue May 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.2-alt1
- Initial build.

