%define tarname xmlrpcplugin
Name: python-module-trac-xmlrpcplugin
%define r_minor r13776
Version: 1.1.2
Release: alt1.%r_minor

Summary: Remote Procedure Call interface for Trac

Group: Development/Python
License: BSD
Url: http://trac-hacks.org/wiki/XmlRpcPlugin

# http://trac-hacks.org/svn/xmlrpcplugin/trunk/
Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
Protocols:
 * XML-RPC
 * JSON-RPC
 
API support:
 * search
 * system
 * ticket
 * ticket.component
 * ticket.milestone
 * ticket.priority
 * ticket.resolution
 * ticket.severity
 * ticket.status
 * ticket.type
 * ticket.version
 * wiki

%prep
%setup -n %tarname

%build
%python_build

%install
%python_install

#Fix rights
chmod -R a+r %buildroot%python_sitelibdir/tracrpc/htdocs
chmod -R a+r %buildroot%python_sitelibdir/tracrpc/templates

%files
%doc
%python_sitelibdir/*

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.r13776
- Version 1.1.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.r9436.1
- Rebuild with Python-2.7

* Wed Nov 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0-alt1.r9436
- Build for ALT
