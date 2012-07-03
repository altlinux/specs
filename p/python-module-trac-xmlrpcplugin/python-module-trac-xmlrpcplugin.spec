%define tarname xmlrpcplugin
Name: python-module-trac-xmlrpcplugin
%define r_minor r9436
Version: 1.1.0
Release: alt1.%r_minor.1

Summary: Remote Procedure Call interface for Trac

Group: Development/Python
License: BSD
Url: http://trac-hacks.org/wiki/XmlRpcPlugin

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

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
%setup -q -n %tarname/trunk

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

#Fix rights
chmod -R a+r %buildroot%python_sitelibdir/tracrpc/htdocs
chmod -R a+r %buildroot%python_sitelibdir/tracrpc/templates

%files
%doc
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.r9436.1
- Rebuild with Python-2.7

* Wed Nov 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0-alt1.r9436
- Build for ALT
