%define oname guppy

Name: python3-module-%oname
Version: 3.1.2
Release: alt1

Summary: Guppy-PE -- A Python Programming Environment
License: MIT
Group: Development/Python3
Url: https://github.com/zhuyifei1999/guppy3

Source: %{oname}3-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Guppy-PE is a library and programming environment for Python, currently
providing in particular the Heapy subsystem, which supports object and
heap memory sizing, profiling and debugging. It also includes a
prototypical specification language, the Guppy Specification Language
(GSL), which can be used to formally specify aspects of Python programs
and generate tests and documentation from a common source.

%package tests
Summary: Tests for guppy
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Guppy-PE is a library and programming environment for Python, currently
providing in particular the Heapy subsystem, which supports object and
heap memory sizing, profiling and debugging. It also includes a
prototypical specification language, the Guppy Specification Language
(GSL), which can be used to formally specify aspects of Python programs
and generate tests and documentation from a common source.

This package contains tests for guppy.

%prep
%setup -n %{oname}3-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/*

%exclude %python3_sitelibdir/%oname/sets/test.py
%exclude %python3_sitelibdir/%oname/heapy/test/

%files tests
%python3_sitelibdir/%oname/sets/test.py
%python3_sitelibdir/%oname/heapy/test/

%changelog
* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 3.1.2-alt1
- Build new version for python3.10.

* Mon Jan 25 2021 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Build new version for python3.9.

* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.0.9-alt1
- Initial build

