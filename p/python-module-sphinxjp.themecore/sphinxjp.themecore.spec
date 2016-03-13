%define mname sphinxjp
%define oname %mname.themecore

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt2.1
Summary: A sphinx theme plugin support extension
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxjp.themecore
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-%mname = %EVR
%py_provides %oname

%description
A sphinx theme plugin support extension.

%package -n python-module-%mname
Summary: Core package of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core package of %mname.

%if_with python3
%package -n python3-module-%oname
Summary: A sphinx theme plugin support extension
Group: Development/Python3
Requires: python3-module-%mname = %EVR
%py3_provides %oname

%description -n python3-module-%oname
A sphinx theme plugin support extension.

%package -n python3-module-%mname
Summary: Core package of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core package of %mname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 src/%mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
popd
%endif

%files
%doc src/*.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc src/*.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Version 0.2.0

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

