Group: System/Libraries
%add_optflags %optflags_shared
%define oldname npth
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libnpth
Version:        1.5
Release:        alt2
Summary:        The New GNU Portable Threads library
License:        LGPLv2+
URL:            http://git.gnupg.org/cgi-bin/gitweb.cgi?p=npth.git
Source:         https://gnupg.org/ftp/gcrypt/npth/%{oldname}-%{version}.tar.bz2
#Source1:        ftp://ftp.gnupg.org/gcrypt/npth/npth-%{version}.tar.bz2.sig
# Manual page is re-used and changed pth-config.1 from pth-devel package
Source2:        npth-config.1

BuildRequires:  gcc-common
Source44: import.info
Provides: npth = %{version}-%{release}

%description
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth. It has been designed as a replacement of
GNU Pth for non-ancient operating systems. In contrast to GNU Pth is is
based on the system's standard threads implementation. Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

%package        devel
Group: Development/C
Summary:        Development files for %{oldname}
Requires:       %{name} = %{version}-%{release}
Provides: npth-devel = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q


%build
%configure --disable-static
%make_build

%install
%makeinstall_std INSTALL='install -p'

mkdir -p %{buildroot}%{_mandir}/man1/
install -pm0644 %{S:2} %{buildroot}%{_mandir}/man1/

find %{buildroot} -name '*.la' -delete -print

%check
make check

%files
%doc COPYING.LIB
%{_libdir}/lib%{oldname}.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{oldname}-config
%{_libdir}/lib%{oldname}.so
%{_includedir}/%{oldname}.h
%{_mandir}/man1/%{oldname}-config.1*
%{_datadir}/aclocal/%{oldname}.m4

%changelog
* Sun Feb 04 2018 Fr. Br. George <george@altlinux.ru> 1.5-alt2
- Remove unused buildreq

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_2
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_6
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_5
- initial fc import

