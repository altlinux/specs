%define module_name protobuf-socket-rpc

%define svn_rev 47
Name: python-module-%module_name
Version: 1.3.1
Release: alt2.svn%svn_rev.1

Summary: Python protobuf rpc implementation using tcp/ip sockets

License: MIT
Group: Development/Python
Url: http://code.google.com/p/protobuf-socket-rpc/

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-module-setuptools

%setup_python_module %module_name


%description
Python protobuf rpc implementation using tcp/ip sockets

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/protobuf
%python_sitelibdir/protobuf_socket_rpc*


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.svn47.1
- Rebuild with Python-2.7

* Wed Feb 24 2010 Denis Klimov <zver@altlinux.org> 1.3.1-alt2.svn47
- add BuildRequires to python-module-setuptools

* Tue Feb 23 2010 Denis Klimov <zver@altlinux.org> 1.3.1-alt1.svn47
- Initial build for ALT Linux
