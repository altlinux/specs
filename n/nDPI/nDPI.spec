Name: nDPI
Version: 2.2
Release: alt1
Summary: Open source deep packet inspection
Group: System/Libraries

Url: http://www.ntop.org/products/ndpi/
License: LGPLv3

Packager: Alexei Takaseev <taf@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Wed Sep 30 2015
# optimized out: gnu-config pkg-config
BuildRequires: libpcap-devel

%description
nDPI is a ntop-maintained superset of the popular OpenDPI
library. Released under the GPL license, its goal is to extend the
original library by adding new protocols that are otherwise available
only on the paid version of OpenDPI. In addition to Unix platforms,
we also support Windows, in order to provide you a cross-platform DPI
experience. Furthermore, we have modified nDPI do be more suitable for
traffic monitoring applications, by disabling specific features that
slow down the DPI engine while being them un-necessary for network
traffic monitoring.

nDPI is used by both ntop and nProbe for adding application-layer
detection of protocols, regardless of the port being used. This means
that it is possible to both detect known protocols on non-standard
ports (e.g. detect http non ports other than 80), and also the opposite
(e.g. detect Skype traffic on port 80). This is because nowadays the
concept of port=application no longer holds.

%package -n lib%name
Summary: Open source deep packet inspection
Group: System/Libraries

%description -n lib%name
nDPI is a ntop-maintained superset of the popular OpenDPI
library. Released under the GPL license, its goal is to extend the
original library by adding new protocols that are otherwise available
only on the paid version of OpenDPI. In addition to Unix platforms,
we also support Windows, in order to provide you a cross-platform DPI
experience. Furthermore, we have modified nDPI do be more suitable for
traffic monitoring applications, by disabling specific features that
slow down the DPI engine while being them un-necessary for network
traffic monitoring.

nDPI is used by both ntop and nProbe for adding application-layer
detection of protocols, regardless of the port being used. This means
that it is possible to both detect known protocols on non-standard
ports (e.g. detect http non ports other than 80), and also the opposite
(e.g. detect Skype traffic on port 80). This is because nowadays the
concept of port=application no longer holds.

%package -n lib%name-devel
Summary: Header files and libraries for developing applications for nDPI
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-devel
These are the header files and libraries for developing applications for nDPI.

%package demo
Summary: Demo for nDPI
License: LGPLv3
Group: System/Libraries

%description demo
Demo for nDPI

%prep
%setup
%patch0 -p1

%build
sh autogen.sh
%configure --with-pic
%make_build

%install
%makeinstall
mv %buildroot%_includedir/libndpi-%version.0/libndpi %buildroot%_includedir
rmdir %buildroot%_includedir/libndpi-%version.0

%files -n lib%name
%_libdir/libndpi.so.*


%files -n lib%name-devel
%doc CHANGELOG.md COPYING INSTALL README.md README.nDPI README.protocols
%_includedir/libndpi
%_libdir/pkgconfig/libndpi.pc
%_libdir/libndpi.so

%files demo
%_bindir/ndpiReader

%changelog
* Mon Dec 04 2017 Alexei Takaseev <taf@altlinux.org> 2.2-alt1
- 2.2

* Wed Feb 15 2017 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Nov 11 2016 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt6
- Re-merge with 1.7-stable, drop i586 compatable patches

* Wed Aug 03 2016 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt5
- Revert "Fix detect http/https"

* Tue Mar 15 2016 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt4
- Add missing include file

* Tue Mar 15 2016 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt3
- Fix detect http/https

* Thu Feb 18 2016 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt2
- Fix memory allocator type compatible with C++ on x686 platforms.
- Fix detect ssl on ipv6
- Fix detect ssl as tor.

* Wed Sep 30 2015 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt1
- Initial build for ALT
