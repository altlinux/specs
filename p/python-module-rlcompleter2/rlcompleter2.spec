%define oname rlcompleter2

%def_without python3

Name: python-module-%oname
Version: 0.98
Release: alt1
Summary: Interactive "tab"-completion for python commandline (readline-based)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/rlcompleter2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
rlcompleter2 is an interactive readline completion handler, featuring:

  * completion on any python expression/statement
  * interactive introspection into function signatures and docstrings
  * convenient completions on module, instance and function objects
  * ultra simple user interface: <tab> (try hit it multiple times!)

%package -n python3-module-%oname
Summary: Interactive "tab"-completion for python commandline (readline-based)
Group: Development/Python3

%description -n python3-module-%oname
rlcompleter2 is an interactive readline completion handler, featuring:

  * completion on any python expression/statement
  * interactive introspection into function signatures and docstrings
  * convenient completions on module, instance and function objects
  * ultra simple user interface: <tab> (try hit it multiple times!)

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.98-alt1
- Version 0.98

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.96-alt2.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.96-alt2
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.96-alt1
- Initial build for Sisyphus

