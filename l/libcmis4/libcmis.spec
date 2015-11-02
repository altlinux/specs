Name: libcmis4
Version: 0.4.1
Release: alt3
Summary: A C++ client library for the CMIS interface
Group: System/Libraries
License: GPLv2+ or LGPLv2+ or MPLv1.1
Url: http://sourceforge.net/projects/libcmis/
Source: libcmis-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libxml-2.0)

BuildRequires: boost-devel boost-program_options-devel
BuildRequires: doxygen
BuildRequires: xmlto

Patch: %name-%version-%release.patch
Provides: libcmis = %version-%release

%description
LibCMIS is a C++ client library for the CMIS interface. This allows C++
applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Provides: libcmis-devel = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n libcmis-%version
%patch -p1
touch ChangeLog
mkdir -p m4
sed -i '/_BOOST_SED_CPP.*boost-lib-version =/c\
     _BOOST_SED_CPP([/^[[^#]][[^\\"]]*\\"/{s///;s/\\"//g;p;g;}],
' m4/boost.m4

%build
%autoreconf
%configure --disable-static --disable-werror --disable-tests DOCBOOK2MAN='xmlto man'
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS COPYING.* NEWS README
%_libdir/*.so.*
%exclude %_bindir/*
%exclude %_man1dir/*.1*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Oct 19 2015 Fr. Br. George <george@altlinux.ru> 0.4.1-alt3
- build legacy libcmis4 version
- rebuild with gcc5

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.4.1-alt2.1
- rebuild with boost 1.57.0

* Thu Mar 20 2014 Fr. Br. George <george@altlinux.ru> 0.4.1-alt2
- fix incorrectly formed patch

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.4.1-alt1
- new version

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- initial build
