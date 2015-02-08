%define mname tw2
%define oname %mname.slideymenu

%def_with python3

Name: python-module-%oname
Version: 2.2
Release: alt1.git20130227
Summary: A tw2 slidey menu
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.slideymenu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.slideymenu.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-tw2.core python-module-tw2.jquery
BuildPreReq: python-module-tw2.jqplugins.ui python-module-BeautifulSoup
BuildPreReq: python-module-nose python-module-FormEncode
BuildPreReq: python-module-webtest
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-tw2.core python3-module-tw2.jquery
BuildPreReq: python3-module-tw2.jqplugins.ui python3-module-BeautifulSoup
BuildPreReq: python3-module-nose python3-module-FormEncode
BuildPreReq: python3-module-webtest
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname genshi mako tw2.core tw2.jquery tw2.jqplugins.ui

%description
tw2.slideymenu is a toscawidgets2 (tw2) package with slidey menu that I
made just for you!

%package -n python3-module-%oname
Summary: A tw2 slidey menu
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname genshi mako tw2.core tw2.jquery tw2.jqplugins.ui

%description -n python3-module-%oname
tw2.slideymenu is a toscawidgets2 (tw2) package with slidey menu that I
made just for you!

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
rm -f setup.cfg
python setup.py test
%if_with python3
pushd ../python3
rm -f setup.cfg
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/slideymenu
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/slideymenu
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Feb 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.git20130227
- Initial build for Sisyphus

