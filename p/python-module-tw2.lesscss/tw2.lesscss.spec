%define mname tw2
%define oname %mname.lesscss

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1.d.git20120309
Summary: Less CSS support for ToscaWidgets 2
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.lesscss/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.lesscss.git
# branch: master
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-mako
BuildPreReq: python-module-nose python-module-strainer
BuildPreReq: python-modules-logging python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-mako
BuildPreReq: python3-module-nose python3-module-strainer
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core mako
%add_python_req_skip widgets

%description
This module adds the ability to link LessCSS based stylesheets.

%package -n python3-module-%oname
Summary: Less CSS support for ToscaWidgets 2
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core mako
%add_python3_req_skip widgets

%description -n python3-module-%oname
This module adds the ability to link LessCSS based stylesheets.

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
%doc *.rst docs/*.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.d.git20120309
- Initial build for Sisyphus

