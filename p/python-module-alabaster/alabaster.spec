%define oname alabaster
Name: python-module-%oname
Version: 0.6.2
Release: alt1
Summary: A configurable sidebar-enabled Sphinx theme
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/alabaster/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

%description
This theme is a modified "Kr" Sphinx theme from @kennethreitz
(especially as used in his [Requests](https://python-requests.org)
project), which was itself originally based on @mitsuhiko's theme used
for [Flask](http://flask.pocoo.org/) & related projects.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc README.md
%python_sitelibdir/*

%changelog
* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

