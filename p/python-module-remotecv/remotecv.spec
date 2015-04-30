%define oname remotecv
Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20150119
Summary: OpenCV worker for facial and feature recognition
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/remotecv/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/thumbor/remotecv.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-argparse
BuildPreReq: python-module-pyres python-module-opencv
BuildPreReq: python-module-setproctitle
BuildPreReq: python-module-nose python-modules-json
BuildPreReq: python-module-Pillow python-module-thumbor
BuildPreReq: python-module-pyvows python-module-preggy
BuildPreReq: python-module-coverage
BuildPreReq: libnumpy-devel

%py_provides %oname
%py_requires cv cv2 PIL thumbor pyvows

%description
remotecv is an OpenCV worker for facial and feature recognition.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
nosetests -v

%files
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150119
- Version 1.0.0

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20140803
- Initial build for Sisyphus

