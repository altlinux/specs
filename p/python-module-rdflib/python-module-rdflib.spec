%define oname rdflib

%def_with python3

Name: python-module-%oname
Version: 3.2.0
Release: alt1

Summary: RDFLib is a Python library for working with RDF

Group: Development/Python
License: See License
Url: http://rdflib.net/

%setup_python_module %oname

Source: http://rdflib.net/%oname-%version.tar.bz2
BuildArch: noarch

%add_python_req_skip FOPLRelationalModel RDF

# Automatically added by buildreq on Tue Sep 18 2007
BuildRequires: pybliographic python-module-MySQLdb python-module-PyXML python-module-Pyrex python-module-setuptools python-module-zope.interface python-modules-email
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information.  The library contains parsers
and serializers for RDF/XML, N3, NTriples, Turtle, TriX and RDFa. The
library presents a Graph interface which can be backed by any one of
a number of store implementations, including, memory, MySQL, Redland,
SQLite, Sleepycat, ZODB and SQLObject.

%if_with python3
%package -n python3-module-%oname
Summary: RDFLib is a Python 3 library for working with RDF
Group: Development/Python3
%add_python3_req_skip FOPLRelationalModel RDF

%description -n python3-module-%oname
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information.  The library contains parsers
and serializers for RDF/XML, N3, NTriples, Turtle, TriX and RDFa. The
library presents a Graph interface which can be backed by any one of
a number of store implementations, including, memory, MySQL, Redland,
SQLite, Sleepycat, ZODB and SQLObject.
%endif

%prep
%setup -n %oname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Version 3.2.0
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.0-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.0-alt3.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt3
- Rebuilt for debuginfo

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 2.4.0-alt1.1
- Rebuilt with python-2.5.

* Tue Sep 18 2007 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- initial build for ALT Linux Sisyphus
