Summary: Tool for Authenticode signing of EXE/CAB files
Name: osslsigncode
Version: 1.7.1
Release: alt1_2
License: GPLv2+
Group: File tools
URL: http://sourceforge.net/projects/osslsigncode/
Source: http://downloads.sf.net/osslsigncode/osslsigncode-%{version}.tar.gz
BuildRequires: libssl-devel
BuildRequires: libcurl-devel
BuildRequires: libgsf libgsf-devel libgsf-gir-devel
BuildRequires: autoconf-common
BuildRequires: automake-common
Source44: import.info

%description
Tool for Authenticode signing of EXE/CAB files.


%prep
%setup -q


%build
%configure --with-curl --with-gsf
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc ChangeLog COPYING README TODO
%{_bindir}/osslsigncode


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_2
- update to new release by fcimport

* Tue May 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_1
- moved to Sysiphus - required by mjg59, requested by mike@

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1
- initial fc import

