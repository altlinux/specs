%define oname gadjo

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.1
Summary: Django base template tailored for management interfaces
License: AGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/gadjo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-xstatic-font-awesome
BuildPreReq: python-module-xstatic-jquery-ui
BuildPreReq: python-module-django
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-xstatic-font-awesome
BuildPreReq: python3-module-xstatic-jquery-ui
BuildPreReq: python3-module-django python-tools-2to3
%endif

%py_provides %oname
%py_requires xstatic.pkg.font_awesome xstatic.pkg.jquery_ui django

%description
Gadjo is a base template for Django applications, tailored for
management interfaces, built to provide a nice and modern look, while
using progressive enhancement and responsive designs to adapt to
different environments.

%package -n python3-module-%oname
Summary: Django base template tailored for management interfaces
Group: Development/Python3
%py3_provides %oname
%py3_requires xstatic.pkg.font_awesome xstatic.pkg.jquery_ui django

%description -n python3-module-%oname
Gadjo is a base template for Django applications, tailored for
management interfaces, built to provide a nice and modern look, while
using progressive enhancement and responsive designs to adapt to
different environments.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

