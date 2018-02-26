%define oname httpencode

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt2.svn20090926
Summary: Fast RPC or encoded calls between WSGI apps
License: MIT
Group: Development/Python
Url: http://pythonpaste.org/httpencode/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.pythonpaste.org/Paste/HTTPEncode/trunk
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
This library allows you to make fast calls between cooperating WSGI
applications, with automatic fallback for non-cooperative applications
or remote applications.

Requests are sent through WSGI obeying all middleware and the WSGI
spec. Serialization/deserialization is avoided when possible.

%if_with python3
%package -n python3-module-%oname
Summary: Fast RPC or encoded calls between WSGI apps (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This library allows you to make fast calls between cooperating WSGI
applications, with automatic fallback for non-cooperative applications
or remote applications.

Requests are sent through WSGI obeying all middleware and the WSGI
spec. Serialization/deserialization is avoided when possible.

%package -n python3-module-%oname-examples
Summary: Examples for fast RPC or encoded calls between WSGI apps (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-examples
This library allows you to make fast calls between cooperating WSGI
applications, with automatic fallback for non-cooperative applications
or remote applications.

Requests are sent through WSGI obeying all middleware and the WSGI
spec. Serialization/deserialization is avoided when possible.

This package contains examples for httpencode.
%endif

%package examples
Summary: Examples for fast RPC or encoded calls between WSGI apps
Group: Development/Python
Requires: %name = %version-%release

%description examples
This library allows you to make fast calls between cooperating WSGI
applications, with automatic fallback for non-cooperative applications
or remote applications.

Requests are sent through WSGI obeying all middleware and the WSGI
spec. Serialization/deserialization is avoided when possible.

This package contains examples for httpencode.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	sed -i 's|%_bindir/env python|%_bindir/env python3|' $i
	2to3 -w -n $i
done
sed -i 's|simplejson|json|' httpencode/json.py
%python3_build
popd
%endif

%install
%python_install

install -d %buildroot%python_sitelibdir/%oname/examples
install -p -m755 examples/* %buildroot%python_sitelibdir/%oname/examples

%if_with python3
pushd ../python3
%python3_install
install -d %buildroot%python3_sitelibdir/%oname/examples
install -p -m755 examples/* %buildroot%python3_sitelibdir/%oname/examples
popd
%endif

%files
%doc docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/examples

%files examples
%python_sitelibdir/*/examples

%if_with python3
%files -n python3-module-%oname
%doc docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/examples
%endif

%changelog
* Sun Jun 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2.svn20090926
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt1.svn20090926.2.1
- Rebuild with Python-2.7

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.svn20090926.2
- Extracted examples into separate package

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.svn20090926.1
- Rebuilt with python 2.6

* Sat Sep 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.svn20090926
- Initial build for Sisyphus

