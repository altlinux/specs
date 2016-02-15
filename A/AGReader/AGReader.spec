Name:           AGReader
Version:        1.2
Release:        alt2_15
Summary:        Console reader for viewing AmigaGuide files
Group:          Text tools
License:        GPL+
URL:            http://main.aminet.net/misc/unix/
Source0:        http://main.aminet.net/misc/unix/%{name}.tar.bz2
Source1:        agr.1
Source44: import.info

%description
A viewer for the UNIX console which can read and display AmigaGuide files. It
supports all of the v39 AmigaGuide specification possible and supports a large
subset of the v40 specifications.


%prep
%setup -qn %{name}


%build
make -C Sources %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1
install -m0755 Sources/agr %{buildroot}%{_bindir}


%files
%{_bindir}/agr
%{_mandir}/man1/agr.1*
%doc Docs/agr.guide Docs/test.guide Docs/agr.html README


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_9
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_8
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_7
- initial release by fcimport

