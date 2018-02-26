Name:           AGReader
Version:        1.2
Release:        alt2_8
Summary:        Console reader for viewing AmigaGuide files
Group:          Text tools
License:        GPL+
URL:            http://main.aminet.net/misc/unix/
Source0:        http://main.aminet.net/misc/unix/%{name}.tar.bz2
Source1:        agr.1
Source44: import.info

%description
A viewer for the UNIX console which can read and display AmigaGuide files. It
supports all of the v39 AmigaGuide specification possible and supports a large
subset of the v40 specifications.


%prep
%setup -qn %{name}


%build
make -C Sources %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1
install -m0755 Sources/agr %{buildroot}%{_bindir}


%files
%{_bindir}/agr
%{_mandir}/man1/agr.1.*
%doc Docs/agr.guide Docs/test.guide Docs/agr.html README


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_8
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_7
- initial release by fcimport

