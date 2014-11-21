%define oname itty
Name: python-module-%oname
Version: 0.8.2
Release: alt1.git20131203
Summary: The itty-bitty Python web framework
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/itty/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toastdriven/itty.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-modules-wsgiref

%py_provides %oname
%py_requires wsgiref

%description
itty.py is a little experiment, an attempt at a Sinatra influenced
micro-framework that does just enough to be useful and nothing more.

%package -n %oname-examples
Summary: Examples for %oname
Group: Development/Python
BuildArch: noarch

%description -n %oname-examples
itty.py is a little experiment, an attempt at a Sinatra influenced
micro-framework that does just enough to be useful and nothing more.

This package contains examples for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc AUTHORS *.rst
%python_sitelibdir/*

%files -n %oname-examples
%doc examples/*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20131203
- Initial build for Sisyphus

