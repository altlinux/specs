%define mname tw2
%define oname %mname.d3

%def_with python3

Name: python-module-%oname
Version: 0.0.8
Release: alt1.git20130409
Summary: toscawidgets2 wrapper for d3 (data-driven documents)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.d3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.d3.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-tw2.jquery
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-tw2.jquery
BuildPreReq: python3-module-nose
%endif

%py_provides %oname
%py_requires %mname tw2.core tw2.jquery

%description
tw2.d3 is a toscawidgets2 (tw2) wrapper for d3.

%package -n python3-module-%oname
Summary: toscawidgets2 wrapper for d3 (data-driven documents)
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core tw2.jquery

%description -n python3-module-%oname
tw2.d3 is a toscawidgets2 (tw2) wrapper for d3.

%prep
%setup

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
%python_sitelibdir/%mname/d3
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/d3
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1.git20130409
- Initial build for Sisyphus

