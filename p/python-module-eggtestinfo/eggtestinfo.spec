%define oname eggtestinfo

Name: python-module-%oname
Version: 0.3
Release: alt1

Summary: Add test information to .egg-info
License: ZPL
Group: Development/Python

Url: https://pypi.python.org/pypi/eggtestinfo

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-distribute

%setup_python_module %oname

%description
This package is a setuptools plugin: it adds a file to the generated
.egg-info directory, capturing the information used by the setup.py test
command when running tests.

%prep
%setup

%build
%python_build_debug
   
%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Sat Apr 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

