%define module_name protobuf-socket-rpc

%def_without python3

%define svn_rev 104
Name: python-module-%module_name
Version: 1.3.1
Release: alt2.svn%svn_rev

Summary: Python protobuf rpc implementation using tcp/ip sockets

License: MIT
Group: Development/Python
Url: http://code.google.com/p/protobuf-socket-rpc/

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %module_name

Requires: python-module-protobuf

%description
Python protobuf rpc implementation using tcp/ip sockets

%package -n python3-module-%module_name
Summary: Python protobuf rpc implementation using tcp/ip sockets
Group: Development/Python3
Requires: python3-module-protobuf

%description -n python3-module-%module_name
Python protobuf rpc implementation using tcp/ip sockets

%prep
%setup
cp proto/rpc.proto python/src/protobuf/socketrpc/

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
%python_sitelibdir/protobuf
%python_sitelibdir/protobuf_socket_rpc*

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/protobuf
%python3_sitelibdir/protobuf_socket_rpc*
%endif

%changelog
* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2.svn104
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.svn47.1
- Rebuild with Python-2.7

* Wed Feb 24 2010 Denis Klimov <zver@altlinux.org> 1.3.1-alt2.svn47
- add BuildRequires to python-module-setuptools

* Tue Feb 23 2010 Denis Klimov <zver@altlinux.org> 1.3.1-alt1.svn47
- Initial build for ALT Linux
