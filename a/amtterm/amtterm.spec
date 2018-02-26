BuildRequires: perl(SOAP/Lite.pm)
Name:         amtterm
License:      GPLv2+
Version:      1.3
Release:      alt2_3
Summary:      Serial-over-lan (sol) client for Intel AMT
Group:        Networking/Other
URL:          http://www.kraxel.org/blog/linux/amtterm/
Source:       http://www.kraxel.org/releases/%{name}/%{name}-%{version}.tar.gz
Requires:     xdg-utils
BuildRequires: libgtk+2-devel libvte-devel desktop-file-utils
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
desktop-file-install \
    --vendor="fedora" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications/ \
    %{buildroot}/%{_datadir}/applications/gamt.desktop

%files
%doc COPYING
%{_bindir}/*
%{_mandir}/man?/*
/usr/share/applications/*.desktop

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1
- initial release by fcimport

