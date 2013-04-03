%define oname apiclient

Name: python-module-%oname
Version: 1.0.2
Release: alt1

Summary: Framework for making good API client libraries using urllib3
License: MIT
Group: Development/Python

Url: https://pypi.python.org/pypi/apiclient/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python

%setup_python_module %oname

%description
Framework for making good API client libraries using urllib3.

%prep
%setup

%build
%python_build_debug
   
%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

