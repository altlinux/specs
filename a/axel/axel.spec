%global commit0 7993512ca6b259cf04e9011541205db403ea1846
%global gittag0 2.5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})


Name:		axel		
Version:	2.5
Release:	alt1_2
Summary:	Light command line download accelerator for Linux and Unix

Group:		Networking/WWW
License:	GPLv2+
URL:		https://github.com/eribertomota/%{name}
Source0:    https://github.com/eribertomota/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildRequires:	gettext
Source44: import.info



%description
Axel tries to accelerate HTTP/FTP downloading process by using 
multiple connections for one file. It can use multiple mirrors for a 
download. Axel has no dependencies and is lightweight, so it might 
be useful as a wget clone on byte-critical systems.

%prep
%setup -q -n %{name}-%{commit0}

%build
export CFLAGS=" %{optflags}"
export CXXFLAGS=" %{optflags}"
./configure --prefix=%{_prefix} --strip=0
make %{?_smp_mflags}


%install
make install \
	DESTDIR=%{buildroot}

install -m 755 -p %{name} %{buildroot}%{_bindir}

%find_lang	%{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%doc CHANGES CREDITS API README
%doc COPYING
%config(noreplace) %{_sysconfdir}/axelrc
%{_mandir}/man1/axel.1*


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_6
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_5
- initial release by fcimport

