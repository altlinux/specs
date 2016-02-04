# test new macroses
%define python_build CFLAGS="%optflags" python setup.py build
%define python_install python setup.py install --root %buildroot --optimize=2

%def_without python3

%define oname pyspatialite
Name: python-module-%oname
Version: 3.0.1
Release: alt1.1

Summary: Python interface to Spatialite

License: zlib
Group: Development/Python
Url: http://pyspatialite.googlecode.com/

%setup_python_module %oname

Source: %oname-%version.tar
Patch0: %oname-3.0.1-vendor-setup.patch
Patch1: %oname-alt-fix-build.patch

BuildRequires: libsqlite3-devel
BuildRequires: libspatialite-devel
BuildRequires: libgeos-devel
BuildRequires: libproj-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3
%endif

%description
pyspatialite is an interface to the SQLite 3.x embedded relational
database engine with spatialite extensions.
It is almost fully compliant with the Python database API version 2.0
and also exposes the unique features of SQLite and spatialite.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %version-%release

%description tests
pyspatialite is an interface to the SQLite 3.x embedded relational
database engine with spatialite extensions.
It is almost fully compliant with the Python database API version 2.0
and also exposes the unique features of SQLite and spatialite.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python interface to Spatialite (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
pyspatialite is an interface to the SQLite 3.x embedded relational
database engine with spatialite extensions.
It is almost fully compliant with the Python database API version 2.0
and also exposes the unique features of SQLite and spatialite.

%package -n python3-module-%oname-tests
Summary: Tests for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
pyspatialite is an interface to the SQLite 3.x embedded relational
database engine with spatialite extensions.
It is almost fully compliant with the Python database API version 2.0
and also exposes the unique features of SQLite and spatialite.

This package contains tests for %oname.
%endif

%prep
%setup -n %oname-%version
%patch0 -p2
%patch1 -p2

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
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

rm -rf %buildroot%_usr/pyspatialite-doc/

%files
%doc doc/install-source.txt
%python_sitelibdir/%{oname}*
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%if_with python3
%files -n python3-module-%oname
%doc doc/install-source.txt
%python3_sitelibdir/%{oname}*
%exclude %python3_sitelibdir/%oname/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test
%endif

%changelog
* Thu Feb 04 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1.1
- Rebuild with new libspatialite

* Sun Jun 09 2013 Ivan Ovcherenko <asdus@altlinux.org> 3.0.1-alt1
- Initial release
