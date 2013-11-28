# vim: set ft=spec: -*- rpm-spec -*-

%define modulename persistent

%def_with python3

%if_with python3
%define py3name python3-module-%modulename
%define py3dir %py3name-%version
%endif

Name: python-module-%modulename
Version: 4.0.6
Release: alt1.1

%setup_python_module %modulename

Summary: Translucent persistent objects
License: ZPL 2.1
Group: Development/Python

Url: http://www.zope.org/Products/ZODB
Packager: Aleksey Avdeev <solo@altlinux.ru>

# git://github.com/zopefoundation/persistent.git
Source: %name-%version.tar

Conflicts: python-module-ZODB3

BuildPreReq: python-module-coverage
BuildPreReq: python-module-nose
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-setuptools-tests

%if_with python3
BuildPreReq: rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-coverage
BuildPreReq: python3-module-distribute
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-zope.interface
BuildPreReq: python3-module-setuptools-tests
%endif

%description
This package contains a generic persistence implementation for Python.
It forms the core protocol for making objects interact "transparently"
with a database such as the ZODB.

%package tests
Summary: Tests for translucent persistent objects
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains a generic tests persistence implementation for
Python. It forms the core protocol for making objects interact
"transparently" with a database such as the ZODB.

%if_with python3
%package -n %py3name
Summary: Sample python3 module specfile
Group: Development/Python

%description -n %py3name
This specfile is provided as sample specfile for python3 module
packages. It contains most of usual tags and constructions used in such
specfiles.

%package -n %py3name-tests
Summary: Sample python3 module tests specfile
Group: Development/Python
Requires: %py3name = %EVR

%description -n %py3name-tests
This specfile is provided as sample specfile for python3 module tests
packages. It contains most of usual tags and constructions used in such
specfiles.

%endif

%prep
%setup
%if_with python3
rm -rf ../%py3dir
cp -a . ../%py3dir
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
popd
%endif
%python_install

%check
%__python setup.py test -q
%if_with python3
pushd ../%py3dir
%__python3 setup.py test -q
popd
%endif

%files
%doc CHANGES.txt COPYRIGHT.txt LICENSE.txt README.txt
%_includedir/python%_python_version
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/test*
%python_sitelibdir/*.egg-info

%files tests
%python_sitelibdir/%modulename/test*

%if_with python3
%files -n %py3name
%doc CHANGES.txt COPYRIGHT.txt LICENSE.txt README.txt
%_includedir/python%_python3_version%_python3_abiflags
%python3_sitelibdir/%modulename/
%exclude %python3_sitelibdir/%modulename/test*
%python3_sitelibdir/*.egg-info

%files -n %py3name-tests
%python3_sitelibdir/%modulename/test*
%endif

%changelog
* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1.1
- Fixed build

* Wed Mar 13 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.6-alt1
- Initial build for ALT Linux Sisyphus
