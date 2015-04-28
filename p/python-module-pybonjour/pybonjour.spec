%define oname pybonjour

%def_disable check

Name: python-module-%oname
Version: 1.1.1
Release: alt1.bzr20090421
Summary: Pure-Python interface to Apple Bonjour and compatible DNS-SD libraries
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pybonjour/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch http://pseudogreen.org/bzr/pybonjour/
Source: %name-%version.tar
BuildArch: noarch

Requires: libavahi

BuildPreReq: python-devel python-module-setuptools-tests libavahi
BuildPreReq: python-modules-ctypes

%py_provides %oname
%py_requires ctypes

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
%python_build_debug

%install
%python_install

%check
python test_pybonjour.py -v

%files
%doc NEWS README examples
%python_sitelibdir/*

%changelog
* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.bzr20090421
- Initial build for Sisyphus

