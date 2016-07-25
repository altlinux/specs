
Name: http-parser
Version: 2.7.0
Release: alt1
Summary: HTTP request/response parser for C

Group: System/Libraries
License: MIT
Url: http://github.com/joyent/http-parser
Source: %name-%version.tar

%description
This is a parser for HTTP messages written in C. It parses both requests and
responses. The parser is designed to be used in performance HTTP applications.
It does not make any syscalls nor allocations, it does not buffer data, it can
be interrupted at anytime. Depending on your architecture, it only requires
about 40 bytes of data per message stream (in a web server that is per
connection).

%package -n lib%name
Summary: HTTP request/response parser for C
Group: System/Libraries

%description -n lib%name
This is a parser for HTTP messages written in C. It parses both requests and
responses. The parser is designed to be used in performance HTTP applications.
It does not make any syscalls nor allocations, it does not buffer data, it can
be interrupted at anytime. Depending on your architecture, it only requires
about 40 bytes of data per message stream (in a web server that is per
connection).

%package -n lib%name-devel
Summary: HTTP request/response parser for C
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development headers and libraries for http-parser.

%prep
%setup -q

%build
%make library

%install
%makeinstall_std PREFIX=%buildroot%_prefix LIBDIR=%buildroot%_libdir

# fix symlinks
cd %buildroot%_libdir
rm -f libhttp_parser.so
ln -sf libhttp_parser.so.2.7.0 libhttp_parser.so


%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS README.md LICENSE-MIT

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Fri Jul 08 2016 Alexey Shabalin <shaba@altlinux.ru> 2.7.0-alt1
- Initial packaging

