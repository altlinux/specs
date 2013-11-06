%define oname sphinxcontrib-programoutput

Name: python-module-%oname
Version: 0.8
Release: alt1

Summary: Sphinx extension to include program output
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-programoutput/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

%description
A Sphinx extension to literally insert the output of arbitrary commands
into documents, helping you to keep your command examples up to date.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.rst doc/*.rst
%python_sitelibdir/*

%changelog
* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

