
Name: libodfgen
Version: 0.0.4
Release: alt1
Summary: An ODF generator library
Group: System/Libraries
License: LGPLv2+ or MPLv2.0+
URL: http://sourceforge.net/projects/libwpd/
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libwpg-0.2) pkgconfig(libwpd-0.9)
BuildRequires: libetonyek-devel doxygen

%description
%name is a library for generating ODF (text and vector drawing formats
only). It is directly pluggable into input filters based on
libwpd/libwpg. It is used in libreoffice, for example.

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup -q

%build
mkdir -p m4
%autoreconf
%configure --disable-silent-rules --disable-static --disable-werror \
 --with-sharedptr=c++11 CXXFLAGS="$CXXFLAGS -std=c++11"
%make_build


%install
%make_install install DESTDIR=%buildroot

%files
%doc COPYING.* README
%_libdir/*.so.*


%files devel
%doc %_defaultdocdir/%name
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.0.4-alt1
- new version

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.0.2-alt1
- initial build
