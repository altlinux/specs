%define module_name jsonrpc
Name: python-module-%module_name
Version: 0.6.2
Release: alt1.git20150204

Summary: json-rpc package which implements JSON-RPC over HTTP

License: LGPL
Group: Development/Python
Url: http://json-rpc.org/wiki/python-json-rpc

Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name
BuildPreReq: python-module-setuptools-tests python-module-bunch
BuildPreReq: python-modules-json

%description
Simple Reference JSON-RPC Implementation for Django

%prep
%setup

%build
%python_build

%install
%python_install

%check
python setup.py test

%files
%python_sitelibdir/*

%changelog
* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20150204
- Version 0.6.2

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141026
- Version 0.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.01-alt1.svn19.1
- Rebuild with Python-2.7

* Mon Feb 22 2010 Denis Klimov <zver@altlinux.org> 0.01-alt1.svn19
- Initial build for ALT Linux

