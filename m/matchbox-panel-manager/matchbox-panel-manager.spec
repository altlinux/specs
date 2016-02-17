# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
BuildRequires: desktop-file-utils
Summary: 	Manager for the Matchbox Desktop panel
Name: 		matchbox-panel-manager
Version: 	0.1
Release: 	alt1_11
Url: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0: 	http://matchbox-project.org/sources/%version/%{name}-%{version}.tar.bz2
Patch0:		matchbox-panel-manager-0.1-linking.patch
Patch1:		matchbox-panel-manager-0.1-automake-1.13.patch
BuildRequires:	libmatchbox-devel 
BuildRequires:	libgtk+2-devel
Requires:	matchbox-panel
Source44: import.info

%description
A GTK2 based manager for the Matchbox Dektop panel

%prep
%setup -q
%patch0 -p1
%patch1 -p1

#fix desktop file
sed -i -e 's,\(Icon=.*\)\.png,\1,g' mb-panel-manager.desktop

%build
autoreconf -vfi
%configure
%make

%install
%makeinstall_std

desktop-file-install \
	--vendor="" \
	--set-key="StartupNotify" \
	--set-value="true" \
	--remove-key="SingleInstance" \
	--remove-category="MB" \
	--remove-category="SystemSettings" \
	--dir=%{buildroot}%{_datadir}/applications \
		%{buildroot}%{_datadir}/applications/*.desktop


%files
%doc README 
%_bindir/%name
%_datadir/applications/*
%_datadir/pixmaps/*


%changelog
* Thu Feb 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_11
- new release

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_10
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_9
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_8
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_7
- update by mgaimport

* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_5
- mageia import

