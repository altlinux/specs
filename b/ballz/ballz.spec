# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate gcc-c++
# END SourceDeps(oneline)
Name:           ballz
Version:        1.0.3
Release:        alt1_2
Summary:        Platform game with some puzzle elements
Group:          Games/Other
License:        BSD
URL:            https://gitlab.com/groups/ballz
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  liballegro-devel dumb-devel libguichan-devel desktop-file-utils
Source44: import.info

%description
Ballz is a platformer with some puzzle elements. You take control of a ball
which is genetically modified by the British secret service. Your mission is
to rescue captured British soldiers from a prison in Iran.

The game was written in 72 hours for the TINS competition, a competition
similar to Speedhack. The name TINS is an recursive acronym for 'TINS is
not Speedhack'.


%prep
%setup -q


%build
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
%configure
make %{?_smp_mflags}


%install
%makeinstall_std
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS README BSD-license ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man6/*


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1
- update to new release by fcimport

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2-alt2_13.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_10
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_6
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_5
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_5
- initial release by fcimport

