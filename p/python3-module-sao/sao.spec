# upstream from sao/py3-new

%define oname sao
Name: python3-module-%oname
Version: 0.1
Release: alt1.b1.git20130306
Summary: Python interface for the SAO developed projects, such as XPA,DS9 & Funtools
License: BSD
Group: Development/Python
Url: http://code.google.com/p/python-sao/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/leejjoon/pysao.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools libxpa-devel

%description
This project is aimed to provide a python interface for some programs
developed by Smithsonian Astrophysical Observatory(SAO). One of the main
goal is to communicate with ds9 from python shell via the XPA protocol.
It provides a python wrapper for subset of XPA library and python module
for ds9 based on the XPA module.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc CHANGELOG LICENSE* doc/*
%python3_sitelibdir/*

%changelog
* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b1.git20130306
- Initial build for Sisyphus

