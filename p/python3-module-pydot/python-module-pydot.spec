%define oname pydot
Name: python3-module-%oname
Version: 1.0.15
Release: alt1.hg20110706

Summary: Python 3 interface to Graphiz's Dot

License: MIT
Group: Development/Python3
Url: https://bitbucket.org/prologic/pydot

# hg clone https://bitbucket.org/prologic/pydot
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-pyparsing

%description
An interface for creating both directed and non directed graphs from
Python. Currently all attributes implemented in the Dot language are
supported (up to Graphviz 1.16).

Output can be inlined in Postscript into interactive scientific
environments like TeXmacs, or output in any of the format's supported
by the Graphviz tools dot, neato, twopi.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc ChangeLog README
%python3_sitelibdir/*

%changelog
* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.15-alt1.hg20110706
- Initial build for Sisyphus

