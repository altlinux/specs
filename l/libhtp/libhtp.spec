Name: libhtp
Epoch: 1
Version: 0.5.25
Release: alt1
Summary: LibHTP is a security-aware parser for the HTTP protocol and the related bits and pieces
License: BSD License
Group: Security/Networking
Url: https://github.com/OISF/libhtp
Source0: %name-%version.tar
BuildRequires: zlib-devel

%description
This is a security-aware parser for the HTTP protocol and the related bits
and pieces. The goals of the project, in the order of importance, are as
follows:

 1. Completeness of coverage; LibHTP must be able to parse virtually all
    traffic that is found in practice.

 2. Permissive parsing; LibHTP must never fail to parse a stream that would
    be parsed by some other web server.

 3. Awareness of evasion techniques; LibHTP must be able to detect and
    effectively deal with various evasion techniques, producing, where
    practical, identical or practically identical results as the web
    server processing the same traffic stream.

 4. Performance; The performance must be adequate for the desired tasks.
    Completeness and security are often detrimental to performance. Our
    idea of handling the conflicting requirements is to put the library
    user in control, allowing him to choose the most desired library
    characteristic.

%package devel
Summary: Development headers and libraries for %name
Requires: %name = %version-%release
Group: Security/Networking

%description devel
Development headers and libraries for %name.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/%{name}*.so.*

%files devel
%_libdir/%name.so
%_includedir/htp
%_libdir/pkgconfig/htp.pc

%changelog
* Thu Jul 21 2017 Starostin Nikita <stark@altlinux.org> 1:0.5.25-alt1
- initial build
