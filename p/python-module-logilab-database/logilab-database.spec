%define oname logilab-database

%def_with python3

Name: python-module-%oname
Version: 1.8.2
Release: alt1.hg20120210
Summary: Provides some classes to make unified access to different RDBMS possible

Group: Development/Python
License: LGPLv2.1+
URL: http://www.logilab.org/project/logilab-database
# hg clone http://hg.logilab.org/logilab/database
Source: database-%version.tar
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-devel python-module-logilab-common
buildPreReq: python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-logilab-common python-tools-2to3
%endif

%description
logilab-database provides some classes to make unified access to
different RDBMS possible:

* actually compatible db-api from different drivers to postgres, mysql,
  sqlite and sqlserver
* additional api for full text search
* extensions functions for common tasks such as creating database,
  index, users, dump and restore, etc...
* sql generation for INSERT/UPDATE/DELETE (in sqlgen.py)

%if_with python3
%package -n python3-module-%oname
Summary: Provides some classes to make unified access to different RDBMS possible (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
logilab-database provides some classes to make unified access to different
RDBMS possible:

* actually compatible db-api from different drivers to postgres, mysql,
  sqlite and sqlserver
* additional api for full text search
* extensions functions for common tasks such as creating database, index,
  users, dump and restore, etc...
* sql generation for INSERT/UPDATE/DELETE (in sqlgen.py)

%package -n python3-module-%oname-tests
Summary: Tests for logilab database package (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
logilab-database provides some classes to make unified access to different
RDBMS possible:

* actually compatible db-api from different drivers to postgres, mysql,
  sqlite and sqlserver
* additional api for full text search
* extensions functions for common tasks such as creating database, index,
  users, dump and restore, etc...
* sql generation for INSERT/UPDATE/DELETE (in sqlgen.py)

This package contains tests for logilab constraint package.
%endif

%package tests
Summary: Tests for logilab database package
Group: Development/Python
Requires: %name = %version-%release

%description tests
logilab-database provides some classes to make unified access to different
RDBMS possible:

* actually compatible db-api from different drivers to postgres, mysql,
  sqlite and sqlserver
* additional api for full text search
* extensions functions for common tasks such as creating database, index,
  users, dump and restore, etc...
* sql generation for INSERT/UPDATE/DELETE (in sqlgen.py)

This package contains tests for logilab constraint package.

%prep
%setup
touch test/__init__.py
%if_with python3
rm -rf ../python3
cp -a . ../python3
touch ../python3/test/__init__.py
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	if [ "$i" != "./setup.py" ]; then
		2to3 -w -n $i
	fi
done
%python3_build
popd
%endif

%install
%python_install
rm -f %buildroot%python_sitelibdir/logilab/__init__.py*
%if_with python3
pushd ../python3
%python3_install
popd
rm -f %buildroot%python3_sitelibdir/logilab/__init__.py*
%endif

%files
%doc ChangeLog README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test

%files tests
%python_sitelibdir/*/*/test

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test
%endif

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2-alt1.hg20120210
- Initial build for Sisyphus

