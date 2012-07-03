%define oname graphcanvas
Name: python-module-%oname
Version: 4.0.1
Release: alt1.git20110627
Summary: Interactive graph (network) visualization
License: BSD
Group: Development/Python
Url: https://github.com/enthought/graphcanvas
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/graphcanvas.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-distribute

%description
graphcanvas is an library for interacting with visualizations of complex
graphs. The aim is to allow the developer to declare the graph by the
simplest means and be able to visualize the graph immediately.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.rst examples
%python_sitelibdir/*

%changelog
* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20110627
- Initial build for Sisyphus

