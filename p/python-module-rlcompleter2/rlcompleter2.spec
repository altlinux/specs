%define oname rlcompleter2
Name: python-module-%oname
Version: 0.96
Release: alt2.1
Summary: Interactive "tab"-completion for python commandline (readline-based)
License: MIT
Group: Development/Python
Url: http://codespeak.net/rlcompleter2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

Source: http://codespeak.net/rlcompleter2/download/rlcompleter2-0.96.tar.gz

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel

%description
rlcompleter2 is an interactive readline completion handler, featuring:

  * completion on any python expression/statement
  * interactive introspection into function signatures and docstrings
  * convenient completions on module, instance and function objects
  * ultra simple user interface: <tab> (try hit it multiple times!)

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.96-alt2.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.96-alt2
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.96-alt1
- Initial build for Sisyphus

