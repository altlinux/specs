%define oname couchquery

%def_with python3

Summary: Python library for simple and dynamic access to CouchDB
Name: python-module-couchquery
Version: 0.10.2
Release: alt1.git20140814.1
# https://github.com/nicolaisi/couchquery.git
Source0: %name-%version-%release.tar
License: GPL
Group: Development/Python
URL: http://github.com/mikeal/couchquery
BuildArch: noarch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python-tools-2to3
%endif

%description
This module is an attempt to combine the best features of httplib with
the scalability of asynchat.

I have pasted as much code as I could from httplib (Python 2.0) because it
is a well written and widely used interface. This may be a mistake,
because the behavior of AsynchHTTPConnection os quite different from that of
httplib.HTTPConnection

%package -n python3-module-%oname
Summary: Python library for simple and dynamic access to CouchDB
Group: Development/Python3

%description -n python3-module-%oname
This module is an attempt to combine the best features of httplib with
the scalability of asynchat.

I have pasted as much code as I could from httplib (Python 2.0) because it
is a well written and widely used interface. This may be a mistake,
because the behavior of AsynchHTTPConnection os quite different from that of
httplib.HTTPConnection

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
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

%files
%doc README.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.2-alt1.git20140814.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20140814
- Version 0.10.2
- Added module for Python 3

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.git20140406
- Version 0.10.1

* Thu Dec 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20131104
- Version 0.10.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt1.1
- Rebuild with Python-2.7

* Mon Dec 21 2009 Mikhail Pokidko <pma@altlinux.org> 0.9-alt1
- release 0.9

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.1
- Rebuilt with python 2.6

* Thu Oct 15 2009 Mikhail Pokidko <pma@altlinux.org> 0.8.3-alt1
- Initial build



