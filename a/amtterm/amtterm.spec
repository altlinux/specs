# BEGIN SourceDeps(oneline):
BuildRequires: perl(SOAP/Lite.pm)
# END SourceDeps(oneline)
Name:         amtterm
License:      GPLv2+
Version:      1.3
Release:      alt2_5
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

