Name:		mg
Version:	20160421
Release:	alt1_1
Summary:	Tiny Emacs-like editor

Group:		Editors
License:	BSD and ISC and MirOS
URL:		http://homepage.boetes.org/software/mg/
Source0:	http://homepage.boetes.org/software/mg/%{name}-%{version}.tar.gz
BuildRequires: libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
BuildRequires:	libbsd-devel >= 0.7.0
Source44: import.info

%description
mg is a tiny, mostly public-domain Emacs-like editor included in the base 
OpenBSD system. It is compatible with Emacs because there shouldn't be any 
reason to learn more editor types than Emacs or vi.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="%{optflags} -lncurses" libdir="%{_libdir}"

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} \
     INSTALL='install -p'

%files
%doc README tutorial
%{_bindir}/mg
%{_mandir}/man1/mg.1.*

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20160421-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20150323-alt1_2
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 20150323-alt1_1
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 20141127-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 20140414-alt1_2
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 20140414-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 20110905-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20110905-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20110905-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20110905-alt2_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20110905-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20110905-alt1_2
- update to new release by fcimport

* Thu Oct 06 2011 Igor Vlasenko <viy@altlinux.ru> 20110905-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 20110120-alt1_1
- initial release by fcimport

