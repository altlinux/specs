%define oname ntlm

Name: python-module-%oname
Version: 1.0.1
Release: alt1

Summary: NTLM support, including an authentication handler for urllib2
License: Free
Group: Development/Python

Url: https://pypi.python.org/pypi/python-ntlm

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-distribute

%setup_python_module %oname

%description
This package allows Python clients running on any operating
system to provide NTLM authentication to a supporting server.

python-ntlm is probably most useful on platforms that are not
Windows, since on Windows it is possible to take advantage of
platform-specific NTLM support.

%prep
%setup

%build
%python_build_debug
   
%install
%python_install

%files
%doc PKG-INFO
%_bindir/*
%python_sitelibdir/*

%changelog
* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

