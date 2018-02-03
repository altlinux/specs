%define oname minify

%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt1.1.1
Summary: Minify provides distutils/setuptools commands for minifying CSS and JS resources
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/minify/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-yuicompressor
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-yuicompressor
%endif

%py_provides %oname
%py_requires yuicompressor

%description
Minify provides distutils/setuptools commands for minifying CSS and JS
resources using the well-known YUI compressor from Yahoo! Inc. When you
install minify, two new commands are available:

* minify_js which minifies Javascript files
* minify_css which minifies CSS files

%package -n python3-module-%oname
Summary: Minify provides distutils/setuptools commands for minifying CSS and JS resources
Group: Development/Python3
%py3_provides %oname
%py3_requires yuicompressor

%description -n python3-module-%oname
Minify provides distutils/setuptools commands for minifying CSS and JS
resources using the well-known YUI compressor from Yahoo! Inc. When you
install minify, two new commands are available:

* minify_js which minifies Javascript files
* minify_css which minifies CSS files

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGES README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus

