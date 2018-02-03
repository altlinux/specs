%define oname cubicweb-email
Name: python-module-%oname
Version: 1.10.0
Release: alt1.1
Summary: Email component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-email/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-file python-module-markdown
BuildPreReq: python-module-logilab-common
BuildPreReq: python-module-cubicweb-comment

Requires: cubicweb python-module-cubicweb-file
Requires: python-module-cubicweb-comment
%py_requires logilab.common

%description
This cube models multipart email messages (Emails and EmailPart) and
provides tools to import your mail box into a cubicweb instance.

Email are automatically stored into`EmailThreads`.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt1
- Initial build for Sisyphus

