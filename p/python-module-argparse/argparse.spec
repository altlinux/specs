%define oname argparse

%def_with python3

Name:           python-module-%oname
Version:        1.2
Release:        alt2.hg20110331
Summary:        Python command line parser

Group:          Development/Python
License:        BSD and/or LGPLv2+
URL:            http://code.google.com/p/argparse/
# hg clone https://code.google.com/p/argparse/
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
%setup_python_module %oname

BuildArch:      noarch
BuildRequires: python-module-setuptools, python-devel
BuildPreReq: python-module-setupdocs python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
The argparse module provides an easy, declarative interface for
creating command line tools.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 command line parser
Group: Development/Python3

%description -n python3-module-%oname
The argparse module provides an easy, declarative interface for
creating command line tools.
%endif

%package docs
Summary: Documentation for argparse
Group: Development/Documentation
BuildArch: noarch

%description docs
The argparse module provides an easy, declarative interface for
creating command line tools.

This package contains documentation for argparse.

%package pickles
Summary: pickles for argparse
Group: Development/Python

%description pickles
The argparse module provides an easy, declarative interface for
creating command line tools.

This package contains pickles for argparse.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install -O1
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%generate_pickles doc/source doc/source %oname
cp -fR pickle %buildroot%python_sitelibdir/%oname

%files
%doc NEWS.txt README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files docs
%doc doc/* test

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc NEWS.txt README.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.hg20110331
- Added module for Python 3

* Sun Dec 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.hg20110331
- Version 1.2

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.svn20100228
- Enabled docs

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.svn20100228.1.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20100228.1
- Rebuilt with python-module-sphinx-devel

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20100228
- Initial build for Sisyphus
