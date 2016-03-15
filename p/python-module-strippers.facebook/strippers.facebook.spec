%define pname strippers
%define oname %pname.facebook

%def_with python3

Name: python-module-%oname
Version: 0.9
Release: alt1.b.1
Summary: Python library for Facebook Graph API
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/strippers.facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-%pname = %EVR

%description
Python library for Facebook Graph API.

%package -n python-module-%pname
Summary: Core files of %pname
Group: Development/Python

%description -n python-module-%pname
Core files of %pname.

%package -n python3-module-%oname
Summary: Python library for Facebook Graph API
Group: Development/Python3
Requires: python3-module-%pname = %EVR

%description -n python3-module-%oname
Python library for Facebook Graph API.

%package -n python3-module-%pname
Summary: Core files of %pname
Group: Development/Python3

%description -n python3-module-%pname
Core files of %pname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%pname/__init__.py \
	%buildroot%python_sitelibdir/%pname/
%if_with python3
pushd ../python3
install -p -m644 src/%pname/__init__.py \
	%buildroot%python3_sitelibdir/%pname/
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*.egg-info
%python_sitelibdir/%pname/facebook

%files -n python-module-%pname
%dir %python_sitelibdir/%pname
%python_sitelibdir/%pname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%pname/facebook

%files -n python3-module-%pname
%dir %python3_sitelibdir/%pname
%python3_sitelibdir/%pname/__init__.py
%dir %python3_sitelibdir/%pname/__pycache__
%python3_sitelibdir/%pname/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt1.b.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.b
- Initial build for Sisyphus

