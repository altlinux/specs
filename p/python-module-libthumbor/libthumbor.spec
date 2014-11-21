%define oname libthumbor
Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20141020
Summary: libthumbor is the python extension to thumbor
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/libthumbor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/thumbor/libthumbor.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-pycrypto
BuildPreReq: python-module-mock python-module-nose
BuildPreReq: python-module-coverage python-module-yanc
BuildPreReq: python-module-preggy python-module-ipdb
BuildPreReq: python-module-coveralls python-module-thumbor

%py_provides %oname

%description
libthumbor is the python extension to thumbor. It allows users to
generate safe urls easily.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
%make test

%files
%doc CONTRIBUTING *.mkd
%python_sitelibdir/*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20141020
- Initial build for Sisyphus

