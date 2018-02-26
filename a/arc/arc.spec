Name:      arc
Version:   5.21o
Release:   alt2_10
Summary:   Arc archiver
Group:     Archiving/Other
License:   GPL+
URL:       http://arc.sourceforge.net/
Source:    http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tgz
Source44: import.info

%description
Arc file archiver and compressor. Long since superseded by zip/unzip
but useful if you have old .arc files you need to unpack.


%prep
%setup -q
sed -i -e 's,^OPT =.*$,OPT = ${RPM_OPT_FLAGS},' Makefile


%build
make %{?_smp_mflags}


%install
rm -fr %{buildroot}
install -m 0755 -d %{buildroot}{%{_bindir},%{_mandir}/man1}
install -m 0755 arc marc %{buildroot}%{_bindir}
install -m 0644 arc.1 %{buildroot}%{_mandir}/man1/


%files
%doc LICENSE COPYING PATCHLEVEL Readme Arc521.doc
%doc %{_mandir}/man1/*
%attr (0755,root,root) %{_bindir}/*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.21o-alt2_10
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 5.21o-alt1_10
- update to new release by fcimport

* Mon Nov 07 2011 Igor Vlasenko <viy@altlinux.ru> 5.21o-alt1_9
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 5.21o-alt1_8
- initial release by fcimport

