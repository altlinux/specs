%define soversion 1
Name: libuv
Version: 0.10.3
Release: alt1
Summary: Evented I/O for NodeJS
Group: Development/Tools
License: MIT License
Url: https://github.com/joyent/libuv
Source: %name-%version.tar

BuildRequires: python-devel gcc-c++ openssl-devel zlib-devel gyp

%add_python_req_skip TestCommon

%description
libuv is a new platform layer for Node. Its purpose is to abstract IOCP on Windows 
and libev on Unix systems. We intend to eventually contain all platform differences in this library.

%package devel
Summary:        Devel package for libuv
Group:          Development/Other
License:        GPL
Requires:	%name = %version

%description devel
libuv header and build tools

%prep
%setup -q

%build
./gyp_uv
%make_build CXXFLAGS="%{optflags}" CFLAGS="%{optflags}" libuv.so

%install
mkdir -p %buildroot{%_libdir,%_includedir}
install libuv.so %buildroot%_libdir/libuv.so.%soversion
ln -s libuv.so.%soversion %buildroot%_libdir/libuv.so
cp -R include/* %buildroot%_includedir

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*


%changelog
* Sat Apr 06 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.3-alt1
- 0.10.3

* Thu Nov 15 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9-alt1
- Initial build

