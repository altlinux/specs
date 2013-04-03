%define oname gflags

Name: python-module-%oname
Version: 2.0
Release: alt1

Summary: Google Commandline Flags Module
License: BSD
Group: Development/Python

Url: https://pypi.python.org/pypi/python-gflags

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-distribute

%setup_python_module %oname

%description
Google Commandline Flags Module.

%prep
%setup

%build
%python_build_debug
   
%install
%python_install

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/*
%python_sitelibdir/*

%changelog
* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

