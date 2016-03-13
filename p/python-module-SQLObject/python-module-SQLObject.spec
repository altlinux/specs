%define oname SQLObject

%def_with python3

%if_with python3
%define py3name python3-module-%oname
%define py3dir %py3name-%version
%endif

Name: python-module-SQLObject
Version: 2.0.0
Release: alt1.a2dev.20141028.1.1

Summary: Object-Relational Manager, aka database wrapper for Python

License: LGPL
Group: Development/Python
Url: http://sqlobject.org
Packager: Sergey Bolshakov <sbolshakov@altlinux.ru>

Source: http://pypi.python.org/packages/source/S/%oname/%oname-%version.tar

BuildArch: noarch
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

#BuildRequires: python-devel python-modules-compiler python-modules-encodings
#BuildPreReq: python-module-distribute

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python-tools-2to3
#BuildPreReq: python3-devel
#BuildPreReq: python3-module-distribute
%endif

%setup_python_module sqlobject

%description
SQLObject is a popular *Object Relational Manager* for providing an
object interface to your database, with tables as classes, rows as
instances, and columns as attributes.

SQLObject includes a Python-object-based query language that makes SQL
more abstract, and provides substantial database independence for
applications.

Supports MySQL, PostgreSQL, SQLite, Firebird, Sybase, and MaxDB (SAPDB).


%if_with python3
%package -n %py3name
Summary: Object-Relational Manager, aka database wrapper for Python3
Group: Development/Python

%description -n %py3name
SQLObject is a popular *Object Relational Manager* for providing an
object interface to your database, with tables as classes, rows as
instances, and columns as attributes.

SQLObject includes a Python-object-based query language that makes SQL
more abstract, and provides substantial database independence for
applications.

Supports MySQL, PostgreSQL, SQLite, Firebird, Sybase, and MaxDB (SAPDB).

%endif

%package doc
Summary: This package contains documentation for SQLObject.
Group: Development/Python

%description doc
SQLObject is a popular *Object Relational Manager* for providing an
object interface to your database, with tables as classes, rows as
instances, and columns as attributes.

SQLObject includes a Python-object-based query language that makes SQL
more abstract, and provides substantial database independence for
applications.

Supports MySQL, PostgreSQL, SQLite, Firebird, Sybase, and MaxDB (SAPDB).


%prep
%setup -n %oname-%version
%if_with python3
rm -rf ../%py3dir
cp -a . ../%py3dir
pushd ../%py3dir
find ./ -name '*.py' -print0 | xargs -0i 2to3 -w {}
popd
%endif

%build
%python_build
%if_with python3
pushd ../%py3dir
%python3_build
popd
%endif

%install
%if_with python3
pushd ../%py3dir
%python3_install
pushd %buildroot%_bindir
for f in `ls`
do
	2to3 -wn $f
	mv $f $f-%_python3_version
	ln -s $f-%_python3_version ${f}3
done
popd
popd
%endif
%python_install

# omit paste for a while
#__subst '/sqlobject\/manager/d' -e '/sqlobject\/wsgi_middleware.py/d' INSTALLED_FILES

%files
%doc README.txt
%_bindir/sqlobject-admin
%_bindir/sqlobject-convertOldURI
%python_sitelibdir/%modulename/
%python_sitelibdir/%oname-*.egg-info

%if_with python3
%files -n %py3name
%doc README.txt
%_bindir/sqlobject-admin-%_python3_version
%_bindir/sqlobject-admin3
%_bindir/sqlobject-convertOldURI-%_python3_version
%_bindir/sqlobject-convertOldURI3
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%oname-*.egg-info
%endif

%files doc
%doc docs/*

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.a2dev.20141028.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 2.0.0-alt1.a2dev.20141028.1
- NMU: Use buildreq for BR.

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a2dev.20141028
- Version 2.0.0a2dev-20141028

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1dev.20140817
- Version 2.0.0a1dev-20140817

* Wed Apr 17 2013 Fr. Br. George <george@altlinux.ru> 1.3.2-alt1.1
- Fix build with 2to3

* Wed Mar 20 2013 Aleksey Avdeev <solo@altlinux.ru> 1.3.2-alt1
- Version 1.3.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13.0-alt1.1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.1
- Fixed build

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- build new version 0.13.0
- cleanup spec and build rules

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1
- Rebuilt with python 2.6

* Mon Sep  1 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.2-alt0.M41.1
- 0.10.2

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.7rc1-alt1.0.1
- Rebuilt with python-2.5.

* Sun Mar 25 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.7rc1-alt1.0
- Rebuilt with rpm-build-python-0.30-alt3.

* Sun Nov 06 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.7rc1-alt1
- Initial build for Sisyphus
