%define mname codeviking
%define oname %mname.math
Name: python3-module-%oname
Version: 0.10.1
Release: alt1.1
Summary: Function and method call math
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/CodeViking.math/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests

%py_provides %oname
Requires: python3-module-%mname = %EVR

%description
A collection of mathematical utility functions.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/%mname/math
%python3_sitelibdir/*.egg-info

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.*
%python3_sitelibdir/%mname/__pycache__/__init__.*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus

