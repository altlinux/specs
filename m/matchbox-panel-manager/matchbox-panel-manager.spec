# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define name 	matchbox-panel-manager
%define version 0.1
%define release %mkrel 5

Summary: 	Manager for the Matchbox Desktop panel
Name: 		%name
Version: 	%version
Release: 	alt1_5
Url: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/%version/%{name}-%{version}.tar.bz2

BuildRequires:	libmatchbox-devel gtk2-devel
Requires:	matchbox-panel
Source44: import.info
Patch33: matchbox-panel-manager-0.1-alt-link.patch

%description
A GTK2 based manager for the Matchbox Dektop panel

%prep
%setup -q
%patch33 -p1

%build
%configure
%make

%install
%makeinstall

%files
%doc README 
%_bindir/%name
%_datadir/applications/*
%_datadir/pixmaps/*




%changelog
* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_5
- mageia import

