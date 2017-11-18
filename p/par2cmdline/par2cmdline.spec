Group: Archiving/Other
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: par2cmdline
Version: 0.7.4
Release: alt1_1
Summary: PAR 2.0 compatible file verification and repair tool

License: GPLv2+
URL: https://github.com/Parchive/par2cmdline/
Source0: https://github.com/Parchive/par2cmdline/releases/download/v%{version}/par2cmdline-%{version}.tar.bz2
Source44: import.info
Conflicts: par2 < 0.5
Obsoletes: par2 < 0.5
Provides: par2 = %version


%description
par2cmdline is a program for creating and using PAR2 files to detect damage
in data files and repair them if necessary. PAR2 files are usually
published in binary newsgroups on Usenet; they apply the data-recovery
capability concepts of RAID-like systems to the posting and recovery of
multi-part archives.


%prep
%setup -q

# Remove executable permission from text files
chmod -x ChangeLog configure.ac INSTALL Makefile.am NEWS stamp-h.in


%build
%configure
%make_build


%install
%makeinstall_std


%check
%{__make} check-TESTS


%files
%doc COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/par2
%{_bindir}/par2create
%{_bindir}/par2repair
%{_bindir}/par2verify
%{_mandir}/man1/par2.1*


%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.4-alt1_1
- new version

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.14-alt2_6
- update to new release by fcimport

* Wed Sep 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.14-alt2_2
- to Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.14-alt1_2
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.14-alt1_1
- update to new release by fcimport

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.tbb.20100203-alt1_17
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.tbb.20100203-alt1_11
- initial fc import

