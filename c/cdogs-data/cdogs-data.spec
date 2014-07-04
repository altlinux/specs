# upstream does data releases with a year-month-day versioning scheme, however
# this releases always coincide with a cdogs-sdl release, so since rpm handles
# year-month-day versioning scheme's badly I've decided to use the matching
# cdogs-sdl release version
%define cdogs_sdl_version 0.4
%define cdogs_data_version 2007-07-06

Name:           cdogs-data
Version:        %{cdogs_sdl_version}
Release:        alt2_11
Summary:        Data files for the CDogs game
Group:          Games/Other
License:        Redistributable, no modification permitted
URL:            http://lumaki.com/code/cdogs/
Source0:        http://icculus.org/cdogs-sdl/files/data/%{name}-%{cdogs_data_version}.tar.bz2
BuildArch:      noarch
Requires:       cdogs-sdl >= %{cdogs_sdl_version} icon-theme-hicolor
Source44: import.info

%description
Data files for the CDogs game.


%prep
# nothing to prep


%build
# nothing to build


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
tar xj --strip-components=1 -f %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/cdogs_icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/cdogs.png
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/cdogs?icon.*


%files
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/cdogs.png


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_7
- update to new release by fcimport

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_6
- converted from Fedora by srpmconvert script

