# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen
# END SourceDeps(oneline)
BuildRequires: chrpath
BuildRequires: gcc-c++
%add_optflags %optflags_shared
Name:           libifp
Version:        1.0.0.2
Release:        alt2_17
Summary:        A general-purpose library-driver for iRiver's iFP portable audio players

Group:          System/Base
License:        GPLv2
URL:            http://ifp-driver.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/ifp-driver/%{name}/%{version}-stable/%{name}-%{version}.tar.gz
Source1:        libifp.hotplug
Source2:        10-libifp.rules
# autoconf-2.69 breaks configure.in (likely configure.in is the broken part)
# Upstream is dead, so fix it here:
Patch0:         libifp-1.0.0.2-fix-broken-configure.in.diff

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires: libusb-compat-devel libusb-devel
Source44: import.info

%description
libifp is a general-purpose library-driver for iRiver's iFP (flash-based)
portable audio players. The source code is pure C and is fairly portable.

Also included is a console app that uses the library.

%package        devel
Summary:        Headers and libraries for developing with libifp
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains headers and libraries for developing apps that use
libifp.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fiv
%configure --with-libusb --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;
install -D -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/sbin/libifp-hotplug
install -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/10-libifp.rules
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done

%files
%doc ChangeLog COPYING README TODO
%{_bindir}/*
%{_libdir}/*.so.*
/sbin/*
%{_sysconfdir}/udev/rules.d/*.rules

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_mandir}/man3/*

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt2_17
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt2_15
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt2_14
- update to new release by fcimport

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.0.2-alt2_13.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for libifp

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt2_13
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt2_12
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt2_11
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt2_10
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0.2-alt1_10
- initial import by fcimport

