%define mname tw2.jqplugins
%define oname %mname.select2

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.6
Release: alt1.git20130318
Summary: ToscaWidgets 2 SelectFields enhanced with the select2 javascript library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.jqplugins.select2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.jqplugins.select2.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-tw2.forms
BuildPreReq: python-module-tw2.jquery python-module-nose
BuildPreReq: python-module-BeautifulSoup python-module-FormEncode
BuildPreReq: python-module-webtest python-module-strainer
BuildPreReq: python-module-mako python-module-genshi
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.forms
BuildPreReq: python3-module-tw2.jquery python3-module-nose
BuildPreReq: python3-module-BeautifulSoup python3-module-FormEncode
BuildPreReq: python3-module-webtest python3-module-strainer
BuildPreReq: python3-module-mako python3-module-genshi
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core tw2.forms tw2.jquery

%description
Select2 is a jQuery based replacement for select boxes. It supports
searching, remote data sets, and infinite scrolling of results.

%package -n python3-module-%oname
Summary: ToscaWidgets 2 SelectFields enhanced with the select2 javascript library
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core tw2.forms tw2.jquery

%description -n python3-module-%oname
Select2 is a jQuery based replacement for select boxes. It supports
searching, remote data sets, and infinite scrolling of results.

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
%doc AUTHORS *.md docs/*.rst
%python_sitelibdir/tw2/jqplugins/select2
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.md docs/*.rst
%python3_sitelibdir/tw2/jqplugins/select2
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Feb 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20130318
- Initial build for Sisyphus

