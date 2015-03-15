Name: xmlrpcxx
Version: 0.7
Release: alt1.git20100306
Summary: C++ implementation of the XML-RPC protocol
License: LGPLv2.1+
Group: System/Libraries
Url: http://xmlrpcpp.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://gitorious.org/xmlrpc/xmlrpc.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake

%description
XmlRpc++ is a C++ implementation of the XML-RPC protocol. It is based
upon Shilad Sen's excellent py-xmlrpc. The XmlRpc protocol was designed
to make remote procedure calls easy: it encodes data in a simple XML
format and uses HTTP for communication. XmlRpc++ is designed to make it
easy to incorporate XML-RPC client and server support into C++
applications.

%package -n lib%name
Summary: C++ implementation of the XML-RPC protocol
Group: System/Libraries

%description -n lib%name
XmlRpc++ is a C++ implementation of the XML-RPC protocol. It is based
upon Shilad Sen's excellent py-xmlrpc. The XmlRpc protocol was designed
to make remote procedure calls easy: it encodes data in a simple XML
format and uses HTTP for communication. XmlRpc++ is designed to make it
easy to incorporate XML-RPC client and server support into C++
applications.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
XmlRpc++ is a C++ implementation of the XML-RPC protocol. It is based
upon Shilad Sen's excellent py-xmlrpc. The XmlRpc protocol was designed
to make remote procedure calls easy: it encodes data in a simple XML
format and uses HTTP for communication. XmlRpc++ is designed to make it
easy to incorporate XML-RPC client and server support into C++
applications.

This package contains development files of %name.

%prep
%setup

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1

%install
%makeinstall_std

%files -n lib%name
%doc *.html
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20100306
- Initial build for Sisyphus

