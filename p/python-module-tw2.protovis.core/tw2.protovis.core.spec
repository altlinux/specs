%define mname tw2.protovis
%define oname %mname.core

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.gi20130826
Summary: toscawidgets2 wrapper for the stanford protovis toolkit
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.protovis.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.protovis.core.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-mako
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-mako
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires tw2.core mako

%description
tw2.protovis.core is a toscawidgets2 (tw2) wrapper for protovis.

%package -n python3-module-%oname
Summary: toscawidgets2 wrapper for the stanford protovis toolkit
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires tw2.core mako

%description -n python3-module-%oname
tw2.protovis.core is a toscawidgets2 (tw2) wrapper for protovis.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires tw2

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname
%py3_requires tw2

%description -n python3-module-%mname
Core files of %mname.

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
%python_sitelibdir/tw2/protovis/core
%python_sitelibdir/*.egg-info

%files -n python-module-%mname
%dir %python_sitelibdir/tw2/protovis
%python_sitelibdir/tw2/protovis/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/tw2/protovis/core
%python3_sitelibdir/*.egg-info

%files -n python3-module-%mname
%dir %python3_sitelibdir/tw2/protovis
%dir %python3_sitelibdir/tw2/protovis/__pycache__
%python3_sitelibdir/tw2/protovis/__init__.py
#python3_sitelibdir/tw2/protovis/__pycache__/__init__.*
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.gi20130826
- Initial build for Sisyphus

