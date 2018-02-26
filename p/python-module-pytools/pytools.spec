%define oname pytools

%def_with python3

Name: python-module-%oname
Version: 2011.5
Release: alt2
Summary: A collection of tools for Python
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pytools
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif
BuildArch: noarch

%description
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of my other software
packages, and is probably of little interest to you unless you use
those.

%if_with python3
%package -n python3-module-%oname
Summary: A collection of tools for Python 3
Group: Development/Python3

%description -n python3-module-%oname
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of my other software
packages, and is probably of little interest to you unless you use
those.

%package -n python3-module-%oname-test
Summary: Test for Pytools (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires decorator

%description -n python3-module-%oname-test
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of my other software
packages, and is probably of little interest to you unless you use
those.

This package contains test for Pytools.
%endif

%package test
Summary: Test for Pytools
Group: Development/Python
Requires: %name = %version-%release

%description test
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of my other software
packages, and is probably of little interest to you unless you use
those.

This package contains test for Pytools.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test.py*

%files test
%python_sitelibdir/%oname/test.py*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test.py*
%exclude %python3_sitelibdir/%oname/__pycache__/test*

%files -n python3-module-%oname-test
%python3_sitelibdir/%oname/test.py*
%python3_sitelibdir/%oname/__pycache__/test*
%endif

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.5-alt2
- Added module for Python 3

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.5-alt1
- Initial build for Sisyphus

