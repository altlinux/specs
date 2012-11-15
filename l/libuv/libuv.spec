Name: libuv
Version: 0.9
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
./gyp_uv -f make
%make libuv.so libuv.a

%install
mkdir -p %buildroot{%_libdir,%_includedir}
install libuv.so %buildroot%_libdir/
install libuv.a %buildroot%_libdir/
cp -R include/* %buildroot%_includedir

%files
%_libdir/*.so

%files devel
%_libdir/*.a
%_includedir/*


%changelog
* Thu Nov 15 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9-alt1
- Initial build

