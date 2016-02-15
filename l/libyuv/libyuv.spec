# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%ifarch %{arm}
%global with_neon --enable-neon
%endif


Name:		libyuv
Summary:	YUV conversion and scaling functionality library
Version:	0
Release:	alt1_0.25.20121221svn522
License:	BSD
Group:		Development/C
Url:		http://code.google.com/p/libyuv/
## svn -r 522 export http://libyuv.googlecode.com/svn/trunk libyuv-0
## tar -cjvf libyuv-0.tar.bz2 libyuv-0
Source0:	%{name}-%{version}.tar.bz2
# Fedora-specific. Upstream isn't interested in this.
Patch1:		libyuv-0001-Initial-autotools-support.patch
# big endian fix - http://code.google.com/p/libyuv/issues/detail?id=171
Patch2:		libyuv-endian.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libgtest-devel
BuildRequires:	libjpeg-devel
Source44: import.info


%description
This is an open source project that includes YUV conversion and scaling
functionality. Converts all webcam formats to YUV (I420). Convert YUV to
formats for rendering/effects. Rotate by 90 degrees to adjust for mobile
devices in portrait mode. Scale YUV to prepare content for compression,
with point, bilinear or box filter.


%package devel
Summary: The development files for %{name}
Group: Development/C
Requires: pkgconfig
Requires: %{name}%{?_isa} = %{version}


%description devel
Additional header files for development with %{name}.


%prep
%setup -q
%patch1 -p1 -b .autotools
%patch2 -p1 -b .endian


%build
sh autogen.sh
%configure --disable-static --with-pic --with-test --with-mjpeg %{?with_neon}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la


%check
make check


%files
%doc AUTHORS LICENSE PATENTS
%{_libdir}/%{name}.so.*


%files devel
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.25.20121221svn522
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.24.20121221svn522
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.22.20121221svn522
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.21.20121221svn522
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.20.20121221svn522
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.19.20121221svn522
- initial fc import

