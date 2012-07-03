# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary: Library for manipulating panoramic images
Name: libpano12
Version: 2.8.6
Release: alt2_5
License: GPLv2+
URL: http://panotools.sourceforge.net/
Group: System/Libraries
Source: http://downloads.sourceforge.net/panotools/%{name}-%{version}.tar.gz
BuildRequires: libjpeg-devel libtiffxx-devel libtiff-devel libpng-devel zlib-devel
BuildRequires: libgcj-devel
Source44: import.info

%description
Helmut Dersch's Panorama Tools library.  Provides very high quality
manipulation, correction and stitching of panoramic photographs.

Due to patent restrictions, this library has a maximum fisheye field-of-view
restriction of 160 degrees to prevent stitching of hemispherical photographs.

%package tools
Summary: Tools that use the libpano12 library
Group: Graphics
Requires: libpano12 = %{version}-%{release}

%description tools
PTOptimizer, a command-line interface for control-point optimisation.
pano12info, a tool for querying the library capabilities

%package devel
Summary: Development tools for programs which will use the libpano12 library
Group: System/Libraries
Requires: libpano12 = %{version}-%{release}

%description devel
The libpano12-devel package includes the header files necessary for developing
programs which will manipulate panoramas using the libpano12 library.

%prep
%setup -q

%build
%configure --disable-static
make

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}/%{_libdir}/libpano12.la

%files
%doc AUTHORS ChangeLog COPYING NEWS README README.linux
%{_libdir}/libpano12.so.0*

%files tools
%doc doc/Optimize.txt doc/stitch.txt
%{_bindir}/PTOptimizer
%{_bindir}/pano12info

%files devel
%{_includedir}/pano12
%{_libdir}/libpano12.so

%changelog
* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.8.6-alt2_5
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.8.6-alt1_5
- initial import by fcimport

* Thu Dec 18 2008 Sergei Epiphanov <serpiph@altlinux.ru> 2.8.4-alt2
- Remove ld.so update

* Mon Sep 25 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.8.4-alt1
- Update to new version

* Wed May 17 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.8.1-alt1
- Update to new version

* Sat Mar 04 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.8.0-alt1
- Update to new version

* Wed Feb 01 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.7.0.14-alt2
- Moving PanoTools to a separate package

* Sat Dec 03 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.7.0.14-alt1
- New version
- Enable java build with libgcj
- Added more programs from panorama-tools written on java

* Fri Sep 23 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.7.0.10-alt5
- Fix lib dependencies

* Fri Sep 23 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.7.0.10-alt4
- Some small spec corrections

* Fri Sep 09 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.7.0.10-alt3
- Adding package PanoTools

* Mon Sep 05 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.7.0.10-alt2
- converting for ALT Linux

* Tue Jul 26 2005 Sergei Epiphanov <serpiph@nikiet.ru> 2.7.0.10-alt1
-initial build
