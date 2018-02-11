
Name: libodfgen
Version: 0.1.6
Release: alt1
Summary: An ODF generator library
Group: System/Libraries
License: LGPLv2+ or MPLv2.0+
URL: http://sourceforge.net/projects/libwpd/
# git-vcs git://git.code.sf.net/p/libwpd/libodfgen
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0)
BuildRequires: doxygen

%description
%name is a library for generating ODF (text and vector drawing formats
only). It is directly pluggable into input filters based on
libwpd/libwpg. It is used in libreoffice, for example.

%package devel
Summary: Development files for %name
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
%configure --disable-silent-rules --disable-static --disable-werror
%make_build

%install
%makeinstall_std

%files
%doc COPYING.* README
%_libdir/*.so.*


%files devel
%doc %_defaultdocdir/%name
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sun Feb 11 2018 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Tue Aug 18 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Mon Jan 19 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Wed Dec 17 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Mon Jun 16 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.0.4-alt1
- new version

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.0.2-alt1
- initial build
