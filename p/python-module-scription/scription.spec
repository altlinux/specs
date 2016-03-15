%define oname scription

%def_with python3

Name: python-module-%oname
Version: 0.74.02
Release: alt1.1
Summary: Simple script parameter parser
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scription/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests /dev/pts
BuildPreReq: python-module-enum34
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-enum34
%endif

%py_provides %oname
Requires: python-module-enum34

%description
light-weight library to enhance command-line scripts; includes
conversion of parameters to specified data types, parameter checking,
basic input/output with users, support for suid, sending email,
executing sub-programs, and having sub-commands within a script.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
light-weight library to enhance command-line scripts; includes
conversion of parameters to specified data types, parameter checking,
basic input/output with users, support for suid, sending email,
executing sub-programs, and having sub-commands within a script.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Simple script parameter parser
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-enum34

%description -n python3-module-%oname
light-weight library to enhance command-line scripts; includes
conversion of parameters to specified data types, parameter checking,
basic input/output with users, support for suid, sending email,
executing sub-programs, and having sub-commands within a script.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
light-weight library to enhance command-line scripts; includes
conversion of parameters to specified data types, parameter checking,
basic input/output with users, support for suid, sending email,
executing sub-programs, and having sub-commands within a script.

This package contains tests for %oname.

%prep
%setup

echo 'simple script parameter parser' >README

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export PYTHONPATH=$PWD
python %oname/test.py -v
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 %oname/test.py -v
popd
%endif

%files
%doc CHANGES README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.74.02-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.74.02-alt1
- Version 0.74.02

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.73.02-alt1
- Version 0.73.02

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.73.01-alt1
- Initial build for Sisyphus

