%define bname xvba
Name: lib%bname-devel
Version: 0.74
Release: alt1
Summary: AES XvBA SDK for Linux
License: Distibutable
Group: Development/C
URL: http://developer.amd.com
Source: %url/wordpress/media/2012/10/%bname-sdk-%version-404001.tar
Provides: %bname-devel = %version-%release

%description
This package contains the AMD Embedded Solutions X-Video Bitstream Acceleration
software development kit for Linux.


%prep
%setup -c


%build


%install
install -d -m 0755 %buildroot{%_libdir,%_includedir}
install -p -m 0644 include/* %buildroot%_includedir/
ln -sf libXvBAW.so.1 %buildroot%_libdir/libXvBAW.so


%files
%doc LICENSE README
%_libdir/*
%_includedir/*


%changelog
* Tue Jun 25 2013 Led <led@altlinux.ru> 0.74-alt1
- initial build
