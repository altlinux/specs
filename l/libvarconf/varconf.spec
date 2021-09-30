Group: Development/Other
%add_optflags %optflags_shared
%define oldname varconf
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libvarconf
Version:        1.0.1
Release:        alt2_16
Summary:        Configuration library used by WorldForge clients

License:        LGPLv2+
URL:            http://worldforge.org/dev/eng/libraries/varconf
Source0:        http://downloads.sourceforge.net/worldforge/%{oldname}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  libsigc++2-devel
Source44: import.info
Provides: varconf = %{version}-%{release}

%description
Varconf is a configuration library intended for all applications. It manages
configuration data in files, command line arguments, and is used by most
WorldForge components.


%package devel
Group: Development/Other
Summary: Development files for varconf library
Requires: pkgconfig %{oldname} = %{version}-%{release}
Provides: varconf-devel = %{version}-%{release}


%description devel
Development libraries and headers for linking against the varconf library.


%prep
%setup -n %{oldname}-%{version} -q



%build
%add_optflags -std=c++14
%configure
%make_build


%install
%makeinstall_std

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

## cleaning up redundant docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{oldname}-%{version}

%check
make %{?_smp_mflags} check
cd tests ; ./conftest < conf.cfg




%files
%doc AUTHORS ChangeLog README THANKS TODO
%doc --no-dereference COPYING
%{_libdir}/lib%{oldname}-1.0.so.*


%files devel
%{_includedir}/%{oldname}-1.0
%{_libdir}/lib%{oldname}-1.0.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Oct 01 2021 Igor Vlasenko <viy@altlinux.org> 1.0.1-alt2_16
- fixed build with gcc11

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_16
- update to new release by fcimport

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1_11.1
- NMU: rebuilt to regenerate ABI.

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_9
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_6
- update to new release by fcimport

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1-alt1_4.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_4
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_3
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_2
- update to new release by fcimport

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_1
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt1_2
- initial release by fcimport

