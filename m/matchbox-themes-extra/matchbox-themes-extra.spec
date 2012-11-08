%define name 	matchbox-themes-extra
%define version 0.3
%define release %mkrel 5

Summary: 	Themes for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	alt1_5
Url: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/matchbox-themes-extra/%version/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Source44: import.info

%description
Extra themes for the Matchbox Desktop

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%doc README TODO
%_iconsdir/*
%_datadir/themes/*




%changelog
* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_5
- mageia import

