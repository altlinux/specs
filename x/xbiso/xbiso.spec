Group: Archiving/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		xbiso
Version:	0.6.1
Release:	alt2_29
Summary:	ISO extraction utility for xdvdfs images
License:	GPLv2+
URL:		http://sourceforge.net/projects/xbiso/
Source0:	http://downloads.sourceforge.net/xbiso/%{name}-%{version}.tar.gz
Patch0:		xbiso-0.6.1-destdir.patch
Patch1:		xbiso-0.6.1-ftplib4.patch
Patch2:		xbiso-configure-c99.patch
Patch3:		xbiso-c99.patch
BuildRequires:  gcc
BuildRequires:	ftplib-devel
Source44: import.info

%description
xbiso is an ISO extraction utility for xdvdfs images.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .ftplib4
%patch2 -p1
%patch3 -p1

%build
%configure
%make_build

%install
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc CHANGELOG LICENSE README
%{_bindir}/xbiso

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.6.1-alt2_29
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_18
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_15
- update to new release by fcimport

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

