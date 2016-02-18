%define oname pybonjour

%def_disable check

Name: python3-module-%oname
Version: 1.1.1
Release: alt1.git20131002.1
Summary: Pure-Python interface to Apple Bonjour and compatible DNS-SD libraries
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pybonjour/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/depl0y/pybonjour-python3.git
Source: %name-%version.tar
BuildArch: noarch

Requires: libavahi

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests libavahi

%py3_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: libgpg-error python-base python3 python3-base
BuildRequires: libavahi rpm-build-python3

%description
pybonjour provides a pure-Python interface (via ctypes) to Apple Bonjour
and compatible DNS-SD libraries (such as Avahi). It allows Python
scripts to take advantage of Zero Configuration Networking (Zeroconf) to
register, discover, and resolve services on both local and wide-area
networks. Since pybonjour is implemented in pure Python, scripts that
use it can easily be ported to Mac OS X, Windows, Linux, and other
systems that run Bonjour.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 test_pybonjour.py -v

%files
%doc NEWS README examples
%python3_sitelibdir/*

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1.git20131002.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20131002
- Initial build for Sisyphus

