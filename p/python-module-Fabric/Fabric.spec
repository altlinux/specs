%define oname Fabric
Name: python-module-%oname
Version: 1.9.0
Release: alt1
Summary: A simple, Pythonic tool for remote execution and deployment
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Fabric/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-paramiko
BuildPreReq: python-module-setuptools python-module-ecdsa
BuildPreReq: python-module-sphinx-devel python-module-alabaster
BuildPreReq: python-module-releases

%py_provides %oname

%description
Fabric is a Python (2.5-2.7) library and command-line tool for
streamlining the use of SSH for application deployment or systems
administration tasks.

It provides a basic suite of operations for executing local or remote
shell commands (normally or via sudo) and uploading/downloading files,
as well as auxiliary functionality such as prompting the running user
for input, or aborting execution.

%package docs
Summary: Documentationr for Fabric
Group: Development/Documentation

%description docs
Fabric is a Python (2.5-2.7) library and command-line tool for
streamlining the use of SSH for application deployment or systems
administration tasks.

It provides a basic suite of operations for executing local or remote
shell commands (normally or via sudo) and uploading/downloading files,
as well as auxiliary functionality such as prompting the running user
for input, or aborting execution.

This package contains documentationr for Fabric.

%prep
%setup

%prepare_sphinx sites
ln -s ../objects.inv sites/docs/
ln -s ../objects.inv sites/www/

%build
%python_build_debug

pushd sites/docs
sphinx-build -b html -d doctrees . docs
popd
pushd sites/www
sphinx-build -b html -d doctrees . www
popd

%install
%python_install

%files
%doc AUTHORS README.rst
%_bindir/*
%python_sitelibdir/*

%files docs
%doc sites/docs/docs
%doc sites/www/www

%changelog
* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus

