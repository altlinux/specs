%define mname tw2
%define oname %mname.ckeditor

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20130211
Summary: tw2 wrapper for CKEditor
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.ckeditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.ckeditor.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-tw2.jquery
BuildPreReq: python-module-tw2.forms python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-tw2.jquery
BuildPreReq: python3-module-tw2.forms python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core tw2.jquery tw2.forms

%description
tw2 wrapper for CKEditor.

%package -n python3-module-%oname
Summary: tw2 wrapper for CKEditor
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core tw2.jquery tw2.forms

%description -n python3-module-%oname
tw2 wrapper for CKEditor.

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
%doc *.md
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20130211
- Initial build for Sisyphus

