# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen pkgconfig(bluez) pkgconfig(libusb-1.0)
# END SourceDeps(oneline)
BuildRequires: chrpath
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major           0
%define libname     libdivecomputer%{major}
%define develname   libdivecomputer-devel

Name:       libdivecomputer
Version:    0.6.0
Release:    alt1_1
Summary:    Library for communication with dive computers
License:    LGPL
Group:      Development/C
URL:        http://www.divesoftware.org/libdc/index.html
Source:     http://www.divesoftware.org/libdc/download/libdivecomputer-%{version}.tar.gz
Source44: import.info

%description
Libdivecomputer is a cross-platform and open source library for communication
with dive computers from various manufacturers.

%package -n %{libname}
Summary:    Libraries for %{name}
Group:      Development/C

%description -n %{libname}
Libraries for %{name}.

%package -n %{develname}
Summary:    Header files and development libraries for %{name}
Group:      Development/C
Requires:   %{libname} = %{version}-%{release}
Provides:   divecomputer-devel = %{version}-%{release}

%description -n %{develname}
Header files and development libraries for %{name}.

%prep
%setup -q

%build
%configure --disable-static
%make

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libdivecomputer.so.%{major}
%{_libdir}/libdivecomputer.so.%{major}.*

%files -n %{develname}
%{_includedir}/%{name}/
%{_mandir}/man3/*
%{_libdir}/libdivecomputer.so
%{_libdir}/pkgconfig/libdivecomputer.pc


%changelog
* Fri Jun 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_1
- new version

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_8
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_6
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_2
- update to new release by fcimport

* Mon Jul 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_1
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_2
- initial fc import

