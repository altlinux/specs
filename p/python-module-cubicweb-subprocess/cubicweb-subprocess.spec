%define oname cubicweb-subprocess
Name: python-module-%oname
Version: 0.2.1
Release: alt1
Summary: This cube helps to manage and monitor subprocesses
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-subprocess/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-file

Requires: cubicweb python-module-cubicweb-file

%description
This cube provides an easy way to run subprocesses using a dedicated
workflow.

Subprocesses can be configured (command line, environment, working
directory).

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

