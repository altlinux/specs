%define oname rdflib

%def_with python3

Name: python-module-%oname
Version: 4.2.1
Release: alt1

Summary: RDFLib is a Python library for working with RDF

Group: Development/Python
License: See License
Url: http://rdflib.net/

%setup_python_module %oname

# Source-url: https://github.com/RDFLib/rdflib/archive/4.0.1.tar.gz
Source: %oname-%version.tar

BuildArch: noarch

#add_python_req_skip FOPLRelationalModel RDF

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-numpy python-module-pyasn1 python-module-serial python-module-setuptools python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-BeautifulSoup python-module-PyXML python-module-Pyrex python-module-bibtex python3-module-setuptools rpm-build-python3

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
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
#add_python3_req_skip FOPLRelationalModel RDF

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
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 4.2.1-alt1
- new version 4.2.1 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.2-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1
- Version 4.1.2

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 4.0.1-alt1
- new version 4.0.1 (with rpmrb script)

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.2.0-alt1.1
- Rebuild with Python-3.3

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
