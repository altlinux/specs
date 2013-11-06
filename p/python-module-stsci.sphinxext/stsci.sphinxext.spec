%define oname stsci.sphinxext

Name: python-module-%oname
Version: 1.2.1
Release: alt1

Summary: A set of tools and templates to customize Sphinx for use in STScI projects
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/stsci.sphinxext/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools python-module-d2to1
BuildPreReq: python-module-stsci.distutils

%description
This project contains extensions to Sphinx to build documentation from
STScI.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc LICENSE_enumitem README
%python_sitelibdir/*

%changelog
* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

