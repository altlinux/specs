%add_optflags %optflags_shared
%global snapshot 20141029
Name:       libecb
Version:    0.%{snapshot}
Release:    alt1_1
Summary:    Compiler built-ins
Group:      Development/C
License:    BSD or GPLv2+
URL:        http://software.schmorp.de/pkg/libecb
# Snapshot from CVS :pserver:anonymous@cvs.schmorp.de/schmorpforge libecb 
Source0:    %{name}-%{snapshot}.tar.xz
BuildArch:  noarch
Source44: import.info

%description
This project delivers you many GCC built-ins, attributes and a number of
generally useful low-level functions, such as popcount, expect, prefetch,
noinline, assume, unreachable and so on.

%prep
%setup -q -n %{name}-%{snapshot}

%build
# Keep empty %%build section for possible RPM hooks

%install
install -d %{buildroot}%{_includedir}
install -m 0644 -t %{buildroot}%{_includedir} *.h 

%files
%doc Changes ecb.pod LICENSE README
%{_includedir}/*

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.20141029-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20130509-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20130509-alt1_2
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.20130509-alt1_1
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.20121022-alt1_2
- initial fc import

