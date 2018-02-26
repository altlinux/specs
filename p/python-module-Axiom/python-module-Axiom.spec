%define version 0.6.0
%define release alt1
%setup_python_module Axiom

Name: %packagename
Version:%version
Release: %release.1
BuildArch: noarch


Summary: An in-process object-relational database
License: MIT
Group: Development/Python
Packager: Alexey Shabalin <shaba@altlinux.ru>
Url: http://divmod.org/trac/wiki/DivmodAxiom

Source: http://divmod.org/trac/attachment/wiki/SoftwareReleases/%modulename-%version.tar.gz

BuildPreReq: rpm-build-python
BuildRequires: python-module-Cython python-module-Epsilon python-module-twisted python-module-apsw python-module-pysqlite2
BuildRequires: python-devel python-module-setuptools
BuildPreReq: python-module-zope.interface

%description
Axiom is a live database, not only an SQL generation tool: it includes
an implementation of a scheduler service, external file references,
automatic upgraders, robust failure handling, and Twisted integration.

Axiom is tightly integrated with Twisted, and can store, start, and stop
Twisted services directly from the database using the included
'axiomatic' command-line tool.

Axiom currently supports only SQLite and does NOT have any features for
dealing with concurrency.  We do plan to add some later, and perhaps
also support other databases in the future.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%_bindir/axiomatic
%python_sitelibdir/Axiom-*.egg-info
%python_sitelibdir/axiom/
%python_sitelibdir/twisted/plugins/*.py*
%doc *.txt LICENSE

#%%exclude %_bindir/*

%changelog
* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt1.1
- Rebuild with Python-2.7

* Tue Mar 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.31-alt1.1
- Rebuilt with python 2.6

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 0.5.31-alt1
- 0.5.31
- build as noarch

* Mon Nov 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.5.27-alt1
- first build for Sisyphus
- thx to aris@ for spec 

