%define module_name jsonrpc
%define svn_rev 19
Name: python-module-%module_name
Version: 0.01
Release: alt1.svn%svn_rev.1

Summary: json-rpc package which implements JSON-RPC over HTTP

License: LGPL
Group: Development/Python
Url: http://json-rpc.org/wiki/python-json-rpc

Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name

%description
Simple Reference JSON-RPC Implementation for Django

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%{module_name}*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.01-alt1.svn19.1
- Rebuild with Python-2.7

* Mon Feb 22 2010 Denis Klimov <zver@altlinux.org> 0.01-alt1.svn19
- Initial build for ALT Linux

