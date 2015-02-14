%define mname tw2
%define oname %mname.tipster

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt1.b9.git20120523
Summary: Tips for your website
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.tipster/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.tipster.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.jqplugins.ui python-module-mako
BuildPreReq: python-module-nose python-module-BeautifulSoup
BuildPreReq: python-module-genshi python-module-FormEncode
BuildPreReq: python-module-strainer python-module-tw2.core-tests
BuildPreReq: python-module-tw2.jquery
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.jqplugins.ui python3-module-mako
BuildPreReq: python3-module-nose python3-module-BeautifulSoup
BuildPreReq: python3-module-genshi python3-module-FormEncode
BuildPreReq: python3-module-strainer python3-module-tw2.core-tests
BuildPreReq: python3-module-tw2.jquery
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.jqplugins.ui mako tw2.core tw2.jquery

%description
Cute little tip widget for your websites.

%package -n python3-module-%oname
Summary: Tips for your website
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.jqplugins.ui mako tw2.core tw2.jquery

%description -n python3-module-%oname
Cute little tip widget for your websites.

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
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b9.git20120523
- Initial build for Sisyphus

