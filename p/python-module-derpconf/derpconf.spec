%define oname derpconf
Name: python-module-%oname
Version: 0.7.2
Release: alt1.git20140930
Summary: derpconf abstracts loading configuration files for your app
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/derpconf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/globocom/derpconf.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-gevent
BuildPreReq: python-module-pyvows python-module-coverage
BuildPreReq: python-module-colorama python-module-tox
BuildPreReq: python-module-six

%py_provides %oname

%description
derpconf abstracts loading configuration files for your app. derpconf
was extracted from thumbor.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.md
%python_sitelibdir/*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20140930
- Initial build for Sisyphus

