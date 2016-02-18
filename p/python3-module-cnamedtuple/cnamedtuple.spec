%define oname cnamedtuple
Name: python3-module-%oname
Version: 0.1.4
Release: alt1.git20150119.1
Summary: collections.namedtuple implemented in c
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/cnamedtuple/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/llllllllll/cnamedtuple.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests

%py3_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python3 python3-base
BuildRequires: python3-devel rpm-build-python3

%description
An implementation of namedtuple written in c for warp speed.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst prof
%python3_sitelibdir/*

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.git20150119.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150119
- Initial build for Sisyphus

