%define oname releases
Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: A Sphinx extension for changelog manipulation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/releases/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

%description
Releases is a Sphinx extension designed to help you keep a source
control friendly, merge friendly changelog file & turn it into useful,
human readable HTML output.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc README.rst
%python_sitelibdir/*

%changelog
* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

