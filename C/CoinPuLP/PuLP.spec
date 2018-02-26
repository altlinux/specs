%define pyname pulp
%define somver 0

%define oname PuLP
Name: Coin%oname
Version: 1.4.9
Release: alt1.svn20110515.1
Summary: Linear Programming modeller written in python
License: MIT
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/PuLP
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/PuLP/trunk
Source: %oname-%version.tar.gz

#BuildPreReq: libglpk libCoinClp libCoinCgl libCoinCbc
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinCbc-devel libCoinCgl-devel
BuildPreReq: libCoinClp-devel libCoinMP-devel libCoinOsi-devel

Requires: python-module-%pyname = %version-%release

%description
PuLP is an LP modeler written in python. PuLP can generate MPS or LP
files and call GLPK, COIN CLP/CBC to solve linear problems.

%package -n python-module-%pyname
Summary: Linear Programming modeller written in python
Group: Development/Python

%description -n python-module-%pyname
PuLP is an LP modeler written in python. PuLP can generate MPS or LP
files and call GLPK, COIN CLP/CBC to solve linear problems.

%package -n python-module-%pyname-docs
Summary: Documentation for PuLP
Group: Development/Documentation
BuildArch: noarch

%description -n python-module-%pyname-docs
PuLP is an LP modeler written in python. PuLP can generate MPS or LP
files and call GLPK, COIN CLP/CBC to solve linear problems.

This package contains documentation for PuLP.

%package -n python-module-%pyname-examples
Summary: Examples for PuLP
Group: Development/Python
BuildArch: noarch
Requires: python-module-%pyname = %version-%release

%description -n python-module-%pyname-examples
PuLP is an LP modeler written in python. PuLP can generate MPS or LP
files and call GLPK, COIN CLP/CBC to solve linear problems.

This package contains examples for PuLP.

%prep
%setup

%build
#python bootstrap.py
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

rm -f %buildroot%python_sitelibdir/%pyname/solverdir/*.so* \
	%buildroot%python_sitelibdir/%pyname/solverdir/*.dll
for i in Cbc CbcSolver Cgl Clp CoinMP CoinUtils Osi OsiCbc OsiClp
do
	ln -s %_libdir/lib$i.so.%somver \
		%buildroot%python_sitelibdir/%pyname/solverdir/
done

%files -n python-module-%pyname
%doc AUTHORS HISTORY LICENSE README ROADMAP
%_bindir/*
%python_sitelibdir/*

%files -n python-module-%pyname-docs
%doc doc/KPyCon2009/*.pdf doc/*.pdf

%files -n python-module-%pyname-examples
%doc examples

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.9-alt1.svn20110515.1
- Rebuild with Python-2.7

* Mon Oct 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.9-alt1.svn20110515
- Version 1.4.9

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.8-alt1.svn20110414
- Version 1.4.8

* Sun Dec 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.7-alt1.svn20100128.1
- Disabled bootstrap from Internet

* Fri Sep 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.7-alt1.svn20100128
- Initial build for Sisyphus

