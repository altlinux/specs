%define oname z3c.jsonrpcproxy

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt3.1
Summary: JSON RPC (javascript) proxy implementation for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.jsonrpcproxy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.publisher zope.viewlet z3c.xmlhttp

%description
This package provides an JSON-RPC (javascript) proxy used for Zope3. But
the javascript itself does not depend on any zope library and can be
used with any other JSON-RPC server. Note the xmlhttp request javascript
library form z3c.xmlhttp is required for this implementation.

%package -n python3-module-%oname
Summary: JSON RPC (javascript) proxy implementation for Zope3
Group: Development/Python3
%py3_requires zope.publisher zope.viewlet z3c.xmlhttp

%description -n python3-module-%oname
This package provides an JSON-RPC (javascript) proxy used for Zope3. But
the javascript itself does not depend on any zope library and can be
used with any other JSON-RPC server. Note the xmlhttp request javascript
library form z3c.xmlhttp is required for this implementation.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

