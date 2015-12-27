Name:		xbiso
Version:	0.6.1
Release:	alt2_14
Summary:	ISO extraction utility for xdvdfs images
Group:		Archiving/Other
License:	GPLv2+
URL:		http://sourceforge.net/projects/xbiso/
Source0:	http://downloads.sourceforge.net/xbiso/%{name}-%{version}.tar.gz
Patch0:		xbiso-0.6.1-destdir.patch
Patch1:		xbiso-0.6.1-ftplib4.patch
BuildRequires:	ftplib-devel
Source44: import.info

%description
xbiso is an ISO extraction utility for xdvdfs images.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .ftplib4

%build
%configure
make %{?_smp_mflags}

%install
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc CHANGELOG LICENSE README
%{_bindir}/xbiso

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_8
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_7
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_6
- initial release by fcimport

