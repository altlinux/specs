# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           bam
Version:        0.4.0

Release:        alt2_10
Summary:        A build-system

Group:          Games/Other
License:        zlib
URL:            http://matricks.github.com/bam/
Source0:        http://github.com/downloads/matricks/bam/%{name}-%{version}.tar.bz2
Source44: import.info


%description
A tool that controls process of producing executables of
software from its source code. Used to build the Teeworlds game.


%prep
%setup -q


%build
sh -x make_unix.sh %{optflags}


%install
install -D -m 0755 %{name} \
        %{buildroot}%{_bindir}/%{name}


%files
%doc docs/ examples/
%{_bindir}/%{name}


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2_7
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2_3
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2_2
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_2
- update to new release by fcimport

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- new origin release

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_4
- converted from Fedora by srpmconvert script

