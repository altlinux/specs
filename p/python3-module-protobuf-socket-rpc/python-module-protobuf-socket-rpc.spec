%define oname protobuf-socket-rpc

Name: python3-module-%oname
Version: 1.3.1
Release: alt3

Summary: Python protobuf rpc implementation using tcp/ip sockets
License: MIT
Group: Development/Python3
Url: http://code.google.com/p/protobuf-socket-rpc/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

Requires: python3-module-protobuf


%description
Python protobuf rpc implementation using tcp/ip sockets

%prep
%setup

cp proto/rpc.proto python/src/protobuf/socketrpc/

# port to py3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|str("", "utf-8")|"".encode("utf-8")|' $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/protobuf
%python3_sitelibdir/protobuf_socket_rpc*


%changelog
* Fri Feb 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.1-alt3
- Porting to python3.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2.svn104
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.svn47.1
- Rebuild with Python-2.7

* Wed Feb 24 2010 Denis Klimov <zver@altlinux.org> 1.3.1-alt2.svn47
- add BuildRequires to python-module-setuptools

* Tue Feb 23 2010 Denis Klimov <zver@altlinux.org> 1.3.1-alt1.svn47
- Initial build for ALT Linux
