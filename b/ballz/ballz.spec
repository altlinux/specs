# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           ballz
Version:        1.0.2
Release:        alt2_5
Summary:        Platform game with some puzzle elements
Group:          Games/Other
License:        BSD
URL:            http://code.google.com/p/db-tins07/
Source0:        http://db-tins07.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  liballegro-devel dumb-devel libguichan-devel desktop-file-utils
Source44: import.info

%description
Ballz is a platformer with some puzzle elements. You take control of a ball
which is genetically modified by the British secret service. Your mission is
to rescue captured British soldiers from a prison in Iran.

The game was written in 72 hours for the TINS competition, a competition
similar to Speedhack. The name TINS is an recursive acronym for a.'TINS is
not Speedhacka.'.


%prep
%setup -q


%build
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%doc AUTHORS README BSD-license ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man6/*


%changelog
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

