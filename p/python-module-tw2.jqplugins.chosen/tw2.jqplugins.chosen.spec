%define mname tw2.jqplugins
%define oname %mname.chosen

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3
Release: alt1.git20140118
Summary: ToscaWidgets 2 SelectFields enhanced with the Chosen javascript library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.jqplugins.chosen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.jqplugins.chosen.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-tw2.forms
BuildPreReq: python-module-tw2.jquery python-module-nose
BuildPreReq: python-module-BeautifulSoup python-module-FormEncode
BuildPreReq: python-module-webtest python-module-strainer
BuildPreReq: python-module-sieve python-module-mako
BuildPreReq: python-module-genshi
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.forms
BuildPreReq: python3-module-tw2.jquery python3-module-nose
BuildPreReq: python3-module-BeautifulSoup python3-module-FormEncode
BuildPreReq: python3-module-webtest python3-module-strainer
BuildPreReq: python3-module-sieve python3-module-mako
BuildPreReq: python3-module-genshi
%endif

%py_provides %oname
%py_requires %mname tw2.core tw2.forms tw2.jquery

%description
Chosen is a JavaScript plugin that makes long, unwieldy select boxes
much more user-friendly.

%package -n python3-module-%oname
Summary: ToscaWidgets 2 SelectFields enhanced with the Chosen javascript library
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core tw2.forms tw2.jquery

%description -n python3-module-%oname
Chosen is a JavaScript plugin that makes long, unwieldy select boxes
much more user-friendly.

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
%doc *.rst docs/*.rst
%python_sitelibdir/tw2/jqplugins/chosen
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/tw2/jqplugins/chosen
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20140118
- Initial build for Sisyphus

