# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dvipdf gcc-c++ texlive-base-bin texlive-latex-base
# END SourceDeps(oneline)
Summary:	2D Quantum Monte Carlo simulator for semiconductor devices
Name:		archimedes
Version:	2.0.1
Release:	alt1_5
License:	GPLv3+
Group:		Engineering
URL:		http://www.gnu.org/software/archimedes/
Source0:	ftp://ftp.gnu.org/gnu/archimedes/%{name}-%{version}.tar.gz

BuildRequires:	dos2unix
Source44: import.info

%description
Archimedes is a package for the design and simulation of submicron
semiconductor devices. It is a 2D Fast Monte Carlo simulator which can take
into account all the relevant quantum effects, thank to the implementation of
the Bohm effective potential method.

The physics and geometry of a general device is introduced by typing a simple
script, which makes, in this sense, Archimedes a powerful tool for the
simulation of quite general semiconductor devices.

%prep
%setup -q

# Use tests as user examples
mv tests/ examples/
rm -rf examples/*/.log

# Suppress rpmlint errors
dos2unix COPYING doc/* doc/*/*
# Fix spurious-executable-perm warning
chmod 644 doc/*/*


%build
%configure
make %{?_smp_mflags}


%install
rm -rf ${buildroot}
%makeinstall_std


%files
%{_bindir}/%{name}
%doc AUTHORS ChangeLog COPYING doc examples NEWS README THANKS

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_2
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_1
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_2
- initial release by fcimport

