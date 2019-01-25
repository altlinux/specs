%define oname argparse

%def_disable check

Name:           python-module-%oname
Version:        1.3.0
Release:        alt3.hg20141215
Summary:        Python command line parser

Group:          Development/Python
License:        BSD and/or LGPLv2+
URL:            http://code.google.com/p/argparse/
# hg clone https://code.google.com/p/argparse/
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
%setup_python_module %oname

BuildArch:      noarch
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules

#BuildRequires: python-module-setuptools-tests python-devel
#BuildPreReq: python-module-setupdocs python-module-sphinx-devel

%py_requires %oname

%description
The argparse module provides an easy, declarative interface for
creating command line tools.

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

#prep
#setup

#touch test/__init__.py

#prepare_sphinx .

#build
#python_build

#install
#python_install -O1

#generate_pickles doc/source doc/source %oname
#cp -fR pickle %buildroot%python_sitelibdir/%oname

#check
#python setup.py test
#py.test

%files
#doc NEWS.txt README.txt
#python_sitelibdir/*
#exclude %python_sitelibdir/%oname/pickle

#files docs
#doc doc/* test

#files pickles
#dir %python_sitelibdir/%oname
#python_sitelibdir/%oname/pickle

%changelog
* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt3.hg20141215
- Removed Python3 module (closes: #35994).

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt2.hg20141215.2
- (NMU) rebuild with python3.6

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt2.hg20141215.1
- NMU: Use buildreq for BR.

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.hg20141215
- Removed content

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.hg20141215
- Version 1.3.0

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.hg20141115
- Version 1.2.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2-alt2.hg20110331.1
- Rebuild with Python-3.3

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
