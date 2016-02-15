Group: File tools
Name:		ath_info
Version:	0
Release:	alt2_0.12.20130214svn
Summary:	Tool to get detailed information from Atheros WLAN cards

License:	GPLv2
URL:		http://madwifi-project.org/wiki/UserDocs/AthInfo
# The source tarball was generated with:
# svn export -r 4151 http://madwifi-project.org/svn/ath_info/trunk ath_info-20130214
# tar -Jcf ath_info-20130214.tar.xz ath_info-20130214/
Source0:	ath_info-20130214.tar.xz
Source44: import.info

%description
ath_info prints some version information of Atheros WLAN modules. It
furthermore allows to change regulatory domain and PCI ID fields in the EEPROM.
Since the output of lspci and dmesg is not always sufficient to correctly
identify chipset versions, it is useful to attach ath_info output to bug
reports for the ath5k driver.

%prep
%setup -q -n ath_info-20130214

%build
make PREFIX=%{_prefix} CFLAGS="%{optflags}" %{?_smp_mflags}

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%doc README
%{_bindir}/ath_info
%{_mandir}/man8/ath_info.*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.12.20130214svn
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.11.20130214svn
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.10.20130214svn
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.9.20130214svn
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.8.20130214svn
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.7.20130214svn
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.5.20100708svn
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.4.20100708svn
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.4.20100708svn
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.3.20100708svn
- initial release by fcimport

