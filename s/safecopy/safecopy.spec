Name:           safecopy
Version:        1.7
Release:        alt2_8
Summary:        Safe copying of files and partitions

Group:          File tools
License:        GPL+
URL:            http://safecopy.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source44: import.info


%description
safecopy is a data recovery tool which tries to extract as much data
as possible from a problematic (i.e. damaged sectors) source - like
floppy drives, harddisk partitions, CDs, tape devices, ..., where
other tools like dd would fail doe to I/O errors.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags} 


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_7
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_5
- update to new release by fcimport

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_4
- moved to Sisyphus by mike@ request

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_4
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_3
- initial fc import

