# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install perl(SOAP/Lite.pm)
# END SourceDeps(oneline)
Name:         amtterm
License:      GPLv2+
Version:      1.4
Release:      alt1_2
Summary:      Serial-over-lan (sol) client for Intel AMT
Group:        Networking/WWW
URL:          http://www.kraxel.org/blog/linux/amtterm/
Source:       http://www.kraxel.org/releases/%{name}/%{name}-%{version}.tar.gz
Requires:     xdg-utils
BuildRequires: gtk2-devel libvte-devel desktop-file-utils
Source44: import.info

%description
Serial-over-lan (sol) client for Intel AMT.
Includes a terminal and a graphical (gtk) version.
Also comes with a perl script to gather informations
about and remotely control AMT managed computers.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make prefix=/usr

%install
make prefix=/usr DESTDIR=%{buildroot} STRIP="" install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ \
    %{buildroot}/%{_datadir}/applications/gamt.desktop

%files
%doc COPYING
%{_bindir}/amtterm
%{_bindir}/amttool
%{_bindir}/gamt
%{_mandir}/man1/amtterm.1*
%{_mandir}/man1/amttool.1*
%{_mandir}/man1/gamt.1*
%{_mandir}/man7/amt-howto.7*
%{_datadir}/applications/gamt.desktop

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_10
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_6
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1
- initial release by fcimport

