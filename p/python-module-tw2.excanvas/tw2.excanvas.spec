%define mname tw2
%define oname %mname.excanvas

%def_with python3

Name: python-module-%oname
Version: 2.0.2
Release: alt1.git20120503
Summary: toscawidgets2 wrapper for excanvas.js resource
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.excanvas/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.excanvas.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-nose
BuildPreReq: python-module-BeautifulSoup python-module-genshi
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-nose
BuildPreReq: python3-module-BeautifulSoup python3-module-genshi
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core

%description
Simple tw2 wrapper for excanvas. Use as a dependency.

%package -n python3-module-%oname
Summary: toscawidgets2 wrapper for excanvas.js resource
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core

%description -n python3-module-%oname
Simple tw2 wrapper for excanvas. Use as a dependency.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/excanvas
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/excanvas
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.git20120503
- Initial build for Sisyphus

