# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define mname codeviking
%define oname %mname.contracts
Name: python3-module-%oname
Version: 0.17.0
#Release: alt1.1
Summary: Function and method call contracts
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/CodeViking.contracts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/32/d2/a2b70df673dc1132e359f13eea00cd1d36c17cf7b6a6c7715a8b4c533045/CodeViking.contracts-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests

%py3_provides %oname
%py3_requires %mname

%description
This package provides simple but powerful support for contract
programming. It includes support for preconditions, postconditions,
invariants, and function signature checking. Decorators are used to
specify preconditions, postconditions, and invariants. Function
signatures are automatically extracted from argument and return type
annotations. All contracts can easily be enabled or disabled. Disabled
contracts add zero runtime overhead.

%prep
%setup -q -n CodeViking.contracts-%{version}

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
rm -f test/test_make_arg_checker.py
python3 setup.py test -vv

%files
%doc *.rst
%python3_sitelibdir/%mname/contracts
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/CodeViking.contracts-*.pth

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.17.0-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13.2-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.2-alt1
- Initial build for Sisyphus

