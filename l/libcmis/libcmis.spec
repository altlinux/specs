Name: libcmis
Version: 0.5.0
Release: alt1
Summary: A C++ client library for the CMIS interface
Group: System/Libraries
License: GPLv2+ or LGPLv2+ or MPLv1.1
Url: http://sourceforge.net/projects/libcmis/
Source: %name-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libxml-2.0)

BuildRequires: boost-devel boost-program_options-devel
BuildRequires: doxygen
BuildRequires: xmlto

Patch: %name-0.4.1-alt2.1.patch

%description
LibCMIS is a C++ client library for the CMIS interface. This allows C++
applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Command line tool to access CMIS
Group: Publishing
Requires: %name = %version-%release

%description tools
The %name-tools package contains a tool for accessing CMIS from the
command line.

%prep
%setup
%patch -p1

%build
touch ChangeLog
mkdir -p m4
%autoreconf
%configure --disable-static --disable-werror --disable-tests DOCBOOK2MAN='xmlto man'
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS COPYING.* NEWS README
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files tools
%_bindir/*
%_man1dir/*.1*

%changelog
* Tue Feb 03 2015 Fr. Br. George <george@altlinux.ru> 0.5.0-alt1
- Autobuild version bump to 0.5.0
- Change packaging scheme

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.4.1-alt2.1
- rebuild with boost 1.57.0

* Thu Mar 20 2014 Fr. Br. George <george@altlinux.ru> 0.4.1-alt2
- fix incorrectly formed patch

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.4.1-alt1
- new version

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- initial build
