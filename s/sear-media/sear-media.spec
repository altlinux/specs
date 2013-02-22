Name:           sear-media
Version:        0.6
# No dist tag because this is large noarch game data.
Release:        alt2_10
Summary:        Media files for the sear worldforge client

Group:          Games/Other
License:        GPLv2+ or GFDL
URL:            http://www.worldforge.org
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-20070206.tar.gz
BuildArch:      noarch
Source44: import.info

%description
Media files for the sear WorldForge client.


%prep
%setup -q

# Remove editor swap file.
rm -f castle/.dot_it.sh.swp

# Rename some doc files to prevent filename conflicts
mv chicken/README README.chicken


%build
# Nothing to build!


%install
install -d $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}
cp -a * $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}

# Remove doc files from the installed media files.
rm -f $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}/COPYING.txt
rm -f $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}/LICENSING.txt
rm -f $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}/README
rm -f $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}/README.chicken


%files
%doc COPYING.txt LICENSING.txt README README.chicken
%dir %{_datadir}/sear
%{_datadir}/sear/%{name}-%{version}


%changelog
* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_8
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_7
- initial release by fcimport

