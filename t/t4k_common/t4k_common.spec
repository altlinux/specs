# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libSDL_ttf-devel pkgconfig(SDL_ttf)
# END SourceDeps(oneline)
Name: t4k_common
Version: 0.1.1
Release: alt2_7
URL: http://tux4kids.alioth.debian.org/
Summary: Library for Tux4Kids applications
License: GPLv3+
Source0: https://alioth.debian.org/frs/download.php/3540/%{name}-%{version}.tar.gz
Patch0: t4k_common-0.1.1-libpng15.patch
Group: System/Libraries
BuildRequires: libSDL-devel libSDL_mixer-devel libSDL_image-devel
BuildRequires: libSDL_pango-devel libSDL_net-devel librsvg-devel libcairo-devel
BuildRequires: libpng-devel libxml2-devel doxygen
Provides: bundled(liblinebreak)
Source44: import.info

%package devel
Summary: Development files for the Tux4Kids library
Group: Development/C++
Requires: t4k_common = %{version}-%{release}

%description
library of code shared by TuxMath, TuxType, and
possibly other Tux4Kids apps in the future.

%description devel
library of code shared by TuxMath, TuxType, and
possibly other Tux4Kids apps in the future.

These are the development files.

%prep
%setup -q

%patch0 -p0

%build
%configure
make %{?_smp_mflags}
doxygen
rm -f doxygen/html/installdox

%install
INSTALL='install -p' make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_includedir}/t4k_scandir.h
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so

%files
%doc COPYING README
%{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}/

%files devel
%doc doxygen/html/
%{_libdir}/lib%{name}.so
%{_includedir}/t4k*.h
%{_libdir}/pkgconfig/t4k_common.pc

%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_7
- converted by srpmconvert script

* Tue Jan 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_2
- dropped hook

* Fri Oct 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_2
- use fedora versions

* Tue Aug 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_1.8
- initial release by fcimport

