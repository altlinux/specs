%define mname tw2.protovis
%define oname %mname.custom

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.a6.git20120623
Summary: toscawidgets2 wrapper for the stanford protovis toolkit
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.protovis.custom/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.protovis.custom.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-tw2.protovis.core
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.protovis.core
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core tw2.protovis.core

%description
tw2.protovis.custom is a `toscawidgets2 (tw2)` wrapper for `protovis`.

%package -n python3-module-%oname
Summary: toscawidgets2 wrapper for the stanford protovis toolkit
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core tw2.protovis.core

%description -n python3-module-%oname
tw2.protovis.custom is a `toscawidgets2 (tw2)` wrapper for `protovis`.

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
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/tw2/protovis/custom
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/tw2/protovis/custom
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.a6.git20120623
- Initial build for Sisyphus

