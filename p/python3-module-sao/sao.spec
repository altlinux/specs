# upstream from sao/py3-new

%define oname sao
Name: python3-module-%oname
Version: 0.1
Release: alt1.b1.git20130306.1.1
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
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.b1.git20130306.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.b1.git20130306.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b1.git20130306
- Initial build for Sisyphus

