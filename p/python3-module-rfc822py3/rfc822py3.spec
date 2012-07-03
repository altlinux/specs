%define oname rfc822py3
Name: python3-module-%oname
Version: 20110416
Release: alt1
Summary: A port of the Python 2.x rfc822 library to Python3
License: Python
Group: Development/Python3
Url: https://github.com/MarkNenadov/rfc822py3
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/MarkNenadov/rfc822py3.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
rfc822py3 - A port of the Python 2.x rfc822 module into Python.

%prep
%setup

%install
install -d %buildroot%python3_sitelibdir
install -p -m644 *.py %buildroot%python3_sitelibdir

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110416-alt1
- Initial build for Sisyphus

