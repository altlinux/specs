%define oname tcpwatch
Name: python-module-%oname
Version: 1.3.1
Release: alt1.1
Summary: TCP monitoring and logging tool with support for HTTP 1.1
License: ZPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/tcpwatch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-modules-tkinter

%py_provides %oname
%py_requires Tkinter

%description
TCPWatch is a utility written in Python that lets you monitor forwarded
TCP connections or HTTP proxy connections. It displays the sessions in a
window with a history of past connections. It is useful for developing
and debugging protocol implementations and web services.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

