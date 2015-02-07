%define mname tw2.util
%define oname %mname.html5shim

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20120827
Summary: HTML5 Shim for ToscaWidgets 2
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.util.html5shim/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.util.html5shim.git
# branch: master
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-mako
BuildPreReq: python-module-nose
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-mako
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires tw2.core mako

%description
HTML5 Shim resource for TW2.

%package -n python3-module-%oname
Summary: HTML5 Shim for ToscaWidgets 2
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires tw2.core mako

%description -n python3-module-%oname
HTML5 Shim resource for TW2.

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

install -p -m644 tw2/util/__init__.py \
	%buildroot%python_sitelibdir/tw2/util/
%if_with python3
pushd ../python3
install -p -m644 tw2/util/__init__.py \
	%buildroot%python3_sitelibdir/tw2/util/
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md docs/*.rst
%python_sitelibdir/tw2/util/html5shim
%python_sitelibdir/*.egg-info

%files -n python-module-%mname
%dir %python_sitelibdir/tw2/util
%python_sitelibdir/tw2/util/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*.rst
%python3_sitelibdir/tw2/util/html5shim
%python3_sitelibdir/*.egg-info

%files -n python3-module-%mname
%dir %python3_sitelibdir/tw2/util
%dir %python3_sitelibdir/tw2/util/__pycache__
%python3_sitelibdir/tw2/util/__init__.py
%python3_sitelibdir/tw2/util/__pycache__/__init__.*
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20120827
- Initial build for Sisyphus

