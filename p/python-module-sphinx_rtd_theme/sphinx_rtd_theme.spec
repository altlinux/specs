%define oname sphinx_rtd_theme

%def_with python3

Name: python-module-%oname
Version: 0.1.8
Release: alt1.git20150730.1
Summary: ReadTheDocs.org theme for Sphinx
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx_rtd_theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/snide/sphinx_rtd_theme.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
This is a prototype mobile-friendly sphinx_ theme I made for
readthedocs.org_. It's currently in development and includes some rtd
variable checks that can be ignored if you're just trying to use it on
your project outside of that site.

%package -n python3-module-%oname
Summary: ReadTheDocs.org theme for Sphinx
Group: Development/Python3

%description -n python3-module-%oname
This is a prototype mobile-friendly sphinx_ theme I made for
readthedocs.org_. It's currently in development and includes some rtd
variable checks that can be ignored if you're just trying to use it on
your project outside of that site.

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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt1.git20150730.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.git20150730
- Version 0.1.8

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20141202
- New snapshot
- Added module for Python 3

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140821
- Initial build for Sisyphus

