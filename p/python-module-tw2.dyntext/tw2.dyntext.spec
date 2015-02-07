%define mname tw2
%define oname %mname.dyntext

%def_with python3

Name: python-module-%oname
Version: 0.0.5
Release: alt1.git20120305
Summary: Dynamic Text widget for TW2
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.dyntext/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.dyntext.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-tw2.jquery
BuildPreReq: python-module-mako python-module-nose
BuildPreReq: python-module-BeautifulSoup python-module-FormEncode
BuildPreReq: python-module-strainer python-module-webtest
BuildPreReq: python-modules-json python-modules-multiprocessing
BuildPreReq: python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.jquery
BuildPreReq: python3-module-mako python3-module-nose
BuildPreReq: python3-module-BeautifulSoup python3-module-FormEncode
BuildPreReq: python3-module-strainer python3-module-webtest
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname json tw2.core tw2.jquery mako

%description
Dynamic Text widget for TW2. Allows text to be pulled from JSON objects
live.

%package -n python3-module-%oname
Summary: Dynamic Text widget for TW2
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname json tw2.core tw2.jquery mako

%description -n python3-module-%oname
Dynamic Text widget for TW2. Allows text to be pulled from JSON objects
live.

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
%doc *.txt docs/*.rst
%python_sitelibdir/%mname/dyntext
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/%mname/dyntext
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20120305
- Initial build for Sisyphus

