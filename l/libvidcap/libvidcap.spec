# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pkg-config gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libvidcap
Version:	0.2.1
Release:	alt1_15
Summary:	Cross-platform video capture library
Group:		System/Libraries
License:	LGPLv2+
URL:		http://libvidcap.sourceforge.net/
Source0:	http://downloads.sourceforge.net/libvidcap/%{name}-%{version}.tar.gz
BuildRequires:	kernel-headers
Source44: import.info

%description
A cross-platform library for capturing video from webcams and other video 
capture devices.

%package devel
Summary:	Development files for %{name}
Group:		Development/Perl
Requires:	%{name} = %{version}
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} PTHREAD_LIBS=-lpthread

%install
make install INSTALL="%{_bindir}/install -p" DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc COPYING.LESSER
%{_libdir}/libvidcap.so.*

%files devel
%{_libdir}/libvidcap.so
%{_libdir}/pkgconfig/vidcap.pc
%{_includedir}/vidcap/

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_10
- update to new release by fcimport

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_9
- fc update

* Tue Jan 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_8
- initial fc import

