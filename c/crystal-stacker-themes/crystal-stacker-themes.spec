# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           crystal-stacker-themes
Version:        1.0
Release:        alt2_13
Summary:        Themes for the Crystal Stacker game
Group:          Games/Other
License:        Crystal Stacker
URL:            http://www.t3-i.com/cstacker.htm
Source0:        http://ncdgames.t3-i.com/csdream.zip
Source1:        http://ncdgames.t3-i.com/csfood.zip
Source2:        http://ncdgames.t3-i.com/csgems.zip
Source3:        http://ncdgames.t3-i.com/cslcd.zip
Source4:        http://ncdgames.t3-i.com/csmatrix.zip
Source5:        http://ncdgames.t3-i.com/csoldcs.zip
Source6:        http://ncdgames.t3-i.com/csstone.zip
Source7:        crystal-stacker-theme-license.txt
Source8:        cs-readme.txt
BuildArch:      noarch
Requires:       crystal-stacker
Source44: import.info

%description
7 new / extra themes for the Crystal Stacker game.


%prep
%setup -q -c -a5 -a6
# don't pass these to %setup, their filenames must be forced to lowercase
unzip -qqLL %{SOURCE1}
unzip -qqLL %{SOURCE2}
unzip -qqLL %{SOURCE3}
unzip -qqLL %{SOURCE4}
# put these somewhere were %%doc can find them
cp %{SOURCE7} %{SOURCE8} .


%build
# nothing to build datafiles only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/crystal-stacker
install -p -m 644 *.xm *.cth $RPM_BUILD_ROOT%{_datadir}/crystal-stacker


%files
%doc crystal-stacker-theme-license.txt cs-readme.txt
%{_datadir}/crystal-stacker/*.xm
%{_datadir}/crystal-stacker/*.cth


%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6
- converted from Fedora by srpmconvert script

