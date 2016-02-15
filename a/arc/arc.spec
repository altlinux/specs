Name:      arc
Version:   5.21p
Release:   alt1_7
Summary:   Arc archiver
Group:     Archiving/Other
License:   GPL+
URL:       http://arc.sourceforge.net/
Source0:   http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# 2 small polish patches courtesy of Debian
Patch0:    arc-5.21p-spelling.patch
Patch1:    arc-5.21p-manpage-section-fix.patch
# Arc was once shareware, but has been relicensed to the GPL with permission
# of its original author. But there still is some confusing license text in the
# docs this clarifies those parts of the text (rhbz#947786)
Patch2:    arc-5.21p-clarify-license.patch
# Fix reading v1 headers
Patch3:    arc-5.21p-hdrv1-read-fix.patch
# Fix arcdie crash
Patch4:    arc-5.21p-fix-arcdie.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1179143
Patch5:    arc-5.21p-directory-traversel.patch
Source44: import.info

%description
Arc file archiver and compressor. Long since superseded by zip/unzip
but useful if you have old .arc files you need to unpack.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
sed -i -e 's,^OPT =.*$,OPT = ${RPM_OPT_FLAGS},' Makefile


%build
make %{?_smp_mflags}


%install
install -m 0755 -d %{buildroot}{%{_bindir},%{_mandir}/man1}
install -m 0755 arc marc %{buildroot}%{_bindir}
install -m 0644 arc.1 marc.1 %{buildroot}%{_mandir}/man1/


%files
%doc LICENSE COPYING PATCHLEVEL Readme Arc521.doc
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 5.21p-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 5.21p-alt1_6
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 5.21p-alt1_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 5.21p-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 5.21p-alt1_3
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 5.21p-alt1_2
- update to new release by fcimport

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 5.21p-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 5.21o-alt2_12
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 5.21o-alt2_11
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.21o-alt2_10
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 5.21o-alt1_10
- update to new release by fcimport

* Mon Nov 07 2011 Igor Vlasenko <viy@altlinux.ru> 5.21o-alt1_9
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 5.21o-alt1_8
- initial release by fcimport

